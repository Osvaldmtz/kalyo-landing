#!/usr/bin/env bash
# Deploy pipeline for batch 8 (articles 1-20) + batch 9 (articles 21-40):
# images (FAL) → fix batch-9 image paths → sitemap/index verify → GSC submit
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

LOG="$ROOT/scripts/article-batch/output/batch89-deploy.log"
mkdir -p "$(dirname "$LOG")"
exec > >(tee -a "$LOG") 2>&1

echo "=== Batch 8+9 deploy started $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

if [[ -z "${FAL_KEY:-}" ]]; then
  echo "ERROR: FAL_KEY missing in .env.local"
  exit 1
fi

# Ensure topics files exist
python3 "$ROOT/scripts/article-batch/generate_topics_batch89.py"

echo ""
echo "=== Phase: images batch 8 (20 articles) ==="
python3 "$ROOT/scripts/article-batch/generate-batch.py" --phase images --batch 8 --limit 20

echo ""
echo "=== Phase: images batch 9 (20 articles) ==="
python3 "$ROOT/scripts/article-batch/generate-batch.py" --phase images --batch 9 --limit 20

echo ""
echo "=== Fix batch-9 HTML image paths (slug-specific assets) ==="
python3 "$ROOT/scripts/article-batch/fix_batch9_image_paths.py"

echo ""
echo "=== Verify index + sitemap coverage ==="
python3 "$ROOT/scripts/article-batch/verify_batch89_index.py"

echo ""
echo "=== Batch 8+9 images deploy finished $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
echo "Next: git commit + push, then run submit-gsc (URLs must be live)."
