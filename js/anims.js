/* Legal Ibogaine — Sanctuary edition motion layer.
   Reveals: CSS transitions + IntersectionObserver (content can never be
   trapped invisible — no JS, no observer, or a stalled tab all degrade to
   fully visible). GSAP handles only decorative motion: parallax, counters,
   hero image drift — where a stall means "static", never "missing". */
(function () {
  "use strict";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) return;

  /* ---------- Reveals ---------- */
  var SELECTORS = [
    ".section-head", ".evidence-item", ".qcard", ".router-card", ".fact",
    ".arenot", ".tl-item", ".keybox", ".res-card", ".post-row",
    ".split-block > *", ".consult-band", ".form-card",
    ".page-hero > div", ".ph-media", ".article-figure",
    ".hero-copy > *"
  ];
  if ("IntersectionObserver" in window) {
    document.documentElement.classList.add("js-anim");
    var els = document.querySelectorAll(SELECTORS.join(", "));
    /* stagger siblings that arrive together */
    var io = new IntersectionObserver(function (entries) {
      var batch = entries.filter(function (e) { return e.isIntersecting; });
      batch.forEach(function (e, i) {
        e.target.style.transitionDelay = Math.min(i * 50, 250) + "ms";
        e.target.classList.add("rv-in");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px 10% 0px" });
    els.forEach(function (el) {
      el.setAttribute("data-rv", "");
      io.observe(el);
    });
    /* absolute failsafe: everything visible after 3s regardless */
    setTimeout(function () {
      document.querySelectorAll("[data-rv]:not(.rv-in)").forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) el.classList.add("rv-in");
      });
    }, 3000);
  }

  /* ---------- Decorative GSAP layer ---------- */
  function gsapLayer() {
    if (!window.gsap || !window.ScrollTrigger) return;
    gsap.registerPlugin(window.ScrollTrigger);

    var heroImg = document.querySelector(".hero-media img");
    if (heroImg) {
      gsap.fromTo(heroImg, { scale: 1.06 }, { scale: 1, duration: 1.6, ease: "power2.out" });
      gsap.to(heroImg, {
        yPercent: 10, ease: "none",
        scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true }
      });
    }

    gsap.utils.toArray(".ph-frame img, .article-figure img").forEach(function (img) {
      gsap.fromTo(img, { yPercent: -6 }, {
        yPercent: 6, ease: "none",
        scrollTrigger: { trigger: img.closest("figure") || img, start: "top bottom", end: "bottom top", scrub: true }
      });
    });

  }
  window.addEventListener("load", gsapLayer);
})();
