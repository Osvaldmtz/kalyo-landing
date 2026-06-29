#!/usr/bin/env bash
# Resume batch inmediato from content (skip existing JSON), then publish all 20
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

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
exec >> "$LOG" 2>&1

echo "=== Batch inmediato RESUME $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

SLUGS=$(python3 -c "
import json
from pathlib import Path
topics = json.loads(Path('scripts/article-batch/topics-batch-inmediato.json').read_text())['topics']
out = Path('scripts/article-batch/output')
for t in topics:
    if not (out / f\"{t['slug']}.json\").exists():
        print(t['slug'])
")

for slug in $SLUGS; do
  echo "--- content: $slug ---"
  python3 scripts/article-batch/generate-batch.py --batch "$BATCH" --phase content --slug "$slug"
done

echo "--- Phase: assemble (20) ---"
python3 scripts/article-batch/generate-batch.py --batch "$BATCH" --phase assemble --limit "$LIMIT"

for slug in $(python3 -c "import json; from pathlib import Path; print(' '.join(t['slug'] for t in json.loads(Path('scripts/article-batch/topics-batch-inmediato.json').read_text())['topics']))"); do
  echo "--- images: $slug ---"
  python3 scripts/article-batch/generate-batch.py --batch "$BATCH" --phase images --slug "$slug"
done

node scripts/regenerate-sitemap.mjs
node scripts/apply-seo-improvements.mjs --index-only

git add articulos/ assets/blog/ sitemap.xml scripts/
git commit -m "Publish batch inmediato: 20 articles (keywords + TEA PL 535-26)" || echo "Nothing to commit"
git push origin main

export VERCEL_ORG_ID="${VERCEL_ORG_ID:-team_X4ytekRKzF0K6JV2x1rqQTTZ}"
export VERCEL_PROJECT_ID="${VERCEL_PROJECT_ID:-prj_oLqqlBWnWs8fuVgcepQ0hb0V9ZXH}"
if [[ -n "${VERCEL_TOKEN:-}" ]]; then
  npx vercel --prod --token "$VERCEL_TOKEN" --yes
fi

python3 scripts/article-batch/submit-gsc.py --batch "$BATCH" --all-batch

echo "=== Batch inmediato RESUME finished $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
