# Survey pages: screening quiz + provider match profile.
# Copy follows the survey specs verbatim. Rules: no em dashes; never
# "eligible", "qualify", "disqualify", "rejected"; never promise a call.

COUNTRIES = [
    "United States", "Canada", "United Kingdom", "Ireland", "Australia", "New Zealand",
    "Mexico", "Brazil", "Argentina", "Chile", "Colombia", "Costa Rica", "Panama",
    "Germany", "France", "Spain", "Portugal", "Italy", "Netherlands", "Belgium",
    "Switzerland", "Austria", "Denmark", "Sweden", "Norway", "Finland", "Iceland",
    "Poland", "Czech Republic", "Slovakia", "Hungary", "Romania", "Bulgaria",
    "Greece", "Croatia", "Serbia", "Ukraine", "Estonia", "Latvia", "Lithuania",
    "Israel", "United Arab Emirates", "Saudi Arabia", "Turkey", "South Africa",
    "Nigeria", "Kenya", "Ghana", "Gabon", "Egypt", "Morocco",
    "India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal", "Thailand", "Vietnam",
    "Philippines", "Indonesia", "Malaysia", "Singapore", "Japan", "South Korea",
    "China", "Hong Kong", "Taiwan", "Russia", "Kazakhstan", "Georgia", "Armenia",
    "Luxembourg", "Malta", "Cyprus", "Slovenia", "Bosnia and Herzegovina",
    "North Macedonia", "Albania", "Moldova", "Belarus", "Peru", "Ecuador",
    "Uruguay", "Paraguay", "Bolivia", "Venezuela", "Guatemala", "Honduras",
    "El Salvador", "Nicaragua", "Dominican Republic", "Jamaica", "Trinidad and Tobago",
    "Bahamas", "Barbados", "Other",
]

COUNTRY_DATALIST = '<datalist id="countries">' + "".join(
    f'<option value="{c}">' for c in COUNTRIES) + "</datalist>"


def opt(name, value, label, kind="radio"):
    return (f'<label class="sv-opt"><input type="{kind}" name="{name}" value="{value}">'
            f'<span>{label}</span></label>')


# ============================================================================
# SURVEY 1: screening quiz  /is-ibogaine-right-for-me
# ============================================================================

