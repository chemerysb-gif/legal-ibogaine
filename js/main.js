/* Legal Ibogaine — analytics consent.
   GA4 sets cookies, so nothing loads until the visitor accepts. Declining
   is one click, same as accepting, and the choice can be changed later from
   the footer — consent you cannot withdraw is not consent.

   Set GA_ID to the Measurement ID from Google Analytics (G-XXXXXXXXXX).
   While it is blank, no banner shows and nothing is loaded. */
(function () {
  "use strict";

  var GA_ID = "";                 /* e.g. "G-ABCD1234EF" */
  var KEY = "ig_consent";         /* "granted" | "denied" */

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function write(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  function loadGA() {
    if (!GA_ID || GA_ID.indexOf("G-") !== 0 || window.__gaLoaded) return;
    window.__gaLoaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?" + "id=" + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_ID, { anonymize_ip: true });
  }

  /* Events are dropped silently without consent, so callers never need to check. */
  window.IGTrack = function (name, params) {
    if (read() !== "granted" || typeof window.gtag !== "function") return;
    window.gtag("event", name, params || {});
  };

  function dismiss(el) {
    el.classList.remove("show");
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 250);
  }

  function banner() {
    var el = document.createElement("div");
    el.className = "consent-bar";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-label", "Analytics consent");
    el.innerHTML =
      '<p>We\'d like to measure which pages people find useful. That uses cookies. ' +
      'Nothing is loaded unless you agree, and we never link it to anything you submit. ' +
      '<a href="' + (document.body.getAttribute("data-root") || "") + 'privacy.html">How we handle data</a></p>' +
      '<div class="consent-actions">' +
      '<button type="button" class="btn btn-ghost" data-consent="denied">Decline</button>' +
      '<button type="button" class="btn btn-ink" data-consent="granted">Accept</button>' +
      "</div>";
    document.body.appendChild(el);
    requestAnimationFrame(function () { el.classList.add("show"); });

    el.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-consent]");
      if (!btn) return;
      var choice = btn.getAttribute("data-consent");
      write(choice);
      if (choice === "granted") loadGA();
      dismiss(el);
    });
  }

  /* Footer link so a decision can be revisited. */
  window.IGConsent = {
    reopen: function () {
      try { localStorage.removeItem(KEY); } catch (e) {}
      if (!document.querySelector(".consent-bar")) banner();
    },
    state: read
  };

  var choice = read();
  if (choice === "granted") loadGA();
  else if (choice !== "denied" && GA_ID) banner();
})();

/* Legal Ibogaine — submission transport.
   Every form on the site posts through here to the Apps Script receiver
   bound to the submissions spreadsheet (see _generator/apps-script/).

   Posted as text/plain rather than JSON: a JSON content-type triggers a
   CORS preflight that script.google.com does not answer, and text/plain
   is a "simple request" that goes straight through. The receiver parses
   the body as JSON regardless. */
(function () {
  "use strict";

  var ENDPOINT = "https://script.google.com/macros/s/AKfycbxfrahyiGh2c4JO_2s6Jy4dh6cF1alo9vsUxrA57JA2V8uadrDz6nMstaRYJsFLOyYd/exec";
  var TOKEN = "RN3JLwGhJi07rtdsYvXp3wGzDBMfT4bh5PErhxcZ";
  var PLACEHOLDER = /PASTE_YOUR|REPLACE_WITH/;

  /* done(outcome) — "placeholder" | "ok" | "fail" */
  function post(form, fields, files, done) {
    if (PLACEHOLDER.test(ENDPOINT) || PLACEHOLDER.test(TOKEN)) { done("placeholder"); return; }
    readFiles(files, function (encoded) {
      fetch(ENDPOINT, {
        method: "POST",
        body: JSON.stringify({ token: TOKEN, form: form, fields: fields, files: encoded }),
        headers: { "Content-Type": "text/plain;charset=utf-8" }
      })
        .then(function (r) { return r.json(); })
        .then(function (d) { done(d && d.status === "ok" ? "ok" : "fail"); })
        .catch(function () { done("fail"); });
    });
  }

  /* Uploads travel base64-encoded inside the JSON body; the receiver
     decodes them into Drive and stores only the links in the sheet. */
  function readFiles(files, cb) {
    var list = [].slice.call(files || []);
    if (!list.length) { cb([]); return; }
    var out = [];
    var pending = list.length;
    list.forEach(function (file, i) {
      var reader = new FileReader();
      reader.onload = function () {
        var s = String(reader.result);
        out[i] = { name: file.name, type: file.type, data: s.slice(s.indexOf(",") + 1) };
        if (--pending === 0) cb(out.filter(Boolean));
      };
      reader.onerror = function () { if (--pending === 0) cb(out.filter(Boolean)); };
      reader.readAsDataURL(file);
    });
  }

  /* Collects a plain <form> into a field object, grouping repeated
     names (checkboxes) into arrays. */
  function fieldsOf(form) {
    var out = {};
    new FormData(form).forEach(function (v, k) {
      if (v instanceof File) return;
      if (out.hasOwnProperty(k)) out[k] = [].concat(out[k], v);
      else out[k] = v;
    });
    return out;
  }

  window.IGForms = { post: post, fieldsOf: fieldsOf, configured: function () {
    return !PLACEHOLDER.test(ENDPOINT) && !PLACEHOLDER.test(TOKEN);
  } };
})();

