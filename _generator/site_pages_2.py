# Root pages — Practical Info + About + FAQ

def faq_item(q, a):
    return f'''          <div class="faq-item" data-open="false">
            <button class="faq-q" aria-expanded="false">{q}
              <svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>
            <div class="faq-a"><p>{a}</p></div>
          </div>'''

FAQS = [
("Basics", [
 ("What is ibogaine, in one sentence?", "A psychoactive alkaloid from the root bark of the African iboga shrub, best known for its reported ability to interrupt opioid withdrawal and quiet craving for weeks after a single dose."),
 ("Is ibogaine the same as iboga?", "Not quite. Iboga is the plant; ibogaine is one purified alkaloid extracted from it. Clinical settings use measured doses of pharmaceutical-grade ibogaine, which allows precise dosing — something raw bark cannot offer."),
 ("Is it a psychedelic like psilocybin or LSD?", "It is psychoactive, but different in kind: it acts on a much broader set of brain targets, produces a long dream-like life review rather than classic psychedelic effects, and leaves behind a metabolite that keeps working for weeks. You remain aware and oriented throughout."),
 ("Does ibogaine cure addiction?", "No. The accurate word is interrupt: it can switch off withdrawal and open a window of reduced craving. What happens in that window — aftercare, environment, support — decides the long-term outcome. Anyone promising a cure is overselling."),
]),
("Treatment &amp; eligibility", [
 ("What conditions is it used for?", "Most-studied: opioid dependence. Also used for alcohol and stimulant dependence, and — with growing research attention — PTSD, trauma, and treatment-resistant depression. Many people come simply because a pattern in their life won't move."),
 ("Who is ruled out?", "People with heart conditions or rhythm abnormalities, certain daily medications, severe liver or kidney impairment, a history of psychosis, and pregnancy. These exclusions exist because ibogaine affects the heart's electrical rhythm — screening is the whole game. See the Eligibility page."),
 ("I'm on methadone or Suboxone. Is that a problem?", "It complicates timing but doesn't automatically rule you out. Long-acting opioids interact badly with ibogaine protocols, so responsible clinics transition you to short-acting opioids over a period first. Be wary of anyone who says 'come as you are.'"),
 ("How long does treatment take?", "The acute experience lasts roughly 24 hours, but a responsible program runs about a week: screening and preparation, the session, and several supervised recovery days before travel."),
 ("Does it work for fentanyl users?", "Fentanyl complicates both the pharmacology and the timing, and most published research predates the fentanyl era. Experienced providers have adapted protocols, but this is exactly the kind of case where provider quality matters most — ask directly about their fentanyl protocol."),
]),
("Safety", [
 ("How dangerous is it, honestly?", "Ibogaine affects heart rhythm and has caused deaths — almost always where screening was absent, heart conditions went undetected, or other drugs were still in the system. With rigorous screening and continuous monitoring the risk drops substantially, but it never reaches zero."),
 ("What does proper screening involve?", "A 12-lead ECG, blood work covering electrolytes and liver and kidney function, full medication and substance disclosure, and a medical history review by a licensed clinician with the authority to say no."),
 ("What should be in place during the session?", "A licensed physician, continuous cardiac monitoring that extends beyond the acute experience, IV access, emergency equipment, staff trained in resuscitation, and a realistic hospital plan. Protocols should align with GITA guidelines."),
 ("Why does monitoring continue after the visions end?", "Because the active metabolite, noribogaine, remains in the body for days to weeks and continues to affect heart rhythm. The medical episode is longer than the experiential one."),
]),
("Practical", [
 ("Where is ibogaine legal?", "It varies completely by country: prohibited in the US and much of Europe, a prescription medicine in New Zealand, and unregulated in countries like Mexico and Costa Rica, where most treatment actually happens. See the Legal Status page for the full picture."),
 ("How much does it cost?", "Programs typically run $5,000–$25,000+ USD for a multi-day stay including medical care, depending on medical intensity. Very cheap offers usually mean the safety infrastructure has been cut — see the Cost page for what drives the price."),
 ("How do I choose a provider?", "Ask precise questions and listen for precise answers: who screens, what monitoring runs during dosing, how they handle methadone and fentanyl, what aftercare actually includes, and who they refuse. Our Choosing a Provider guide gives you the full checklist."),
 ("Will insurance cover it?", "Almost never — ibogaine is unapproved, so treatment is essentially always self-funded. Budget for travel and aftercare as well as the program fee."),
]),
("About this site", [
 ("Are you a clinic?", "No. We are an independent information and placement service. We don't provide treatment and we aren't a telehealth service. Providers pay us a placement fee when we refer someone they accept — you pay us nothing, we publish our vetting standard, and we decline providers who fail it."),
 ("What happens after I submit a provider match profile?", "A person reads it, usually within one business day. We take your case to the providers we think can handle it, describe your medical picture before we describe you, and come back within three business days with the ones who confirmed they can take you. If nobody fits, we tell you that instead of stretching to find someone."),
 ("Can you give me medical advice?", "No — and be suspicious of any website that does. Final suitability is always determined by a licensed physician through proper screening. What we can give you is the evidence, straight, and the right questions to ask."),
]),
]

