#!/usr/bin/env python3
"""Legal Ibogaine site generator v3 — full IA: root pages, library, sitemap."""
import os, sys, datetime, re, json, hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_data_1 import ARTICLES as A1
from review_data_2 import ARTICLES as A2
import site_pages_1, site_pages_2, site_pages_3, site_pages_4
from site_pages_3 import resource_card

ARTICLES = A1 + A2
ROOT_PAGES = site_pages_1.PAGES + site_pages_2.PAGES + site_pages_3.PAGES + site_pages_4.PAGES

# Eligibility page: the embedded quiz became its own page; leave a bridge card.
QUIZ_CTA = '''<div class="dark consult-band" style="margin-top: 34px; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:24px;">
  <div style="max-width: 58ch;">
    <h2 style="color:#FFFFFF; margin:0 0 8px; font-size:clamp(1.3rem,2.6vw,1.8rem);">Take the two-minute screening quiz</h2>
    <p style="margin:0; color:var(--on-dark);">Six questions. Not a medical assessment: a straight, directional answer to whether ibogaine is worth taking further in your situation, with the reasoning spelled out.</p>
  </div>
  <a class="btn btn-ink" href="is-ibogaine-right-for-me.html">Start the quiz</a>
</div>'''
SITE = "https://legal-ibogaine.com"
# Repo root: the folder containing _generator/. Keeps the build portable.
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'

RESOURCES = [
    ("Checklist", "Provider Vetting Checklist", "The 12 questions from our provider guide as a printable one-pager — take it into every clinic call.", "provider-checklist"),
    ("Guide", "Pre-Treatment Preparation Guide", "Medication timing, what to disclose, what to pack, and how to prepare in the weeks before treatment.", "prep-guide"),
    ("Template", "Aftercare Planning Template", "The five questions every aftercare plan must answer, in a fill-in format — built before treatment, when it works best.", "aftercare-template"),
    ("Checklist", "Eligibility Self-Check", "The medical exclusions in plain language, to review with your physician before you spend money on anything.", "eligibility-check"),
]


PAGE_IMG = {
    "what-is-ibogaine": ("iboga-leaves.jpg", "Tabernanthe iboga branches with distinctive orange fruits", "Fig. — Tabernanthe iboga, fruiting branch"),
    "how-it-works": ("vial.jpg", "Gloved hands pipetting into sample vials", "Fig. — Receptor assay, bench work"),
    "research": ("pipette.jpg", "A researcher pipetting samples into tubes", "Fig. — Clinical sample processing"),
    "eligibility": ("stethoscope.jpg", "A stethoscope on a pale blue background", "Fig. — Screening comes first"),
    "safety-protocols": ("monitor.jpg", "A hospital monitor displaying vital signs with a green waveform", "Fig. — Continuous cardiac monitoring"),
    "what-to-expect": ("room.jpg", "A bright, calm bedroom filled with plants", "Fig. — The recovery setting"),
    "legal-status": ("passport.jpg", "A passport resting on a world map beside a camera", "Fig. — Treatment usually means travel"),
    "cost": ("calculator.jpg", "Hands using a calculator at a desk", "Fig. — Budgeting the whole journey"),
    "choosing-a-provider": ("talk.jpg", "Two people in a bright room having a conversation", "Fig. — Ask precise questions"),
    "about": ("jungle-mist.jpg", "Mist drifting through tropical forest", "Fig. — Iboga's native range"),
    "faq": ("leaves.jpg", "Dense green tropical leaves", "Fig. — The source plant family"),
    "consultation": ("support.jpg", "Two people talking over coffee at a table", "Fig. — A conversation, not a pitch"),
    "contact": ("desk.jpg", "A person at a sunlit desk talking on the phone", "Fig. — We respond within 24 hours"),
    "resources": ("checklist.jpg", "A hand ticking items in a checklist notebook", "Fig. — Tools for the decision"),
    "quiz": ("forest-path.jpg", "Stone steps rising through sunlit forest", "Fig. — Orient yourself first"),
    "aftercare": ("support.jpg", "Two people talking over coffee at a table", "Fig. — The second half of treatment"),
    "alternatives": ("hero-forest.jpg", "Light breaking through forest canopy", "Fig. — More than one path"),
}

UPDATED = datetime.date.today().strftime("%B %d, %Y").replace(" 0", " ")

def webp(name):
    return name.replace(".jpg", ".webp")