/* Legal Ibogaine — shared behaviors */
(function () {
  "use strict";

  /* Mobile nav */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* FAQ accordion */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var btn = item.querySelector(".faq-q");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var open = item.getAttribute("data-open") === "true";
      item.setAttribute("data-open", open ? "false" : "true");
      btn.setAttribute("aria-expanded", open ? "false" : "true");
    });
  });

  /* Topic filters (blog index) */
  var filterBar = document.querySelector(".filter-bar");
  if (filterBar) {
    var cards = document.querySelectorAll("[data-topic]");
    var applyTopic = function (topic) {
      filterBar.querySelectorAll(".filter-btn").forEach(function (b) {
        b.setAttribute("aria-pressed", b.getAttribute("data-filter") === topic ? "true" : "false");
      });
      cards.forEach(function (card) {
        var show = topic === "all" || card.getAttribute("data-topic") === topic;
        card.style.display = show ? "" : "none";
      });
    };
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest(".filter-btn");
      if (!btn) return;
      var topic = btn.getAttribute("data-filter");
      applyTopic(topic);
      var url = new URL(window.location);
      if (topic === "all") { url.searchParams.delete("topic"); } else { url.searchParams.set("topic", topic); }
      history.replaceState(null, "", url);
    });
    var initial = new URLSearchParams(window.location.search).get("topic");
    if (initial) applyTopic(initial);
  }

  /* Scroll reveal (skipped for reduced motion via CSS) */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("visible"); });
  }

  /* Contact / guidance form — posts to the submissions spreadsheet. */
  document.querySelectorAll("form[data-guide-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type="submit"], button:not([type])');
      if (btn) btn.disabled = true;
      window.IGForms.post("consultation", window.IGForms.fieldsOf(form), null, function (outcome) {
        if (btn) btn.disabled = false;
        if (!status) return;
        if (outcome === "placeholder") {
          status.textContent = "The form isn't connected yet. Site owner: set the endpoint and token in js/main.js.";
          status.className = "form-status warn show";
        } else if (outcome === "ok") {
          form.reset();
          status.textContent = "Thank you. Your message reached us, and a person will reply by email within 24 hours.";
          window.IGTrack("generate_lead", { form: "consultation" });
          status.className = "form-status ok show";
        } else {
          status.textContent = "Something went wrong sending your message. Please try again in a moment.";
          status.className = "form-status warn show";
        }
      });
    });
  });
})();

