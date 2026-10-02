# Root pages — Ibogaine section + Is It Right For Me section (component layouts)

CHK = '<svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'
CROSS = '<svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>'
INFO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg>'

PAGES = [

# ============================================================ what-is
{
"slug": "what-is-ibogaine",
"mdesc": "What ibogaine is, where it comes from, and what it can and cannot do. The plain-language starting point for understanding this treatment.",
"kicker": "Ibogaine",
"title": "What is ibogaine?",
"htitle": "What Is Ibogaine?",
"desc": "A psychoactive alkaloid from a Central African shrub, best known for interrupting patterns — chemical and psychological — that people have spent years trying to out-think.",
"body": """
<div class="page-body">
<div class="prose">
<h2 class="sec-label">The short version</h2>
<p>Ibogaine comes from the root bark of <em>Tabernanthe iboga</em>, a shrub native to Gabon, used for generations in Bwiti spiritual practice. It entered Western awareness in 1962, when a young New Yorker with a heroin habit took it for the experience — and noticed afterward that his withdrawal never came. That accidental observation has since been documented, in the same direction, by independent clinical teams on three continents.</p>
</div>

<div class="split-block">
  <div>
    <h2 class="sec-label">One dose, two molecules</h2>
    <p style="color: var(--muted);">The liver converts ibogaine into <strong style="color: var(--ink);">noribogaine</strong>, a long-acting metabolite that stays in the body for weeks. The intense, dream-like experience lasts about a day; the pharmacological tail unwinds slowly over the following month.</p>
    <ul class="icon-list">
      <li>""" + CHK + """<span><strong>Hours 1–24:</strong> the acute experience — a waking, dream-like life review</span></li>
      <li>""" + CHK + """<span><strong>Weeks 1–4:</strong> the window — craving quiet, mood supported, patterns loose</span></li>
    </ul>
  </div>
  <figure class="ph-media"><span class="ph-frame"><img class="mono" src="assets/img/leaves.jpg" alt="Dense green tropical foliage" loading="lazy"></span><figcaption>Fig. — The alkaloid's botanical family</figcaption></figure>
</div>

<h2 class="sec-label">What people use it for</h2>
<div class="evidence-grid cols-2" style="gap: 32px 40px;">
  <div class="evidence-item"><span class="num">01</span><h2 class="c3">Opioid dependence</h2><p>The most-studied application: interruption of withdrawal and craving, without substituting another opioid.</p></div>
  <div class="evidence-item"><span class="num">02</span><h2 class="c3">Alcohol &amp; other substances</h2><p>Reported benefit across dependencies, with a thinner evidence base than opioids.</p></div>
  <div class="evidence-item"><span class="num">03</span><h2 class="c3">PTSD, trauma &amp; mood</h2><p>The 2024 Stanford veterans study documented large improvements in PTSD, depression, and anxiety.</p></div>
  <div class="evidence-item"><span class="num">04</span><h2 class="c3">Patterns that won't move</h2><p>A growing group comes not in crisis but stuck: burnout, compulsion, a loop that willpower hasn't broken.</p></div>
</div>

<h2 class="sec-label">What it is not</h2>
<ul class="icon-list">
  <li>""" + CROSS + """<span><strong>Not a cure.</strong> It interrupts; what happens in the weeks after decides the outcome.</span></li>
  <li>""" + CROSS + """<span><strong>Not an approved medicine.</strong> No large controlled trial completed yet — formal trials are funded and underway.</span></li>
  <li>""" + CROSS + """<span><strong>Not casual.</strong> A serious medical undertaking that belongs in a screened, supervised setting.</span></li>
</ul>

<div class="keybox">""" + INFO + """<p>If you remember one thing: ibogaine opens a <strong>window</strong>, not a door marked "cured." The evidence for the window is strong; what you build inside it is the treatment.</p></div>

<h2 class="sec-label">Where to go next</h2>
<div class="router-grid cols-3">
  <a class="router-card" href="how-it-works.html"><span class="rc-k">Next</span><h3>How it works</h3><p>The mechanism, told for humans first.</p><span class="go">Read →</span></a>
  <a class="router-card" href="eligibility.html"><span class="rc-k">Then</span><h3>Eligibility</h3><p>Who it fits, who it doesn't, and the quiz.</p><span class="go">Check →</span></a>
  <a class="router-card" href="research.html"><span class="rc-k">Deeper</span><h3>Research</h3><p>The evidence base, study by study.</p><span class="go">Explore →</span></a>
</div>
</div>
""",
"cta": True,
},

# ============================================================ how it works
{
"slug": "how-it-works",
"kicker": "Ibogaine",
"title": "How ibogaine works",
"htitle": "How Ibogaine Works",
"desc": "Most drugs aim at one target. Ibogaine touches many at once — which may be exactly why it does what it does.",
"body": """
<div class="page-body">
<div class="prose">
<h2 class="sec-label">Pattern interruption, literally</h2>
<p>Dependency, trauma responses, and compulsive loops are not character flaws — they are circuits, wired in by thousands of repetitions. Ibogaine appears to act on that wiring directly, in three acts:</p>
</div>

<div class="timeline">
  <div class="tl-item">
    <span class="tl-dot">01</span>
    <span class="tl-k">Hours 1–24</span>
    <h2 class="c3">The reset</h2>
    <p>Ibogaine interacts with opioid receptors in an atypical way — not substituting like methadone, but appearing to shift the receptor system's adapted state back toward baseline. This is the leading explanation for withdrawal that largely fails to arrive.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">02</span>
    <span class="tl-k">Alongside</span>
    <h2 class="c3">The review</h2>
    <p>A long, dream-like state most describe as a life review: memories replayed with unusual detachment — witnessing rather than reliving. Whether this experience is essential or incidental is one of the field's live questions.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">03</span>
    <span class="tl-k">Weeks 1–4</span>
    <h2 class="c3">The long tail</h2>
    <p>The metabolite noribogaine takes over: a strong serotonin-reuptake inhibitor with opioid-system activity, clearing slowly over weeks. Craving stays quiet; mood is supported; the taper is built in.</p>
  </div>
</div>

<h2 class="sec-label">Under the hood</h2>
<table style="width:100%; border-collapse: collapse; font-size: 0.92rem; margin: 8px 0 16px;">
  <tr style="border-bottom: 1px solid var(--ink);"><th style="text-align:left; padding: 10px 12px 10px 0; font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase;">Target</th><th style="text-align:left; padding: 10px 0; font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase;">Proposed role</th></tr>
  <tr style="border-bottom: 1px solid var(--hairline);"><td style="padding: 11px 12px 11px 0;"><strong>μ / κ opioid receptors</strong></td><td style="padding: 11px 0; color: var(--muted);">Withdrawal suppression without substitution</td></tr>
  <tr style="border-bottom: 1px solid var(--hairline);"><td style="padding: 11px 12px 11px 0;"><strong>Serotonin transporter</strong></td><td style="padding: 11px 0; color: var(--muted);">Mood support in the post-treatment window</td></tr>
  <tr style="border-bottom: 1px solid var(--hairline);"><td style="padding: 11px 12px 11px 0;"><strong>NMDA receptors</strong></td><td style="padding: 11px 0; color: var(--muted);">Anti-craving; destabilizing learned loops</td></tr>
  <tr style="border-bottom: 1px solid var(--hairline);"><td style="padding: 11px 12px 11px 0;"><strong>Nicotinic α3β4</strong></td><td style="padding: 11px 0; color: var(--muted);">Reduced drug self-administration (animal data)</td></tr>
  <tr><td style="padding: 11px 12px 11px 0;"><strong>GDNF pathway</strong></td><td style="padding: 11px 0; color: var(--muted);">Neuroplasticity — durable circuit change</td></tr>
</table>
<p style="color: var(--muted); font-size: 0.92rem;">No single row explains the clinical picture; the breadth may be the point. Full receptor detail: <a href="library/pharmacology-of-ibogaine.html">the pharmacology entry</a>.</p>

<div class="keybox">""" + INFO + """<p><strong>The honest asterisk:</strong> much of this map comes from animal and lab work. The clinical observations are consistent; the wiring diagram behind them is still partly hypothesis. Anyone who tells you exactly how ibogaine works is ahead of the science.</p></div>
</div>
""",
"cta": True,
},

# ============================================================ research
{
"slug": "research",
"kicker": "Ibogaine",
"title": "The research",
"htitle": "Ibogaine Research",
"desc": "Six decades of observation, one landmark study, and a funded trial pipeline. The state of the science — including what nobody can promise you yet.",
"body": """
<div class="fact-grid" style="margin-bottom: 64px;">
  <div class="fact"><strong>1901</strong><span>Year ibogaine was first isolated from iboga root bark</span></div>
  <div class="fact"><strong>191</strong><span>Patients in the largest published open-label treatment series</span></div>
  <div class="fact"><strong>30</strong><span>Veterans in the 2024 Stanford MISTIC cohort</span></div>
  <div class="fact"><strong>$50M</strong><span>Public funds committed to FDA-track trials (Texas, 2025)</span></div>
</div>

<div class="evidence-grid" style="margin-bottom: 56px;">
  <div class="evidence-item"><span class="num">01</span><h2 class="c3">Withdrawal interruption</h2><p>Independent teams on three continents keep documenting the same thing: a single dose can switch off opioid withdrawal — without replacing one dependency with another.</p></div>
  <div class="evidence-item"><span class="num">02</span><h2 class="c3">Craving that goes quiet</h2><p>People report the pull going quiet for weeks after treatment — long after the medicine has left the body. The follow-up data backs them.</p></div>
  <div class="evidence-item"><span class="num">03</span><h2 class="c3">The metabolite explanation</h2><p>Ibogaine converts to noribogaine, which clears over weeks. Its receptor activity is the leading account of the extended effect window.</p></div>
  <div class="evidence-item"><span class="num">04</span><h2 class="c3">A neuroplasticity signal</h2><p>In animal models, ibogaine upregulates GDNF in dopamine circuitry — placing it among compounds that may promote rewiring, not just relief.</p></div>
  <div class="evidence-item"><span class="num">05</span><h2 class="c3">The evidence ceiling</h2><p>No adequately powered randomized controlled trial has been completed. Every efficacy claim above rests on observational data.</p></div>
  <div class="evidence-item"><span class="num">06</span><h2 class="c3">Institutional momentum</h2><p>A Nature Medicine publication, state trial funding, and engineered analogs have moved ibogaine to a funded research agenda.</p></div>
</div>

<div class="keybox">""" + INFO + """<p>The observational signal is too strong to dismiss — and too unconfirmed to declare settled. <strong>Both statements are true at once.</strong> That is the position of this entire site.</p></div>

<h2 class="sec-label">Read the detail</h2>
<div class="router-grid">
  <a class="router-card" href="library/ibogaine-evidence-overview.html"><span class="rc-k">Start</span><h3>The 2026 overview</h3><p>The whole field in one entry.</p><span class="go">Read →</span></a>
  <a class="router-card" href="library/clinical-studies-summarized.html"><span class="rc-k">Data</span><h3>Every major study</h3><p>What each measured, found, and can't show.</p><span class="go">Read →</span></a>
  <a class="router-card" href="library/mistic-study-close-read.html"><span class="rc-k">Landmark</span><h3>MISTIC close read</h3><p>The paper that changed the conversation.</p><span class="go">Read →</span></a>
  <a class="router-card" href="library/open-questions.html"><span class="rc-k">Next</span><h3>Open questions</h3><p>What rigorous trials must answer.</p><span class="go">Read →</span></a>
</div>
""",
"cta": True,
},

# ============================================================ eligibility
{
"slug": "eligibility",
"kicker": "Is it right for me?",
"title": "Eligibility",
"htitle": "Ibogaine Eligibility",
"desc": "Ibogaine is not for everyone — and the exclusions are not fine print, they are the whole game.",
"body": """
<div class="page-body">
<div class="arenot-grid" style="margin-bottom: 8px;">
  <div class="arenot">
    <h2 class="c3">Who tends to be a candidate</h2>
    <ul>
      <li>""" + CHK.replace('i-yes','yes-i') + """<span>Opioid, alcohol, or stimulant dependence — especially where other approaches have repeatedly failed</span></li>
      <li>""" + CHK.replace('i-yes','yes-i') + """<span>PTSD, trauma, or treatment-resistant depression that has plateaued under conventional care</span></li>
      <li>""" + CHK.replace('i-yes','yes-i') + """<span>High-functioning but stuck — capable, outwardly fine, privately exhausted by a loop</span></li>
      <li>""" + CHK.replace('i-yes','yes-i') + """<span>Able to travel to a country where treatment is lawful, and serious about aftercare</span></li>
    </ul>
  </div>
  <div class="arenot not">
    <h2 class="c3">Who is typically ruled out</h2>
    <ul>
      <li>""" + CROSS.replace('i-no','no-i') + """<span>Heart conditions — arrhythmia, prolonged QT, structural disease, prior cardiac events</span></li>
      <li>""" + CROSS.replace('i-no','no-i') + """<span>Certain daily medications, including some antidepressants and methadone (transition protocols exist, but take time)</span></li>
      <li>""" + CROSS.replace('i-no','no-i') + """<span>Severe liver or kidney impairment</span></li>
      <li>""" + CROSS.replace('i-no','no-i') + """<span>History of psychosis · pregnancy</span></li>
    </ul>
  </div>
</div>
<p style="color: var(--muted); font-size: 0.92rem; max-width: 68ch;">The exclusions exist because ibogaine affects the heart's electrical rhythm. If one applies to you, the conversation starts with a physician and an ECG, not a booking form — the full medical logic is on <a href="safety-protocols.html">Safety &amp; Protocols</a>, and <a href="alternatives.html">the alternatives page</a> shows what still works if the answer is no.</p>

<h2 class="sec-label">Orient yourself in two minutes</h2>
<p style="max-width: 68ch;">The quiz below won't diagnose anything — only proper medical screening can. It will tell you, directionally, whether ibogaine is worth a serious conversation in your case.</p>
</div>
@@QUIZ@@
""",
"cta": True,
},

# ============================================================ vetting standard
{
"slug": "vetting-standard",
"kicker": "Our standard",
"title": "The vetting standard",
"htitle": "Provider Vetting Standard",
"desc": "What we require before a provider receives a single introduction — and what gets a provider declined. Published in full, applied to everyone.",
"body": """
<div class="page-body">
<p style="max-width:68ch;">Every provider we work with is held to the standard on this page. It is built from the published safety literature and from how properly run programs actually operate. A provider who fails it does not receive introductions, whatever they offer to pay.</p>

<h2 class="sec-label">Screening — before anyone travels</h2>
<ul class="icon-list">
  <li><span>Medical screening performed by a named, verifiable, licensed physician, involved before travel</span></li>
  <li><span>A 12-lead ECG and blood work, including liver and kidney panels, before any dose</span></li>
  <li><span>A screening process with the authority to say no — a program that never declines anyone is theatre</span></li>
</ul>

<h2 class="sec-label">Supervision — during treatment</h2>
<ul class="icon-list">
  <li><span>Continuous cardiac monitoring through at least the first 24 hours — not periodic vitals checks</span></li>
  <li><span>Medical staff physically present during the session</span></li>
  <li><span>Defibrillator and IV access on site, staff current in advanced life support, and a realistic hospital plan</span></li>
  <li><span>Pharmaceutical-grade ibogaine with certificates of analysis, dosed by body weight</span></li>
  <li><span>Structured transitions for methadone, buprenorphine, and fentanyl — never "come as you are"</span></li>
</ul>

<h2 class="sec-label">Honesty — before, during, and after</h2>
<ul class="icon-list">
  <li><span>Aftercare that is defined: named follow-up contact and integration support, not a farewell dinner</span></li>
  <li><span>Outcome claims matched by methodology — precise success rates with no follow-up process are fiction</span></li>
  <li><span>A specific, immediate answer to "who should not come to you?"</span></li>
</ul>

<h2 class="sec-label">How we apply it</h2>
<p style="max-width:68ch;">We put the <a href="choosing-a-provider.html">twelve questions</a> behind this standard to every provider directly, and we verify what can be verified. When you submit a <a href="find-a-provider.html">provider match profile</a>, your case only goes to providers who have already passed. Providers pay us a placement fee when an introduction succeeds; you pay us nothing, and the fee never overrides this page.</p>
</div>
""",
"cta": True,
},

# ============================================================ safety

{
"slug": "safety-protocols",
"mdesc": "Ibogaine's real risks and how proper screening manages them: ECG, blood work, continuous cardiac monitoring, and the protocols that save lives.",
"kicker": "Is it right for me?",
"title": "Safety &amp; protocols",
"htitle": "Safety & Protocols",
"desc": "Ibogaine is powerful medicine and must be treated with absolute respect. The risks are real, specific, and — in a properly run clinical setting — systematically managed.",
"body": """
<div class="page-body">
<div class="keybox warn" style="margin-top: 0;">""" + INFO + """<p><strong>The risk, named plainly:</strong> ibogaine prolongs the QT interval — the heart's recharge time between beats. In vulnerable people that can trigger dangerous arrhythmias. Documented fatalities cluster around three factors: undetected heart conditions, other drugs still in the system, and settings with no medical screening or monitoring at all.</p></div>

<h2 class="sec-label">What proper screening looks like</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">S·01</span><h3>12-lead ECG</h3><p>Read by someone qualified to interpret it — before any dose, no exceptions.</p></div>
  <div class="qcard"><span class="qn">S·02</span><h3>Blood work</h3><p>Electrolytes, liver and kidney function — the chemistry that determines how the body handles the dose.</p></div>
  <div class="qcard"><span class="qn">S·03</span><h3>Full disclosure</h3><p>Every medication and substance, verified where possible. Screening only protects you if the inputs are true.</p></div>
  <div class="qcard"><span class="qn">S·04</span><h3>A clinician who can say no</h3><p>History review by a licensed clinician with authority to reject. A screening process that never rejects anyone is theatre.</p></div>
</div>

<h2 class="sec-label">What proper supervision looks like</h2>
<ul class="icon-list">
  <li>""" + CHK + """<span>Treatment overseen by a <strong>licensed physician</strong>, supported by nursing staff</span></li>
  <li>""" + CHK + """<span><strong>Continuous cardiac monitoring</strong> through the session and beyond it — the metabolite keeps working after the visions end</span></li>
  <li>""" + CHK + """<span>IV access in place, emergency equipment on site, staff trained in resuscitation</span></li>
  <li>""" + CHK + """<span>A realistic plan for reaching a hospital</span></li>
  <li>""" + CHK + """<span>Protocols aligned with <strong>GITA guidelines</strong>, plus newer cardiac-protective measures such as IV magnesium (used in the 2024 Stanford study)</span></li>
</ul>

<div class="keybox">""" + INFO + """<p><strong>The one-sentence summary:</strong> the danger is concentrated where medicine is absent. Depth is only possible because safety comes first — and a provider who treats screening as a formality has already told you everything you need to know.</p></div>

<h2 class="sec-label">Next step</h2>
<div class="router-grid cols-2" style="max-width: 640px;">
  <a class="router-card" href="choosing-a-provider.html"><span class="rc-k">Apply this</span><h3>Choosing a provider</h3><p>The 12 questions that expose whether any of the above is real.</p><span class="go">Get the questions →</span></a>
  <a class="router-card" href="quiz.html"><span class="rc-k">Orient</span><h3>Eligibility quiz</h3><p>Two minutes, directional, honest.</p><span class="go">Take it →</span></a>
</div>

<h2 class="sec-label">Sources</h2>
<ul class="icon-list" style="font-size: 0.88rem;">
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Alper et al. (2012), fatality review, <em>J Forensic Sci</em> · Koenig &amp; Hilber (2015), cardiac pharmacology, <em>Molecules</em></span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Global Ibogaine Therapy Alliance (2015), <em>Clinical Guidelines for Ibogaine-Assisted Detoxification</em></span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Cherian et al. (2024), magnesium–ibogaine protocol, <em>Nature Medicine</em> — full analysis in <a href="library/mistic-study-close-read.html">our close read</a></span></li>
</ul>
</div>
""",
"cta": True,
},

# ============================================================ what to expect
{
"slug": "what-to-expect",
"kicker": "Is it right for me?",
"title": "What to expect",
"htitle": "What to Expect",
"desc": "From the first phone call to the flight home — the honest, stage-by-stage shape of a properly run ibogaine treatment.",
"body": """
<div class="page-body">
<div class="timeline">
  <div class="tl-item">
    <span class="tl-dot">01</span>
    <span class="tl-k">Weeks before</span>
    <h2 class="c3">Preparation</h2>
    <p>Medical records, a full medication list, honest disclosure. Some medications need tapering; long-acting opioids like methadone are transitioned to short-acting ones first. A provider who skips this phase is a provider to skip.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">02</span>
    <span class="tl-k">Days 1–2</span>
    <h2 class="c3">Screening &amp; intake</h2>
    <p>ECG, blood work, physician interview — and psychological alignment: what you're carrying in, what you want out. For opioid patients, dosing is timed to the onset of early withdrawal.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">03</span>
    <span class="tl-k">Treatment day · hours 1–8</span>
    <h2 class="c3">The visionary phase</h2>
    <p>A dream-like, eyes-closed state — often a detached life review. You stay aware and oriented. Coordination goes; walking requires help; nausea is common. Monitoring runs continuously.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">04</span>
    <span class="tl-k">Hours 8–24</span>
    <h2 class="c3">The processing phase</h2>
    <p>Visions fade into quiet, reflective wakefulness. Sleep rarely comes. This is where medical supervision earns its cost.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">05</span>
    <span class="tl-k">The day after</span>
    <h2 class="c3">The grey day</h2>
    <p>Profoundly tired, emotionally raw — and, for opioid patients, typically without the withdrawal that would ordinarily be raging. Quiet and patience are the agenda.</p>
  </div>
  <div class="tl-item">
    <span class="tl-dot">06</span>
    <span class="tl-k">Days 3–7</span>
    <h2 class="c3">Surfacing</h2>
    <p>Sleep rebuilds, energy returns, the session's material starts arranging itself into meaning. Good programs use these days deliberately: rest, integration sessions, and the reset-tolerance conversation no one should skip.</p>
  </div>
</div>

<div class="split-block">
  <figure class="ph-media"><span class="ph-frame"><img class="mono" src="assets/img/support.jpg" alt="Two people talking over coffee at a table" loading="lazy"></span><figcaption>Fig. — Integration is half the treatment</figcaption></figure>
  <div>
    <h2 class="sec-label">The months after</h2>
    <p style="color: var(--muted);">Every follow-up study says the same thing: the treatment opens a window; what you build in it decides the result. Integration support, therapy, environment changes, and community are not accessories — they are the second half of treatment.</p>
    <p style="color: var(--muted); margin: 0;">Providers who treat aftercare as an afterthought are selling half a process.</p>
  </div>
</div>
</div>
""",
"cta": True,
},

]

