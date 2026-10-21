#!/usr/bin/env python3
"""Re-check a built article against the house rules, immediately before deploy.

The drafting rules are enforced on the markdown draft by nomena-blog's
tools/rulecheck.py, but that runs by hand, on a different machine, against a
file that is not what ships. Anything introduced after that point -- a change
to a generator template, a hand edit to an ARTICLES dict, a queue payload that
was never re-checked -- reaches the live site unexamined. The disclaimer
wording on every library page drifted out of rule 26 exactly that way.

So this checks the deployable artifact: the built HTML in library/<slug>.html,
after build_site.py has run and before anything is committed.

  python3 _generator/precheck.py <slug> [<slug>...]
  python3 _generator/precheck.py --all

Exit 0 when every page checked is clean, 1 when any rule fails. promote_next.py
calls it as the last gate and refuses to commit on a non-zero exit.

Only mechanically checkable rules live here. Judgement calls -- whether a
rewrite is better than the page it replaces, whether evidence is framed
honestly -- are not automatable and stay with the editor.
"""
import argparse
import os
import re
import sys
from html.parser import HTMLParser

GEN = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(GEN)

# Rule 1/2: fixed verbatim, "dangerous" and "not safe to take unsupervised"
# are load-bearing and are never edited out.
FOOTER_LABEL = 'Safety.'
FOOTER = ("Ibogaine prolongs the heart's QT interval and can trigger dangerous arrhythmias. "
          "Treatment requires an EKG and bloodwork before dosing, continuous cardiac "
          "monitoring during, and medically trained staff present. Ibogaine is not safe to "
          "take unsupervised.")

# Rule 26: the disclaimer says the article is general information and not
# medical advice, and nothing else. No regulatory status, no efficacy framing,
# no risk summary -- those belong in body prose with a source, or in the
# rule 1 footer.
DISCLAIMER_MUST_SAY = ('general information', 'not medical advice')
DISCLAIMER_MUST_NOT_SAY = (
    'unapproved', 'not approved', 'unlicensed', 'schedule i', 'illegal',
    'potent', 'psychoactive', 'risk', 'dangerous', 'fatal', 'arrhythmia',
    'effective', 'works', 'cure',
)

WORDS_LO, WORDS_HI = 1800, 2200                      # rule 28

BANNED_PROSE = [
    (r'(?i)\bprov(en|ed)\b', 'rule 14: "proven"'),
    (r'(?i)\bcures?\b|will heal|guarantee|permanent fix|miracle|breakthrough'
     r'|life-changing', 'rule 52: hype'),
    (r'(?i)\bdelve\b|\btestament\b|\bmoreover\b|it\'s important to note'
     r'|in conclusion|\bfurthermore\b', 'rule 33: AI tell'),
    (r'(?i)never (been )?(licensed|approved)', 'rule 65: false licensing claim'),
    (r'—|–', 'em/en dash'),
    (r'\[(SECONDARY|NEEDS|UNVERIFIED|HUMAN|TODO|TK)', 'unresolved draft flag'),
    (r'\[E1[2-5]\]', 'retired source E12-E15'),
    (r'@@[A-Z_]+@@', 'unsubstituted template placeholder'),
]
FIRST_SECOND_PERSON = re.compile(
    r'\b(I|we|We|my|My|our|Our|us|you|You|your|Your|yours)\b')     # rule 30
# "Schedule I", "Phase I", "Type I" and friends are roman numerals, not the
# first person. Checked on the word before the match.
NOT_PRONOUN_AFTER = re.compile(
    r'(?i)\b(schedule|phase|class|type|part|appendix|table|figure|stage|tier|'
    r'group|chapter|section|annex|category|grade|world war|trial)\s*$')

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}


class Node:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs or []), parent
        self.kids, self.text = [], ''

    def cls(self):
        return self.attrs.get('class', '')


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.cur = Node('#root')
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
            return
        if tag in VOID:
            return
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        self.cur = n

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
            return
        if tag in VOID:
            return
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, d):
        if not self.skip:
            self.cur.text += d


def find(node, pred):
    if pred(node):
        yield node
    for k in node.kids:
        yield from find(k, pred)


def text_of(node):
    """Visible text, with a space at every tag boundary.

    Without the space, adjacent nodes fuse: "...content" + "I..." reads as the
    pronoun "I", and an inline <strong> label merges into the word after it."""
    out = [node.text]
    for k in node.kids:
        out.append(text_of(k))
    return ' '.join(p for p in out if p)


def flat(s):
    return re.sub(r'\s+', ' ', s).strip()


def is_prose(n):
    """A node whose own text counts as readable body copy under rule 28:
    inside .article-body, and not scaffolding, references, captions, tables,
    headings, the contents box, the CTA or the safety note."""
    p = n
    while p is not None:
        c, t = p.cls(), p.tag
        if (t in ('h1', 'h2', 'h3', 'h4', 'figure', 'figcaption', 'table', 'aside')
                or 'article-refs' in c or 'inline-cta' in c or 'article-note' in c
                or 'toc' in c):
            return False
        if 'article-body' in c:
            return True
        p = p.parent
    return False


