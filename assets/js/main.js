/* HONEST — interacciones */
(function () {
  "use strict";

  /* Header shadow on scroll */
  var header = document.querySelector(".site-header");
  var onScroll = function () {
    if (!header) return;
    header.classList.toggle("scrolled", window.scrollY > 8);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobile nav */
  var burger = document.querySelector(".burger");
  var mnav = document.querySelector(".mobile-nav");
  var scrim = document.querySelector(".scrim");
  function closeNav() {
    if (burger) burger.classList.remove("open");
    if (mnav) mnav.classList.remove("open");
    if (scrim) scrim.classList.remove("open");
    document.body.style.overflow = "";
  }
  function toggleNav() {
    var open = mnav && mnav.classList.contains("open");
    if (open) { closeNav(); return; }
    if (burger) burger.classList.add("open");
    if (mnav) mnav.classList.add("open");
    if (scrim) scrim.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  if (burger) burger.addEventListener("click", toggleNav);
  if (scrim) scrim.addEventListener("click", closeNav);
  if (mnav) mnav.querySelectorAll("a").forEach(function (a) {
    a.addEventListener("click", closeNav);
  });
  window.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeNav();
  });

  /* Reveal on scroll */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* Portfolio filter (portfolio page) */
  var chips = document.querySelectorAll(".chip");
  var works = document.querySelectorAll("[data-cat]");
  if (chips.length && works.length) {
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        chips.forEach(function (c) { c.classList.remove("active"); });
        chip.classList.add("active");
        var f = chip.getAttribute("data-filter");
        works.forEach(function (w) {
          var show = f === "all" || w.getAttribute("data-cat") === f;
          w.style.display = show ? "" : "none";
        });
      });
    });
  }

  /* Contact form (demo, no backend) */
  var form = document.querySelector("form[data-demo]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var btn = form.querySelector("button[type=submit]");
      var ok = form.querySelector(".form-ok");
      if (btn) { btn.textContent = "¡Gracias! Te escribimos pronto"; btn.disabled = true; }
      if (ok) ok.hidden = false;
      form.reset();
      setTimeout(function () {
        if (btn) { btn.textContent = "Enviar"; btn.disabled = false; }
      }, 3500);
    });
  }

  /* Wordmark interactivo: cuadrado de color aleatorio al hacer hover (estilo honestpg) */
  var WM_COLORS = ["#387B4F", "#334C80", "#C43E2F", "#F7DE50"];
  document.querySelectorAll(".wm--interactive i").forEach(function (letter) {
    if (letter.classList.contains("dot")) return;
    letter.addEventListener("mouseenter", function () {
      var c = WM_COLORS[Math.floor(Math.random() * WM_COLORS.length)];
      letter.style.setProperty("--sq", c);
    });
  });

  /* Year in footer */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
