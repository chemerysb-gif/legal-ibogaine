# Legal Ibogaine — legal-ibogaine.com

Static informational + lead-gen website about ibogaine treatment. Positions the business
as an **independent placement service**: providers pay a placement fee, visitors pay nothing.
Owner: Bogdan (non-technical). Never promise a phone call anywhere in the copy.

**Business reality (2026-10-01, do not publish):** Bogdan also owns nomena.life, an ibogaine provider
in Phuket, Thailand — the first (unnamed) provider this site refers to; other partners come later for
people who won't travel to Thailand. NEVER name nomena.life on the site, and never add claims like
"no clinic ownership" or "no commissions that bias us" — they would be false. "Not tied to a single
partner" stays per Bogdan (multiple partners planned).

## Live setup
- **Hosting: GitHub Pages** — repo `chemerysb-gif/legal-ibogaine` (public), branch `main`, root.
  Deploy = push to that repo. GitHub account authorized via `gh` CLI on this Mac.
- **Domain: legal-ibogaine.com** (GoDaddy, registered on the owner's mom's account; DNS at GoDaddy:
  A `@` → 185.199.108.153, CNAME `www` → chemerysb-gif.github.io).
- **Netlify is deprecated** for this site (old project "ibogaine-guide", ID a640b869-7ff3-4abe-bcc6-fadd782a124c) —
  account was credit-blocked and free plan shows a "Powered by Netlify" badge. Do not deploy there.
- Local preview: `python3 -m http.server 8343` from this folder (run in background via Bash, not launch.json — macOS TCC blocks spawned servers).

## Architecture
- The site is **generated**: edit sources in `_generator/`, then run `python3 _generator/build_site.py`
  (from `_generator/`). NEVER hand-edit the root .html files — they get overwritten.
  - `build_site.py` — templates (HEAD/header/footer/CTA bands), PAGE_IMG, renderers, sitemap,
    and a post-pass that injects `width`/`height` into every `<img>` (via sips).
  - `site_pages_1/2/3/4.py` — page bodies. `site_pages_4.py` = the two surveys. `home_body.html` = homepage.
  - `review_data_1/2.py` — the 10 library articles.
- `css/styles.css` and `js/*.js` are hand-maintained (not generated).
- **Deploy procedure**: rebuild, then rsync everything except `_generator`, `README.md`, `.netlify`, `.DS_Store`
  into a staging dir with a `CNAME` file (`legal-ibogaine.com`) + `.nojekyll`, commit, push to
  `chemerysb-gif/legal-ibogaine` main. (Previous deploy used scratchpad dir `gh-pages-site`.)

## Design system
- Font: **Aileron** only, self-hosted in `assets/fonts/` (300/400/400i/600/700). No Google Fonts.
- Palette: ink navy `#15252F`, sage `#C5DDD5`, pale citrus `#FDF7B1` (primary buttons/accents).
  CSS custom properties in `:root` of styles.css; old var names (--pine, --rose…) are remapped, keep using them.
- h1 = Light (300). Reveal animations: CSS + IntersectionObserver in `js/anims.js` (GSAP only decorative). No Lenis.
- Measured floors (keep them): body lines ≤72ch, caps/legal text ≥0.68rem, tap targets ≥40px,
  every `<img>` gets width/height (post-pass does it), one h1 per page, no h1→h3 skips
  (card titles after h1 use `<h2 class="c3">`).

## The two surveys (core conversion flows)
- `/is-ibogaine-right-for-me.html` — 6-screen screening quiz, result variants A/B/C (cardiac "yes" always → C).
  Email on the result page is **optional** (spec forbids gating the result).
- `/find-a-provider.html` — 7-page provider match profile. Recognizes returning quiz-takers via
  localStorage (`ig_quiz_record`), computes flags (cardiac/psychiatric/pregnancy/withdrawal/washout),
  never rejects anyone. Engine: `js/survey.js`.
- Copy rules (from the spec, binding): no em dashes in survey copy; never "eligible/qualify/disqualify/rejected";
  never a "contraindications" heading; never promise a call; second person; grade ~10 reading level.
- Specs live at `~/Downloads/survey-1-screening-quiz.md` and `~/Downloads/survey-2-provider-match v2.md`.
- E2E test: `node test-surveys.js` (playwright-core + cached headless Chromium) — script recreated in the
  session scratchpad when needed; covers all variants, flags, recognition, mobile.

## Form submissions
- All forms post through `window.IGForms` (top of `js/main.js`) to a **Google Apps Script receiver**
  that writes to a submissions spreadsheet — set up by a parallel session on 2026-09-30; see
  `_generator/apps-script/` (Code.gs + SETUP.md). Endpoint URL + token live in `js/main.js`.
- WORKING since 2026-10-02: fresh deployment (ID starts AKfycbxfrahy…), Execute as Me / access Anyone.
  All four form types verified delivering end to end. Note for curl tests: Apps Script answers POST via a
  302 redirect — do NOT force `-X POST` through it (gives 405/404); plain `curl -L --data` behaves like fetch.
- As of 2026-10-02 the receiver is live (verified: real token accepted, unknown form rejected).
- hello@legal-ibogaine.com has NO MAILBOX (domain has no MX record), so it was removed from the site
  on 2026-10-02. Contact = a message form on contact.html (`data-guide-form`, posts as form
  "consultation" with `topic: Contact page message`). A failed match send shows "Send my profile
  again" + a link to the contact page. Do not reintroduce the address until forwarding/MX exists.
- Never promise an email or file the receiver does not send. Code.gs only notifies the owners; the
  quiz/resource email offers say the file is "being finished" and will be sent once, when ready.

## Placeholders still pending (ask Bogdan)
- Authorship/medical-reviewer names for E-E-A-T (YMYL site, currently no bylines).
- Resource PDFs (4 gated downloads + "cardiac screening sheet" + "taper discussion sheet") don't exist yet.
- 5-email post-quiz sequence (spec §6) is ESP-side, not built.
- `consultation.html` DELETED (2026-10-01). `quiz.html` redirect stub remains, noindexed. New page: `vetting-standard.html` (the published standard every disclosure links to).
- SEO state (2026-10-01): meta titles ≤60 / descriptions ≤165 via `htitle`/`mdesc` override keys, llms.txt at root,
  dynamic "Updated" date, both old Netlify duplicate sites pending deletion by Bogdan.

## Related sites (same content, different designs, separate folders)
- `../ibogaine-guide/` (port 8341) and `../ibogaine-review/` (port 8342, Netlify "ibogaine-review").
  This folder (sanctuary) is the primary/live one.
