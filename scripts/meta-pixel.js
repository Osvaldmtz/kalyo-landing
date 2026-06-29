import { createBrowserClient } from 'https://cdn.jsdelivr.net/npm/@supabase/ssr@0.9.0/+esm';

var PIXEL_ID = '3356117344562696';

function getCookieOptions() {
  var host = location.hostname;
  if (host === 'kalyo.io' || host.endsWith('.kalyo.io')) {
    return { domain: '.kalyo.io', path: '/', sameSite: 'lax', secure: true };
  }
  return undefined;
}

!function (f, b, e, v, n, t, s) {
  if (f.fbq) return;
  n = f.fbq = function () {
    n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
  };
  if (!f._fbq) f._fbq = n;
  n.push = n;
  n.loaded = !0;
  n.version = '2.0';
  n.queue = [];
  t = b.createElement(e);
  t.async = !0;
  t.src = v;
  s = b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t, s);
}(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

function splitName(fullName) {
  if (!fullName) return {};
  var parts = fullName.trim().split(/\s+/);
  if (parts.length === 1) return { fn: parts[0] };
  return { fn: parts[0], ln: parts.slice(1).join(' ') };
}

function buildAdvancedMatching(user, psych) {
  var params = {};

  if (user.email) {
    params.em = user.email.trim().toLowerCase();
  }

  if (psych) {
    if (psych.phone) {
      params.ph = psych.phone;
    }
    var names = splitName(psych.full_name);
    if (names.fn) params.fn = names.fn.toLowerCase();
    if (names.ln) params.ln = names.ln.toLowerCase();
  }

  return Object.keys(params).length ? params : null;
}

async function getAdvancedMatchingParams() {
  var config = window.KALYO_AUTH_CONFIG;
  if (!config || !config.supabaseUrl || !config.supabaseAnonKey) return null;

  try {
    var cookieOptions = getCookieOptions();
    var supabase = createBrowserClient(
      config.supabaseUrl,
      config.supabaseAnonKey,
      cookieOptions ? { cookieOptions: cookieOptions } : undefined
    );
    var userResult = await supabase.auth.getUser();
    var user = userResult.data.user;
    if (!user) return null;

    var psychResult = await supabase
      .from('psychologists')
      .select('full_name, phone')
      .eq('auth_id', user.id)
      .maybeSingle();

    return buildAdvancedMatching(user, psychResult.data);
  } catch (_err) {
    return null;
  }
}

async function initMetaPixel() {
  var advanced = await getAdvancedMatchingParams();

  if (advanced) {
    fbq('init', PIXEL_ID, advanced);
  } else {
    fbq('init', PIXEL_ID);
  }

  fbq('track', 'PageView');
}

initMetaPixel();
