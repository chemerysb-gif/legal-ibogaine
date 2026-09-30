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

  /* Contact / guidance form — Formspree-ready.
     Replace YOUR_FORM_ID in the form's action attribute to go live. */
  document.querySelectorAll("form[data-guide-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      var action = form.getAttribute("action") || "";
      var status = form.querySelector(".form-status");
      if (action.indexOf("YOUR_FORM_ID") !== -1) {
        e.preventDefault();
        if (status) {
          status.textContent =
            "The form isn't connected yet. Site owner: create a free form at formspree.io and replace YOUR_FORM_ID in this form's action attribute.";
          status.className = "form-status warn show";
        }
        return;
      }
      /* Live Formspree submission via fetch for a no-redirect experience */
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = new FormData(form);
      fetch(action, {
        method: "POST",
        body: data,
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            if (status) {
              status.textContent = "Thank you — your message has been sent. We'll reply within one business day.";
              status.className = "form-status ok show";
            }
          } else {
            throw new Error("Request failed");
          }
        })
        .catch(function () {
          if (status) {
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
      var action = form.getAttribute("action") || "";
      if (action.indexOf("YOUR_FORM_ID") !== -1) {
        if (status) {
          status.textContent = "Downloads aren't connected yet. Site owner: connect Formspree (replace YOUR_FORM_ID) and set up the auto-reply with the download link.";
          status.className = "form-status warn show";
        }
        return;
      }
      if (!form.checkValidity()) { form.reportValidity(); return; }
      fetch(action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (res) {
          if (!res.ok) throw new Error("failed");
          form.reset();
          if (status) {
            status.textContent = "Done — check your inbox. The download link is on its way.";
            status.className = "form-status ok show";
          }
        })
        .catch(function () {
          if (status) {
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