# ============================================================ aftercare
PAGES.append({
"slug": "aftercare",
"kicker": "Is it right for me?",
"title": "Aftercare &amp; integration",
"htitle": "Aftercare & Integration",
"desc": "Every follow-up study agrees: the treatment opens a window, and what you build inside it decides the outcome. This page is the second half of ibogaine treatment.",
"body": """
<div class="page-body">
<div class="keybox" style="margin-top: 0;">""" + INFO + """<p><strong>Why this page matters most:</strong> across every dataset, long-term outcomes track what happens <strong>after</strong> treatment more closely than anything about the session itself. People who plan aftercare before they travel do meaningfully better than people who improvise it afterward.</p></div>

<h2 class="sec-label">The window, and what fills it</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">A·01</span><h3>Structured support</h3><p>Therapy or counselling starting within days of returning — ideally arranged before you leave, with someone experienced in addiction or trauma.</p></div>
  <div class="qcard"><span class="qn">A·02</span><h3>Processing the experience</h3><p>The session's material tends to carry personal meaning. Journalling, integration sessions, and facilitated groups all have a place.</p></div>
  <div class="qcard"><span class="qn">A·03</span><h3>Environment</h3><p>Distance from active-use contacts and settings; for some, sober living for the first months. The old environment re-runs the old pattern.</p></div>
  <div class="qcard"><span class="qn">A·04</span><h3>Body &amp; community</h3><p>Sleep, food, movement, and people — unglamorous, and cited constantly by those who sustain the change.</p></div>
</div>

<h2 class="sec-label">The plan — five questions, answered in writing, before treatment</h2>
<div class="timeline">
  <div class="tl-item"><span class="tl-dot">01</span><h3>Who is my support professional?</h3><p>Named therapist or counsellor, first session booked for the week you return.</p></div>
  <div class="tl-item"><span class="tl-dot">02</span><h3>Where am I living for 90 days?</h3><p>And who lives there — is the environment part of the solution or part of the loop?</p></div>
  <div class="tl-item"><span class="tl-dot">03</span><h3>What happens if craving returns?</h3><p>Precisely: who do you call, what do you do in the first hour.</p></div>
  <div class="tl-item"><span class="tl-dot">04</span><h3>Who knows about reset tolerance?</h3><p>After ibogaine, opioid tolerance drops sharply — a relapse at the old dose can be fatal. Your household must know this sentence.</p></div>
  <div class="tl-item"><span class="tl-dot">05</span><h3>What fills my weekdays?</h3><p>Structure for the first month, written down before it's needed.</p></div>
</div>

<div class="keybox warn">""" + INFO + """<p><strong>The one non-negotiable:</strong> tolerance reset. It is the single most dangerous fact in post-ibogaine life, and the reason every plan above exists. If someone relapses, the dose that was once routine can now kill. Everyone around the person should know it.</p></div>

<h2 class="sec-label">Get the template</h2>
<p style="max-width: 66ch;">Turn the five questions into a written plan before treatment, when it works best. Providers who ask to see a plan like this before accepting you are showing you a mark of quality.</p>
</div>
""",
"cta": True,
})