def faq_body():
    parts = []
    for group, items in FAQS:
        parts.append(f'        <h2 style="margin-top: 48px; font-size: clamp(1.3rem, 2.4vw, 1.7rem);">{group}</h2>')
        parts.append('        <div class="faq-list" style="margin-top: 20px;">')
        for q, a in items:
            parts.append(faq_item(q, a))
        parts.append('        </div>')
    return "\n".join(parts)

PAGES = [

# ============================================================ legal status
{
"slug": "legal-status",
"mdesc": "Where ibogaine is legal, restricted, or unregulated, country by country, and why unregulated never means safe.",
"kicker": "Practical info",
"title": "Legal status",
"htitle": "Ibogaine Legal Status by Country",
"desc": "Ibogaine is banned in some countries, a prescription medicine in others, and simply unregulated in many more. The global picture — and why “unregulated” does not mean “safe”.",
"body": """
<div class="page-body">
<h2 class="sec-label">Three legal categories</h2>
<div class="qcard-grid cols-3">
  <div class="qcard"><span class="qn">A</span><h3>Prohibited</h3><p>Possession and supply are criminal offences.</p></div>
  <div class="qcard"><span class="qn">B</span><h3>Medically restricted</h3><p>Classified as a medicine — lawful only through medical channels.</p></div>
  <div class="qcard"><span class="qn">C</span><h3>Unregulated</h3><p>Not scheduled; clinics operate with no oversight at all.</p></div>
</div>
<p style="color: var(--muted); font-size: 0.92rem;">Ibogaine is not scheduled under the UN drug conventions — every country decides for itself, which is why the map is a patchwork.</p>

<h2 class="sec-label">Status we can tie to a primary source</h2>
<p style="max-width: 68ch;">Every row below links to the statute, regulation or regulator's own record it rests on. Scheduling is amended regularly, so check the linked text for the version in force before you rely on it.</p>
<table>
<tr><th>Country</th><th>Category</th><th>Status and instrument</th></tr>
<tr><td>United States</td><td>Prohibited</td><td>Schedule I of the Controlled Substances Act, DEA code 7260 — no accepted medical use in the federal scheme and no approved product (<a href="https://www.ecfr.gov/current/title-21/chapter-II/part-1308" rel="noopener">21 CFR 1308.11</a>)</td></tr>
<tr><td>France</td><td>Prohibited</td><td>Added to Annex IV of the narcotics list by the order of 12 March 2007, covering <em>Tabernanthe iboga</em>, <em>Tabernanthe manii</em>, ibogaine and their preparations (<a href="https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000647822" rel="noopener">Légifrance</a>)</td></tr>
<tr><td>United Kingdom</td><td>Prohibited</td><td>No named listing; production, supply and import of psychoactive substances are prohibited by the blanket regime of the <a href="https://www.legislation.gov.uk/ukpga/2016/2/contents" rel="noopener">Psychoactive Substances Act 2016</a>. Possession alone is not an offence except in custodial settings</td></tr>
<tr><td>New Zealand</td><td>Medically restricted</td><td>Reclassified as a prescription medicine by the Medicines Classification Committee in November 2009 — the clearest framework anywhere (<a href="https://www.medsafe.govt.nz/profs/class/Minutes/2006-2010/mccMin03Nov2009.htm" rel="noopener">Medsafe minutes</a>)</td></tr>
<tr><td>Australia</td><td>Medically restricted</td><td>Listed in <strong>Schedule 4</strong> of the Poisons Standard, which makes it prescription-only rather than prohibited (<a href="https://www.legislation.gov.au/F2026L00060/asmade/2026-01-30/text/original/pdf" rel="noopener">current Poisons Standard</a>)</td></tr>
<tr><td>European Union</td><td>Medically restricted</td><td>No authorised medicinal product containing ibogaine exists anywhere in the EU; national scheduling then varies state by state (<a href="https://europepmc.org/article/PMC/PMC12899015" rel="noopener">Esperança 2026 review</a>)</td></tr>
</table>

<div class="keybox warn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><p><strong>We corrected this page in October 2026.</strong> It previously listed Australia as prohibited with no lawful therapeutic products. The Poisons Standard lists ibogaine in Schedule 4, which means prescription-only. The earlier entry was wrong.</p></div>

<h2 class="sec-label">The United States, federal and state</h2>
<p style="max-width: 68ch;">US coverage usually stops at "Schedule I", which misses what has changed. Texas has begun funding ibogaine research directly, and it is worth being precise about what that does and does not mean.</p>
<table>
<tr><th>Level</th><th>What is in force</th></tr>
<tr><td>Federal</td><td>Schedule I, DEA code 7260. Treatment outside an authorised research protocol is unlawful, and prosecutions do happen — a Colorado man was sentenced to 48 months for ibogaine distribution in September 2025 (<a href="https://www.dea.gov/press-releases/2025/09/25/broomfield-man-sentenced-48-months-for-ibogaine-distribution" rel="noopener">DEA</a>)</td></tr>
<tr><td>Texas</td><td>Senate Bill 2308 (2025) created a consortium to run FDA drug-development trials of ibogaine and added Chapter 491 to the Health and Safety Code (<a href="https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02308F.htm" rel="noopener">enrolled bill</a>). The budget appropriated <strong>$50 million</strong> to HHSC for fiscal 2026 to implement it (<a href="https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB00001F.pdf" rel="noopener">SB 1, Art. IX §18.74</a>)</td></tr>
<tr><td>Texas, where it stands</td><td>HHSC selected UTHealth Houston as lead institution, but as of October 2026 states that plans submitted so far do not meet Chapter 491's requirements on matching funds and intellectual-property revenue (<a href="https://www.hhs.texas.gov/services/mental-health-substance-use/mental-health-substance-use-resources/ibogaine-clinical-trials" rel="noopener">HHSC</a>)</td></tr>
<tr><td>Other states</td><td>We have found no state that has changed the legal status of ibogaine treatment. Several have considered study or funding bills; none of that makes treatment lawful</td></tr>
</table>
<div class="keybox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><p><strong>State funding is not legalisation.</strong> Texas is paying for trials aimed at eventual FDA approval. Ibogaine remains Schedule I federally, and a state appropriation does not create a lawful route to treatment in Texas or anywhere else in the US.</p></div>

<h2 class="sec-label">Countries we could not verify</h2>
<p style="max-width: 68ch;">These appear on almost every ibogaine legal map, and we could not confirm any of them against a statute or regulator record. The secondary sources disagree with each other, many of them are clinic marketing pages, and several are years out of date. We would rather tell you that than repeat a number we cannot stand behind.</p>
<table>
<tr><th>Country</th><th>What is claimed, and the problem</th></tr>
<tr><td>Thailand</td><td>Ibogaine does not appear in the Thai FDA's published traveller lists, but those are explicitly labelled as <em>examples</em> of Schedule II and III narcotics, so its absence there proves nothing. The complete schedules are searchable only through the <a href="https://permitfortraveler.fda.moph.go.th/" rel="noopener">Thai FDA permit tool</a> and are published in Thai. Secondary sources conflict, and at least one places it in Category 1, the most serious tier. Treat the status as unresolved rather than permissive</td></tr>
<tr><td>Brazil</td><td>Variously described as prescription-legal in São Paulo from 2016, decriminalised for therapeutic use by ANVISA in 2017, and as a controlled substance. These cannot all be right. Check ANVISA directly</td></tr>
<tr><td>South Africa</td><td>Described as Schedule 6 prescription-controlled by some sources and as unscheduled by others. Check the Medicines Control Council schedules</td></tr>
<tr><td>Gabon</td><td>Widely described as legal, with iboga protected as national heritage; export of root bark is also reported to have been restricted since 2019. We could not source either claim to a Gabonese legal text</td></tr>
<tr><td>Sweden · Denmark · Norway · Belgium · Switzerland</td><td>Commonly listed as prohibited. Plausible, and we found no primary instrument naming ibogaine in any of them</td></tr>
<tr><td>Mexico · Costa Rica</td><td>Commonly described as unregulated, which is consistent with most treatment happening there. We found no statute to cite either way, because the claim is about an absence</td></tr>
</table>

<h2 class="sec-label">Where it is unregulated</h2>
<p style="max-width: 68ch;">Most of the world's ibogaine treatment happens where the law is simply silent: <strong>Mexico</strong> (the de facto hub), <strong>Costa Rica</strong>, and several Caribbean and Central American jurisdictions. No licence is required, there are no inspections and no outcome register — the openness that makes treatment accessible makes quality entirely your problem to verify. Unregulated is not a safety rating. It means nobody is checking.</p>

<div class="keybox warn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><p><strong>Three practical consequences:</strong> treatment usually means travel · in unregulated countries the vetting burden is entirely yours · and never transport ibogaine across borders — that is a serious offence everywhere prohibition applies, and the sentence above shows it is enforced.</p></div>

<h2 class="sec-label">Sources</h2>
<p style="color: var(--muted); font-size: 0.88rem;">Last reviewed October 2026. Legal status changes; the links below are the texts themselves, so you can check the current version rather than trusting this page.</p>
<ul class="icon-list" style="font-size: 0.88rem;">
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>United States: <a href="https://www.ecfr.gov/current/title-21/chapter-II/part-1308" rel="noopener">21 CFR 1308.11</a>, Schedule I hallucinogenic substances, DEA code 7260 · enforcement example, <a href="https://www.dea.gov/press-releases/2025/09/25/broomfield-man-sentenced-48-months-for-ibogaine-distribution" rel="noopener">DEA press release, 25 September 2025</a></span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Texas: <a href="https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02308F.htm" rel="noopener">S.B. 2308 (89R), enrolled</a> · <a href="https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB00001F.pdf" rel="noopener">S.B. 1, General Appropriations Act, Article IX §18.74</a> · <a href="https://www.hhs.texas.gov/services/mental-health-substance-use/mental-health-substance-use-resources/ibogaine-clinical-trials" rel="noopener">HHSC, Ibogaine Clinical Trials</a></span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>France: <a href="https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000647822" rel="noopener">Arrêté du 12 mars 2007</a> amending the order of 22 February 1990 listing substances classified as narcotics</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>United Kingdom: <a href="https://www.legislation.gov.uk/ukpga/2016/2/contents" rel="noopener">Psychoactive Substances Act 2016</a></span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>New Zealand: <a href="https://www.medsafe.govt.nz/profs/class/Minutes/2006-2010/mccMin03Nov2009.htm" rel="noopener">Medicines Classification Committee, 42nd meeting minutes, 3 November 2009</a> · a treatment death and a duty-of-care breach by a legal provider, <a href="https://www.hdc.org.nz/decisions/search-decisions/2015/13hdc00966/" rel="noopener">HDC decision 13HDC00966</a></span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Australia: <a href="https://www.legislation.gov.au/F2026L00060/asmade/2026-01-30/text/original/pdf" rel="noopener">Therapeutic Goods (Poisons Standard — February 2026) Instrument</a>, Schedule 4</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>European Union: Esperança, Gomes &amp; Campos 2026, <em>Molecules</em> 31(3):545 — no authorised medicinal products containing ibogaine in the EU (<a href="https://europepmc.org/article/PMC/PMC12899015" rel="noopener">full text</a>)</span></li>
</ul>
</div>
""",
"cta": True,
},

# ============================================================ cost
{
"slug": "cost",
"kicker": "Practical info",
"title": "Cost",
"htitle": "Ibogaine Treatment Cost",
"desc": "What ibogaine treatment actually costs, what drives the price, and why the cheapest option is usually the most expensive decision you can make.",
"body": """
<div class="page-body">
<h2 class="sec-label">The ranges</h2>
<p style="max-width: 68ch;">These are the bands programmes advertised between 2024 and 2026. Prices move, and they are set by each provider rather than by any schedule, so treat the table as orientation and confirm the current figure directly with whoever you are talking to.</p>
<table>
<tr><th>Tier</th><th>Typical price (USD)</th><th>What it usually means</th></tr>
<tr><td>Budget / underground</td><td>Under $4,000</td><td>Minimal medical infrastructure — the savings come out of screening and monitoring</td></tr>
<tr><td>Clinic standard</td><td>$5,000–$10,000</td><td>Multi-day programme: physician screening, cardiac monitoring, nursing, basic aftercare</td></tr>
<tr><td>Premium / residential</td><td>$10,000–$25,000+</td><td>Higher staffing ratios, longer stays, structured integration, extended follow-up</td></tr>
</table>
<p style="color: var(--muted); font-size: 0.92rem;">We do not publish named clinic prices. A quoted price goes out of date quickly, it rarely covers the same things from one provider to the next, and a treatment website is not a source we would cite for anything else on this site. What follows is what the published medical protocols actually require, which is the part you can hold a quote against.</p>

<h2 class="sec-label">What you are actually paying for</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">C·01</span><h3>Medical screening</h3><p>A 12-lead ECG, blood count and metabolic panel, and physician review before you are accepted.</p></div>
  <div class="qcard"><span class="qn">C·02</span><h3>Supervision</h3><p>Physician oversight, nursing, and continuous cardiac telemetry through the session and well beyond it.</p></div>
  <div class="qcard"><span class="qn">C·03</span><h3>Time &amp; medicine</h3><p>Several days of care, using tested pharmaceutical-grade ibogaine with a certificate of analysis.</p></div>
  <div class="qcard"><span class="qn">C·04</span><h3>Aftercare</h3><p>Integration sessions and follow-up — the one element with any supporting outcome data.</p></div>
</div>

<h2 class="sec-label">What the protocols require, and what it costs to provide</h2>
<p style="max-width: 68ch;">Each line below is a real cost, and each is specified in a published study rather than invented by a clinic's marketing. This is the list to price a quote against.</p>
<table>
<tr><th>Requirement</th><th>Where it comes from</th></tr>
<tr><td>12-lead ECG, safety bloodwork and physical exam before acceptance</td><td>A 191-person inpatient series screened exactly this way (<a href="https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2018.00529/full" rel="noopener">Mash 2018</a>)</td></tr>
<tr><td>Potassium and magnesium checked and corrected before dosing</td><td>Required within a defined range in a monitored series; low electrolytes raise arrhythmia risk independently (<a href="https://europepmc.org/article/PMC/PMC9292417" rel="noopener">Knuijver 2022</a>)</td></tr>
<tr><td>Continuous telemetry from before dosing to at least 24 hours after</td><td>Run from one hour before to 24 hours after in the 191-person series (<a href="https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2018.00529/full" rel="noopener">Mash 2018</a>); a prolonged QT interval persisted past 24 hours in 6 of 14 closely screened patients (<a href="https://europepmc.org/article/PMC/PMC9292417" rel="noopener">Knuijver 2022</a>)</td></tr>
<tr><td>Monitoring to 72 hours, and physical assistance throughout</td><td>The most cautious published protocol monitored for 72 hours; every patient in one series was temporarily unable to walk unaided (<a href="https://europepmc.org/article/PMC/PMC10878970" rel="noopener">Cherian 2024</a>)</td></tr>
<tr><td>Supervised medication washout before arrival</td><td>Eight categories of medicine were withdrawn before dosing, including CYP2D6 inhibitors, beta blockers and all psychiatric medication (<a href="https://europepmc.org/article/PMC/PMC10878970" rel="noopener">Cherian 2024</a>)</td></tr>
<tr><td>CYP2D6 genotyping, or a halved dose for poor metabolisers</td><td>Recommended by the authors who measured the interaction; genotype alone drives a more than tenfold spread in clearance (<a href="https://doi.org/10.1002/jcph.471" rel="noopener">Glue 2015</a>)</td></tr>
<tr><td>Physicians on site, IV fluids and electrolytes, resuscitation capability</td><td>Documented at a residential clinic treating 88 surveyed patients (<a href="https://europepmc.org/article/PMC/PMC6157925" rel="noopener">Davis 2017</a>)</td></tr>
</table>

<div class="keybox warn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><p>When a price looks too good, ask which of those seven is missing. The answer is almost always <strong>monitoring hours and pre-dosing screening</strong> — which is another way of saying "the safety". Genotyping and 72-hour telemetry are the first things to disappear from a cheap quote, and they are the two that address the risk that actually kills people.</p></div>

<h2 class="sec-label">Budget beyond the programme fee</h2>
<ul class="icon-list">
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg><span><strong>Travel</strong> — flights and, for most nationalities, an international trip</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg><span><strong>Preparation</strong> — the medication washout is a supervised medical procedure, not an instruction to stop taking tablets, and stopping psychiatric medicine or benzodiazepines carries its own risk</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg><span><strong>Extra nights</strong> — the insomnia after a dose often runs about 72 hours, so plan not to be travelling the next day</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg><span><strong>Aftercare at home</strong> — therapy or coaching in the months after; give it a budget line from day one</span></li>
  <li><svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span><strong>Insurance</strong> — the FDA has approved three medications for opioid use disorder, and ibogaine is not among them, so coverage is essentially nonexistent; assume self-funding</span></li>
</ul>
<p style="color: var(--muted); font-size: 0.92rem;">Treat aggressive financing pressure like any other high-pressure sales tactic — as a red flag. The full list: <a href="choosing-a-provider.html">Choosing a Provider</a>.</p>

<div class="keybox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><p><strong>On aftercare being worth paying for.</strong> The cohort reporting the longest abstinence combined ibogaine with psychotherapy and reported a median of 5.5 months after one treatment and 8.4 after repeat treatment. That study was retrospective with no control group and cannot separate the therapy from the drug, so read it as the best available argument rather than a settled one.</p></div>

<h2 class="sec-label">Sources</h2>
<p style="color: var(--muted); font-size: 0.88rem;">Last reviewed October 2026. Price bands are observed advertised ranges, not a survey, and no clinic pricing page is cited as a source anywhere on this site.</p>
<ul class="icon-list" style="font-size: 0.88rem;">
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Screening and 24-hour telemetry: Mash, Duque, Page &amp; Allen-Ferdinand 2018, <em>Front Pharmacol</em> 9:529 (<a href="https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2018.00529/full" rel="noopener">full text</a>)</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Electrolyte limits and QT persisting past 24 hours: Knuijver et al. 2022, <em>Addiction</em> 117(1) (<a href="https://europepmc.org/article/PMC/PMC9292417" rel="noopener">full text</a>)</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>72-hour monitoring and the medication washout: Cherian et al. 2024, <em>Nat Med</em> 30(2):373-381 (<a href="https://europepmc.org/article/PMC/PMC10878970" rel="noopener">full text</a>)</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>CYP2D6 genotyping and dose reduction: Glue et al. 2015, <em>J Clin Pharmacol</em> 55(6):680-687 (<a href="https://doi.org/10.1002/jcph.471" rel="noopener">doi</a>)</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>On-site physicians, IV fluids and electrolytes at a residential clinic: Davis et al. 2017, <em>J Psychedelic Stud</em> 1(2):65-73 (<a href="https://europepmc.org/article/PMC/PMC6157925" rel="noopener">full text</a>)</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Ibogaine plus psychotherapy, abstinence durations: Schenberg et al. 2014, <em>J Psychopharmacol</em> 28(11):993-1000 (<a href="https://europepmc.org/article/MED/25271214" rel="noopener">abstract</a>)</span></li>
  <li><svg class="i-yes" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.07 0l3-3a5 5 0 00-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 00-7.07 0l-3 3a5 5 0 007.07 7.07l1.5-1.5"/></svg><span>Approved medications for opioid use disorder: <a href="https://www.fda.gov/drugs/food-and-drug-administration-overdose-prevention-framework/information-about-medications-opioid-use-disorder-moud" rel="noopener">US Food and Drug Administration</a></span></li>
</ul>
</div>
""",
"cta": True,
},

# ============================================================ provider
{
"slug": "choosing-a-provider",
"mdesc": "How to vet an ibogaine provider: the questions that separate medical programs from marketing operations, and the red flags that should end a call.",
"kicker": "Practical info",
"title": "Choosing a provider",
"htitle": "Choosing an Ibogaine Provider",
"desc": "In an unregulated field, the questions you ask are the only inspection a clinic will ever face. Twelve of them — with the answers you should hear — plus the red flags that end the conversation.",
"body": """
<div class="page-body">
<div class="keybox" style="margin-top: 0;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><p><strong>The right mental model:</strong> you are not choosing a retreat. You are choosing a medical procedure in a foreign country, in a field with no regulator behind you. Precise questions get you past the brochure.</p></div>

<h2 class="sec-label">The twelve questions</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">Q·01</span><h3>Who performs medical screening?</h3><p>A named, verifiable, licensed physician — involved before you travel.</p></div>
  <div class="qcard"><span class="qn">Q·02</span><h3>What screening before dosing?</h3><p>The only acceptable answer includes a 12-lead ECG and blood work — heart rhythm mentioned unprompted.</p></div>
  <div class="qcard"><span class="qn">Q·03</span><h3>Is cardiac monitoring continuous?</h3><p>Through at least the first 24 hours. “We check vitals regularly” is not the same thing.</p></div>
  <div class="qcard"><span class="qn">Q·04</span><h3>What emergency capability is on site?</h3><p>Defibrillator, IV access as standard, staff current in advanced life support.</p></div>
  <div class="qcard"><span class="qn">Q·05</span><h3>How far is the nearest hospital?</h3><p>Honest providers answer without flinching — and admit transfers have happened.</p></div>
  <div class="qcard"><span class="qn">Q·06</span><h3>How do you handle methadone or fentanyl?</h3><p>Structured transitions and extended timelines — never “come as you are.”</p></div>
  <div class="qcard"><span class="qn">Q·07</span><h3>How is dose determined?</h3><p>By body weight, adjusted for screening, often with a test dose. Never one-size-fits-all.</p></div>
  <div class="qcard"><span class="qn">Q·08</span><h3>What form of ibogaine, and how tested?</h3><p>Pharmaceutical-grade with certificates of analysis — not root bark of unstated potency.</p></div>
  <div class="qcard"><span class="qn">Q·09</span><h3>Who is with the patient during the session?</h3><p>Medical staff physically present — not a camera and a call button.</p></div>
  <div class="qcard"><span class="qn">Q·10</span><h3>What does aftercare actually include?</h3><p>Named follow-up contact, integration sessions, referral relationships — not a farewell dinner.</p></div>
  <div class="qcard"><span class="qn">Q·11</span><h3>What are your outcomes, and how do you know?</h3><p>Honest clinics describe follow-up attempts and limits. Precise success rates with no methodology are fiction.</p></div>
  <div class="qcard"><span class="qn">Q·12</span><h3>Who should NOT come to you?</h3><p>The most revealing question. A trustworthy provider answers immediately and specifically.</p></div>
</div>

<h2 class="sec-label">Red flags that end the conversation</h2>
<ul class="icon-list">
  <li><svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span>Guaranteed results, “cure” language, or booking pressure (“one spot left this month”)</span></li>
  <li><svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span>No physician involvement before arrival, or screening only after payment</span></li>
  <li><svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span>Dismissiveness about cardiac risk</span></li>
  <li><svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span>Unwillingness to name staff, location, or hospital arrangements</span></li>
  <li><svg class="i-no" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span>Prices dramatically below market — see <a href="cost.html">why</a></span></li>
</ul>

</div>
""",
"cta": True,
},

# ============================================================ about
{
"slug": "about",
"kicker": "About",
"title": "About Legal Ibogaine",
"htitle": "About",
"desc": "Independent ibogaine treatment information for people who've exhausted conventional options — written to inform a serious decision, not to sell one.",
"body": """
<div class="prose">
<h2>Why this site exists</h2>
<p>Information about ibogaine comes in two flavors: promotion from people selling treatment, and dismissal from people who stopped reading in 1970. If you're facing a real decision, neither helps. Legal Ibogaine exists to be the third option — a place where the published evidence is summarized honestly, the risks are stated plainly, and nobody is upsold.</p>

</div>
<h2 class="sec-label">How we work</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">01</span><h3>Everything is sourced</h3><p>Claims trace to the peer-reviewed literature; every library entry carries its references.</p></div>
  <div class="qcard"><span class="qn">02</span><h3>Everything is dated</h3><p>Entries are revised as new trials report, and say when they were last updated.</p></div>
  <div class="qcard"><span class="qn">03</span><h3>Hype gets cut both ways</h3><p>The strongest findings and hardest limitations appear in the same paragraph, on purpose.</p></div>
  <div class="qcard"><span class="qn">04</span><h3>Honest conversations</h3><p>When people ask whether ibogaine fits their situation, "no" is an answer we actually give.</p></div>
</div>

<div style="margin: 48px 0;">
  <div class="arenot-grid">
    <div class="arenot">
      <h3>We are</h3>
      <ul>
        <li><svg class="yes-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg><span>An independent information resource</span></li>
        <li><svg class="yes-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg><span>A neutral guide through the ibogaine landscape</span></li>
        <li><svg class="yes-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg><span>A bridge between you and the right provider for your situation</span></li>
      </ul>
    </div>
    <div class="arenot not">
      <h3>We are not</h3>
      <ul>
        <li><svg class="no-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg><span>A treatment clinic</span></li>
        <li><svg class="no-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg><span>A referral service tied to a single partner</span></li>
        <li><svg class="no-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg><span>A medical provider or telehealth service</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="prose">
<h2>Talk to us</h2>
<p>Questions about the evidence, corrections, or your own situation — <a href="contact.html">contact us</a> or <a href="find-a-provider.html">start a provider match profile</a>. We respond within 24 hours, and we'll tell you honestly if ibogaine isn't right for you.</p>
</div>
""",
"cta": True,
},

# ============================================================ faq
{
"slug": "faq",
"kicker": "FAQ",
"title": "Frequently asked questions",
"htitle": "FAQ",
"desc": "Straight answers, grouped by topic — from “what is it” to “what does it cost” to “who should never take it.”",
"body": "@@FAQ@@",
"cta": True,
},

]

