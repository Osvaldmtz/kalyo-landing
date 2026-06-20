/**
 * Stripe Price IDs — Kalyo landing → app checkout
 * Reemplaza los priceId con los IDs reales del dashboard de Stripe (price_...).
 */
const PRICE_PRO_ANNUAL = 'PRICE_PRO_ANNUAL';
const PRICE_MAX_ANNUAL = 'PRICE_MAX_ANNUAL';

window.KALYO_STRIPE_PRICES = {
  pro: {
    monthly: null,
    annual: {
      priceId: PRICE_PRO_ANNUAL,
      amountCents: 17400,
      interval: 'year',
      currency: 'usd',
    },
  },
  max: {
    monthly: null,
    annual: {
      priceId: PRICE_MAX_ANNUAL,
      amountCents: 23400,
      interval: 'year',
      currency: 'usd',
    },
  },
};
