/** Stripe Price IDs — Kalyo landing → app checkout */
const PRICE_PRO_MONTHLY = 'price_1TA0VXD5T9oDXXE9jHgkoaox';
const PRICE_MAX_MONTHLY = 'price_1TEY2CD5T9oDXXE9zjAO1ust';
const PRICE_PRO_ANNUAL = 'price_1TkWoDD5T9oDXXE9DWMi9xOO';
const PRICE_MAX_ANNUAL = 'price_1TkWoED5T9oDXXE9UxosC0kk';

window.KALYO_STRIPE_PRICES = {
  pro: {
    monthly: {
      priceId: PRICE_PRO_MONTHLY,
      amountCents: 2900,
      interval: 'month',
      currency: 'usd',
    },
    annual: {
      priceId: PRICE_PRO_ANNUAL,
      amountCents: 17400,
      interval: 'year',
      currency: 'usd',
    },
  },
  max: {
    monthly: {
      priceId: PRICE_MAX_MONTHLY,
      amountCents: 3900,
      interval: 'month',
      currency: 'usd',
    },
    annual: {
      priceId: PRICE_MAX_ANNUAL,
      amountCents: 23400,
      interval: 'year',
      currency: 'usd',
    },
  },
};
