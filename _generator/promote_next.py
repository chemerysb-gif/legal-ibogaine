#!/usr/bin/env python3
"""
Promote the next queued article rewrite, one per run.

The 11 library rewrites replace pages that are already live and indexed, so
they are never appended and never date-gated (a future date would drop the
live page from library/, the index and the sitemap until that day). Instead
each rewrite waits in _generator/publish_queue/<slug>.json, and on its day
this script swaps its fields into the existing ARTICLES dict in
review_data_1.py / review_data_2.py, sets `date`, rebuilds the site and
checks the result. The page is never offline.

  python3 _generator/promote_next.py            # promote today's, if any
  python3 _generator/promote_next.py --dry-run  # show what would happen
  python3 _generator/promote_next.py --today 2026-10-09

It does not commit or push; the caller does, one article per commit.
Exit codes: 0 promoted or nothing due, 1 a check failed (nothing to commit).
"""
import argparse, ast, datetime, hashlib, json, os, re, subprocess, sys

GEN = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(GEN)
QUEUE = os.path.join(GEN, 'publish-queue.json')
DATA = [os.path.join(GEN, 'review_data_1.py'), os.path.join(GEN, 'review_data_2.py')]
FIELDS = ('title', 'htitle', 'mdesc', 'desc', 'toc', 'refs', 'body', 'readtime',
          'topic', 'img', 'imgalt', 'figcap')
FOOTER = "Ibogaine is not safe to take unsupervised."


def pystr(s):
    if '"""' not in s and '\\' not in s and not s.endswith('"'):
        return '"""' + s + '"""'
    return repr(s)


def render(d):
    out = ['{']
    for k, v in d.items():
        if k == 'toc':
            out.append('"toc": [')
            out += ['    (%s, %s),' % (json.dumps(i), json.dumps(l, ensure_ascii=False)) for i, l in v]
            out.append('],')
        elif k == 'refs':
            out.append('"refs": [')
            out += ['    %s,' % repr(r) for r in v]
            out.append('],')
        elif k == 'body':
            out.append('"body": %s,' % pystr(v))
        else:
            out.append('%s: %s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)))
    out[-1] = out[-1].rstrip(',')
    return '\n'.join(out) + '\n}'


def find_dict(slug):
    """(path, source, start, end, current dict) for the ARTICLES entry with this slug."""
    for path in DATA:
        src = open(path, encoding='utf-8').read()
        lines = src.splitlines(keepends=True)
        offs = [0]
        for l in lines:
            offs.append(offs[-1] + len(l))
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Dict):
                keys = [k.value for k in node.keys if isinstance(k, ast.Constant)]
                if 'slug' not in keys:
                    continue
                d = ast.literal_eval(node)
                if d.get('slug') == slug:
                    start = offs[node.lineno - 1] + node.col_offset
                    end = offs[node.end_lineno - 1] + node.end_col_offset
                    return path, src, start, end, d
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--today', default=datetime.date.today().isoformat())
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    queue = json.load(open(QUEUE))
    due = [e for e in queue if not e.get('done') and e['publish_on'] <= a.today]
    if not due:
        nxt = next((e for e in queue if not e.get('done')), None)
        print('nothing due on %s; next: %s' % (a.today, nxt and '%s on %s' % (nxt['slug'], nxt['publish_on'])))
        return 0
    entry = sorted(due, key=lambda e: e['publish_on'])[0]
    slug = entry['slug']
    payload = json.load(open(os.path.join(GEN, 'publish_queue', slug + '.json'), encoding='utf-8'))
    hit = find_dict(slug)
    if not hit:
        print('FAIL: no ARTICLES entry with slug %s (rewrites replace, never append)' % slug)
        return 1
    path, src, start, end, cur = hit

    new = dict(cur)
    for k in FIELDS:
        if k in payload:
            new[k] = [tuple(t) for t in payload[k]] if k == 'toc' else payload[k]
    new['date'] = a.today
    print('promoting %s (queued for %s) into %s' % (slug, entry['publish_on'], os.path.basename(path)))
    print('  fields replaced: %s' % ', '.join(k for k in FIELDS if k in payload))
    if a.dry_run:
        return 0

    # checks on the content before touching anything
    ids = re.findall(r'<h2 id="([^"]+)"', new['body'])
    problems = []
    if ids != [i for i, _ in new['toc']]:
        problems.append('toc ids %s do not match body h2 ids %s' % ([i for i, _ in new['toc']], ids))
    if FOOTER not in new['body']:
        problems.append('rule 1 safety footer missing from body')
    if new['body'].count('@@CTA@@') > 1:
        problems.append('more than one @@CTA@@')
    if not os.path.exists(os.path.join(ROOT, 'assets', 'img', new['img'])):
        problems.append('image assets/img/%s missing' % new['img'])
    if problems:
        print('FAIL before build:\n  ' + '\n  '.join(problems))
        return 1

    with open(path, 'w', encoding='utf-8') as f:
        f.write(src[:start] + render(new) + src[end:])
    if find_dict(slug)[4] != new:
        print('FAIL: rewritten dict does not round-trip')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(src)
        return 1

    r = subprocess.run([sys.executable, os.path.join(GEN, 'build_site.py')], cwd=ROOT,
                       capture_output=True, text=True)
    print('\n'.join(r.stdout.strip().splitlines()[-2:]))
    if r.returncode:
        print('FAIL: build_site.py errored\n' + r.stderr)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(src)
        return 1

    page = open(os.path.join(ROOT, 'library', slug + '.html'), encoding='utf-8').read()
    for i in ids:
        if 'href="#%s"' % i not in page:
            problems.append('contents link to #%s missing on page' % i)
    if FOOTER not in page:
        problems.append('footer missing on built page')
    if problems:
        print('FAIL after build:\n  ' + '\n  '.join(problems))
        return 1

    entry['done'] = True
    entry['promoted_on'] = a.today
    with open(QUEUE, 'w') as f:
        json.dump(queue, f, indent=1)
        f.write('\n')
    print('OK: %s live as of %s' % (slug, a.today))
    return 0


if __name__ == '__main__':
    sys.exit(main())