ORG_LD = """  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Organization","name":"Legal Ibogaine","url":"%s/","logo":"%s/assets/apple-touch-icon.png","description":"Independent ibogaine treatment information."}
  </script>
""" % (SITE, SITE)

# Pages carrying clinical information get MedicalWebPage; logistics, legal and
# contact pages stay plain WebPage. Typing a cost table as medical content is
# the kind of over-claiming that YMYL review penalises.
MEDICAL_PAGES = {
    "what-is-ibogaine", "how-it-works", "research", "eligibility",
    "safety-protocols", "what-to-expect", "aftercare", "alternatives",
    "is-ibogaine-right-for-me",
}

def page_ld(pg, canon):
    """Per-page JSON-LD: the page itself plus a Home > Page breadcrumb."""
    url = f"{SITE}/{canon}"
    node = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage" if pg["slug"] in MEDICAL_PAGES else "WebPage",
        "name": pg["htitle"],
        "description": pg.get("mdesc", pg["desc"]),
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": "Legal Ibogaine", "url": f"{SITE}/"},
        "publisher": {"@type": "Organization", "name": "Legal Ibogaine", "url": f"{SITE}/"},
    }
    if node["@type"] == "MedicalWebPage":
        node["audience"] = {"@type": "MedicalAudience", "audienceType": "Patient"}
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": pg["htitle"], "item": url},
        ],
    }
    out = ""
    for n in (node, crumbs):
        out += '  <script type="application/ld+json">\n  ' + json.dumps(n) + "\n  </script>\n"
    return out

def ld_block(*nodes):
    return "".join(
        '  <script type="application/ld+json">\n  ' + json.dumps(n) + "\n  </script>\n"
        for n in nodes
    )

HOME_LD = ORG_LD + ld_block({
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Legal Ibogaine",
    "url": f"{SITE}/",
    "description": "Independent ibogaine treatment information.",
    "publisher": {"@type": "Organization", "name": "Legal Ibogaine", "url": f"{SITE}/"},
})

LIBRARY_LD = ORG_LD + ld_block(
    {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Article library",
        "url": f"{SITE}/library/index.html",
        "isPartOf": {"@type": "WebSite", "name": "Legal Ibogaine", "url": f"{SITE}/"},
        "publisher": {"@type": "Organization", "name": "Legal Ibogaine", "url": f"{SITE}/"},
    },
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Articles", "item": f"{SITE}/library/index.html"},
        ],
    },
)

def header(P):
    return f'''  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container">
      <nav class="nav-shell" aria-label="Main navigation">
        <a class="brand" href="{P}index.html" aria-label="Legal Ibogaine — home"><span class="mark" aria-hidden="true">I*</span> LEGAL IBOGAINE</a>
        <button class="nav-toggle" aria-expanded="false" aria-label="Open menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
        <ul class="nav-links">
          <li class="has-sub" data-open="false">
            <button type="button" aria-expanded="false" aria-haspopup="true">Learn {CHEV}</button>
            <ul class="sub-menu mega">
              <li class="mg-col">
                <span class="mg-t">Ibogaine</span>
                <a href="{P}what-is-ibogaine.html">What is ibogaine</a>
                <a href="{P}how-it-works.html">How it works</a>
                <a href="{P}research.html">Research</a>
              </li>
              <li class="mg-col">
                <span class="mg-t">Is it right for me?</span>
                <a href="{P}eligibility.html">Eligibility</a>
                <a href="{P}is-ibogaine-right-for-me.html">Screening quiz</a>
                <a href="{P}safety-protocols.html">Safety &amp; protocols</a>
                <a href="{P}what-to-expect.html">What to expect</a>
                <a href="{P}aftercare.html">Aftercare</a>
              </li>
              <li class="mg-col">
                <span class="mg-t">Practical info</span>
                <a href="{P}legal-status.html">Legal status</a>
                <a href="{P}cost.html">Cost</a>
                <a href="{P}choosing-a-provider.html">Choosing a provider</a>
              </li>
            </ul>
          </li>
          <li><a href="{P}library/index.html">Articles</a></li>
          <li><a href="{P}about.html">About</a></li>
          <li><a href="{P}faq.html">FAQ</a></li>
          <li><a href="{P}contact.html">Contact us</a></li>
          <li class="nav-cta"><a class="btn btn-ink" href="{P}find-a-provider.html">Find a provider</a></li>
        </ul>
      </nav>
    </div>
  </header>'''

