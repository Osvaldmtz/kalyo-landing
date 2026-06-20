/** Stripe Price IDs — mirror of scripts/stripe-prices.js for typed consumers */

export const PRICE_PRO_ANNUAL = "PRICE_PRO_ANNUAL";
export const PRICE_MAX_ANNUAL = "PRICE_MAX_ANNUAL";

export const stripePrices = {
  pro: {
    monthly: null as string | null,
    annual: {
      priceId: PRICE_PRO_ANNUAL,
      amountCents: 29000,
      interval: "year" as const,
      currency: "usd",
    },
  },
  max: {
    monthly: null as string | null,
    annual: {
      priceId: PRICE_MAX_ANNUAL,
      amountCents: 39000,
      interval: "year" as const,
      currency: "usd",
    },
  },
} as const;
