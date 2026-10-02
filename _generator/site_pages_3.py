# Root pages — Conversion / utility + legal

QUIZ_HTML = """
<form class="quiz-card" data-quiz method="POST" novalidate>
  <div class="quiz-q"><fieldset>
    <legend class="q-label">1. What are you hoping ibogaine could help with?</legend>
    <div class="quiz-opts">
      <label class="quiz-opt"><input type="radio" name="q_goal" value="opioid"> Opioid dependence</label>
      <label class="quiz-opt"><input type="radio" name="q_goal" value="alcohol"> Alcohol or another substance</label>
      <label class="quiz-opt"><input type="radio" name="q_goal" value="trauma"> PTSD, trauma, or depression</label>
      <label class="quiz-opt"><input type="radio" name="q_goal" value="pattern"> A pattern I can't break</label>
    </div>
  </fieldset></div>
  <div class="quiz-q"><fieldset>
    <legend class="q-label">2. Have you ever been diagnosed with a heart condition, rhythm abnormality, or had an abnormal ECG?</legend>
    <div class="quiz-opts">
      <label class="quiz-opt"><input type="radio" name="q_heart" value="no"> No</label>
      <label class="quiz-opt"><input type="radio" name="q_heart" value="yes"> Yes</label>
      <label class="quiz-opt"><input type="radio" name="q_heart" value="unsure"> Not sure</label>
    </div>
  </fieldset></div>
  <div class="quiz-q"><fieldset>
    <legend class="q-label">3. Are you currently taking daily medication (including methadone, Suboxone, or antidepressants)?</legend>
    <div class="quiz-opts">
      <label class="quiz-opt"><input type="radio" name="q_meds" value="no"> No</label>
      <label class="quiz-opt"><input type="radio" name="q_meds" value="yes"> Yes</label>
    </div>
  </fieldset></div>
  <div class="quiz-q"><fieldset>
    <legend class="q-label">4. Have you tried conventional treatment for this before?</legend>
    <div class="quiz-opts">
      <label class="quiz-opt"><input type="radio" name="q_tried" value="none"> Not yet</label>
      <label class="quiz-opt"><input type="radio" name="q_tried" value="some"> Once or twice</label>
      <label class="quiz-opt"><input type="radio" name="q_tried" value="many"> Many times — it hasn't held</label>
    </div>
  </fieldset></div>
  <div class="quiz-q"><fieldset>
    <legend class="q-label">5. Could you travel internationally for treatment?</legend>
    <div class="quiz-opts">
      <label class="quiz-opt"><input type="radio" name="q_travel" value="yes"> Yes</label>
      <label class="quiz-opt"><input type="radio" name="q_travel" value="maybe"> Maybe — depends on logistics</label>
      <label class="quiz-opt"><input type="radio" name="q_travel" value="no"> No</label>
    </div>
  </fieldset></div>
  <div class="quiz-q"><fieldset>
    <legend class="q-label">6. What's your timeline?</legend>
    <div class="quiz-opts">
      <label class="quiz-opt"><input type="radio" name="q_when" value="asap"> As soon as possible</label>
      <label class="quiz-opt"><input type="radio" name="q_when" value="months"> In the next 1–3 months</label>
      <label class="quiz-opt"><input type="radio" name="q_when" value="research"> Just researching for now</label>
    </div>
  </fieldset></div>
  <div class="quiz-error" role="alert" style="display:none; color: var(--navy); font-weight: 600; font-size: 0.92rem; margin-bottom: 14px;">Please answer every question — it takes 30 seconds.</div>
  <div class="quiz-q">
    <span class="q-label">7. Where should we send your results?</span>
    <div class="form-row">
      <div class="field" style="margin-bottom:0;">
        <label for="qz-email">Email</label>
        <input id="qz-email" name="email" type="email" autocomplete="email" placeholder="you@email.com" required>
      </div>
      <div class="field" style="margin-bottom:0;">
        <label for="qz-name">First name (optional)</label>
        <input id="qz-name" name="first_name" type="text" autocomplete="given-name">
      </div>
    </div>
  </div>
  <input type="hidden" name="quiz_outcome" value="">
  <button class="btn btn-ink" type="submit">See my result &amp; email it to me</button>
  <div class="form-status" role="status" aria-live="polite"></div>
  <div class="quiz-result good" role="status">
    <h3>You look like a candidate for a real conversation.</h3>
    <p>Nothing in your answers is an obvious rule-out, and your situation is the kind ibogaine is most often used for. A copy of this result with next steps is on its way to your inbox. The next step isn't a booking — it's a short, honest conversation about your specifics, and then proper medical screening.</p>
    <a class="btn btn-ink" href="consultation.html" style="margin-top: 8px;">Request a free consultation</a>
  </div>
  <div class="quiz-result caution" role="status">
    <h3>Worth a conversation — with your cardiac history front and center.</h3>
    <p>A heart condition, rhythm issue, or unknown cardiac status is the single most important factor in ibogaine screening. That doesn't automatically rule you out, but it means an ECG and a physician's judgment come before anything else. We'll tell you honestly what your options look like — and if ibogaine is off the table, <a href="alternatives.html">these evidence-backed alternatives</a> are not.</p>
    <a class="btn btn-ink" href="consultation.html" style="margin-top: 8px;">Request a free consultation</a>
  </div>
  <p class="quiz-note">Directional only — not a medical assessment. Final suitability is always determined by a licensed physician through proper screening.</p>
</form>
"""

