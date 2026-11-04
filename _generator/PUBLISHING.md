# Publishing an article

Articles are data, not files. You add a dict; the generator writes the page,
adds it to the library index, puts it in the sitemap with today's date, and
emits its Article + BreadcrumbList schema. There is no separate blog engine.

## The loop

1. Append an `ARTICLES.append({...})` block to the end of
   `_generator/review_data_2.py` (see the template below).
2. Drop the image in `assets/img/`. A `.jpg` is fine — the build generates and
   references a `.webp` automatically.
3. Run the generator from anywhere:

   ```
   python3 _generator/build_site.py
   ```

4. Check it locally: `python3 -m http.server 8343` then open
   `http://127.0.0.1:8343/library/<slug>.html`.
5. Commit and push. GitHub Pages redeploys within a minute or two.

Never edit `library/*.html` or any root `.html` by hand — the next build
overwrites it.

## Template

```python
ARTICLES.append({
"slug": "url-slug-no-html-suffix",
"htitle": "Short Title for the Browser Tab",
"mdesc": "Meta description, 140-160 characters. This is the sentence that
           appears in Google results, so write it for a person deciding
           whether to click, not for a keyword.",
"title": "The Full Headline Shown on the Page",
"topic": "Evidence",          # the tag on the card: Evidence, Safety, Practical, Legal
"desc": "Standfirst under the headline. Two sentences. Says what the piece
         argues, not what it covers.",
"date": "2026-10-02",         # YYYY-MM-DD, shown on the page and in Article schema
"readtime": 7,                # minutes, roughly words / 220
"img": "filename.jpg",        # must exist in assets/img/
"imgalt": "Literal description of the image for screen readers",
"figcap": "Fig. 11 — Caption under the hero image",
"toc": [
    ("anchor-id", "Section heading as shown in the contents list"),
    ("another-id", "Second section"),
],
"refs": [
    'Author, A.B., et al. (2024). Title of the paper. <em>Journal</em>, 12(3), 45-67.',
],
"body": """<h2 id="anchor-id">Section heading</h2>
<p>Body copy as HTML.</p>
@@CTA@@
<h2 id="another-id">Second section</h2>
<p>More copy.</p>"""
})
```

### Rules the build enforces, or quietly depends on

- Every `id` in `toc` must exist as an `<h2 id="...">` in `body`, and in the
  same order. The contents list links to them; a mismatch gives a dead link.
- `figcap` numbers run in sequence across the whole library. Check the highest
  existing `Fig. NN` before picking one.
- `@@CTA@@` drops the consultation block mid-article. One per piece, after the
  section that earns it. Omit it rather than forcing it in.
- `refs` entries are raw HTML strings; `<em>` for journal names. They render as
  a numbered reference list at the foot of the page.
- Internal links from an article use `../` — e.g. `<a href="../eligibility.html">`.

## What this does for SEO

- The page is added to `sitemap.xml` with a `<lastmod>` of the build date.
  That date then stays fixed until the page's content actually changes, which
  is why rebuilding does not re-date the whole site.
- `Article` and `BreadcrumbList` JSON-LD are emitted automatically from the
  dict — `datePublished` and `dateModified` both come from `date`.
- The card appears on `library/index.html`, giving the new page an internal
  link from an already-crawled page. This is how a new article gets found.

Authorship is deliberately the organisation, not a named person. If that ever
changes, the `author` object lives in `render_article` in `build_site.py` and
needs changing in one place.

## Before you write

Content is the whole strategy here. The site competes on depth and citations,
not on authorship signals, so a post that restates what the existing pages
already say is worse than no post — it splits the topic across two URLs and
leaves both weaker. Check `library/index.html` and the root pages first, and
when a topic is already covered, extend that page instead of adding one.

## Rewriting a live article: the publish queue

Rewrites of pages that are already live never append a new dict and are never
date-gated: a future `date` would drop the live page from `library/`, the index
and the sitemap until that day. Instead:

1. A rewrite is converted (from the nomena-blog drafts, by
   `tools/to-article-dict.py`) into `_generator/publish_queue/<slug>.json`,
   holding the replacement `title, htitle, mdesc, desc, toc, refs, body,
   readtime`. Image, caption and topic stay as they are in the live dict.
2. `_generator/publish-queue.json` lists each slug with a `publish_on` date.
3. `python3 _generator/promote_next.py` swaps the oldest due rewrite into its
   existing dict in `review_data_1.py` / `review_data_2.py`, sets `date` to
   today, rebuilds, and checks the result (contents links, safety footer, one
   `@@CTA@@` at most). It rolls back on any failure. It does not commit.
4. One promoted article per commit: `Publish rewrite: <title>`.

A daily scheduled Claude routine runs step 3 and pushes. `--dry-run` shows what
would happen; `--today YYYY-MM-DD` simulates a date.

Logged exemptions to the house content rules (nomena-blog `CLAUDE.md`) for this
site: rule 26, organisation authorship rather than a named byline; rule 27,
one `@@CTA@@` per rewrite, placed after the section that earns it. Both were
decided by the site owner on 2026-10-07.

### Sitemap dates

`lastmod.json` hashes each page with the build-time "Updated <date>" stamp
and the related-article cards masked out, so a rebuild, or a change to another
article's card, does not re-date a page. The stamp is then rewritten to the
page's content date.

## Keeping the scheduler running

`.github/workflows/publish-next.yml` runs at 01:00 UTC (08:00 Bangkok) and
publishes every article whose `date` has arrived. A missed day needs no repair:
the next run renders everything due, so a gap closes itself.

Two ways it stops, and only one of them is noisy.

A run that **fails** files a GitHub issue (the last step in the workflow). The
rule gate blocks the deploy on any failure, so a broken build commits nothing
and the live site keeps the last good version.

A run that **never happens** reports nothing, because a job cannot observe its
own absence. That is what the 2026-10-22 to 11-04 outage was: the workflow had
never been pushed, so there was no run to fail, and nothing published for 13
days without a single alert. Two causes to watch for:

- **The `workflow` OAuth scope.** Pushing any file under `.github/workflows/`
  needs it; a token without it gets a 404 from the contents API, which reads
  like the path is missing rather than like a permission problem. `gh auth
  status` lists the scopes.
- **GitHub disables scheduled workflows after 60 days of repository
  inactivity.** Daily publish commits count as activity, so the schedule stays
  alive while the queue has articles in it. The queue currently ends
  2026-11-20; if nothing is added, expect the schedule to be switched off
  silently around late January 2027 and to need re-enabling from the Actions
  tab.

The cheap check, from anywhere: the newest `<lastmod>` in
`https://legal-ibogaine.com/sitemap.xml` should be within a day or two of
today whenever articles remain queued.