def check(slug):
    """Return a list of rule failures for one built article."""
    path = os.path.join(ROOT, 'library', slug + '.html')
    if not os.path.exists(path):
        return ['no built page at library/%s.html' % slug]
    html = open(path, encoding='utf-8').read()
    t = Tree()
    t.feed(html)
    bad = []

    prose_nodes = [n for n in find(t.root, is_prose) if n.text.strip()]
    prose = flat(' '.join(n.text for n in prose_nodes))
    n_words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", prose))

    # rule 28
    if not WORDS_LO <= n_words <= WORDS_HI:
        bad.append('rule 28: %d words of body prose, need %d-%d'
                   % (n_words, WORDS_LO, WORDS_HI))

    notes = [flat(text_of(n)) for n in find(t.root, lambda n: 'article-note' in n.cls())]
    joined_notes = ' '.join(notes)

    # rules 1 and 2
    visible = flat(re.sub(r'<[^>]+>', ' ', html).replace('&#39;', "'")
                   .replace('&rsquo;', "'").replace('’', "'"))
    if FOOTER.replace('’', "'") not in visible:
        bad.append('rules 1-2: safety footer missing or not verbatim')
    elif FOOTER_LABEL not in visible:
        bad.append('rules 1-2: safety footer present but the "Safety." label is missing')

    # rule 26
    disc = next((n for n in notes if 'medical advice' in n.lower()), None)
    if disc is None:
        bad.append('rule 26: no medical disclaimer found')
    else:
        low = disc.lower()
        for must in DISCLAIMER_MUST_SAY:
            if must not in low:
                bad.append('rule 26: disclaimer missing "%s"' % must)
        extra = sorted({w for w in DISCLAIMER_MUST_NOT_SAY if w in low})
        if extra:
            bad.append('rule 26: disclaimer carries regulatory status / risk framing '
                       '(%s) -- it must say general information and not medical advice, '
                       'and nothing else' % ', '.join(extra))

    # rule 27: exactly one CTA
    n_cta = len(list(find(t.root, lambda n: 'inline-cta' in n.cls())))
    if n_cta > 1:
        bad.append('rule 27: %d CTA blocks, at most one' % n_cta)

    # rules 14, 33, 52, 65 and leftovers, prose only
    for pat, label in BANNED_PROSE:
        hits = re.findall(pat, prose)
        if hits:
            bad.append('%s: %d occurrence(s)' % (label, len(hits)))

    # rule 30: third person throughout
    person = {m.group(0) for m in FIRST_SECOND_PERSON.finditer(prose)
              if not (m.group(0) == 'I'
                      and NOT_PRONOUN_AFTER.search(prose[max(0, m.start() - 24):m.start()]))}
    if person:
        bad.append('rule 30: first/second person in prose (%s)'
                   % ', '.join(sorted(person)[:6]))

    # rule 66: every reference carries a live link
    for refs in find(t.root, lambda n: 'article-refs' in n.cls()):
        items = list(find(refs, lambda n: n.tag == 'li'))
        unlinked = [i for i, li in enumerate(items, 1)
                    if not list(find(li, lambda n: n.tag == 'a' and n.attrs.get('href', '')
                                     .startswith('http')))]
        if unlinked:
            bad.append('rule 66: reference(s) %s have no live link'
                       % ', '.join(map(str, unlinked)))
    return bad


SITE_SKIP = ('google',)            # Search Console verification file


def check_site():
    """Whole-site checks on every built page, not just library articles.

    @@MDESC@@ reached the live meta description of library/index.html because
    this gate only ever read library/<slug>.html. A reviewer found it before
    we did. These checks are cheap and cover the pages the article loop skips.
    """
    bad = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ('_generator', '.git', 'assets', 'node_modules')]
        for fn in sorted(files):
            if not fn.endswith('.html') or fn.startswith(SITE_SKIP):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, ROOT)
            html = open(path, encoding='utf-8').read()

            left = sorted(set(re.findall(r'@@[A-Z_]+@@', html)))
            if left:
                bad.append('%s: unsubstituted %s' % (rel, ', '.join(left)))

            # quiz.html uses "noindex,follow", 404.html plain "noindex".
            noindex = bool(re.search(r'name="robots"\s+content="[^"]*noindex', html))

            # A noindexed page's meta description never reaches a search
            # result, so only its placeholders matter. quiz.html is a
            # noindexed redirect stub and legitimately carries a short one.
            m = re.search(r'<meta name="description" content="([^"]*)"', html)
            if not m:
                bad.append('%s: no meta description' % rel)
            elif not noindex and len(m.group(1).strip()) < 50:
                bad.append('%s: meta description too short (%d chars)'
                           % (rel, len(m.group(1).strip())))

            if not noindex and '<link rel="canonical"' not in html:
                bad.append('%s: no canonical and not noindexed' % rel)
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slugs', nargs='*')
    ap.add_argument('--all', action='store_true', help='check every built library article')
    ap.add_argument('--site', action='store_true',
                    help='whole-site checks (placeholders, meta description, canonical)')
    a = ap.parse_args()
    slugs = a.slugs
    if a.all:
        lib = os.path.join(ROOT, 'library')
        slugs = sorted(f[:-5] for f in os.listdir(lib)
                       if f.endswith('.html') and f != 'index.html')
    if not slugs and not a.site:
        ap.error('give one or more slugs, or --all, or --site')
    worst = 0
    if a.site or a.all:
        site_bad = check_site()
        if site_bad:
            worst = 1
            print('FAIL site-wide')
            for b in site_bad:
                print('       %s' % b)
        else:
            print('ok   site-wide (placeholders, meta descriptions, canonicals)')
    for s in slugs:
        bad = check(s)
        if bad:
            worst = 1
            print('FAIL %s' % s)
            for b in bad:
                print('       %s' % b)
        else:
            print('ok   %s' % s)
    print('\n%s' % ('one or more rule checks failed; nothing should be deployed'
                    if worst else 'all checks passed'))
    return worst


if __name__ == '__main__':
    sys.exit(main())