def footer(P):
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="{P}index.html"><span class="mark" aria-hidden="true">I*</span> LEGAL IBOGAINE</a>
          <p style="font-size:0.9rem; color:var(--muted); max-width:36ch;">Independent ibogaine treatment information for people who've exhausted conventional options.</p>
          <p class="availability">We respond within 24 hours.</p>
        </div>
        <div>
          <p class="fh">Understand</p>
          <ul>
            <li><a href="{P}what-is-ibogaine.html">What is ibogaine</a></li>
            <li><a href="{P}how-it-works.html">How it works</a></li>
            <li><a href="{P}research.html">Research</a></li>
            <li><a href="{P}library/index.html">Articles</a></li>
            <li><a href="{P}faq.html">FAQ</a></li>
          </ul>
        </div>
        <div>
          <p class="fh">Decide &amp; act</p>
          <ul>
            <li><a href="{P}eligibility.html">Eligibility</a></li>
            <li><a href="{P}is-ibogaine-right-for-me.html">Screening quiz</a></li>
            <li><a href="{P}safety-protocols.html">Safety &amp; protocols</a></li>
            <li><a href="{P}legal-status.html">Legal status</a> · <a href="{P}cost.html">Cost</a> · <a href="{P}choosing-a-provider.html">Providers</a></li>
            <li><a href="{P}what-to-expect.html">What to expect</a> · <a href="{P}aftercare.html">Aftercare</a></li>
            <li><a href="{P}find-a-provider.html">Find a provider</a> · <a href="{P}contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-disclaimer">
        <p>In crisis? Contact local emergency services · US: SAMHSA helpline 1-800-662-4357 (free, 24/7)</p>
        <p><a href="{P}medical-disclaimer.html">Medical disclaimer</a> · <a href="{P}privacy.html">Privacy policy</a> · <a href="{P}terms.html">Terms of use</a> · <a href="{P}vetting-standard.html">Vetting standard</a> · <a href="#" onclick="event.preventDefault();window.IGConsent&amp;&amp;window.IGConsent.reopen();">Cookie settings</a></p>
        <p>Legal Ibogaine provides general educational information only. It is not medical advice and is no substitute for consultation with a qualified physician. Ibogaine is a potent, unapproved psychoactive compound, restricted in many jurisdictions. We do not sell, supply, or facilitate access to any controlled substance. We are a placement service: providers pay us a fee when we refer someone they accept. You pay us nothing.</p>
        <p>Iboga plant photography: Hiobson &amp; Marco Schmidt via Wikimedia Commons (CC BY-SA); other photography via Unsplash. © 2026 Legal Ibogaine.</p>
      </div>
    </div>
  </footer>
  <script src="{P}js/main.js"></script>
  <script defer src="{P}js/anims.js"></script>'''

def cta_band(P):
    return f'''    <section class="dark" style="padding: 64px 0; margin-top: 80px;">
      <div class="container" style="display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:20px;">
        <div>
          <h2 style="color:#FFFFFF; margin:0 0 6px; font-size:clamp(1.3rem,2.6vw,1.8rem); max-width:26ch;">Wondering if ibogaine fits your situation?</h2>
          <p style="color:var(--on-dark-muted); margin:0; font-size:0.95rem;">Six questions, two minutes. A straight answer, and we'll tell you honestly if it's no.</p>
        </div>
        <a class="btn btn-paper" href="{P}is-ibogaine-right-for-me.html">Take the screening quiz {ARROW}</a>
      </div>
    </section>'''

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#F5F9F7">
  <title>@@HTITLE@@ — Legal Ibogaine</title>
  <meta name="description" content="@@MDESC@@">
  <link rel="canonical" href="@@URL@@">
  <meta property="og:type" content="website">
  <meta property="og:title" content="@@HTITLE@@ — Legal Ibogaine">
  <meta property="og:description" content="@@MDESC@@">
  <meta property="og:url" content="@@URL@@">
  <meta property="og:image" content="@@OGIMG@@">
  <link rel="icon" type="image/svg+xml" href="@@P@@assets/favicon.svg">
  <meta property="og:site_name" content="Legal Ibogaine">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="@@P@@assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
  <link rel="preload" href="@@P@@assets/fonts/Aileron-Regular.woff" as="font" type="font/woff" crossorigin>
  <link rel="preload" href="@@P@@assets/fonts/Aileron-Light.woff" as="font" type="font/woff" crossorigin>
  <link rel="stylesheet" href="@@P@@css/styles.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <!-- Ahrefs Web Analytics. Cookieless, so it sits outside the consent gate
       that GA4 needs; the data-key is public by design. -->
  <script src="https://analytics.ahrefs.com/analytics.js" data-key="7hwJ/iCWNcvDtrJ++eWUXQ" async></script>
@@JSONLD@@</head>
<body>
'''