# ============================================================ alternatives
PAGES.append({
"slug": "alternatives",
"mdesc": "If ibogaine is ruled out, these evidence-backed alternatives still work: what each offers, the success rates, and how to choose a path that fits.",
"kicker": "Is it right for me?",
"title": "Ruled out? Here's what still works.",
"htitle": "If Ibogaine Isn't an Option",
"desc": "A heart condition, certain medications, or circumstances can take ibogaine off the table. That is not the end of the road — it's a redirect to options with far more evidence behind them.",
"body": """
<div class="page-body">
<div class="prose">
<p>This page exists because an honest guide has to serve the people it turns away. If screening rules you out — or travel, cost, or timing do — the alternatives below are not consolation prizes. Several carry far stronger evidence than ibogaine currently does.</p>
</div>

<h2 class="sec-label">For opioid dependence</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">R·01</span><h3>Buprenorphine (Suboxone)</h3><p>Office-prescribed, strong evidence for reduced mortality and a stabilized life. The most accessible first-line option in many countries.</p></div>
  <div class="qcard"><span class="qn">R·02</span><h3>Methadone maintenance</h3><p>Decades of evidence; the standard of care where retention matters most.</p></div>
  <div class="qcard"><span class="qn">R·03</span><h3>Extended-release naltrexone</h3><p>An opioid blocker for people who complete detox and want no maintenance opioid.</p></div>
  <div class="qcard"><span class="qn">R·04</span><h3>Contingency management &amp; CBT</h3><p>The strongest behavioral evidence base — and for stimulants, the main evidenced option.</p></div>
</div>

<h2 class="sec-label">For PTSD, trauma &amp; mood</h2>
<div class="qcard-grid">
  <div class="qcard"><span class="qn">R·05</span><h3>Trauma-focused therapy</h3><p>EMDR and trauma-focused CBT — first-line, well-evidenced, widely available.</p></div>
  <div class="qcard"><span class="qn">R·06</span><h3>Ketamine-assisted therapy</h3><p>Legally available in clinics in many countries for treatment-resistant depression.</p></div>
  <div class="qcard"><span class="qn">R·07</span><h3>Clinical trials</h3><p>Psychedelic-assisted therapy trials — including ibogaine trials with cardiac protocols — recruit continuously: a lawful, screened path to the same frontier.</p></div>
  <div class="qcard"><span class="qn">R·08</span><h3>Intensive outpatient programs</h3><p>Structure without residential commitment, often insurance-covered where ibogaine never is.</p></div>
</div>

<div class="keybox">""" + '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg>' + """<p>Being ruled out by screening is the system <strong>working</strong>, not failing. The same honesty that says "not this" can also say what's next — <a href="contact.html">talk it through with us</a> and we'll point you to the best-evidenced path for your situation.</p></div>
</div>
""",
"cta": True,
})
