# Google Search Console — keyword phase

## Auth: OAuth2 (recommended — same as Botio / Vercel)

Uses refresh token already configured in Vercel:

```bash
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GOOGLE_REFRESH_TOKEN=...
GSC_SITE_URL=https://kalyo.io/
```

Pull from Vercel:

```bash
npx vercel env pull .env.local --environment=production
```

Or copy the three `GOOGLE_*` vars from Botio/Vercel into `Kalyo/.env.local`.

The refresh token must include scope `https://www.googleapis.com/auth/webmasters.readonly`
(or `webmasters`) from the original OAuth consent flow.

## Auth: Service Account (fallback)

Optional if OAuth is unavailable:

1. Google Cloud → Search Console API → service account JSON
2. Save as `scripts/article-batch/gsc-service-account.json`
3. Add SA email as user in Search Console

## Run

```bash
python scripts/article-batch/generate-batch.py --phase keywords --limit 40
```

Outputs:
- `output/gsc-queries.json` — real GSC queries + topic matches
- `output/keyword-scores.json` — Haiku scores with `gsc_opportunity`

## Property URL

Kalyo production property is **URL prefix**:

```
GSC_SITE_URL=https://kalyo.io/
```

Must match exactly what appears in Search Console (trailing slash included).