def render_root_page(pg):
    P = ""
    body = pg["body"]
    fig = PAGE_IMG.get(pg["slug"])
    figure = ""
    if fig:
        figure = f'''
        <figure class="ph-media">
          <span class="ph-frame"><img class="mono" src="assets/img/{webp(fig[0])}" alt="{fig[1]}"></span>
          <figcaption>{fig[2]}</figcaption>
        </figure>'''
    body = body.replace("@@QUIZ@@", QUIZ_CTA)
    faq_ld = None
    if "@@FAQ@@" in body:
        import json as _json
        qa = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub(r"<[^>]+>","",a)}} for grp, items in site_pages_2.FAQS for q, a in items]
        faq_ld = '  <script type="application/ld+json">\n  ' + _json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":qa}) + '\n  </script>\n'
    body = body.replace("@@FAQ@@", site_pages_2.faq_body())
    if "RESCARDS" in body:
        body = body.replace("RESCARDS", "\n".join(resource_card(*r) for r in RESOURCES))
    ogimg = SITE + "/assets/img/" + (fig[0] if fig else "hero-forest.jpg")
    canon = pg.get("canonical", pg["slug"] + ".html")
    html = HEAD.replace("@@HTITLE@@", pg["htitle"]).replace("@@MDESC@@", pg.get("mdesc", pg["desc"]).replace('"', "&quot;")).replace("@@DESC@@", pg["desc"].replace('"', "&quot;")) \
               .replace("@@URL@@", f"{SITE}/{canon}").replace("@@P@@", P).replace("@@OGIMG@@", ogimg)
    if pg.get("noindex"):
        html = html.replace('<meta name="viewport"', '<meta name="robots" content="noindex,follow">\n  <meta name="viewport"')
    blocks = ORG_LD + page_ld(pg, canon)
    if faq_ld:
        blocks += faq_ld
    html = html.replace("@@JSONLD@@", blocks)
    if pg.get("body_attr"):
        html = html.replace("<body>", f'<body {pg["body_attr"]}>')
    html += header(P)
    if pg.get("raw"):
        html += f'''
  <main id="main">
    <div class="container">
{body}
    </div>
  </main>
''' + footer(P) + "\n</body>\n</html>\n"
        with open(os.path.join(OUT, pg["slug"] + ".html"), "w") as f:
            f.write(html)
        print("wrote", pg["slug"] + ".html")
        return
    hero_cls = "article-hero page-hero" if figure else "article-hero"
    html += f'''
  <main id="main">
    <div class="container">
      <div class="{hero_cls}">
        <div>
          <div class="kicker"><span class="t">{pg["kicker"]}</span><span>Updated {UPDATED}</span></div>
          <h1>{pg["title"]}</h1>
          <p class="lead">{pg["desc"]}</p>
        </div>{figure}
      </div>
{body}
    </div>
'''
    if pg.get("cta"):
        html += cta_band(P) + "\n"
    html += "  </main>\n" + footer(P) + "\n</body>\n</html>\n"
    with open(os.path.join(OUT, pg["slug"] + ".html"), "w") as f:
        f.write(html)
    print("wrote", pg["slug"] + ".html")

# ---------------- Library (articles) ----------------
CTA_BLOCK = '''<div class="inline-cta">
  <p>If something here speaks to your situation, the next step is a five-minute provider match profile. We read it personally, take your case to vetted providers, and come back with the ones who say yes — or tell you honestly if ibogaine is not the answer.</p>
  <a class="btn btn-paper" href="../find-a-provider.html">Find a provider</a>
</div>'''

