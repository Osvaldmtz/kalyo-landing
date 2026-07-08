(function () {
  var NAMED_CTAS = {
    cta_demo_hero: true,
    cta_demo_section: true,
    cta_whatsapp_landing: true,
    cta_signup_navbar: true,
    cta_signup_hero: true,
    cta_demo_confirmed: true,
  };

  function trackGa(eventName, params, callback) {
    if (typeof gtag !== 'function') {
      if (callback) callback();
      return;
    }
    var eventParams = params ? Object.assign({}, params) : {};
    if (callback) eventParams.event_callback = callback;
    gtag('event', eventName, eventParams);
  }

  function trackMeta(eventName) {
    if (typeof fbq !== 'function') return;
    fbq('trackCustom', eventName, { content_name: eventName });
  }

  function trackCta(eventName, callback) {
    trackMeta(eventName);
    trackGa(eventName, {}, callback);
  }

  window.kalyoTrack = {
    ga: trackGa,
    meta: trackMeta,
    cta: trackCta,
    demoConfirmed: function () {
      trackCta('cta_demo_confirmed');
    },
  };

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-ga-event]');
    if (!a) return;

    var eventName = a.getAttribute('data-ga-event');
    if (!NAMED_CTAS[eventName]) return;

    var href = a.getAttribute('href');
    var opensNewTab = a.target === '_blank' || e.ctrlKey || e.metaKey || e.shiftKey;

    if (opensNewTab || !href) {
      trackCta(eventName);
      return;
    }

    e.preventDefault();
    var navigated = false;
    function navigate() {
      if (navigated) return;
      navigated = true;
      window.location.href = href;
    }
    trackCta(eventName, navigate);
    setTimeout(navigate, 500);
  });
})();
