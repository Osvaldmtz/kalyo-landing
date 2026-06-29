#!/usr/bin/env bash
# Enrich batches 1, 2, 3 — 10 articles per chunk to avoid API saturation
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

LOG="$ROOT/scripts/article-batch/output/enrich-batches-123-run.log"
mkdir -p "$(dirname "$LOG")"
exec > >(tee -a "$LOG") 2>&1

run_chunk() {
  local batch=$1 offset=$2
  echo ""
  echo "=== Batch $batch offset=$offset limit=10 $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  python3 scripts/article-batch/enrich-articles.py --batch "$batch" --offset "$offset" --limit 10
  echo "=== Cooldown 30s ==="
  sleep 30
}

echo "=== Enrich batches 1/2/3 started $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

for offset in 0 10 20; do
  run_chunk 1 "$offset"
done

run_chunk 2 0

for offset in 0 10 20 30; do
  run_chunk 3 "$offset"
done

echo "=== Enrich batches 1/2/3 finished $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