ART_PAGE = HEAD.replace('content="website"', 'content="article"') + '''@@HEADER@@
  <main id="main">
    <div class="container">
      <div class="article-hero">
        <div class="kicker">
          <span class="t">@@TOPIC@@</span>
          <span>No. @@NO@@</span>
          <span>@@DATE_H@@</span>
          <span>@@READTIME@@ min read</span>
        </div>
        <h1>@@TITLE@@</h1>
        <p class="lead">@@DESC@@</p>
        <figure class="article-figure">
          <img class="mono" src="../assets/img/@@IMGW@@" alt="@@IMGALT@@">
          <figcaption>@@FIGCAP@@</figcaption>
        </figure>
      </div>
      <div class="article-layout">
        <aside class="toc" aria-label="Contents">
          <h2>Contents</h2>
          <ol>
@@TOC@@
          </ol>
        </aside>
        <div class="article-body">
@@BODY@@
          <div class="article-note"><strong>Disclaimer:</strong> This entry is educational and not medical advice. Ibogaine is a potent, unapproved psychoactive compound. Always consult a qualified physician before making treatment decisions.</div>
          <div class="article-refs">
            <h2>References</h2>
            <ol>
@@REFS@@
            </ol>
          </div>
        </div>
      </div>

      <section class="related" aria-label="Related entries">
        <span class="tag">Continue reading</span>
        <div class="lib-list">
@@RELATED@@
        </div>
      </section>
    </div>
@@CTABAND@@
  </main>
@@FOOTER@@
</body>
</html>
'''

def human_date(iso):
    return datetime.date.fromisoformat(iso).strftime("%B %-d, %Y")

def row_html(a):
    idx = ARTICLES.index(a) + 1
    return f'''          <a class="lib-row" data-topic="{a['topic']}" href="{a['slug']}.html">
            <span class="no">{idx:02d}</span>
            <span class="title">{a['title']}</span>
            <span class="topic">{a['topic']}</span>
            <span class="rt">{a['readtime']} min</span>
            <span class="arrow">{ARROW}</span>
          </a>'''

def post_html(a):
    d = datetime.date.fromisoformat(a['date']).strftime("%b %-d, %Y")
    return f'''          <a class="post-row" data-topic="{a['topic']}" href="{a['slug']}.html">
            <span class="thumb"><img class="mono" src="../assets/img/{webp(a['img'])}" alt="{a['imgalt']}" loading="lazy"></span>
            <span class="body">
              <span class="meta"><span class="t">{a['topic']}</span><span>{d}</span><span>{a['readtime']} min read</span></span>
              <h2 class="pr-t">{a['title']}</h2>
              <p>{a['desc']}</p>
              <span class="go">Read entry →</span>
            </span>
          </a>'''

def related_for(a):
    same = [x for x in ARTICLES if x['topic'] == a['topic'] and x['slug'] != a['slug']]
    others = [x for x in ARTICLES if x['topic'] != a['topic'] and x['slug'] != a['slug']]
    return "\n".join(row_html(x) for x in (same + others)[:3])

def render_article(a, no):
    P = "../"
    toc = "\n".join(f'            <li><a href="#{sid}">{label}</a></li>' for sid, label in a['toc'])
    refs = "\n".join(f"              <li>{r}</li>" for r in a['refs'])
    body = a['body'].replace("@@CTA@@", CTA_BLOCK)
    art_ld = """  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Article","headline":"%s","description":"%s","datePublished":"%s","dateModified":"%s","image":"%s/assets/img/%s","author":{"@type":"Organization","name":"Legal Ibogaine","url":"%s/"},"publisher":{"@type":"Organization","name":"Legal Ibogaine"},"mainEntityOfPage":"%s/library/%s.html"}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},{"@type":"ListItem","position":2,"name":"Articles","item":"%s/library/index.html"},{"@type":"ListItem","position":3,"name":"%s"}]}
  </script>
""" % (a['title'].replace('"','\\"'), a['desc'].replace('"','\\"'), a['date'], a['date'], SITE, a['img'], SITE, SITE, a['slug'], SITE, SITE, a['title'].replace('"','\\"'))
    html = (ART_PAGE
        .replace("@@JSONLD@@", art_ld)
        .replace("@@HEADER@@", header(P))
        .replace("@@FOOTER@@", footer(P))
        .replace("@@CTABAND@@", cta_band(P))
        .replace("@@HTITLE@@", a.get('htitle', a['title']))
        .replace("@@MDESC@@", a.get('mdesc', a['desc']))
        .replace("@@TITLE@@", a['title'])
        .replace("@@DESC@@", a['desc'])
        .replace("@@URL@@", f"{SITE}/library/{a['slug']}.html")
        .replace("@@P@@", P)
        .replace("@@OGIMG@@", SITE + "/assets/img/" + a['img'])
        .replace("@@TOPIC@@", a['topic'])
        .replace("@@NO@@", f"{no:02d}")
        .replace("@@DATE_H@@", human_date(a['date']))
        .replace("@@READTIME@@", str(a['readtime']))
        .replace("@@IMGW@@", webp(a['img']))
        .replace("@@IMGALT@@", a['imgalt'])
        .replace("@@FIGCAP@@", a['figcap'])
        .replace("@@TOC@@", toc)
        .replace("@@BODY@@", body)
        .replace("@@REFS@@", refs)
        .replace("@@RELATED@@", related_for(a)))
    with open(os.path.join(OUT, "library", a['slug'] + ".html"), "w") as f:
        f.write(html)
    print("wrote library/" + a['slug'] + ".html")