QUIZ_PAGE_BODY = '''
<div class="survey-wrap">

  <section class="sv-screen active" id="s0">
    <h1 style="margin-bottom:18px;">Is ibogaine worth a look for me?</h1>
    <p style="max-width:62ch;">Six questions, about two minutes. This is not a medical assessment. It gives you a straight answer to one question: is this worth taking further in your situation?</p>
    <p style="max-width:62ch;">We place people with providers. We do not treat anyone and we do not sell treatment. That means we can tell you when the answer is no.</p>
    <div class="sv-nav"><button type="button" class="btn btn-ink" data-next>Start</button></div>
  </section>

  <section class="sv-screen" id="s1">
    <p class="sv-progress">Screen 1 of 6</p>
    <h2 class="sv-label">What brings you here?</h2>
    <p class="sv-sub">Select everything that applies.</p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("indications", "opioid", "Opioid dependence (heroin, fentanyl, pain medication)", "checkbox"),
          opt("indications", "maintenance", "Methadone, buprenorphine, or Suboxone maintenance", "checkbox"),
          opt("indications", "substance", "Alcohol or another substance", "checkbox"),
          opt("indications", "trauma", "PTSD, trauma, or depression", "checkbox"),
          opt("indications", "tbi", "Traumatic brain injury or a neurological condition", "checkbox"),
          opt("indications", "growth", "Personal growth or spiritual work", "checkbox"),
          opt("indications", "pattern", "A pattern I cannot break", "checkbox"),
      ]) + '''
    </div>
    <p class="sv-micro">Most people tick more than one. Providers specialise, so this shapes the answer more than anything else you tell us.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="s2">
    <p class="sv-progress">Screen 2 of 6</p>
    <h2 class="sv-label">Has a doctor ever told you about a heart condition, an irregular heartbeat, or an abnormal ECG?</h2>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("cardiac_history", "no", "No"),
          opt("cardiac_history", "yes", "Yes"),
          opt("cardiac_history", "unknown", "I don't know"),
      ]) + '''
    </div>
    <p class="sv-micro">Cardiac safety sits at the centre of responsible ibogaine care. In the published review of 19 deaths linked to ibogaine, existing heart disease was the leading contributing factor. Any provider worth your money requires an ECG before they accept you. If you answered yes or I do not know, keep going. It changes the conversation, and often it does not end it.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="s3">
    <p class="sv-progress">Screen 3 of 6</p>
    <h2 class="sv-label">Do you drink alcohol daily, or take benzodiazepines daily?</h2>
    <p class="sv-sub">Benzodiazepines include Xanax, Valium, Klonopin, and Ativan.</p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("daily_depressants", "neither", "Neither"),
          opt("daily_depressants", "alcohol", "Alcohol, most days"),
          opt("daily_depressants", "benzos", "Benzodiazepines, most days"),
          opt("daily_depressants", "both", "Both"),
      ]) + '''
    </div>
    <p class="sv-micro">Stopping either one suddenly can cause seizures, and withdrawal seizures appear in the ibogaine fatality reviews. You need a supervised taper first. This does not rule you out. It changes the order of the steps, and that order protects you.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="s4">
    <p class="sv-progress">Screen 4 of 6</p>
    <h2 class="sv-label">Which of these do you take?</h2>
    <p class="sv-sub">Select everything that applies.</p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("medications", "antidepressants", "Antidepressants (SSRIs or SNRIs, such as Lexapro, Zoloft, Prozac, Effexor)", "checkbox"),
          opt("medications", "maintenance", "Methadone, buprenorphine, or Suboxone", "checkbox"),
          opt("medications", "cardiacmed", "Heart or blood pressure medication", "checkbox"),
          opt("medications", "stabilisers", "Mood stabilisers or antipsychotics (such as lithium, Seroquel, Abilify)", "checkbox"),
          opt("medications", "none", "None of these", "checkbox"),
      ]) + '''
    </div>
    <p class="sv-micro">Several of these need a supervised taper or a switch before treatment, because of how they interact with ibogaine in the liver and the heart. Your own prescriber runs that taper, not us and not the provider. This affects your timeline more than anything else.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="s5">
    <p class="sv-progress">Screen 5 of 6</p>
    <h2 class="sv-label">Where would you travel from?</h2>
    <div class="sv-field" style="max-width:380px;">
      <label for="sv-country">Country, type to search</label>
      <input id="sv-country" type="text" list="countries" autocomplete="country-name" placeholder="Start typing your country">
      ''' + COUNTRY_DATALIST + '''
    </div>
    <p class="sv-micro">Ibogaine is legal, unregulated, or restricted depending on where you go. Your home country shapes your visa options and your realistic destinations.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="s6">
    <p class="sv-progress">Screen 6 of 6</p>
    <h2 class="sv-label">When could you realistically travel?</h2>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("timeline", "asap", "As soon as I can arrange it"),
          opt("timeline", "months", "Within the next 1 to 3 months"),
          opt("timeline", "year", "Later this year"),
          opt("timeline", "research", "I am researching for now"),
      ]) + '''
    </div>
    <p class="sv-micro">Answer honestly. Half the people who take this quiz are reading, not booking, and we would rather send you good information than chase you.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>See my result</button></div>
  </section>

  <section class="sv-result" id="sv-result-1">
    <div class="verdict">
      <h2></h2>
      <p class="vp1"></p>
      <p class="vp2"></p>
    </div>

    <div class="sv-reasons">
      <h3>Why we say that</h3>
      <ul></ul>
    </div>

    <div class="sv-path">
      <h3>What the path usually looks like</h3>
      <div class="path-strip"></div>
    </div>

    <div class="sv-email-block">
      <h3></h3>
      <p class="sv-email-p"></p>
      <form id="sv1-email-form" novalidate>
        <div class="sv-row" style="margin-top:16px;">
          <div class="sv-field"><label for="sv1-first">First name (optional)</label><input id="sv1-first" type="text" autocomplete="given-name"></div>
          <div class="sv-field"><label for="sv1-email">Email address</label><input id="sv1-email" type="email" required autocomplete="email"></div>
        </div>
        <button type="submit" class="btn btn-ink">Email me when it's ready</button>
        <p class="form-status" role="status"></p>
      </form>
    </div>

    <div class="sv-next">
      <h3>What to do with this</h3>
      <p><a href="library/index.html">Keep reading</a>. Most people sit with this for a few weeks before they decide anything, and that is the right pace for a decision this size.</p>
      <p>When you are ready to go deeper, or to be introduced to vetted providers who might fit your case, the next step is our <a href="find-a-provider.html">Provider Match Profile</a>. It takes about five minutes. A person reads it, and we come back to you with up to three providers matched on your medical picture, your budget, and your dates. You decide who to meet before anyone learns your name.</p>
    </div>

    <div class="sv-honesty">
      <h3>What ibogaine does not do</h3>
      <p>It does not erase addiction. In the twelve-month follow-up study of opioid patients, the people who did well built something afterwards: therapy, community, a changed daily life. Ibogaine interrupts physical dependence and opens a window. What you do inside that window decides the outcome.</p>
      <p>It is not an approved medicine in the United States, and it carries real risk that screening reduces without removing. Anyone who tells you otherwise is selling.</p>
    </div>

    <div class="sv-disclosure">
      <p>We are an independent placement service. Providers pay us a fee when we refer someone they accept. You pay us nothing. We publish our <a href="vetting-standard.html">full vetting standard</a> and we decline providers who fail it.</p>
      <p>If you are in crisis right now, ibogaine is not the immediate answer. Contact your local emergency service or a crisis line.</p>
    </div>
  </section>

