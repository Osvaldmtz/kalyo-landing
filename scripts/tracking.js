(function () {
  function trackGa(eventName, params, callback) {
    if (typeof gtag !== 'function') {
      if (callback) callback();
      return;
    }
    var eventParams = params ? Object.assign({}, params) : {};
    if (callback) eventParams.event_callback = callback;
    gtag('event', eventName, eventParams);
  }

  function trackMeta(eventName, params) {
    if (typeof fbq === 'function') {
      fbq('track', eventName, params || {});
    }
  }

  function trackPair(gaEvent, gaParams, metaEvent, metaParams, callback) {
    trackMeta(metaEvent, metaParams);
    trackGa(gaEvent, gaParams, callback);
  }

  var CTA_MAP = {
    'cta_demo:hero': {
      ga: ['generate_lead', { source: 'hero_cta' }],
      meta: ['Lead', { content_name: 'demo_hero' }],
    },
    'cta_demo:demo_section': {
      ga: ['generate_lead', { source: 'demo_section_cta' }],
      meta: ['Lead', { content_name: 'demo_section' }],
    },
    'cta_whatsapp': {
      ga: ['contact', { method: 'whatsapp' }],
      meta: ['Contact', { content_name: 'whatsapp_cta' }],
    },
    'cta_empieza_gratis:header': {
      ga: ['sign_up', { source: 'landing' }],
      meta: ['InitiateCheckout', { content_name: 'free_signup' }],
    },
    'cta_empieza_gratis:hero': {
      ga: ['sign_up', { source: 'landing' }],
      meta: ['InitiateCheckout', { content_name: 'free_signup' }],
    },
  };

  function resolveMapping(eventName, ubicacion) {
    if (eventName === 'cta_whatsapp') return CTA_MAP['cta_whatsapp'];
    var key = eventName + ':' + (ubicacion || '');
    return CTA_MAP[key] || null;
  }

  window.kalyoTrack = {
    ga: trackGa,
    meta: trackMeta,
    pair: trackPair,
    demoConfirmed: function () {
      trackPair(
        'conversion',
        { event_category: 'demo', event_label: 'confirmed' },
        'Schedule',
        { content_name: 'demo_confirmed' },
      );
    },
  };

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-ga-event]');
    if (!a) return;

    var eventName = a.getAttribute('data-ga-event');
    var ubicacion = a.getAttribute('data-ga-ubicacion') || '';
    var mapping = resolveMapping(eventName, ubicacion);
    var href = a.getAttribute('href');
    var opensNewTab = a.target === '_blank' || e.ctrlKey || e.metaKey || e.shiftKey;

    if (mapping) {
      if (opensNewTab || !href) {
        trackPair(mapping.ga[0], mapping.ga[1], mapping.meta[0], mapping.meta[1]);
        return;
      }
      e.preventDefault();
      var navigated = false;
      function navigate() {
        if (navigated) return;
        navigated = true;
        window.location.href = href;
      }
      trackPair(mapping.ga[0], mapping.ga[1], mapping.meta[0], mapping.meta[1], navigate);
      setTimeout(navigate, 500);
      return;
    }

    if (opensNewTab || !href) {
      trackGa(eventName, ubicacion ? { ubicacion: ubicacion } : {});
      return;
    }

    e.preventDefault();
    var navDone = false;
    function go() {
      if (navDone) return;
      navDone = true;
      window.location.href = href;
    }
    trackGa(eventName, ubicacion ? { ubicacion: ubicacion } : {}, go);
    setTimeout(go, 500);
  });
})();
