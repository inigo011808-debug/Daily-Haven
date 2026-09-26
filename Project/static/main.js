(function () {
  'use strict';

  /* Overheard strip rotates on a timer, not on page load, so the line
     changes while someone is still sitting on the page. */
  var ROTATE_MS = 3 * 60 * 1000;
  var FADE_MS = 300;

  function initOverheard() {
    var line = document.querySelector('[data-overheard]');
    var data = document.getElementById('overheard-data');
    if (!line || !data) return;

    var lines;
    try {
      lines = JSON.parse(data.textContent);
    } catch (err) {
      return;
    }
    if (!lines.length) return;

    var timeEl = line.querySelector('.talk-time');
    var quoteEl = line.querySelector('.talk-quote');
    var index = Math.floor(Math.random() * lines.length);

    function render(i) {
      timeEl.textContent = lines[i].time;
      quoteEl.textContent = '"' + lines[i].quote + '"';
    }

    render(index);

    setInterval(function () {
      index = (index + 1) % lines.length;
      line.classList.add('is-fading');
      setTimeout(function () {
        render(index);
        line.classList.remove('is-fading');
      }, FADE_MS);
    }, ROTATE_MS);
  }

  /* Menu category filter. Every group is in the DOM, so the page still
     shows the full menu if this never runs. */
  function initMenuFilter() {
    var grid = document.querySelector('.menu-grid');
    var buttons = document.querySelectorAll('.menu-cat-btn');
    if (!grid || !buttons.length) return;
    var groups = grid.querySelectorAll('.menu-group');

    function show(category) {
      groups.forEach(function (group) {
        group.hidden = group.dataset.category !== category;
      });
      buttons.forEach(function (button) {
        var isActive = button.dataset.category === category;
        button.classList.toggle('active', isActive);
        button.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      });
    }

    grid.classList.add('is-filtered');
    buttons.forEach(function (button) {
      button.addEventListener('click', function () {
        show(button.dataset.category);
      });
    });

    var initial = document.querySelector('.menu-cat-btn.active') || buttons[0];
    show(initial.dataset.category);
  }

  function init() {
    initOverheard();
    initMenuFilter();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
