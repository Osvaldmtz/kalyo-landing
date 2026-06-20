(function () {
  const APP_BASE = 'https://app.kalyo.io';
  const prices = window.KALYO_STRIPE_PRICES || {};

  const PRICING = {
    starter: {
      monthly: { display: '$0', suffix: '/ mes', period: 'Empieza gratis. Sin tarjeta.', note: '' },
    },
    pro: {
      monthly: { display: '$29', suffix: 'USD / mes', period: 'Menos que una sesión. Todo lo esencial.', note: '' },
      annual: {
        display: '$14.5',
        suffix: 'USD / mes',
        period: '',
        note: '$174 USD facturado anualmente · Ahorras $174',
      },
    },
    max: {
      monthly: { display: '$39', suffix: 'USD / mes', period: 'La experiencia clínica completa.', note: '' },
      annual: {
        display: '$19.5',
        suffix: 'USD / mes',
        period: '',
        note: '$234 USD facturado anualmente · Ahorras $234',
      },
    },
  };

  function readUtms() {
    try {
      return JSON.parse(sessionStorage.getItem('kalyo_utm') || '{}');
    } catch {
      return {};
    }
  }

  function buildCheckoutUrl(priceId) {
    const url = new URL(APP_BASE);
    if (priceId) url.searchParams.set('price_id', priceId);
    Object.entries(readUtms()).forEach(([key, value]) => {
      if (value) url.searchParams.set(key, value);
    });
    return url.toString();
  }

  function resolvePriceId(plan, billing) {
    if (billing !== 'annual') return null;
    return prices[plan]?.annual?.priceId || null;
  }

  function renderPriceAmount(wrap, data) {
    if (!wrap) return;
    wrap.replaceChildren();
    const value = document.createElement('span');
    value.className = 'precio-price-value';
    value.textContent = data.display;
    const suffix = document.createElement('span');
    suffix.className = 'precio-price-suffix';
    suffix.textContent = ` ${data.suffix}`;
    wrap.appendChild(value);
    wrap.appendChild(suffix);
  }

  function updateCard(card, billing) {
    const plan = card.dataset.plan;
    const tier = PRICING[plan];
    if (!tier) return;

    const isAnnual = billing === 'annual' && Boolean(tier.annual);
    const data = isAnnual ? tier.annual : tier.monthly;
    const amountEl = card.querySelector('.precio-amount');
    const periodEl = card.querySelector('[data-price-period]');
    const noteEl = card.querySelector('[data-price-note]');
    const ctaEl = card.querySelector('[data-price-cta]');

    card.classList.toggle('is-annual-billing', isAnnual);
    renderPriceAmount(amountEl, data);

    if (periodEl) {
      periodEl.textContent = data.period;
      periodEl.hidden = !data.period;
    }
    if (noteEl) {
      noteEl.textContent = data.note || '';
      noteEl.hidden = !data.note;
    }
    if (ctaEl) {
      ctaEl.href = buildCheckoutUrl(resolvePriceId(plan, billing));
    }
  }

  function setBilling(billing) {
    document.querySelectorAll('.precios-billing-option').forEach((btn) => {
      const active = btn.dataset.billing === billing;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    });

    document.querySelectorAll('.precio-card[data-plan]').forEach((card) => {
      updateCard(card, billing);
    });

    document.body.dataset.preciosBilling = billing;
  }

  function init() {
    const toggle = document.querySelector('.precios-billing-toggle');
    if (!toggle) return;

    toggle.querySelectorAll('.precios-billing-option').forEach((btn) => {
      btn.addEventListener('click', () => setBilling(btn.dataset.billing));
    });

    setBilling('monthly');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
