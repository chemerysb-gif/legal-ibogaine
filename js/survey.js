/* Legal Ibogaine — survey engine.
   Powers Survey 1 (screening quiz, body[data-survey="quiz"]) and
   Survey 2 (provider match profile, body[data-survey="match"]).
   Static-site adaptation: per-screen persistence uses browser storage;
   the full record posts to the form endpoint at the defined submit points. */
(function () {
  "use strict";
  var MODE = document.body.getAttribute("data-survey");
  if (!MODE) return;


  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return [].slice.call((root || document).querySelectorAll(sel)); }
  function vals(name) { return $all('input[name="' + name + '"]:checked').map(function (i) { return i.value; }); }
  function val(name) { var el = $('input[name="' + name + '"]:checked'); return el ? el.value : ""; }
  function uuid() {
    return (window.crypto && crypto.randomUUID) ? crypto.randomUUID() :
      "t-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 10);
  }
  function store(key, obj) { try { localStorage.setItem(key, JSON.stringify(obj)); } catch (e) {} }
  function load(key) { try { return JSON.parse(localStorage.getItem(key) || "null"); } catch (e) { return null; } }
  function sstore(key, obj) { try { sessionStorage.setItem(key, JSON.stringify(obj)); } catch (e) {} }
  function sload(key) { try { return JSON.parse(sessionStorage.getItem(key) || "null"); } catch (e) { return null; } }

  /* Exclusive "none" checkboxes */
  function wireExclusive(groupName, noneValue) {
    $all('input[name="' + groupName + '"]').forEach(function (box) {
      box.addEventListener("change", function () {
        if (box.value === noneValue && box.checked) {
          $all('input[name="' + groupName + '"]').forEach(function (o) { if (o !== box) o.checked = false; });
        } else if (box.checked) {
          var none = $('input[name="' + groupName + '"][value="' + noneValue + '"]');
          if (none) none.checked = false;
        }
      });
    });
  }

  function showError(screen, msg) {
    var e = $(".sv-error", screen);
    if (e) { e.textContent = msg; e.classList.add("show"); }
  }
  function clearError(screen) {
    var e = $(".sv-error", screen);
    if (e) e.classList.remove("show");
  }

  /* Routes through the shared transport in js/main.js, which posts to
     the Apps Script receiver. done(outcome): "placeholder" | "ok" | "fail". */
  function postRecord(fields, files, done) {
    var form = fields.form === "provider-match" ? "provider-match" : "screening-quiz";
    if (!window.IGForms) { done("placeholder"); return; }
    window.IGForms.post(form, fields, files, done);
  }

  /* ================================================================
     SURVEY 1 — SCREENING QUIZ
     ================================================================ */
  if (MODE === "quiz") {
    var screens = $all(".sv-screen");
    var order = screens.map(function (s) { return s.id; });
    var state = sload("ig_s1") || {};
    var current = 0;

    function go(i) {
      screens.forEach(function (s, n) { s.classList.toggle("active", n === i); });
      current = i;
      window.scrollTo({ top: 0, behavior: "auto" });
    }

    function restore() {
      if (state.indications) state.indications.forEach(function (v) { var el = $('input[name="indications"][value="' + v + '"]'); if (el) el.checked = true; });
      ["cardiac_history", "daily_depressants", "timeline"].forEach(function (n) {
        if (state[n]) { var el = $('input[name="' + n + '"][value="' + state[n] + '"]'); if (el) el.checked = true; }
      });
      if (state.medications) state.medications.forEach(function (v) { var el = $('input[name="medications"][value="' + v + '"]'); if (el) el.checked = true; });
      if (state.country) $("#sv-country").value = state.country;
    }

    function collect(id) {
      if (id === "s1") state.indications = vals("indications");
      if (id === "s2") state.cardiac_history = val("cardiac_history");
      if (id === "s3") state.daily_depressants = val("daily_depressants");
      if (id === "s4") state.medications = vals("medications");
      if (id === "s5") state.country = $("#sv-country").value.trim();
      if (id === "s6") state.timeline = val("timeline");
      sstore("ig_s1", state);
    }

    function valid(id) {
      if (id === "s1") return vals("indications").length >= 1;
      if (id === "s2") return !!val("cardiac_history");
      if (id === "s3") return !!val("daily_depressants");
      if (id === "s4") return vals("medications").length >= 1;
      if (id === "s5") return $("#sv-country").value.trim().length >= 2;
      if (id === "s6") return !!val("timeline");
      return true;
    }

    wireExclusive("medications", "none");

    $all("[data-next]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var scr = screens[current];
        clearError(scr);
        if (!valid(scr.id)) { showError(scr, "Choose an answer to continue."); return; }
        collect(scr.id);
        if (scr.id === "s6") { renderResult(); return; }
        go(current + 1);
      });
    });
    $all("[data-back]").forEach(function (btn) {
      btn.addEventListener("click", function () { if (current > 0) go(current - 1); });
    });

    function variantOf(s) {
      if (s.cardiac_history === "yes") return "C";
      var medsFlag = (s.medications || []).some(function (m) {
        return m === "antidepressants" || m === "stabilisers" || m === "maintenance";
      });
      if (s.daily_depressants !== "neither" || medsFlag || s.cardiac_history === "unknown") return "B";
      return "A";
    }

    function reasonsFor(v, s) {
      var r = [];
      var meds = s.medications || [];
      if (v === "A") {
        r.push("You have no known heart condition or rhythm problem, which removes the single largest risk factor.");
        r.push("You do not drink daily or take benzodiazepines daily, so you skip the taper that delays most people.");
        r.push("You take no medication that needs a washout before treatment.");
        if (s.timeline === "asap" || s.timeline === "months") {
          r.push("You can travel within three months, which puts real dates within reach.");
        } else if (s.timeline === "year") {
          r.push("You are aiming for later this year, which leaves plenty of room to arrange screening properly.");
        } else {
          r.push("You are researching rather than booking, which is the right speed for a decision this size.");
        }
      } else if (v === "B") {
        if (s.daily_depressants === "benzos" || s.daily_depressants === "both") {
          r.push("You take benzodiazepines daily. Stopping them suddenly can cause seizures, so your prescriber needs to taper you down first.");
        }
        if (s.daily_depressants === "alcohol" || s.daily_depressants === "both") {
          r.push("You drink daily. Alcohol withdrawal carries the same seizure risk and needs the same medical supervision.");
        }
        if (meds.indexOf("antidepressants") !== -1) {
          r.push("You take an SSRI or SNRI, which interacts with ibogaine and needs a supervised washout. The length depends on which one.");
        }
        if (meds.indexOf("stabilisers") !== -1) {
          r.push("You take a mood stabiliser or antipsychotic, which needs a supervised plan with your prescriber before treatment.");
        }
        if (meds.indexOf("maintenance") !== -1) {
          r.push("You are on methadone or buprenorphine. Most providers bridge you to a short-acting opioid before treatment, which extends your stay.");
        }
        if (s.cardiac_history === "unknown") {
          r.push("You are not certain about your cardiac history. An ECG settles it, and you can book one this week.");
        } else if (s.cardiac_history === "no") {
          r.push("Your cardiac history is clear, which removes the largest risk factor from the equation.");
        }
      } else {
        r.push("A diagnosed cardiac condition is the most serious flag in ibogaine screening, ahead of everything else people worry about.");
        r.push("Providers who run proper medical protocols will ask for a current ECG with your QTc measurement before they consider you.");
        r.push("Some will decline. Some will accept with conditions, such as continuous cardiac monitoring or a lower dose protocol.");
        r.push("Your own cardiologist's written opinion carries more weight than anything else you can bring to that conversation.");
      }
      return r;
    }

    var PATHS = {
      A: ["Choose a provider", "Screening and ECG (1 to 2 weeks)", "Medical clearance (a few days)", "Travel and treatment (7 to 14 days)", "Aftercare"],
      B: ["Speak to your prescriber (this week)", "Taper or washout (weeks to months)", "Choose a provider", "Screening and ECG (1 to 2 weeks)", "Travel and treatment"],
      C: ["Cardiology review and current ECG", "Written opinion in hand", "Provider assessment", "Provider's physician decides"]
    };

    var VERDICTS = {
      A: { h: "Ibogaine is worth exploring for your case.",
           p1: "Nothing you told us stands in the way. Your next step is a cardiac screen and blood work, which a provider arranges once you choose one.",
           p2: "That is as far as six questions can take you. A physician makes the real decision, and they will want an ECG before they say yes.",
           email: { h: "Get the Screening Checklist when it is ready", p: "We are finishing a printable version of the twelve questions we put to every provider. Leave your email and we will send it once, when it is ready. Nothing else unless you ask. Use it on us. Use it on anyone." } },
      B: { h: "Ibogaine is worth a serious look, but will require some time and effort.",
           p1: "Your answers point to a supervised taper before treatment. This is common and it is solvable. It usually adds four to eight weeks.",
           p2: "A provider who offers to take you tomorrow without raising this is telling you something about how they operate.",
           email: { h: "Get the Screening Checklist when it is ready", p: "We are finishing a printable version of the twelve questions we put to every provider. Leave your email and we will send it once, when it is ready. Nothing else unless you ask." } },
      C: { h: "Your answers raise a flag that requires further review.",
           p1: "You told us a doctor has diagnosed you with a heart condition. Ibogaine affects the heart's electrical rhythm, and the published review of deaths linked to ibogaine found existing heart disease to be the leading contributing factor.",
           p2: "We are not the ones who decide whether you can be treated. A cardiologist and a provider's physician make that call. What we can tell you is that this flag follows you into every conversation, and that any provider who waves it away is the wrong provider.",
           email: { h: "Get the cardiac screening sheet when it is ready", p: "We are finishing a one-page sheet that names the measurements a cardiologist should report, written for a clinician to read. Leave your email and we will send it once, when it is ready. Until then, ask for a 12-lead ECG with your QTc measurement." } }
    };

    function renderResult() {
      var v = variantOf(state);
      state.result_variant = v;
      sstore("ig_s1", state);
      screens.forEach(function (s) { s.classList.remove("active"); });
      var res = $("#sv-result-1");
      res.classList.add("active");

      var vd = VERDICTS[v];
      var verdict = $(".verdict", res);
      verdict.className = "verdict v" + v;
      $("h2", verdict).textContent = vd.h;
      $(".vp1", verdict).textContent = vd.p1;
      $(".vp2", verdict).textContent = vd.p2;

      var ul = $(".sv-reasons ul", res);
      ul.innerHTML = "";
      reasonsFor(v, state).forEach(function (t) {
        var li = document.createElement("li");
        var span = document.createElement("span");
        span.textContent = t;
        li.appendChild(span);
        ul.appendChild(li);
      });

      var strip = $(".path-strip", res);
      strip.innerHTML = "";
      PATHS[v].forEach(function (step, i) {
        if (i) { var a = document.createElement("span"); a.className = "path-arrow"; a.textContent = "→"; strip.appendChild(a); }
        var el = document.createElement("span");
        el.className = "path-step";
        el.textContent = step;
        strip.appendChild(el);
      });

      $(".sv-email-block h3", res).textContent = vd.email.h;
      $(".sv-email-block .sv-email-p", res).textContent = vd.email.p;

      /* store recognition snapshot for Survey 2 */
      var rec = load("ig_quiz_record") || {};
      var record = {
        indications: state.indications, cardiac_history: state.cardiac_history,
        daily_depressants: state.daily_depressants, medications: state.medications,
        country: state.country, timeline: state.timeline,
        result_variant: v, source: "quiz",
        resume_token: rec.resume_token || uuid(),
        completed_at: new Date().toISOString(),
        email: rec.email || "", first_name: rec.first_name || "",
        quiz_date: new Date().toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })
      };
      store("ig_quiz_record", record);
      window.scrollTo({ top: 0, behavior: "auto" });
    }

    var emailForm = $("#sv1-email-form");
    if (emailForm) {
      emailForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var email = $("#sv1-email").value.trim();
        var first = $("#sv1-first").value.trim();
        var status = $(".form-status", emailForm);
        if (!$("#sv1-email").checkValidity() || !email) { $("#sv1-email").reportValidity(); return; }
        var record = load("ig_quiz_record") || {};
        record.email = email;
        record.first_name = first;
        store("ig_quiz_record", record);
        var fields = Object.assign({}, record, { form: "screening-quiz" });
        postRecord(fields, null, function (outcome) {
          if (outcome === "placeholder") {
            status.textContent = "Email delivery isn't connected yet. Site owner: connect the form endpoint in js/survey.js.";
            status.className = "form-status warn show";
          } else if (outcome === "ok") {
            status.textContent = "Saved. We will email it to you once, when it is ready.";
            status.className = "form-status ok show";
            window.IGTrack("generate_lead", { form: "screening-quiz" });
            emailForm.querySelector("button").disabled = true;
          } else {
            status.textContent = "We couldn't save that just now. Your result stays on this page either way.";
            status.className = "form-status warn show";
          }
        });
      });
    }

    restore();
    go(0);
  }

  /* ================================================================
     SURVEY 2 — PROVIDER MATCH PROFILE
     ================================================================ */
  if (MODE === "match") {
    var pages = $all(".sv-screen");
    var s2 = sload("ig_s2") || {};
    var quizRec = load("ig_quiz_record");
    var params = new URLSearchParams(window.location.search);
    var recognised = !!(quizRec && quizRec.completed_at &&
      (!params.get("rt") || params.get("rt") === quizRec.resume_token));
    if (params.get("rt") && quizRec && params.get("rt") !== quizRec.resume_token) recognised = false;
    if (!quizRec) recognised = false;
    var idx = 0;

    var LABELS = {
      indications: { opioid: "Opioid dependence", maintenance: "Methadone, buprenorphine, or Suboxone maintenance", substance: "Alcohol or another substance", trauma: "PTSD, trauma, or depression", tbi: "Traumatic brain injury or a neurological condition", growth: "Personal growth or spiritual work", pattern: "A pattern I cannot break" },
      cardiac: { no: "No cardiac history reported", yes: "Cardiac history reported", unknown: "Cardiac history uncertain" },
      depressants: { neither: "No daily alcohol or benzodiazepines", alcohol: "Alcohol most days", benzos: "Benzodiazepines most days", both: "Alcohol and benzodiazepines daily" },
      medications: { antidepressants: "Antidepressants (SSRI or SNRI)", maintenance: "Methadone, buprenorphine, or Suboxone", cardiacmed: "Heart or blood pressure medication", stabilisers: "Mood stabilisers or antipsychotics", none: "No listed medications" },
      conditions: { liver: "Liver disease or hepatitis", kidney: "Kidney disease", seizures: "Seizures or epilepsy", psychiatric: "Schizophrenia, psychosis, or bipolar disorder with mania", pregnancy: "Pregnant or nursing", none: "None reported" },
      timeline: { asap: "As soon as it can be arranged", months: "Within 1 to 3 months", year: "Later this year", research: "Researching for now", unsure: "Not sure yet" }
    };

    function pageVisible(id) {
      if (id === "p3") {
        var ind = s2.indications || [];
        var meds = s2.medications || [];
        return ind.indexOf("opioid") !== -1 || ind.indexOf("maintenance") !== -1 ||
               meds.indexOf("maintenance") !== -1 || (s2.daily_depressants && s2.daily_depressants !== "neither");
      }
      return true;
    }

    function goP(i, dir) {
      while (i >= 0 && i < pages.length && !pageVisible(pages[i].id)) i += (dir || 1);
      pages.forEach(function (p, n) { p.classList.toggle("active", n === i); });
      idx = i;
      if (pages[i].id === "p3") setupP3();
      window.scrollTo({ top: 0, behavior: "auto" });
    }

    function setupP3() {
      var ind = s2.indications || [];
      var meds = s2.medications || [];
      var opioid = ind.indexOf("opioid") !== -1 || ind.indexOf("maintenance") !== -1 || meds.indexOf("maintenance") !== -1;
      var depress = s2.daily_depressants && s2.daily_depressants !== "neither";
      $("#opioid-block").style.display = opioid ? "" : "none";
      $("#depressant-block").style.display = depress ? "" : "none";
    }

    /* Recognition: page 1 variants */
    var coldP1 = $("#p1-cold");
    var recP1 = $("#p1-recognised");
    if (recognised) {
      coldP1.style.display = "none";
      recP1.style.display = "";
      $("#quiz-date").textContent = quizRec.quiz_date || "an earlier visit";
      s2.indications = quizRec.indications;
      s2.cardiac_history = quizRec.cardiac_history;
      s2.daily_depressants = quizRec.daily_depressants;
      s2.medications = quizRec.medications;
      s2.travel_window = quizRec.timeline;
      s2.country = quizRec.country;
      s2.source = "quiz";
      s2.resume_token = quizRec.resume_token;
      var tw = $("#tw-group");
      if (tw) tw.style.display = "none";
      var mn = $("#merge-note");
      if (mn) mn.style.display = "none";
      var em = $("#f-email");
      if (em && quizRec.email) em.value = quizRec.email;
      var fn = $("#f-first");
      if (fn && quizRec.first_name) fn.value = quizRec.first_name;
      /* chips */
      var chipDefs = [
        ["Seeking treatment for", (quizRec.indications || []).map(function (v) { return LABELS.indications[v] || v; }).join(", "), "g-indications"],
        ["Cardiac history", LABELS.cardiac[quizRec.cardiac_history] || "", "g-cardiac"],
        ["Daily alcohol or benzodiazepines", LABELS.depressants[quizRec.daily_depressants] || "", "g-depressants"],
        ["Current medications", (quizRec.medications || []).map(function (v) { return LABELS.medications[v] || v; }).join(", "), "g-medications"],
        ["Travelling from", quizRec.country || "", null],
        ["Timeline", LABELS.timeline[quizRec.timeline] || "", null]
      ];
      var chipWrap = $(".chips", recP1);
      chipDefs.forEach(function (d) {
        var c = document.createElement("button");
        c.type = "button";
        c.className = "chip";
        c.textContent = d[0] + ": " + (d[1] || "—");
        c.addEventListener("click", function () {
          if (!d[2]) return;
          var g = $("#" + d[2]);
          coldP1.style.display = "";
          $("#p1-cold-intro").style.display = "none";
          $all(".sv-q", coldP1).forEach(function (q) { q.style.display = q.id === d[2] ? "" : "none"; });
          restoreP1();
        });
        chipWrap.appendChild(c);
      });
    } else {
      recP1.style.display = "none";
      s2.source = "cold";
    }

    function restoreP1() {
      (s2.indications || []).forEach(function (v) { var el = $('input[name="m_indications"][value="' + v + '"]'); if (el) el.checked = true; });
      if (s2.cardiac_history) { var a = $('input[name="m_cardiac"][value="' + s2.cardiac_history + '"]'); if (a) a.checked = true; }
      if (s2.daily_depressants) { var b = $('input[name="m_depressants"][value="' + s2.daily_depressants + '"]'); if (b) b.checked = true; }
      (s2.medications || []).forEach(function (v) { var el = $('input[name="m_medications"][value="' + v + '"]'); if (el) el.checked = true; });
    }

    wireExclusive("m_medications", "none");
    wireExclusive("m_conditions", "none");

    function collectPage(id) {
      if (id === "p1") {
        if (coldP1.style.display !== "none") {
          var iv = vals("m_indications"); if (iv.length) s2.indications = iv;
          if (val("m_cardiac")) s2.cardiac_history = val("m_cardiac");
          if (val("m_depressants")) s2.daily_depressants = val("m_depressants");
          var mv = vals("m_medications"); if (mv.length) s2.medications = mv;
        }
      }
      if (id === "p2") {
        s2.age = $("#f-age").value;
        s2.unit_system = val("unit_system") || "metric";
        s2.height = $("#f-height").value;
        s2.weight = $("#f-weight").value;
        s2.conditions = vals("m_conditions");
      }
      if (id === "p3") {
        s2.opioid_type = val("opioid_type");
        s2.opioid_amount = ($("#f-opioid-amount") || {}).value || "";
        s2.opioid_last_use = val("opioid_last_use");
        s2.opioid_duration = val("opioid_duration");
        s2.alcohol_amount = ($("#f-alcohol-amount") || {}).value || "";
        s2.benzo_detail = ($("#f-benzo-detail") || {}).value || "";
        s2.depressant_last_use = ($("#f-dep-last") || {}).value || "";
      }
      if (id === "p4") {
        s2.ecg_status = val("ecg_status");
        s2.bloodwork_status = val("bloodwork_status");
      }
      if (id === "p5") {
        s2.budget_band = val("budget_band");
        s2.days_available = val("days_available");
        s2.setting_preference = val("setting_preference");
        s2.travel_companion = val("travel_companion");
        if (!recognised) s2.travel_window = val("travel_window");
        s2.language = $("#f-language").value || "English";
      }
      if (id === "p6") {
        s2.first_name = $("#f-first").value.trim();
        s2.last_name = $("#f-last").value.trim();
        s2.email = $("#f-email").value.trim();
        s2.phone = $("#f-phone").value.trim();
        s2.goal_text = $("#f-goal").value.trim();
        s2.consent_share = $("#c-share").checked;
        s2.consent_marketing = $("#c-marketing").checked;
      }
      sstore("ig_s2", s2);
      store("ig_s2_partial", s2);
    }

    function validPage(id) {
      if (id === "p1") {
        if (recognised && coldP1.style.display === "none") return true;
        return (vals("m_indications").length || (s2.indications || []).length) &&
               (val("m_cardiac") || s2.cardiac_history) &&
               (val("m_depressants") || s2.daily_depressants) &&
               (vals("m_medications").length || (s2.medications || []).length);
      }
      if (id === "p2") {
        var age = parseInt($("#f-age").value, 10);
        return age >= 18 && $("#f-height").value && $("#f-weight").value && vals("m_conditions").length >= 1;
      }
      if (id === "p3") {
        var okO = $("#opioid-block").style.display === "none" || (val("opioid_type") && val("opioid_last_use") && val("opioid_duration"));
        var okD = $("#depressant-block").style.display === "none" || true;
        return okO && okD;
      }
      if (id === "p4") return !!val("ecg_status") && !!val("bloodwork_status");
      if (id === "p5") {
        var tw = recognised ? true : !!val("travel_window");
        return val("budget_band") && val("days_available") && val("setting_preference") && val("travel_companion") && tw;
      }
      if (id === "p6") {
        var f = $("#f-first"), l = $("#f-last"), e = $("#f-email");
        if (!f.value.trim() || !l.value.trim()) return false;
        if (!e.checkValidity() || !e.value.trim()) { e.reportValidity(); return false; }
        if (!$("#c-share").checked) return false;
        return true;
      }
      return true;
    }

    $all("[data-next]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var pg = pages[idx];
        clearError(pg);
        if (!validPage(pg.id)) { showError(pg, pg.id === "p6" && !$("#c-share").checked ? "The first consent box is required before we can take your case to anyone." : "Answer everything on this page to continue."); return; }
        collectPage(pg.id);
        if (pg.id === "p1" && recognised) { coldP1.style.display = "none"; $all(".sv-q", coldP1).forEach(function (q) { q.style.display = ""; }); }
        goP(idx + 1, 1);
      });
    });
    $all("[data-back]").forEach(function (btn) {
      btn.addEventListener("click", function () { if (idx > 0) goP(idx - 1, -1); });
    });

    function computeFlags() {
      var f = [];
      var c = s2.conditions || [];
      var m = s2.medications || [];
      if (s2.cardiac_history === "yes") f.push("flag_cardiac");
      if (s2.cardiac_history === "unknown") f.push("flag_cardiac_unknown");
      if (s2.daily_depressants && s2.daily_depressants !== "neither") f.push("flag_withdrawal");
      if (c.indexOf("seizures") !== -1) f.push("flag_seizure");
      if (c.indexOf("psychiatric") !== -1) f.push("flag_psychiatric");
      if (c.indexOf("pregnancy") !== -1) f.push("flag_pregnancy");
      if (c.indexOf("liver") !== -1 || c.indexOf("kidney") !== -1) f.push("flag_hepatorenal");
      if (m.indexOf("antidepressants") !== -1 || m.indexOf("stabilisers") !== -1 || m.indexOf("maintenance") !== -1) f.push("flag_washout");
      return f;
    }

    var uploads = [];
    var upEl = $("#f-uploads");
    if (upEl) {
      upEl.addEventListener("change", function () {
        uploads = [].slice.call(upEl.files).filter(function (f) { return f.size <= 20 * 1024 * 1024; });
        $("#upload-note").textContent = uploads.length ? uploads.length + " file(s) attached." : "";
      });
    }

    var submitBtn = $("#sv2-submit");
    if (submitBtn) {
      submitBtn.addEventListener("click", function () {
        var pg = pages[idx];
        clearError(pg);
        if (!validPage("p6")) { showError(pg, !$("#c-share").checked ? "The first consent box is required before we can take your case to anyone." : "Fill in your name and email to submit."); return; }
        collectPage("p6");
        /* merge rule: cold arrival whose email matches a quiz record */
        if (s2.source === "cold" && quizRec && quizRec.email && quizRec.email.toLowerCase() === s2.email.toLowerCase()) {
          s2.source = "quiz";
          s2.resume_token = quizRec.resume_token;
        }
        s2.flags = computeFlags();
        s2.submitted_at = new Date().toISOString();
        store("ig_match_record", s2);
        submitBtn.disabled = true;
        renderResult2();
        postRecord(Object.assign({ form: "provider-match" }, s2), uploads, function (outcome) {
          if (outcome === "fail" || outcome === "placeholder") addSendFailNote();
          else window.IGTrack("generate_lead", { form: "provider-match" });
        });
      });
    }

    function flagBlocks() {
      var blocks = [];
      var c = s2.conditions || [];
      var m = s2.medications || [];
      var dep = s2.daily_depressants;
      if (s2.cardiac_history === "yes") {
        blocks.push({ id: "cardiac", html:
          "<p>You told us a doctor has diagnosed you with a heart condition. We flagged this at the top of your profile, in bold, because it is the most serious signal in ibogaine screening. Ibogaine affects the heart's electrical rhythm, and the published review of deaths linked to ibogaine found existing heart disease to be the leading contributing factor.</p>" +
          "<p>We are not qualified to rule you out and we have not tried to. What we can tell you is what to expect. Some of the providers we approach will decline. The ones who continue will want a current ECG with your QTc measurement, and most will want your own cardiologist's written opinion before they go further.</p>" +
          "<p>Start that now rather than waiting for them to ask.</p>" });
      }
      if (c.indexOf("psychiatric") !== -1) {
        blocks.push({ id: "psychiatric", html:
          "<p>You told us about a psychiatric diagnosis. We flagged this at the top of your profile. Ibogaine produces an extended altered state lasting many hours, and providers assess psychosis and mania history carefully before they take someone into that.</p>" +
          "<p>Providers vary widely here. Some decline outright. Others accept with a psychiatric review and a support plan in place. Your treating psychiatrist's written view will matter more than anything else you bring.</p>" });
      }
      if (c.indexOf("pregnancy") !== -1) {
        blocks.push({ id: "pregnancy", html:
          "<p>You told us you are pregnant or nursing. We flagged this at the top of your profile. Every provider we work with declines treatment during pregnancy and nursing, so expect that answer wherever we ask.</p>" +
          "<p>Your profile stays with our team anyway, so you can ask about timing directly. When you are ready to revisit this, reopen your profile and we will run the match again.</p>" });
      }
      if ((dep && dep !== "neither") || c.indexOf("seizures") !== -1) {
        var what = c.indexOf("seizures") !== -1 ? "have a seizure history" :
                   dep === "both" ? "drink daily and take benzodiazepines daily" :
                   dep === "benzos" ? "take benzodiazepines daily" : "drink daily";
        blocks.push({ id: "withdrawal", html:
          "<p>You told us you " + what + ". We flagged this at the top of your profile. Withdrawal from alcohol or benzodiazepines can cause seizures, and withdrawal seizures appear in the ibogaine fatality reviews.</p>" +
          "<p>This does not stop anyone treating you. It changes the sequence. Expect providers to ask for either a supervised taper with your own prescriber before you travel, or a stabilisation period on site before treatment. The second option costs more and takes longer.</p>" +
          "<p>Book time with your prescriber this week and ask about a taper. You will be ahead of the question.</p>" });
      }
      var higher = blocks.length > 0;
      if (!higher && (m.indexOf("antidepressants") !== -1 || m.indexOf("stabilisers") !== -1 || m.indexOf("maintenance") !== -1)) {
        var cls = m.indexOf("maintenance") !== -1 ? "a maintenance opioid" :
                  m.indexOf("antidepressants") !== -1 ? "an antidepressant" : "a mood stabiliser or antipsychotic";
        blocks.push({ id: "washout", html:
          "<p>You take " + cls + ". We noted this in your profile. It interacts with ibogaine, so providers will ask your prescriber to taper or switch you before treatment.</p>" +
          "<p>Expect this to move your dates by four to eight weeks, depending on the medication. Methadone works differently again: most providers bridge you to a short-acting opioid for a week or more before treatment, which lengthens your stay.</p>" +
          "<p>Speak to your prescriber this week and you keep your timeline intact.</p>" });
      }
      return blocks;
    }

    function addSendFailNote() {
      var res = $("#sv-result-2");
      if ($(".send-fail-note", res)) return;
      var note = document.createElement("div");
      note.className = "flag-block send-fail-note";
      note.innerHTML = "<p><strong>Your profile did not reach our team.</strong> It is saved on this device, so nothing is lost. Check your connection and send it again.</p>" +
        '<button type="button" class="btn btn-ink send-retry">Send my profile again</button>' +
        '<p class="send-retry-status" role="status" style="margin-top:10px;"></p>' +
        '<p>If it still does not go through, send us a note through our <a href="contact.html">contact page</a> with your name and email, and we will pick it up from there. Everything below still stands.</p>';
      var verdict = $(".verdict", res);
      verdict.parentNode.insertBefore(note, verdict.nextSibling);
      var retry = $(".send-retry", note);
      var retryStatus = $(".send-retry-status", note);
      retry.addEventListener("click", function () {
        retry.disabled = true;
        retryStatus.textContent = "Sending…";
        postRecord(Object.assign({ form: "provider-match" }, s2), uploads, function (outcome) {
          if (outcome === "ok") {
            note.innerHTML = "<p><strong>Sent.</strong> Your profile reached our team. Everything below still stands.</p>";
          } else {
            retry.disabled = false;
            retryStatus.textContent = "Still not going through. Try again in a minute, or use the contact page.";
          }
        });
      });
    }

    function renderResult2() {
      pages.forEach(function (p) { p.classList.remove("active"); });
      var res = $("#sv-result-2");
      res.classList.add("active");
      var wrap = $("#flag-wrap");
      wrap.innerHTML = "";
      var blocks = flagBlocks();
      blocks.forEach(function (b, i) {
        var div = document.createElement("div");
        div.className = "flag-block";
        var head = "";
        if (i === 0) {
          head = "<h3>" + (blocks.length > 1 ? "Some things you should know before they reply" : "One thing you should know before they reply") + "</h3>";
        }
        div.innerHTML = head + b.html;
        wrap.appendChild(div);
      });

      var c = s2.conditions || [];
      var rows = [
        ["Seeking treatment for", (s2.indications || []).map(function (v) { return LABELS.indications[v] || v; }).join(", ")],
        ["Age, height, weight", s2.age + " · " + s2.height + (s2.unit_system === "imperial" ? " in" : " cm") + " · " + s2.weight + (s2.unit_system === "imperial" ? " lb" : " kg")],
        ["Cardiac history", LABELS.cardiac[s2.cardiac_history] || ""],
        ["Daily alcohol or benzodiazepines", LABELS.depressants[s2.daily_depressants] || ""],
        ["Medications", (s2.medications || []).map(function (v) { return LABELS.medications[v] || v; }).join(", ")],
        ["Diagnosed conditions", c.length ? c.map(function (v) { return LABELS.conditions[v] || v; }).join(", ") : "None reported"],
        ["Recent ECG", ({ have: "Yes, in hand", no: "Not yet", soon: "Can get one within two weeks" })[s2.ecg_status] || ""],
        ["Recent blood work", ({ have: "Yes, in hand", no: "Not yet", soon: "Can get one within two weeks" })[s2.bloodwork_status] || ""],
        ["Budget", ({ b1: "Under 8,000 USD", b2: "8,000 to 15,000 USD", b3: "15,000 to 25,000 USD", b4: "Over 25,000 USD", unsure: "Not yet decided" })[s2.budget_band] || ""],
        ["Days available", ({ d1: "5 to 7", d2: "8 to 14", d3: "15 to 30", d4: "More than 30", unsure: "Not sure" })[s2.days_available] || ""],
        ["Setting", ({ medical: "Medical first", retreat: "Private retreat", traditional: "Traditional", all: "Comparing all three" })[s2.setting_preference] || ""],
        ["Companion", ({ yes: "Travelling with someone", no: "Travelling alone", unsure: "Not sure yet" })[s2.travel_companion] || ""],
        ["Timeline", LABELS.timeline[s2.travel_window] || ""],
        ["Care language", s2.language || "English"]
      ];
      if (s2.goal_text) rows.push(["In your own words", s2.goal_text]);
      var dl = $("#readback-dl");
      dl.innerHTML = "";
      rows.forEach(function (r) {
        if (!r[1]) return;
        var row = document.createElement("div");
        row.className = "rb-row";
        var dt = document.createElement("dt"); dt.textContent = r[0];
        var dd = document.createElement("dd"); dd.textContent = r[1];
        row.appendChild(dt); row.appendChild(dd);
        dl.appendChild(row);
      });
      window.scrollTo({ top: 0, behavior: "auto" });
    }

    /* unit toggle relabel */
    $all('input[name="unit_system"]').forEach(function (r) {
      r.addEventListener("change", function () {
        var imp = val("unit_system") === "imperial";
        $("#f-height").placeholder = imp ? "Height (inches)" : "Height (cm)";
        $("#f-weight").placeholder = imp ? "Weight (lb)" : "Weight (kg)";
      });
    });

    /* restore partial */
    var partial = load("ig_s2_partial");
    if (partial && !recognised) { s2 = Object.assign(partial, s2); }

    goP(0, 1);
  }
})();