def render_library_index():
    P = "../"
    rows = "\n".join(post_html(a) for a in ARTICLES)
    html = HEAD.replace("@@HTITLE@@", "Articles").replace("@@DESC@@", "Every Legal Ibogaine article: evidence summaries, pharmacology, history, and research analysis. Filter by topic.") \
               .replace("@@URL@@", f"{SITE}/library/index.html").replace("@@P@@", P).replace("@@OGIMG@@", SITE + "/assets/img/iboga-leaves.jpg").replace("@@JSONLD@@", LIBRARY_LD)
    html += header(P)
    html += f'''
  <main id="main">
    <div class="container">
      <div class="article-hero">
        <div class="kicker"><span class="t">Articles</span><span>{len(ARTICLES)} entries and growing</span></div>
        <h1>Articles</h1>
        <p class="lead">Every entry is sourced, dated, and written for a careful non-specialist. Start with the overview; go as deep as you like.</p>
      </div>
      <div class="filter-bar" role="group" aria-label="Filter entries by topic">
        <button class="filter-btn" data-filter="all" aria-pressed="true">All</button>
        <button class="filter-btn" data-filter="Evidence" aria-pressed="false">Evidence</button>
        <button class="filter-btn" data-filter="Pharmacology" aria-pressed="false">Pharmacology</button>
        <button class="filter-btn" data-filter="History" aria-pressed="false">History</button>
        <button class="filter-btn" data-filter="Research" aria-pressed="false">Research</button>
      </div>
      <div class="post-list">
{rows}
      </div>
    </div>
{cta_band(P)}
  </main>
'''
    html += footer(P) + "\n</body>\n</html>\n"
    with open(os.path.join(OUT, "library", "index.html"), "w") as f:
        f.write(html)
    print("wrote library/index.html")

# Related-article cards repeat other articles' titles and summaries; a change
# there is not a change to this page, so they are left out of the hash too.
_RELATED_RE = re.compile(rb'<section class="related"[^>]*>.*?</section>', re.S)
_UPDATED_RE = re.compile(rb"Updated [A-Z][a-z]+ \d{1,2}, \d{4}")
LASTMOD_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lastmod.json")

def _file_for(url):
    """The generated file a sitemap URL points at."""
    rel = url[len(SITE):].lstrip("/") or "index.html"
    return os.path.join(OUT, rel)

def _lastmods(urls):
    """Date each URL by content, not by build time.

    A page keeps its stored date until its bytes actually change, so rebuilding
    does not tell Google that all 32 pages were revised today. Dates live in
    _generator/lastmod.json and are committed with the site.

    Pass every generated page here, not just the ones in the sitemap. A page
    left out keeps the build-time kicker from UPDATED and so changes its bytes
    on every single build -- which showed up as a spurious quiz.html diff in
    each daily publish commit."""
    try:
        with open(LASTMOD_DB) as f:
            db = json.load(f)
    except (OSError, ValueError):
        db = {}
    today = datetime.date.today().isoformat()
    dates, changed = {}, 0
    for u in urls:
        try:
            with open(_file_for(u), "rb") as f:
                # The "Updated <date>" kicker is stamped at build time, so it is
                # masked out of the hash; otherwise every build re-dates every
                # root page. It is rewritten to the content date below.
                digest = hashlib.sha256(_RELATED_RE.sub(b"", _UPDATED_RE.sub(b"Updated @", f.read()))).hexdigest()
        except OSError:
            dates[u] = db.get(u, {}).get("date", today)
            continue
        rec = db.get(u)
        if rec and rec.get("hash") == digest:
            dates[u] = rec["date"]
        else:
            dates[u] = today
            changed += 1
        db[u] = {"hash": digest, "date": dates[u]}
    db = {u: db[u] for u in urls if u in db}          # drop retired URLs
    for u in urls:                                     # stamp the content date
        try:
            with open(_file_for(u), "rb") as f:
                raw = f.read()
        except OSError:
            continue
        shown = datetime.date.fromisoformat(dates[u]).strftime("%B %-d, %Y").encode()
        fixed = _UPDATED_RE.sub(b"Updated " + shown, raw)
        if fixed != raw:
            with open(_file_for(u), "wb") as f:
                f.write(fixed)
    with open(LASTMOD_DB, "w") as f:
        json.dump(db, f, indent=1, sort_keys=True)
        f.write("\n")
    return dates, changed

