# Google Search Console — keywords + indexing

## Auth: OAuth2 (recommended)

Uses refresh token in `Kalyo/.env.local` or Vercel production:

```bash
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GOOGLE_REFRESH_TOKEN=...
GSC_SITE_URL=https://kalyo.io/
```

### Write scopes (sitemap submit + URL indexing)

The default Botio token only has `webmasters.readonly`. For automatic indexing after publish, re-authorize once with the Desktop app OAuth client (no redirect URI to register in Cloud Console):

```bash
cd ~/gsc-auth && node auth-write.js
~/gsc-auth/update-token.sh "PASTE_NEW_REFRESH_TOKEN"
```

Uses `http://localhost:3333` by default (same as `auth.js`). For manual code paste:

```bash
OAUTH_REDIRECT_URI=urn:ietf:wg:oauth:2.0:oob node auth-write.js
```

Required scopes:

- `https://www.googleapis.com/auth/webmasters.readonly` — keyword phase
- `https://www.googleapis.com/auth/webmasters` — submit sitemap
- `https://www.googleapis.com/auth/indexing` — request URL indexing

Google Cloud Console:

1. OAuth client type: **Desktop app** (no redirect URI registration needed)
2. Enable **Search Console API** and **Web Search Indexing API**

Pull env from Vercel (client id/secret only; refresh token must be set locally):

```bash
npx vercel env pull .env.local --environment=production
```

**Important:** `submit-gsc.py` runs locally and reads `Kalyo/.env.local` only — not Vercel. After `auth-write.js`, always run:

```bash
~/gsc-auth/update-token.sh "PASTE_NEW_REFRESH_TOKEN"
```

## Keyword phase

```bash
python scripts/article-batch/generate-batch.py --phase keywords --limit 40
```

Outputs:

- `output/gsc-queries.json` — real GSC queries + topic matches
- `output/keyword-scores.json` — Haiku scores with `gsc_opportunity`

## Index phase (after deploy)

Regenerates `sitemap.xml`, submits to GSC, and requests indexing for live URLs:

```bash
# Single article
python scripts/article-batch/generate-batch.py --phase index --slug test-moca-evaluacion-cognitiva

# Or directly:
python scripts/article-batch/submit-gsc.py --slug test-moca-evaluacion-cognitiva

# Batch (from topics-batch3.json slice)
python scripts/article-batch/generate-batch.py --phase index --limit 5 --offset 0

# All batch 3
python scripts/article-batch/submit-gsc.py --all-batch3
```

**Run `index` only after articles are live on https://kalyo.io** (git push + Vercel deploy).

## Auth: Service Account (fallback)

Optional if OAuth is unavailable:

1. Google Cloud → Search Console API → service account JSON
2. Save as `scripts/article-batch/gsc-service-account.json`
3. Add SA email as user in Search Console

## Property URL

Kalyo production property is **URL prefix**:

```
GSC_SITE_URL=https://kalyo.io/
```

Must match exactly what appears in Search Console (trailing slash included).
