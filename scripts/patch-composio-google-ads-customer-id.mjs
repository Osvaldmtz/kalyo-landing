#!/usr/bin/env node
/**
 * Patch Composio Google Ads connected account customer_id.
 *
 * Usage:
 *   COMPOSIO_API_KEY=... node scripts/patch-composio-google-ads-customer-id.mjs
 *
 * Optional:
 *   COMPOSIO_CONNECTED_ACCOUNT_ID=googleads_forger-punky  (default)
 *   GOOGLE_ADS_CUSTOMER_ID=4356627994                     (default)
 */
const API_KEY = process.env.COMPOSIO_API_KEY?.trim();
const ACCOUNT_ID = process.env.COMPOSIO_CONNECTED_ACCOUNT_ID?.trim() || 'googleads_forger-punky';
const CUSTOMER_ID = (process.env.GOOGLE_ADS_CUSTOMER_ID || '4356627994').replace(/\D/g, '');

if (!API_KEY) {
  console.error('Missing COMPOSIO_API_KEY');
  process.exit(1);
}

if (!/^\d{10}$/.test(CUSTOMER_ID)) {
  console.error(`Invalid GOOGLE_ADS_CUSTOMER_ID: ${CUSTOMER_ID}`);
  process.exit(1);
}

const BASE = 'https://backend.composio.dev/api/v3.1';

async function api(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, {
    ...options,
    headers: {
      'x-api-key': API_KEY,
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
  });
  const text = await res.text();
  let json;
  try {
    json = JSON.parse(text);
  } catch {
    json = { raw: text };
  }
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${JSON.stringify(json)}`);
  }
  return json;
}

async function main() {
  const list = await api(
    `/connected_accounts?connected_account_ids[]=${encodeURIComponent(ACCOUNT_ID)}&limit=1`,
  );
  const account = list.items?.[0];
  if (!account) {
    throw new Error(`Connected account not found: ${ACCOUNT_ID}`);
  }

  const authScheme = account.state?.authScheme || account.auth_config?.auth_scheme || 'OAUTH2';
  const currentVal = account.state?.val || {};
  const currentCustomerId =
    currentVal.customer_id || currentVal.customerId || currentVal.generic_id || '(unset)';

  console.log('Account:', account.id, account.alias || '');
  console.log('Current customer_id in connection:', currentCustomerId);
  console.log('Patching to:', CUSTOMER_ID);

  const patch = await api(`/connected_accounts/${account.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      connection: {
        state: {
          authScheme,
          val: {
            ...currentVal,
            customer_id: CUSTOMER_ID,
          },
        },
      },
    }),
  });

  console.log('Patch result:', JSON.stringify(patch, null, 2));
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
