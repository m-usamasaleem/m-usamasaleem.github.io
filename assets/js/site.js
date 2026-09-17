/* Progressive enhancement only — all content lives in the HTML.
   Covers: hamburger nav, scroll-spy, news show-more, viewport-aware video. */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Hamburger navigation -------------------------------------------- */
  var navToggle = document.querySelector('.nav-toggle');
  var navMenu = document.getElementById('site-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function () {
      var open = navMenu.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    navMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navMenu.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* --- Scroll-spy -------------------------------------------------------- */
  var spyLinks = document.querySelectorAll('.nav-links a[href^="#"]');
  var sections = [];
  spyLinks.forEach(function (link) {
    var el = document.getElementById(link.getAttribute('href').slice(1));
    if (el) sections.push({ el: el, link: link });
  });
  if (sections.length && 'IntersectionObserver' in window) {
    var current = null;
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          if (current) current.classList.remove('active');
          var match = sections.find(function (s) { return s.el === entry.target; });
          if (match) { match.link.classList.add('active'); current = match.link; }
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    sections.forEach(function (s) { spy.observe(s.el); });
  }

  /* --- News show all / show less ---------------------------------------- */
  var moreBtn = document.querySelector('.show-more');
  var oldNews = document.querySelectorAll('.news-item[data-old]');
  if (moreBtn && oldNews.length) {
    moreBtn.setAttribute('aria-expanded', 'false');
    moreBtn.addEventListener('click', function () {
      var expanded = moreBtn.getAttribute('aria-expanded') === 'true';
      oldNews.forEach(function (item) { item.hidden = expanded; });
      moreBtn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      moreBtn.textContent = expanded ? 'Show all news' : 'Show less';
    });
  } else if (moreBtn) {
    moreBtn.hidden = true;
  }

  /* --- Viewport-aware research video playback ---------------------------
     Videos ship with preload="none" + poster; they start only when near the
     viewport and pause when they leave. Autoplay failures are ignored.
     Under prefers-reduced-motion nothing plays. */
  var videos = document.querySelectorAll('video[data-autoplay]');
  if (videos.length && !reducedMotion && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var v = entry.target;
        if (entry.isIntersecting) {
          var p = v.play();
          if (p && p.catch) p.catch(function () { /* autoplay blocked — poster stays */ });
        } else if (!v.paused) {
          v.pause();
        }
      });
    }, { rootMargin: '200px 0px' });
    videos.forEach(function (v) { io.observe(v); });
  }
})();
