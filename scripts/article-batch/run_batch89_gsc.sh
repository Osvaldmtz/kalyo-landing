#!/usr/bin/env bash
# Submit all batch 8+9 URLs to Google Search Console (run AFTER deploy is live).
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

SLUGS=$(python3 -c "
import json
from pathlib import Path
slugs=[]
for b in ('8','9'):
    d=json.loads(Path('scripts/article-batch/topics-batch-'+b+'.json').read_text())
    slugs.extend(t['slug'] for t in d['topics'])
print(' '.join(slugs))
")

echo "=== GSC submit for ${#SLUGS[@]} slugs ==="
python3 "$ROOT/scripts/article-batch/submit-gsc.py" --slugs $SLUGS --no-library-index