# Generated but deliberately kept out of the sitemap: a noindexed redirect
# stub and two retired pages. They still need a content date, or their
# "Updated" kicker is restamped on every build.
UNLISTED = ("quiz", "consultation", "resources")

def render_sitemap():
    listed = [f"{SITE}/"]
    listed += [f"{SITE}/{p['slug']}.html" for p in ROOT_PAGES
               if p['slug'] not in UNLISTED and not p.get("noindex")]
    listed += [f"{SITE}/library/index.html"] + [f"{SITE}/library/{a['slug']}.html" for a in ARTICLES]
    # Date every generated page; list only the ones the sitemap should carry.
    unlisted = [f"{SITE}/{p['slug']}.html" for p in ROOT_PAGES
                if f"{SITE}/{p['slug']}.html" not in listed]
    dates, changed = _lastmods(listed + unlisted)
    items = "\n".join(f"  <url><loc>{u}</loc><lastmod>{dates[u]}</lastmod></url>" for u in listed)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("sitemap:", len(listed), "urls (+robots),", changed, "with a new lastmod")


def render_home():
    P = ""
    body = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "home_body.html")).read()
    html = HEAD.replace("@@HTITLE@@", "Independent Ibogaine Treatment Information") \
               .replace("@@MDESC@@", "Independent, evidence-based guide to ibogaine treatment: eligibility, safety, cost, and vetted providers. Written for people weighing a serious decision.") \
               .replace("@@URL@@", SITE + "/").replace("@@P@@", P).replace("@@OGIMG@@", SITE + "/assets/img/hero-forest.jpg").replace("@@JSONLD@@", HOME_LD)
    html = html.replace("<title>Independent Ibogaine Treatment Information — Legal Ibogaine</title>",
                        "<title>Legal Ibogaine — Independent Ibogaine Treatment Information</title>")
    html = html.replace("</head>", '  <link rel="preload" as="image" href="assets/img/hero-forest.webp">\n</head>')
    feat = []
    for slug in ["ibogaine-evidence-overview", "withdrawal-interruption-mechanisms", "ibogaine-vs-medications"]:
        a = next(x for x in ARTICLES if x["slug"] == slug)
        feat.append(f"""          <a class="router-card" href="library/{a['slug']}.html">
            <span class="rc-k">{a['topic']}</span>
            <h3>{a['title']}</h3>
            <p>{a['desc'][:150].rsplit(' ', 1)[0]}…</p>
            <span class="go">Read →</span>
          </a>""")
    body = body.replace("@@FEATURED@@", '<div class="router-grid cols-3">\n' + "\n".join(feat) + "\n        </div>")
    html += header(P) + "\n" + body + "\n" + footer(P) + "\n</body>\n</html>\n"
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(html)
    print("wrote index.html")