</div>
<script defer src="js/survey.js"></script>
'''

# ============================================================================
# SURVEY 2: provider match profile  /find-a-provider
# ============================================================================

SAFETY_GROUPS = '''
      <div class="sv-q" id="g-indications">
        <h2 class="sv-label">What are you seeking treatment for?</h2>
        <p class="sv-sub">Tap everything that applies.</p>
        <div class="sv-opts">
          ''' + "\n          ".join([
              opt("m_indications", "opioid", "Opioid dependence (heroin, fentanyl, pain medication)", "checkbox"),
              opt("m_indications", "maintenance", "Methadone, buprenorphine, or Suboxone maintenance", "checkbox"),
              opt("m_indications", "substance", "Alcohol or another substance", "checkbox"),
              opt("m_indications", "trauma", "PTSD, trauma, or depression", "checkbox"),
              opt("m_indications", "tbi", "Traumatic brain injury or a neurological condition", "checkbox"),
              opt("m_indications", "growth", "Personal growth or spiritual work", "checkbox"),
          ]) + '''
        </div>
      </div>

      <div class="sv-q" id="g-cardiac">
        <h2 class="sv-label">Has a doctor ever told you about a heart condition, an irregular heartbeat, or an abnormal ECG?</h2>
        <div class="sv-opts">
          ''' + "\n          ".join([
              opt("m_cardiac", "no", "No"),
              opt("m_cardiac", "yes", "Yes"),
              opt("m_cardiac", "unknown", "I do not know"),
          ]) + '''
        </div>
        <p class="sv-micro">Cardiac safety decides more here than anything else you will tell us. In the published review of 19 deaths linked to ibogaine, existing heart disease was the leading contributing factor. Every provider we work with requires an ECG before they accept anyone.</p>
      </div>

      <div class="sv-q" id="g-depressants">
        <h2 class="sv-label">Do you drink alcohol daily, or take benzodiazepines daily?</h2>
        <p class="sv-sub">Benzodiazepines include Xanax, Valium, Klonopin, and Ativan.</p>
        <div class="sv-opts">
          ''' + "\n          ".join([
              opt("m_depressants", "neither", "Neither"),
              opt("m_depressants", "alcohol", "Alcohol, most days"),
              opt("m_depressants", "benzos", "Benzodiazepines, most days"),
              opt("m_depressants", "both", "Both"),
          ]) + '''
        </div>
        <p class="sv-micro">Stopping either one suddenly can cause seizures. Providers handle this with a supervised taper, either at home with your own prescriber or on site before treatment. Telling us now decides which.</p>
      </div>

      <div class="sv-q" id="g-medications">
        <h2 class="sv-label">Which of these do you take?</h2>
        <p class="sv-sub">Tap everything that applies.</p>
        <div class="sv-opts">
          ''' + "\n          ".join([
              opt("m_medications", "antidepressants", "Antidepressants (SSRIs or SNRIs)", "checkbox"),
              opt("m_medications", "maintenance", "Methadone, buprenorphine, or Suboxone", "checkbox"),
              opt("m_medications", "cardiacmed", "Heart or blood pressure medication", "checkbox"),
              opt("m_medications", "stabilisers", "Mood stabilisers or antipsychotics", "checkbox"),
              opt("m_medications", "none", "None of these", "checkbox"),
          ]) + '''
        </div>
        <p class="sv-micro">Several of these need a supervised taper before treatment. Your prescriber runs it. This affects your dates more than anything else.</p>
      </div>
