#!/usr/bin/env bash
# Full pipeline for topics-batch-inmediato.json (20 articles)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

# Load .env.local
if [[ -f .env.local ]]; then
  set -a
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    key="${line%%=*}"
    val="${line#*=}"
    val="${val%\"}"; val="${val#\"}"
    val="${val%\'}"; val="${val#\'}"
    export "$key=$val"
  done < .env.local
  set +a
fi

BATCH=inmediato
LIMIT=20
LOG="$ROOT/scripts/article-batch/output/batch-inmediato-run.log"
mkdir -p "$(dirname "$LOG")"

exec > >(tee -a "$LOG") 2>&1

echo "=== Batch inmediato pipeline started $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

echo "--- Phase: content (20) ---"
python3 scripts/article-batch/generate-batch.py --batch "$BATCH" --phase content --limit "$LIMIT"

echo "--- Phase: assemble (20) ---"
python3 scripts/article-batch/generate-batch.py --batch "$BATCH" --phase assemble --limit "$LIMIT"

echo "--- Phase: images (20) ---"
python3 scripts/article-batch/generate-batch.py --batch "$BATCH" --phase images --limit "$LIMIT"

echo "--- Regenerate sitemap ---"
node scripts/regenerate-sitemap.mjs

echo "--- Update article index ---"
node scripts/apply-seo-improvements.mjs --index-only

echo "--- Git commit + push ---"
git add articulos/ assets/blog/ sitemap.xml scripts/
git config user.name "github-actions[bot]" 2>/dev/null || git config user.name "Kalyo Batch"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com" 2>/dev/null || true
git commit -m "Publish batch inmediato: 20 articles (keywords + TEA PL 535-26)" || echo "Nothing to commit"
git push origin main

echo "--- Deploy Vercel ---"
export VERCEL_ORG_ID="${VERCEL_ORG_ID:-team_X4ytekRKzF0K6JV2x1rqQTTZ}"
export VERCEL_PROJECT_ID="${VERCEL_PROJECT_ID:-prj_oLqqlBWnWs8fuVgcepQ0hb0V9ZXH}"
if [[ -z "${VERCEL_TOKEN:-}" ]]; then
  echo "WARN: VERCEL_TOKEN not set — skipping Vercel deploy (Hostinger deploy via push still runs)"
else
  npx vercel --prod --token "$VERCEL_TOKEN" --yes
fi

echo "--- GSC index (20 URLs) ---"
python3 scripts/article-batch/submit-gsc.py --batch "$BATCH" --all-batch

echo "=== Batch inmediato pipeline finished $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
