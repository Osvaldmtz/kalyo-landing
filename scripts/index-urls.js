#!/usr/bin/env node
/**
 * Request Google Indexing API (URL_UPDATED) for a fixed list of Kalyo URLs.
 *
 * Auth (in order):
 * 1. Service account JSON (GSC_CREDENTIALS_PATH or common repo paths)
 * 2. OAuth refresh token from .env.local (GOOGLE_CLIENT_ID/SECRET/REFRESH_TOKEN)
 *
 * Usage: node scripts/index-urls.js
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { google } = require('googleapis');

const ROOT = path.resolve(__dirname, '..');
const DELAY_MS = 500;
const INDEXING_SCOPE = 'https://www.googleapis.com/auth/indexing';

const URLS = [
  // P3 — shortened titles
  'https://kalyo.io/articulos/test-vocacional-riasec.html',
  'https://kalyo.io/articulos/consentimiento-informado-psicologia.html',
  'https://kalyo.io/articulos/panss-esquizofrenia.html',
  'https://kalyo.io/articulos/ley-1090-psicologia-colombia.html',
  'https://kalyo.io/articulos/nom-035-ssa3-salud-mental-trabajo.html',
  'https://kalyo.io/articulos/ados-2-evaluacion-tea.html',
  'https://kalyo.io/articulos/que-es-el-phq-9.html',
  'https://kalyo.io/articulos/tipos-de-memoria.html',
  // P4 — priority orphans (new inbound links)
  'https://kalyo.io/articulos/scared-ansiedad-infantil.html',
  'https://kalyo.io/articulos/cbcl-cuestionario-capacidades-comportamiento.html',
  'https://kalyo.io/articulos/cdi-2-inventario-depresion-infantil.html',
  'https://kalyo.io/articulos/rads-2-depresion-adolescentes.html',
  'https://kalyo.io/articulos/mdq-trastorno-bipolar-tamizaje.html',
  'https://kalyo.io/articulos/ymrs-escala-mania-young.html',
  'https://kalyo.io/articulos/panss-esquizofrenia.html',
  'https://kalyo.io/articulos/cope-inventario-afrontamiento.html',
  'https://kalyo.io/articulos/ley-1616-2013-salud-mental-colombia.html',
  'https://kalyo.io/articulos/ley-2460-2025-salud-mental-colombia.html',
  'https://kalyo.io/articulos/ley-tea-colombia-pl-535-26.html',
  'https://kalyo.io/articulos/ruta-atencion-tea-colombia.html',
  'https://kalyo.io/articulos/derechos-pacientes-tea-colombia.html',
  'https://kalyo.io/articulos/vanderbilt-tdah-padres-maestros.html',
  'https://kalyo.io/articulos/mchat-rf-autismo-infantil.html',
  'https://kalyo.io/articulos/vineland-3-conducta-adaptativa.html',
  'https://kalyo.io/articulos/psqi-indice-calidad-sueno.html',
  'https://kalyo.io/articulos/ess-escala-somnolencia-epworth.html',
  'https://kalyo.io/articulos/sbq-r-conducta-suicida.html',
  'https://kalyo.io/articulos/bssi-ideacion-suicida-beck.html',
];

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function loadEnvLocal() {
  const envPath = path.join(ROOT, '.env.local');
  if (!fs.existsSync(envPath)) return;
  for (const line of fs.readFileSync(envPath, 'utf8').split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue;
    const eq = trimmed.indexOf('=');
    const key = trimmed.slice(0, eq).trim();
    let val = trimmed.slice(eq + 1).trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    if (!process.env[key]) process.env[key] = val;
  }
}

function looksLikeServiceAccount(filePath) {
  try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    return data.type === 'service_account' && Boolean(data.private_key);
  } catch {
    return false;
  }
}

function findServiceAccountPath() {
  const explicit = process.env.GSC_CREDENTIALS_PATH;
  if (explicit && fs.existsSync(explicit) && looksLikeServiceAccount(explicit)) {
    return explicit;
  }

  const candidates = [
    path.join(ROOT, 'scripts', 'article-batch', 'gsc-service-account.json'),
    path.join(ROOT, 'secrets', 'gsc-service-account.json'),
    path.join(ROOT, 'secrets', 'service_account.json'),
    path.join(ROOT, 'config', 'gsc-service-account.json'),
    path.join(ROOT, 'config', 'service_account.json'),
    path.join(ROOT, 'gsc-service-account.json'),
    path.join(ROOT, 'service_account.json'),
    path.join(ROOT, 'credentials.json'),
  ];

  for (const candidate of candidates) {
    if (fs.existsSync(candidate) && looksLikeServiceAccount(candidate)) {
      return candidate;
    }
  }

  const searchDirs = [
    ROOT,
    path.join(ROOT, 'scripts'),
    path.join(ROOT, 'scripts', 'article-batch'),
    path.join(ROOT, 'secrets'),
    path.join(ROOT, 'config'),
  ];

  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)) {
      if (!name.endsWith('.json')) continue;
      const lower = name.toLowerCase();
      if (
        !lower.includes('service_account') &&
        !lower.includes('service-account') &&
        !lower.includes('credentials') &&
        lower !== 'gsc-service-account.json'
      ) {
        continue;
      }
      const full = path.join(dir, name);
      if (looksLikeServiceAccount(full)) return full;
    }
  }

  return null;
}

async function getAuthClient() {
  loadEnvLocal();

  const saPath = findServiceAccountPath();
  if (saPath) {
    console.log(`Auth: service account (${saPath})`);
    return new google.auth.GoogleAuth({
      keyFile: saPath,
      scopes: [INDEXING_SCOPE],
    });
  }

  const clientId = process.env.GOOGLE_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_CLIENT_SECRET;
  const refreshToken = process.env.GOOGLE_REFRESH_TOKEN;

  if (!clientId || !clientSecret || !refreshToken) {
    throw new Error(
      'No service account JSON found and OAuth env missing. ' +
        'Expected scripts/article-batch/gsc-service-account.json or ' +
        'GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET / GOOGLE_REFRESH_TOKEN in .env.local'
    );
  }

  console.log('Auth: OAuth refresh token (.env.local) — no service account JSON found');
  const oauth2Client = new google.auth.OAuth2(clientId, clientSecret);
  oauth2Client.setCredentials({ refresh_token: refreshToken });
  return oauth2Client;
}

async function publishUrl(auth, url) {
  const indexing = google.indexing({ version: 'v3', auth });
  try {
    const res = await indexing.urlNotifications.publish({
      requestBody: {
        url,
        type: 'URL_UPDATED',
      },
    });
    const status = res.status || 200;
    return { ok: status >= 200 && status < 300, status };
  } catch (err) {
    const status = err?.response?.status || err?.code || 'ERR';
    const message = err?.response?.data
      ? JSON.stringify(err.response.data).slice(0, 160)
      : err.message;
    return { ok: false, status, message };
  }
}

async function main() {
  const auth = await getAuthClient();
  const uniqueUrls = [...new Set(URLS)];
  let ok = 0;
  let fail = 0;

  console.log(`\nIndexing ${uniqueUrls.length} URLs via Google Indexing API...\n`);

  for (let i = 0; i < uniqueUrls.length; i++) {
    const url = uniqueUrls[i];
    const result = await publishUrl(auth, url);

    if (result.ok) {
      ok += 1;
      console.log(`[${i + 1}/${uniqueUrls.length}] ${url} → ${result.status} OK`);
    } else {
      fail += 1;
      const detail = result.message ? ` ${result.message}` : '';
      console.log(`[${i + 1}/${uniqueUrls.length}] ${url} → ${result.status} FAIL${detail}`);
    }

    if (i < uniqueUrls.length - 1) {
      await sleep(DELAY_MS);
    }
  }

  console.log('\n=== Resumen ===');
  console.log(`Total enviadas: ${uniqueUrls.length}`);
  console.log(`Exitosas:       ${ok}`);
  console.log(`Fallidas:       ${fail}`);

  if (fail > 0) process.exitCode = 1;
}

main().catch((err) => {
  console.error('ERROR:', err.message || err);
  process.exit(1);
});
