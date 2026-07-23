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
  'https://kalyo.io/articulos/apego-desorganizado.html',
  'https://kalyo.io/articulos/apego-ansioso.html',
  'https://kalyo.io/articulos/apego-evitativo.html',
  'https://kalyo.io/articulos/dismorfia-corporal.html',
  'https://kalyo.io/articulos/fases-del-duelo.html',
  'https://kalyo.io/articulos/habilidades-sociales.html',
  'https://kalyo.io/articulos/comunicacion-asertiva.html',
  'https://kalyo.io/articulos/dependencia-emocional.html',
  'https://kalyo.io/articulos/alexitimia.html',
  'https://kalyo.io/articulos/sindrome-del-impostor.html',
  'https://kalyo.io/articulos/condicionamiento-operante.html',
  'https://kalyo.io/articulos/condicionamiento-clasico.html',
  'https://kalyo.io/articulos/tipos-de-memoria.html',
  'https://kalyo.io/articulos/gaslighting.html',
  'https://kalyo.io/articulos/distorsiones-cognitivas.html',
  'https://kalyo.io/articulos/coeficiente-intelectual.html',
  'https://kalyo.io/articulos/disonancia-cognitiva.html',
  'https://kalyo.io/articulos/violencia-psicologica.html',
  'https://kalyo.io/articulos/terapia-familiar-sistemica.html',
  'https://kalyo.io/articulos/desensibilizacion-sistematica.html',
  'https://kalyo.io/articulos/claustrofobia.html',
  'https://kalyo.io/articulos/adiccion-redes-sociales.html',
  'https://kalyo.io/articulos/agorafobia.html',
  'https://kalyo.io/articulos/psicologia-humanista.html',
  'https://kalyo.io/articulos/trastorno-de-panico.html',
  'https://kalyo.io/articulos/psicologia-del-deporte.html',
  'https://kalyo.io/articulos/burnout-laboral.html',
  'https://kalyo.io/articulos/crianza-respetuosa.html',
  'https://kalyo.io/digitalizar-consulta-psicologica/',
  'https://kalyo.io/cobrar-sesiones-psicologia-en-linea/',
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
  let ok = 0;
  let fail = 0;

  console.log(`\nIndexing ${URLS.length} URLs via Google Indexing API...\n`);

  for (let i = 0; i < URLS.length; i++) {
    const url = URLS[i];
    const result = await publishUrl(auth, url);

    if (result.ok) {
      ok += 1;
      console.log(`[${i + 1}/${URLS.length}] ${url} → ${result.status} OK`);
    } else {
      fail += 1;
      const detail = result.message ? ` ${result.message}` : '';
      console.log(`[${i + 1}/${URLS.length}] ${url} → ${result.status} FAIL${detail}`);
    }

    if (i < URLS.length - 1) {
      await sleep(DELAY_MS);
    }
  }

  console.log('\n=== Resumen ===');
  console.log(`Total enviadas: ${URLS.length}`);
  console.log(`Exitosas:       ${ok}`);
  console.log(`Fallidas:       ${fail}`);

  if (fail > 0) process.exitCode = 1;
}

main().catch((err) => {
  console.error('ERROR:', err.message || err);
  process.exit(1);
});