'''

MATCH_PAGE_BODY = '''
<div class="survey-wrap">

  <section class="sv-screen active" id="p0">
    <h1 style="margin-bottom:18px;">Find a provider that fits your case.</h1>
    <p style="max-width:62ch;">About five minutes. We read it ourselves, speak to the providers we think can handle your case, and come back to you with the ones who say yes.</p>
    <p style="max-width:62ch;">This is for people who have decided to go ahead. If you are still working out whether ibogaine makes sense for you, start with the two-minute quiz instead: <a href="is-ibogaine-right-for-me.html">Is ibogaine worth a serious look in my case?</a></p>
    <p style="max-width:62ch;">Nothing here is automated. No software matches you to anyone. We take what you tell us to providers we know, describe your case before we describe you, and only bring you a name once they have confirmed they can treat you safely.</p>
    <p style="max-width:62ch;">We do not decide who gets treated. Their physicians do. If something in your history is likely to concern them, we will tell you before they do.</p>
    <p style="max-width:62ch;">Providers pay us a placement fee. You pay us nothing. We publish our vetting standard and we decline providers who fail it.</p>
    <div class="sv-nav"><button type="button" class="btn btn-ink" data-next>Start</button></div>
    <p class="sv-micro" style="margin-top:30px;">Not sure you are ready for this? <a href="vetting-standard.html">Read our vetting standard first</a>. No form, no email.</p>
  </section>

  <section class="sv-screen" id="p1">
    <p class="sv-progress">Page 1 of 7</p>

    <div id="p1-recognised" style="display:none;">
      <h2 class="sv-label">We already have your answers from the quiz.</h2>
      <p class="sv-sub">You took our screening quiz on <span id="quiz-date"></span>. Check these and fix anything that has changed.</p>
      <div class="chips"></div>
      <p class="sv-micro">Nothing here gets asked twice. Tap a chip to change an answer.</p>
    </div>

    <div id="p1-cold">
      <div id="p1-cold-intro">
        <h2 class="sv-label">First, four questions about safety.</h2>
        <p class="sv-sub">Providers cannot assess you without these. Answer them straight, including anything you would normally leave off a form. Nothing here stops us introducing you.</p>
      </div>
