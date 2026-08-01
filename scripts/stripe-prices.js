/** Stripe Price IDs — Kalyo landing → app checkout */
const PRICE_PRO_MONTHLY = 'price_1TA0VXD5T9oDXXE9jHgkoaox';
const PRICE_MAX_MONTHLY = 'price_1TEY2CD5T9oDXXE9zjAO1ust';
const PRICE_PRO_ANNUAL = 'price_1TzTIYD5T9oDXXE90kIcfsdx';
const PRICE_MAX_ANNUAL = 'price_1TzTIZD5T9oDXXE9G37MORkm';
const PRICE_ULTRA_MONTHLY = 'price_1TqguUD5T9oDXXE9DG7um2mU';
const PRICE_ULTRA_ANNUAL = 'price_1TzTIaD5T9oDXXE9vjFaebx6';

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
      amountCents: 27800,
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
      amountCents: 37400,
      interval: 'year',
      currency: 'usd',
    },
  },
  ultra: {
    monthly: {
      priceId: PRICE_ULTRA_MONTHLY,
      amountCents: 6900,
      interval: 'month',
      currency: 'usd',
    },
    annual: {
      priceId: PRICE_ULTRA_ANNUAL,
      amountCents: 66200,
      interval: 'year',
      currency: 'usd',
    },
  },
};
