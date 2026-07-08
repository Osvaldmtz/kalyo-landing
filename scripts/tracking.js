(function () {
  var NAMED_CTAS = {
    cta_demo_hero: true,
    cta_demo_section: true,
    cta_whatsapp_landing: true,
    cta_signup_navbar: true,
    cta_signup_hero: true,
    cta_demo_confirmed: true,
    cta_plan_starter: true,
    cta_plan_pro: true,
    cta_plan_max: true,
    cta_plan_ultra: true,
  };

  function isPlanCta(eventName) {
    return /^cta_plan_(starter|pro|max|ultra)$/.test(eventName);
  }

  var SESSION_KEY = 'kalyo_sid';

  function getSessionId() {
    try {
      var existing = localStorage.getItem(SESSION_KEY);
      if (existing) return existing;
      var sid = 'sess_' + Date.now() + '_' + Math.random().toString(36).slice(2, 10);
      localStorage.setItem(SESSION_KEY, sid);
      return sid;
    } catch (e) {
      return 'sess_anon_' + Date.now();
    }
  }

  function postCtaTrack(eventName) {
    var payload = {
      event: eventName,
      source: window.location.pathname || '/',
      session_id: getSessionId(),
      country: null,
      city: null,
    };

    try {
      var geoRaw = sessionStorage.getItem('kalyo_geo');
      if (geoRaw) {
        var geo = JSON.parse(geoRaw);
        if (geo && geo.country) payload.country = geo.country;
        if (geo && geo.city) payload.city = geo.city;
      }
    } catch (e) {
      // ignore geo parse errors
    }

    fetch('/api/cta-track', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      keepalive: true,
    }).catch(function () {
      // fire-and-forget
    });
  }

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
    var metaParams = { content_name: eventName };
    if (isPlanCta(eventName)) metaParams.source = 'landing';
    fbq('trackCustom', eventName, metaParams);
  }

  function trackCta(eventName, callback) {
    trackMeta(eventName);
    postCtaTrack(eventName);
    var gaParams = isPlanCta(eventName) ? { source: 'landing_pricing' } : {};
    trackGa(eventName, gaParams, callback);
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
