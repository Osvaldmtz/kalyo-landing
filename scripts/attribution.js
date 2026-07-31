(function () {
  var STORAGE_KEY = 'kalyo_attribution';
  var COOKIE_NAME = 'kalyo_attribution';
  var COOKIE_MAX_AGE = 90 * 24 * 60 * 60;
  var PARAM_KEYS = [
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_content',
    'utm_term',
    'gclid',
    'fbclid',
  ];

  function isKalyoHost() {
    var host = window.location.hostname;
    return host === 'kalyo.io' || host.endsWith('.kalyo.io') || host === 'localhost';
  }

  function readCookie() {
    try {
      var match = document.cookie.match(new RegExp('(?:^|;\\s*)' + COOKIE_NAME + '=([^;]*)'));
      if (!match) return null;
      return JSON.parse(decodeURIComponent(match[1]));
    } catch (e) {
      return null;
    }
  }

  function writeCookie(data) {
    try {
      var encoded = encodeURIComponent(JSON.stringify(data));
      var secure = window.location.protocol === 'https:' ? '; Secure' : '';
      var domain =
        window.location.hostname === 'localhost' ? '' : '; domain=.kalyo.io';
      document.cookie =
        COOKIE_NAME +
        '=' +
        encoded +
        '; path=/' +
        domain +
        '; max-age=' +
        COOKIE_MAX_AGE +
        '; SameSite=Lax' +
        secure;
    } catch (e) {
      // ignore cookie write errors
    }
  }

  function readStored() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) {
      // ignore parse errors
    }
    return readCookie();
  }

  function writeStored(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
      // ignore quota errors
    }
    writeCookie(data);
  }

  function deriveSource(params) {
    if (params.gclid) return 'google';
    if (params.fbclid) return 'facebook';
    var src = (params.utm_source || '').toLowerCase();
    if (src.indexOf('google') !== -1) return 'google';
    if (src.indexOf('facebook') !== -1 || src.indexOf('meta') !== -1 || src.indexOf('instagram') !== -1) {
      return 'facebook';
    }
    return src || 'direct';
  }

  function captureFromUrl() {
    if (!isKalyoHost()) return null;
    if (readStored()) return readStored();

    var search = new URLSearchParams(window.location.search);
    var params = {};
    PARAM_KEYS.forEach(function (key) {
      var value = search.get(key);
      if (value) params[key] = value;
    });

    if (Object.keys(params).length === 0) return null;

    var data = {
      source: deriveSource(params),
      utm_source: params.utm_source || null,
      utm_medium: params.utm_medium || null,
      utm_campaign: params.utm_campaign || null,
      utm_content: params.utm_content || null,
      utm_term: params.utm_term || null,
      gclid: params.gclid || null,
      fbclid: params.fbclid || null,
      landing_url: window.location.href,
      first_seen_at: new Date().toISOString(),
    };

    writeStored(data);
    return data;
  }

  function appendToUrl(href) {
    var data = readStored();
    if (!data || !href) return href;

    try {
      var url = new URL(href, window.location.origin);
      if (url.hostname.indexOf('kalyo.io') === -1) return href;

      PARAM_KEYS.forEach(function (key) {
        if (data[key] && !url.searchParams.has(key)) {
          url.searchParams.set(key, data[key]);
        }
      });

      if (data.landing_url && !url.searchParams.has('landing_url')) {
        url.searchParams.set('landing_url', data.landing_url);
      }

      return url.toString();
    } catch (e) {
      return href;
    }
  }

  function decorateAppLinks(root) {
    var scope = root || document;
    scope.querySelectorAll('a[href*="app.kalyo.io"], a[href*="kalyo.io/login"]').forEach(function (a) {
      var next = appendToUrl(a.getAttribute('href'));
      if (next) a.setAttribute('href', next);
    });
  }

  function init() {
    captureFromUrl();
    decorateAppLinks();

    if (typeof MutationObserver === 'function') {
      var observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
          mutation.addedNodes.forEach(function (node) {
            if (node.nodeType !== 1) return;
            if (node.matches && node.matches('a[href*="app.kalyo.io"], a[href*="kalyo.io/login"]')) {
              var href = appendToUrl(node.getAttribute('href'));
              if (href) node.setAttribute('href', href);
            }
            if (node.querySelectorAll) decorateAppLinks(node);
          });
        });
      });
      observer.observe(document.body, { childList: true, subtree: true });
    }
  }

  window.kalyoAttribution = {
    captureFromUrl: captureFromUrl,
    read: readStored,
    appendToUrl: appendToUrl,
    decorateAppLinks: decorateAppLinks,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