/* ---- v3: dropdown nav ---- */
(function () {
  "use strict";
  var subs = document.querySelectorAll(".has-sub");
  subs.forEach(function (li) {
    var btn = li.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = li.getAttribute("data-open") === "true";
      subs.forEach(function (o) { o.setAttribute("data-open", "false"); o.querySelector("button").setAttribute("aria-expanded", "false"); });
      li.setAttribute("data-open", open ? "false" : "true");
      btn.setAttribute("aria-expanded", open ? "false" : "true");
    });
  });
  document.addEventListener("click", function () {
    subs.forEach(function (o) { o.setAttribute("data-open", "false"); var b = o.querySelector("button"); if (b) b.setAttribute("aria-expanded", "false"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      subs.forEach(function (o) { o.setAttribute("data-open", "false"); var b = o.querySelector("button"); if (b) b.setAttribute("aria-expanded", "false"); });
    }
  });

  /* ---- v3: eligibility quiz ---- */
  var quiz = document.querySelector("[data-quiz]");
  if (quiz) {
    quiz.addEventListener("submit", function (e) {
      e.preventDefault();
      var good = quiz.querySelector(".quiz-result.good");
      var caution = quiz.querySelector(".quiz-result.caution");
      var err = quiz.querySelector(".quiz-error");
      var status = quiz.querySelector(".form-status");
      good.classList.remove("show");
      caution.classList.remove("show");
      var heart = (quiz.querySelector('input[name="q_heart"]:checked') || {}).value;
      var answered = ["q_goal", "q_heart", "q_meds", "q_tried", "q_travel", "q_when"].every(function (n) {
        return quiz.querySelector('input[name="' + n + '"]:checked');
      });
      var emailEl = quiz.querySelector('input[name="email"]');
      if (!answered) {
        if (err) { err.style.display = "block"; err.scrollIntoView({ behavior: "smooth", block: "center" }); }
        return;
      }
      if (emailEl && !emailEl.checkValidity()) { emailEl.reportValidity(); return; }
      if (err) err.style.display = "none";
      var goal = (quiz.querySelector('input[name="q_goal"]:checked') || {}).value || "";
      var outcome = (heart === "yes" || heart === "unsure") ? "cardiac-caution" : "candidate";
      var outcomeEl = quiz.querySelector('input[name="quiz_outcome"]');
      if (outcomeEl) outcomeEl.value = outcome;
      var target = outcome === "candidate" ? good : caution;
      target.querySelectorAll('a[href*="consultation"]').forEach(function (a) {
        a.href = a.href.split("?")[0] + (goal ? "?concern=" + encodeURIComponent(goal) : "");
      });
      target.classList.add("show");
      target.scrollIntoView({ behavior: "smooth", block: "center" });
      /* send answers + email so the result can be emailed */
      var action = quiz.getAttribute("action") || "";
      if (action.indexOf("YOUR_FORM_ID") !== -1) {
        if (status) {
          status.textContent = "Email delivery isn't connected yet. Site owner: connect Formspree (replace YOUR_FORM_ID) and enable its auto-reply to send results.";
          status.className = "form-status warn show";
        }
        return;
      }
      fetch(action, { method: "POST", body: new FormData(quiz), headers: { Accept: "application/json" } })
        .then(function (res) {
          if (!res.ok) throw new Error("failed");
          if (status) {
            status.textContent = "Your result is on its way to your inbox.";
            status.className = "form-status ok show";
          }
        })
        .catch(function () {
          if (status) {
            status.textContent = "We couldn't send the email just now — your result is shown above either way.";
            status.className = "form-status warn show";
          }
        });
    });
  }

  /* ---- v3: email-gated resources ---- */
  document.querySelectorAll("form[data-res-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type="submit"], button:not([type])');
      if (btn) btn.disabled = true;
      window.IGForms.post("resource-gate", window.IGForms.fieldsOf(form), null, function (outcome) {
        if (btn) btn.disabled = false;
        if (!status) return;
        if (outcome === "placeholder") {
          status.textContent = "Downloads aren't connected yet. Site owner: set the endpoint and token in js/main.js.";
          status.className = "form-status warn show";
        } else if (outcome === "ok") {
          form.reset();
          status.textContent = "Saved. We will email it to you once, when it is ready.";
          window.IGTrack("generate_lead", { form: "resource-gate" });
          status.className = "form-status ok show";
        } else {
          status.textContent = "Something went wrong. Please try again in a moment.";
          status.className = "form-status warn show";
        }
      });
    });
  });
})();

/* ---- v4: prefill consultation concern from quiz ---- */
(function () {
  var sel = document.querySelector("#f-concern");
  if (!sel) return;
  var map = { opioid: "Opioid dependence", alcohol: "Alcohol", trauma: "PTSD / trauma", pattern: "A pattern I can't break" };
  var c = new URLSearchParams(window.location.search).get("concern");
  if (c && map[c]) sel.value = map[c];
})();
