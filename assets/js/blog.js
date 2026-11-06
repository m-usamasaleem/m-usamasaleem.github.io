/* Blog motion: reveal figures and timeline items as they scroll into view.
   Pure progressive enhancement; without JS or with reduced motion, everything is shown. */
(function () {
  'use strict';
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) { root.classList.add('anim-off'); return; }
  root.classList.add('anim-on');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.15 });
  document.querySelectorAll('[data-anim]').forEach(function (el) { io.observe(el); });
})();

/* Era player: auto-advances while visible; buttons select an era; pauses on hover/focus.
   Reduced motion: no auto-advance, eras still selectable. */
(function () {
  'use strict';
  var player = document.querySelector('.era');
  if (!player) return;
  var data = JSON.parse(player.getAttribute('data-eras'));
  var dots = player.querySelectorAll('.era-dot');
  var yearEl = player.querySelector('.era-year');
  var toolEl = player.querySelector('.era-tool');
  var gainEl = player.querySelector('.era-gain');
  var costEl = player.querySelector('.era-cost');
  var glass = player.querySelector('.era-glass');
  var playBtn = player.querySelector('.era-play');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var MS = 4200, idx = 0, timer = null, visible = false, userPaused = reduce, hover = false;
  player.style.setProperty('--era-ms', MS + 'ms');

  function render(i, animate) {
    idx = i;
    var d = data[i];
    var apply = function () {
      yearEl.textContent = d.year;
      yearEl.classList.toggle('now', !!d.now);
      toolEl.textContent = d.tool;
      gainEl.textContent = d.gain;
      costEl.textContent = d.cost;
      glass.innerHTML = document.getElementById(d.svg).innerHTML;
      dots.forEach(function (b, j) { b.setAttribute('aria-selected', j === i ? 'true' : 'false'); b.tabIndex = j === i ? 0 : -1; });
      player.classList.remove('switching');
    };
    if (animate && !reduce) { player.classList.add('switching'); setTimeout(apply, 260); } else { apply(); }
  }
  function playing() { return visible && !userPaused && !hover; }
  function schedule() {
    clearTimeout(timer);
    player.classList.toggle('playing', playing());
    // restart the progress bar animation
    var bar = player.querySelector('.era-dot[aria-selected="true"] .bar');
    if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
    if (playing()) timer = setTimeout(function () { render((idx + 1) % data.length, true); setTimeout(schedule, 300); }, MS);
  }
  dots.forEach(function (b, j) {
    b.addEventListener('click', function () { render(j, true); setTimeout(schedule, 300); });
    b.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        var n = (idx + (e.key === 'ArrowRight' ? 1 : data.length - 1)) % data.length;
        render(n, true); dots[n].focus(); setTimeout(schedule, 300);
      }
    });
  });
  playBtn.addEventListener('click', function () {
    userPaused = !userPaused;
    playBtn.textContent = userPaused ? 'Play' : 'Pause';
    playBtn.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
    schedule();
  });
  playBtn.textContent = userPaused ? 'Play' : 'Pause';
  player.addEventListener('mouseenter', function () { hover = true; schedule(); });
  player.addEventListener('mouseleave', function () { hover = false; schedule(); });
  player.addEventListener('focusin', function () { hover = true; schedule(); });
  player.addEventListener('focusout', function () { hover = false; schedule(); });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { visible = es[0].isIntersecting; schedule(); }, { threshold: 0.4 }).observe(player);
  }
  render(0, false);
})();