''' + SAFETY_GROUPS + '''
    </div>

    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="p2">
    <p class="sv-progress">Page 2 of 7</p>
    <h2 class="sv-label">A few things providers ask before anything else.</h2>

    <div class="sv-row" style="max-width:560px; margin-top:22px;">
      <div class="sv-field"><label for="f-age">Age</label><input id="f-age" type="number" min="18" max="99" inputmode="numeric"></div>
      <div class="sv-field">
        <label>Units</label>
        <div class="sv-inline">
          <label class="sv-opt" style="flex:1;"><input type="radio" name="unit_system" value="metric" checked><span>Metric</span></label>
          <label class="sv-opt" style="flex:1;"><input type="radio" name="unit_system" value="imperial"><span>Imperial</span></label>
        </div>
      </div>
    </div>
    <div class="sv-row" style="max-width:560px;">
      <div class="sv-field"><label for="f-height">Height</label><input id="f-height" type="number" min="1" inputmode="decimal" placeholder="Height (cm)"></div>
      <div class="sv-field"><label for="f-weight">Weight</label><input id="f-weight" type="number" min="1" inputmode="decimal" placeholder="Weight (kg)"></div>
    </div>
    <p class="sv-micro">Ibogaine is dosed by body weight, in milligrams per kilogram. Providers cannot build you a protocol without this.</p>

    <h2 class="sv-label" style="margin-top:34px;">Has a doctor diagnosed you with any of these?</h2>
    <p class="sv-sub">Tap everything that applies.</p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("m_conditions", "liver", "Liver disease or hepatitis", "checkbox"),
          opt("m_conditions", "kidney", "Kidney disease", "checkbox"),
          opt("m_conditions", "seizures", "Seizures or epilepsy", "checkbox"),
          opt("m_conditions", "psychiatric", "Schizophrenia, psychosis, or bipolar disorder with mania", "checkbox"),
          opt("m_conditions", "pregnancy", "I am pregnant or nursing", "checkbox"),
          opt("m_conditions", "none", "None of these", "checkbox"),
      ]) + '''
    </div>
    <p class="sv-micro">Your liver clears ibogaine from your body and your kidneys finish the job, so both affect your dose. Seizure history and psychosis history change how a provider runs your protocol. Nobody here is judging you and none of these ends the conversation. Providers use them to keep you safe.</p>
    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="p3">
    <p class="sv-progress">Page 3 of 7</p>
    <h2 class="sv-label">The specifics matter here.</h2>
    <p class="sv-sub">Providers build your protocol around these numbers. Rough figures are fine. Guessing low helps nobody, least of all you.</p>

    <div id="opioid-block" style="margin-top:26px;">
      <h3 style="font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--pine); margin-bottom:14px;">Opioid use</h3>
      <p class="sv-sub" style="margin-bottom:8px;"><strong>Which opioid do you use most?</strong></p>
      <div class="sv-opts">
        ''' + "\n        ".join([
            opt("opioid_type", "heroin", "Heroin"),
            opt("opioid_type", "fentanyl", "Fentanyl or street pills"),
            opt("opioid_type", "prescription", "Prescription pain medication"),
            opt("opioid_type", "methadone", "Methadone"),
            opt("opioid_type", "buprenorphine", "Buprenorphine or Suboxone"),
            opt("opioid_type", "other", "Something else"),
        ]) + '''
      </div>
      <div class="sv-field" style="max-width:420px; margin-top:18px;"><label for="f-opioid-amount">Roughly how much per day?</label><input id="f-opioid-amount" type="text" placeholder="&quot;80mg methadone&quot; or &quot;about 1g heroin, smoked&quot;"></div>
      <p class="sv-sub" style="margin-bottom:8px;"><strong>When did you last use?</strong></p>
      <div class="sv-opts">
        ''' + "\n        ".join([
            opt("opioid_last_use", "today", "Today"),
            opt("opioid_last_use", "days3", "Within the last 3 days"),
            opt("opioid_last_use", "weeks2", "Within the last 2 weeks"),
            opt("opioid_last_use", "longer", "Longer ago"),
        ]) + '''
      </div>
      <p class="sv-sub" style="margin:14px 0 8px;"><strong>How long has this been going on?</strong></p>
      <div class="sv-opts">
        ''' + "\n        ".join([
            opt("opioid_duration", "under1", "Under a year"),
            opt("opioid_duration", "y1to5", "1 to 5 years"),
            opt("opioid_duration", "y5to10", "5 to 10 years"),
            opt("opioid_duration", "over10", "More than 10 years"),
        ]) + '''
      </div>
      <p class="sv-micro">Methadone is the one that changes plans. Its long half-life means most providers bridge you to a short-acting opioid for a week or more before treatment, which extends your stay and your cost. Better to know now than at the airport.</p>
    </div>

    <div id="depressant-block" style="margin-top:30px;">
      <h3 style="font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--pine); margin-bottom:14px;">Alcohol and benzodiazepines</h3>
      <div class="sv-field" style="max-width:420px;"><label for="f-alcohol-amount">Roughly how much alcohol per day?</label><input id="f-alcohol-amount" type="text" placeholder="&quot;a bottle of wine&quot; or &quot;6 beers&quot;"></div>
      <div class="sv-field" style="max-width:420px;"><label for="f-benzo-detail">Which benzodiazepine, and what dose per day?</label><input id="f-benzo-detail" type="text" placeholder="&quot;Xanax, about 2mg&quot;"></div>
      <div class="sv-field" style="max-width:420px;"><label for="f-dep-last">When did you last drink or take a dose?</label><input id="f-dep-last" type="text"></div>
      <p class="sv-micro">Withdrawal from either one can trigger seizures. This detail decides whether you stabilise at home with your own doctor or on site with a provider who runs medical detox. The two paths cost different amounts and take different lengths of time.</p>
    </div>

    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="p4">
    <p class="sv-progress">Page 4 of 7</p>
    <h2 class="sv-label">Do you already have recent test results?</h2>

    <p class="sv-sub" style="margin:22px 0 8px;"><strong>An ECG from the last 12 months</strong></p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("ecg_status", "have", "Yes, I have it"),
          opt("ecg_status", "no", "No"),
          opt("ecg_status", "soon", "I can get one within two weeks"),
      ]) + '''
    </div>

    <p class="sv-sub" style="margin:22px 0 8px;"><strong>Blood work from the last 12 months, including liver and kidney panels</strong></p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("bloodwork_status", "have", "Yes, I have it"),
          opt("bloodwork_status", "no", "No"),
          opt("bloodwork_status", "soon", "I can get one within two weeks"),
      ]) + '''
    </div>
    <p class="sv-micro">If you already have these, you cut one to two weeks off your placement. Providers still run their own tests before treatment. Yours tell them today whether to start the conversation.</p>

    <div class="sv-field" style="max-width:480px; margin-top:26px;">
      <label for="f-uploads">Upload anything you have (optional)</label>
      <input id="f-uploads" type="file" accept=".pdf,.jpg,.jpeg,.png" multiple>
      <p id="upload-note" class="sv-micro" style="margin-top:8px;"></p>
    </div>
    <p class="sv-micro">PDF or photo, up to 20MB per file. Sent over an encrypted connection, shared only with providers you approve, deleted whenever you ask.</p>

    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="p5">
    <p class="sv-progress">Page 5 of 7</p>
    <h2 class="sv-label">Now the practical side.</h2>
    <p class="sv-sub">Providers differ more on these four things than on anything medical.</p>

    <p class="sv-sub" style="margin:24px 0 4px;"><strong>What is your realistic budget for the full program?</strong></p>
    <p class="sv-sub" style="margin-bottom:8px;">Programs run from about 5,000 to over 25,000 US dollars, depending on medical intensity and length. Travel is usually extra.</p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("budget_band", "b1", "Under 8,000"),
          opt("budget_band", "b2", "8,000 to 15,000"),
          opt("budget_band", "b3", "15,000 to 25,000"),
          opt("budget_band", "b4", "Over 25,000"),
          opt("budget_band", "unsure", "I do not know yet"),
      ]) + '''
    </div>
    <p class="sv-micro">We would rather show you three providers you can afford than ten you cannot. If you are unsure, tap the last option and we will show you the range that fits your medical picture.</p>

    <p class="sv-sub" style="margin:24px 0 8px;"><strong>How many days can you be away?</strong></p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("days_available", "d1", "5 to 7"),
          opt("days_available", "d2", "8 to 14"),
          opt("days_available", "d3", "15 to 30"),
          opt("days_available", "d4", "More than 30"),
          opt("days_available", "unsure", "I am not sure"),
      ]) + '''
    </div>
    <p class="sv-micro">Opioid detoxification usually needs longer than psycho-spiritual work. Methadone needs longer still.</p>

    <p class="sv-sub" style="margin:24px 0 8px;"><strong>What kind of setting do you want?</strong></p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("setting_preference", "medical", "Medical first. Hospital-grade monitoring, physician on site, clinical rooms."),
          opt("setting_preference", "retreat", "Private retreat. Medical staff on site, but the setting feels like a home or a retreat centre."),
          opt("setting_preference", "traditional", "Traditional. Ceremony, Bwiti lineage, an iboga provider working in the original context."),
          opt("setting_preference", "all", "Show me all three and let me compare."),
      ]) + '''
    </div>
    <p class="sv-micro">All three exist and all three can be run well or badly. Our vetting standard applies to every one of them.</p>

    <p class="sv-sub" style="margin:24px 0 8px;"><strong>Will anyone travel with you?</strong></p>
    <div class="sv-opts">
      ''' + "\n      ".join([
          opt("travel_companion", "yes", "Yes"),
          opt("travel_companion", "no", "No"),
          opt("travel_companion", "unsure", "I am not sure yet"),
      ]) + '''
    </div>
    <p class="sv-micro">Some providers require a companion for the first 48 hours after treatment. Others provide that support themselves.</p>

    <div id="tw-group">
      <p class="sv-sub" style="margin:24px 0 8px;"><strong>When could you realistically travel?</strong></p>
      <div class="sv-opts">
        ''' + "\n        ".join([
            opt("travel_window", "asap", "As soon as I can arrange it"),
            opt("travel_window", "months", "Within 1 to 3 months"),
            opt("travel_window", "year", "Later this year"),
            opt("travel_window", "unsure", "I am not sure"),
        ]) + '''
      </div>
      <p class="sv-micro">Providers hold different lead times, some under two weeks and some over two months. Your dates narrow the list fast.</p>
    </div>

    <div class="sv-field" style="max-width:380px; margin-top:26px;">
      <label for="f-language">What language do you want your care in?</label>
      <select id="f-language">
        <option selected>English</option><option>Spanish</option><option>French</option>
        <option>German</option><option>Portuguese</option><option>Italian</option>
        <option>Dutch</option><option>Russian</option><option>Ukrainian</option>
        <option>Arabic</option><option>Other</option>
      </select>
    </div>

    <p class="sv-error" role="alert"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" data-next>Continue</button></div>
  </section>

  <section class="sv-screen" id="p6">
    <p class="sv-progress">Page 6 of 7</p>
    <h2 class="sv-label">Last page. Then we go to work.</h2>

    <div class="sv-row" style="max-width:560px; margin-top:22px;">
      <div class="sv-field"><label for="f-first">First name</label><input id="f-first" type="text" autocomplete="given-name" required></div>
      <div class="sv-field"><label for="f-last">Last name</label><input id="f-last" type="text" autocomplete="family-name" required></div>
    </div>
    <div class="sv-row" style="max-width:560px;">
      <div class="sv-field"><label for="f-email">Email</label><input id="f-email" type="email" autocomplete="email" required></div>
      <div class="sv-field"><label for="f-phone">WhatsApp or phone (optional)</label><input id="f-phone" type="tel" autocomplete="tel"></div>
    </div>
    <p class="sv-micro">We message on WhatsApp because providers do. We will not call you out of the blue.<span id="merge-note"> If you took our quiz earlier, use the same address and we will merge the two records.</span></p>

    <div class="sv-field" style="max-width:560px; margin-top:22px;">
      <label for="f-goal">In your own words, what do you want this to change?</label>
      <textarea id="f-goal" rows="5" placeholder="Write as much or as little as you want. Providers read this before they read anything else."></textarea>
    </div>
    <p class="sv-micro">This field shapes your match more than any checkbox. People who write two honest sentences here get better introductions than people who write nothing.</p>

    <h3 style="font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--pine); margin:30px 0 14px;">Consent</h3>
    <label class="consent-box"><input type="checkbox" id="c-share"><span>I agree that you may discuss my medical picture with vetted providers so their medical team can assess whether they can treat me safely. I understand you will not pass on my name or contact details until I approve the introduction. I can withdraw this at any time by replying to any email from you. <strong>(Required)</strong></span></label>
    <label class="consent-box"><input type="checkbox" id="c-marketing"><span>Send me the Screening Checklist and occasional research updates. No more than twice a month. (Optional)</span></label>

    <h3 style="font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--pine); margin:30px 0 14px;">What happens next</h3>
    <ol style="max-width:62ch; display:grid; gap:10px; padding-left:20px;">
      <li>A person reads your profile. Every one of them gets read, usually within one business day.</li>
      <li>We take your case to the providers we think can handle it. We describe your medical picture before we describe you, and we do not give them your name at this stage.</li>
      <li>We come back to you within three business days with the providers who confirmed they can take you, what each would cost, and what we think of them. If nobody fits, we tell you that instead of stretching to find someone.</li>
      <li>You decide who to meet. Only then do we make the introduction.</li>
    </ol>

    <p class="sv-error" role="alert"></p>
    <p class="form-status" id="sv2-status" role="status"></p>
    <div class="sv-nav"><button type="button" class="sv-back" data-back>Back</button><button type="button" class="btn btn-ink" id="sv2-submit">Submit my profile</button></div>
  </section>

  <section class="sv-result" id="sv-result-2">
    <div class="verdict vA">
      <h2>Your profile is with our team.</h2>
      <p class="vp1">A person reads it, usually within one business day. Within three business days we come back to you with the providers who confirmed they can take your case, what each would cost, and what we think of them. Nothing that identifies you goes to any provider until you approve an introduction.</p>
      <p class="vp2">If you have not heard from us by then, send us a note through our <a href="contact.html" style="color:#FFFFFF;">contact page</a>.</p>
    </div>

    <div id="flag-wrap"></div>

    <div class="readback">
      <h3>What your profile says</h3>
      <dl id="readback-dl"></dl>
    </div>

    <div class="sv-disclosure">
      <p>We are an independent placement service. Providers pay us a fee when we refer someone they accept. You pay us nothing. We publish our <a href="vetting-standard.html">full vetting standard</a> and we decline providers who fail it.</p>
      <p>If you are in crisis right now, ibogaine is not the immediate answer. Contact your local emergency service or a crisis line.</p>
    </div>
  </section>

</div>
<script defer src="js/survey.js"></script>
'''

PAGES = [
{
"slug": "is-ibogaine-right-for-me",
"kicker": "Is it right for me?",
"title": "Is ibogaine worth a look for me?",
"htitle": "Screening Quiz",
"desc": "Six questions, about two minutes. Not a medical assessment: a straight answer to whether ibogaine is worth taking further in your situation.",
"body": QUIZ_PAGE_BODY,
"cta": False,
"raw": True,
"body_attr": 'data-survey="quiz"',
},
{
"slug": "find-a-provider",
"kicker": "Get matched",
"title": "Find a provider that fits your case",
"htitle": "Find a Provider",
"desc": "A five-minute profile. We read it ourselves, take your case to vetted providers, and come back with the ones who say yes.",
"body": MATCH_PAGE_BODY,
"cta": False,
"raw": True,
"body_attr": 'data-survey="match"',
},
]