def resource_card(kicker, title, desc, resid):
    return f'''          <div class="res-card">
            <span class="rc-k">{kicker}</span>
            <h2 class="c3">{title}</h2>
            <p>{desc}</p>
            <form class="res-gate" data-res-form method="POST" novalidate>
              <input type="hidden" name="resource" value="{resid}">
              <input type="email" name="email" placeholder="you@email.com" aria-label="Email address" required>
              <button class="btn btn-ink" type="submit">Email me when it's ready</button>
              <div class="form-status" role="status" aria-live="polite" style="width:100%;"></div>
            </form>
          </div>'''

PAGES = [

# ============================================================ contact
{
"slug": "contact",
"kicker": "Contact",
"title": "Contact",
"htitle": "Contact",
"desc": "Questions, corrections, or your own situation — reach us any of these ways. We respond within 24 hours.",
"body": """
<form class="form-card" id="contact-form" data-guide-form method="POST" novalidate style="max-width: 640px;">
  <input type="hidden" name="topic" value="Contact page message">
  <div class="field"><label for="c-name">Your name (optional)</label><input id="c-name" name="first_name" type="text" autocomplete="name"></div>
  <div class="field"><label for="c-email">Email address</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
  <div class="field"><label for="c-message">Your message</label><textarea id="c-message" name="message" required></textarea></div>
  <button class="btn btn-ink" type="submit">Send message</button>
  <div class="form-status" role="status" aria-live="polite"></div>
  <p class="quiz-note" style="margin-top: 18px;">A person reads every message and replies by email, within 24 hours. Your message is stored privately and never shared with a provider.</p>
</form>
<ul class="info-list" style="margin-top: 40px;">
  <li><span class="k">Provider match</span><span><a href="find-a-provider.html">Start a provider match profile</a></span></li>
  <li><span class="k">Response time</span><span>Within 24 hours, every day</span></li>
</ul>
<div class="prose" style="margin-top: 40px;">
<p>If your question is about whether ibogaine fits your situation, the fastest route is the <a href="is-ibogaine-right-for-me.html">two-minute screening quiz</a> — it exists precisely for that question. For corrections to any article, send us the entry name and the source using the form above; we take accuracy seriously and fix errors fast.</p>
</div>
""",
"cta": False,
},

# ============================================================ resources
{
"slug": "resources",
"kicker": "Resources",
"title": "Guides &amp; checklists",
"htitle": "Resources",
"desc": "Practical tools for each stage of the decision — vetting providers, preparing properly, and planning the months after. Leave your email and we'll send each one when it's ready.",
"body": """
<div class="res-grid">
RESCARDS
</div>
<p class="quiz-note" style="margin-top: 24px;">These are still being finished. Leave your email and we will send the file once, when it is ready. Nothing else unless you ask.</p>
""",
"cta": True,
},

# ============================================================ quiz standalone
{
"slug": "quiz",
"noindex": True,
"canonical": "is-ibogaine-right-for-me.html",
"kicker": "Eligibility quiz",
"title": "The quiz has moved",
"htitle": "Eligibility Quiz",
"desc": "The screening quiz now lives at its own address.",
"body": """
<div class="page-body">
<p style="max-width:62ch;">The screening quiz now lives at <a href="is-ibogaine-right-for-me.html">is-ibogaine-right-for-me</a>. Taking you there now.</p>
</div>
<script>location.replace('is-ibogaine-right-for-me.html');</script>
""",
"cta": False,
},

# ============================================================ legal: disclaimer
{
"slug": "medical-disclaimer",
"kicker": "Legal",
"title": "Medical disclaimer",
"htitle": "Medical Disclaimer",
"desc": "Please read this before relying on anything published on this site.",
"body": """
<div class="prose">
<p><strong>Legal Ibogaine is an informational resource only.</strong> Nothing on this website constitutes medical advice, diagnosis, or treatment, and nothing here creates a physician–patient relationship of any kind.</p>
<h2>We are not a treatment provider</h2>
<p>Legal Ibogaine does not provide medical care, does not administer or supply ibogaine or any other substance, does not operate a clinic, and is not a telehealth service. Consultations offered through this site are informational conversations about publicly available evidence and practical considerations — they are not medical assessments.</p>
<h2>Ibogaine is a serious, unapproved compound</h2>
<p>Ibogaine is a potent psychoactive substance that is not approved as a medicine by the FDA, EMA, or comparable regulators, is illegal in many jurisdictions, and carries genuine medical risks, including potentially fatal cardiac risks. Decisions about whether to pursue ibogaine treatment must be made with a licensed physician who knows your full medical history, and any treatment should occur only under qualified medical supervision where it is lawful.</p>
<h2>Accuracy and currency</h2>
<p>We work to keep content accurate and sourced, but research evolves and laws change. Content reflects our understanding at the date shown on each page and may contain errors or become outdated. Use it as a starting point for your own verification, not a substitute for it.</p>
<h2>Emergencies</h2>
<p>If you are experiencing a medical emergency, contact your local emergency services immediately. If you are in crisis in the United States, the SAMHSA National Helpline is 1-800-662-4357.</p>
</div>
""",
"cta": False,
},

# ============================================================ legal: privacy
{
"slug": "privacy",
"kicker": "Legal",
"title": "Privacy policy",
"htitle": "Privacy Policy",
"desc": "What we collect, why, and what we will never do with it. Written for humans.",
"body": """
<div class="prose">
<p>Last updated: September 2026. This policy covers legal-ibogaine.com (the "site").</p>
<h2>What we collect</h2>
<ul>
<li><strong>Information you submit through forms</strong> — name, email, phone (if provided), country, and anything you write about your situation, including health-related information you choose to share.</li>
<li><strong>Basic technical data</strong> — standard server logs (IP address, browser type, pages viewed) if analytics are enabled.</li>
</ul>
<h2>Health information — read this part</h2>
<p>When you describe your situation in our consultation, quiz, or resource forms, you may voluntarily share sensitive information about your health. We treat all such information as confidential. Specifically:</p>
<ul>
<li>It is used for exactly one purpose: responding to your request and preparing for a conversation you asked for.</li>
<li>It is never sold, rented, shared with advertisers, or used for marketing lists.</li>
<li>It is transmitted over an encrypted connection and stored in a private Google Workspace account (Google Sheets, and Google Drive for any documents you upload). Access is limited to the people who respond to enquiries.</li>
<li>If you upload an ECG, blood work, or any other medical document, that file is stored in private Drive storage and is never shared outside the provider you asked us to approach.</li>
<li>You should share only what you are comfortable submitting through a website form.</li>
<li>We are an informational service, not a healthcare provider — information you submit is not a medical record and is not covered by HIPAA or equivalent healthcare regulations.</li>
</ul>
<h2>Your rights</h2>
<p>Email us at any time to ask what we hold about you, correct it, or have it deleted. Deletion requests are honored within 30 days.</p>
<h2>Third parties</h2>
<p>Form submissions are received and stored by Google (Sheets and Drive) under Google's privacy policy; fonts are served by Google Fonts. We do not run advertising or tracking pixels, and we do not use a third-party form or marketing platform.</p>
<h2>Contact</h2>
<p>Privacy questions: <a href="contact.html">contact us</a>.</p>
</div>
""",
"cta": False,
},

# ============================================================ legal: terms
{
"slug": "terms",
"kicker": "Legal",
"title": "Terms of use",
"htitle": "Terms of Use",
"desc": "The short, fair version of the rules for using this site.",
"body": """
<div class="prose">
<p>Last updated: September 2026. By using legal-ibogaine.com, you agree to these terms.</p>
<h2>Informational use only</h2>
<p>The site provides general information about ibogaine and related topics. It is not medical, legal, or professional advice, and you use it at your own risk. Our full <a href="medical-disclaimer.html">Medical Disclaimer</a> is part of these terms.</p>
<h2>No unlawful use</h2>
<p>Nothing on this site is an offer to sell, supply, or facilitate access to any controlled substance. You are responsible for knowing and complying with the laws that apply to you.</p>
<h2>Intellectual property</h2>
<p>Site content is © Legal Ibogaine. You may quote brief excerpts with attribution and a link; wholesale reproduction requires permission. Photography credits appear in the footer.</p>
<h2>Limitation of liability</h2>
<p>The site is provided "as is," without warranties of any kind. To the maximum extent permitted by law, Legal Ibogaine and its operators are not liable for any damages arising from use of the site or reliance on its content.</p>
<h2>Changes</h2>
<p>We may update these terms; the date above reflects the current version. Continued use after changes constitutes acceptance.</p>
</div>
""",
"cta": False,
},

]