def render_404():
    P = ""
    html = HEAD.replace("@@HTITLE@@", "Page Not Found").replace("@@DESC@@", "That page doesn't exist. Start from the guide's main routes.") \
               .replace("@@URL@@", SITE + "/404.html").replace("@@P@@", P).replace("@@OGIMG@@", SITE + "/assets/img/hero-forest.jpg").replace("@@JSONLD@@", ORG_LD)
    html = html.replace('<link rel="canonical" href="' + SITE + '/404.html">', '<meta name="robots" content="noindex">')
    html += header(P)
    html += f'''
  <main id="main">
    <div class="container">
      <div class="article-hero">
        <div class="kicker"><span class="t">404</span></div>
        <h1>That page doesn't exist.</h1>
        <p class="lead">The link may be old, or the page may have moved. These routes cover everything on the site.</p>
      </div>
      <div class="router-grid" style="margin-bottom: 80px;">
        <a class="router-card" href="index.html"><span class="rc-k">Start</span><h2 class="c3">Home</h2><p>Orientation, trust, and where to go next.</p><span class="go">Go home →</span></a>
        <a class="router-card" href="what-is-ibogaine.html"><span class="rc-k">Learn</span><h2 class="c3">What is ibogaine</h2><p>The plain-language picture, from zero.</p><span class="go">Read →</span></a>
        <a class="router-card" href="library/index.html"><span class="rc-k">Browse</span><h2 class="c3">Articles</h2><p>The full evidence library, filterable by topic.</p><span class="go">Browse →</span></a>
        <a class="router-card" href="find-a-provider.html"><span class="rc-k">Match</span><h2 class="c3">Find a provider</h2><p>A five-minute profile, read personally.</p><span class="go">Start →</span></a>
      </div>
    </div>
  </main>
'''
    html += footer(P) + "\n</body>\n</html>\n"
    with open(os.path.join(OUT, "404.html"), "w") as f:
        f.write(html)
    print("wrote 404.html")

_DIM_CACHE = {}

def _header_dims(path):
    """Intrinsic pixel size read from the file header (WebP, PNG, JPEG), so the
    build gives identical output on Linux, where sips does not exist."""
    import struct
    with open(path, "rb") as f:
        d = f.read(1 << 16)
    if d[:4] == b"RIFF" and d[8:12] == b"WEBP":
        c = d[12:16]
        if c == b"VP8X":
            return 1 + int.from_bytes(d[24:27], "little"), 1 + int.from_bytes(d[27:30], "little")
        if c == b"VP8L":
            b = int.from_bytes(d[21:25], "little")
            return 1 + (b & 0x3FFF), 1 + ((b >> 14) & 0x3FFF)
        if c == b"VP8 ":
            return struct.unpack("<H", d[26:28])[0] & 0x3FFF, struct.unpack("<H", d[28:30])[0] & 0x3FFF
    if d[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", d[16:24])
    if d[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(d):
            if d[i] != 0xFF:
                i += 1
                continue
            m = d[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", d[i + 5:i + 9])
                return w, h
            i += 2 + struct.unpack(">H", d[i + 2:i + 4])[0]
    return None, None

def img_dims(path):
    """Intrinsic pixel size, cached per file: header parse first, sips fallback."""
    if path not in _DIM_CACHE:
        try:
            w, h = _header_dims(path)
        except OSError:
            w, h = None, None
        if w:
            _DIM_CACHE[path] = (w, h)
            return _DIM_CACHE[path]
        import subprocess
        try:
            out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                                 capture_output=True, text=True, timeout=10).stdout
            w = h = None
            for line in out.splitlines():
                if "pixelWidth" in line: w = int(line.split(":")[1])
                if "pixelHeight" in line: h = int(line.split(":")[1])
            _DIM_CACHE[path] = (w, h)
        except Exception:
            _DIM_CACHE[path] = (None, None)
    return _DIM_CACHE[path]

def inject_img_dims():
    """Post-pass: give every <img> explicit width/height (prevents CLS)."""
    import glob as _glob
    n = 0
    for f in _glob.glob(os.path.join(OUT, "*.html")) + _glob.glob(os.path.join(OUT, "library", "*.html")):
        html = open(f).read()
        base = os.path.dirname(f)

        def _fix(m):
            nonlocal n
            tag = m.group(0)
            if "width=" in tag:
                return tag
            src = re.search(r'src="([^"]+)"', tag)
            if not src or src.group(1).startswith("http"):
                return tag
            p = os.path.normpath(os.path.join(base, src.group(1)))
            w, h = img_dims(p)
            if not w:
                return tag
            n += 1
            return tag[:-1] + f' width="{w}" height="{h}">'

        new = re.sub(r"<img [^>]*>", _fix, html)
        if new != html:
            open(f, "w").write(new)
    print("img dims injected:", n)

if __name__ == "__main__":
    for pg in ROOT_PAGES:
        if pg["slug"] == "resources":  # hidden until the PDFs exist
            continue
        render_root_page(pg)
    for i, a in enumerate(ARTICLES, 1):
        render_article(a, i)
    render_library_index()
    render_home()
    render_404()
    inject_img_dims()
    render_sitemap()
    print("done:", len(ROOT_PAGES), "root pages +", len(ARTICLES), "articles")
