// Ponymail-style alphabetical tabs on the /projects overview page.
(function () {
  var tabs = document.getElementById('project-tabs');
  if (!tabs) {
    return;
  }
  tabs.classList.add('js-enabled');

  var buttons = tabs.querySelectorAll('.project-tab');
  var panels = tabs.querySelectorAll('.project-tab-panel');

  function activate(letter) {
    var matched = false;
    buttons.forEach(function (button) {
      var on = button.getAttribute('data-letter') === letter;
      button.classList.toggle('active', on);
      button.setAttribute('aria-selected', on ? 'true' : 'false');
      matched = matched || on;
    });
    panels.forEach(function (panel) {
      panel.classList.toggle('active', panel.getAttribute('data-letter') === letter);
    });
    return matched;
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      var letter = button.getAttribute('data-letter');
      activate(letter);
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', '#letter-' + letter);
      }
    });
  });

  // Deep link: #letter-X selects the matching tab.
  function fromHash() {
    var letterMatch = /^#letter-(.+)$/.exec(window.location.hash);
    if (letterMatch) {
      return activate(letterMatch[1]);
    }
    return false;
  }

  fromHash();
  window.addEventListener('hashchange', fromHash);
})();