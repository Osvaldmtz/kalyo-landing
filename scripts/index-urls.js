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
  // P4 batches 2+3 — 38 orphan articles
  'https://kalyo.io/articulos/hads-ansiedad-depresion-hospitalaria.html',
  'https://kalyo.io/articulos/ham-d-escala-hamilton-depresion.html',
  'https://kalyo.io/articulos/isi-indice-severidad-insomnio.html',
  'https://kalyo.io/articulos/k6-tamizaje-salud-mental.html',
  'https://kalyo.io/articulos/ley-1616-2013-salud-mental-colombia.html',
  'https://kalyo.io/articulos/ley-2460-2025-salud-mental-colombia.html',
  'https://kalyo.io/articulos/mejor-software-para-psicologos-clinicos.html',
  'https://kalyo.io/articulos/neo-pi-r-personalidad.html',
  'https://kalyo.io/articulos/nom-025-ssa2-atencion-psiquiatrica.html',
  'https://kalyo.io/articulos/oq-45-resultados-terapia.html',
  'https://kalyo.io/articulos/paralisis-del-sueno.html',
  'https://kalyo.io/articulos/pdss-depresion-postparto.html',
  'https://kalyo.io/articulos/politica-nacional-salud-mental-2024-2033.html',
  'https://kalyo.io/articulos/psicologia-del-deporte.html',
  'https://kalyo.io/articulos/psicologia-humanista.html',
  'https://kalyo.io/articulos/psicologia-inclusion-educativa-tea.html',
  'https://kalyo.io/articulos/rcmas-2-ansiedad-infantil.html',
  'https://kalyo.io/articulos/resiliencia-que-es.html',
  'https://kalyo.io/articulos/resolucion-1888-salud-mental-colombia.html',
  'https://kalyo.io/articulos/resolucion-2764-2022-riesgo-psicosocial.html',
  'https://kalyo.io/articulos/rips-registros-individuales-colombia.html',
  'https://kalyo.io/articulos/scid-5-entrevista-clinica.html',
  'https://kalyo.io/articulos/scoff-trastornos-alimentarios.html',
  'https://kalyo.io/articulos/sivigila-notificacion-salud-mental.html',
  'https://kalyo.io/articulos/srq-20-salud-mental-autorreportado.html',
  'https://kalyo.io/articulos/tdah-adultos.html',
  'https://kalyo.io/articulos/test-wartegg-proyectiva.html',
  'https://kalyo.io/articulos/tests-psicologicos-de-personalidad.html',
  'https://kalyo.io/articulos/tipos-de-memoria.html',
  'https://kalyo.io/articulos/tlp-trastorno-limite.html',
  'https://kalyo.io/articulos/trastorno-de-panico.html',
  'https://kalyo.io/articulos/violencia-psicologica.html',
  'https://kalyo.io/articulos/zung-escala-ansiedad.html',
  'https://kalyo.io/articulos/zung-escala-depresion.html',
  'https://kalyo.io/articulos/adiccion-que-es.html',
  'https://kalyo.io/articulos/anorexia-que-es.html',
  'https://kalyo.io/articulos/crianza-respetuosa.html',
  'https://kalyo.io/articulos/empatia-que-es.html',
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
