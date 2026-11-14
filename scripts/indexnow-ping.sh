#!/usr/bin/env bash
# IndexNow ping for Bing — kalyo-landing (https://kalyo.io)
#
# API key (keep in sync with root verification file):
#   bf63cc655f454739808db18cfbb65d70
# Verification file (must be live at site root):
#   https://kalyo.io/bf63cc655f454739808db18cfbb65d70.txt
# Full docs: scripts/INDEXNOW.md
#
# Usage:
#   ./scripts/indexnow-ping.sh URL [URL ...]
#   ./scripts/indexnow-ping.sh --file urls.txt
#   ./scripts/indexnow-ping.sh --articles
#   ./scripts/indexnow-ping.sh --write-urls scripts/indexnow-article-urls.txt
#   cat urls.txt | ./scripts/indexnow-ping.sh --stdin
#
set -euo pipefail

INDEXNOW_KEY="bf63cc655f454739808db18cfbb65d70"
HOST="kalyo.io"
ENDPOINT="https://api.indexnow.org/indexnow"
# IndexNow allows up to 10_000 URLs per request
BATCH_SIZE=10000

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ARTICULOS_DIR="${ROOT}/articulos"

usage() {
  sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
}

collect_article_urls() {
  local f base
  for f in "${ARTICULOS_DIR}"/*.html; do
    [[ -f "$f" ]] || continue
    base="$(basename "$f")"
    [[ "$base" == "index.html" ]] && continue
    printf 'https://%s/articulos/%s\n' "$HOST" "$base"
  done | sort
}

urls=()
write_urls_path=""
mode=""
file_path=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      ;;
    --articles)
      mode="articles"
      shift
      ;;
    --file)
      mode="file"
      [[ $# -ge 2 ]] || { echo "error: --file requires a path" >&2; exit 1; }
      file_path="$2"
      shift 2
      ;;
    --stdin)
      mode="stdin"
      shift
      ;;
    --write-urls)
      [[ $# -ge 2 ]] || { echo "error: --write-urls requires a path" >&2; exit 1; }
      write_urls_path="$2"
      shift 2
      ;;
    --)
      shift
      urls+=("$@")
      break
      ;;
    -*)
      echo "error: unknown option: $1" >&2
      usage
      ;;
    *)
      urls+=("$1")
      shift
      ;;
  esac
done

if [[ -n "$write_urls_path" ]]; then
  collect_article_urls > "$write_urls_path"
  count="$(wc -l < "$write_urls_path" | tr -d ' ')"
  echo "Wrote ${count} article URLs → ${write_urls_path}"
  if [[ -z "$mode" && ${#urls[@]} -eq 0 ]]; then
    exit 0
  fi
fi

case "$mode" in
  articles)
    while IFS= read -r line; do
      [[ -n "$line" ]] && urls+=("$line")
    done < <(collect_article_urls)
    ;;
  file)
    while IFS= read -r line || [[ -n "$line" ]]; do
      line="${line%%#*}"
      line="$(printf '%s' "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
      [[ -n "$line" ]] && urls+=("$line")
    done < "$file_path"
    ;;
  stdin)
    while IFS= read -r line || [[ -n "$line" ]]; do
      line="${line%%#*}"
      line="$(printf '%s' "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
      [[ -n "$line" ]] && urls+=("$line")
    done
    ;;
esac

if [[ ${#urls[@]} -eq 0 ]]; then
  echo "error: no URLs provided. Pass URLs, --file, --articles, or --stdin." >&2
  usage
fi

# Deduplicate (order-preserving; bash 3.2 compatible)
deduped=()
for u in "${urls[@]}"; do
  skip=0
  for d in "${deduped[@]+"${deduped[@]}"}"; do
    if [[ "$d" == "$u" ]]; then
      skip=1
      break
    fi
  done
  [[ $skip -eq 1 ]] && continue
  deduped+=("$u")
done
urls=("${deduped[@]}")

total=${#urls[@]}
echo "IndexNow: submitting ${total} URL(s) for host=${HOST}"

batch_num=0
offset=0
while [[ $offset -lt $total ]]; do
  batch_num=$((batch_num + 1))
  batch=("${urls[@]:offset:BATCH_SIZE}")
  batch_count=${#batch[@]}

  payload="$(
    printf '%s\n' "${batch[@]}" | INDEXNOW_KEY="$INDEXNOW_KEY" HOST="$HOST" python3 -c '
import json, os, sys
url_list = [line.strip() for line in sys.stdin if line.strip()]
key = os.environ["INDEXNOW_KEY"]
host = os.environ["HOST"]
print(json.dumps({
    "host": host,
    "key": key,
    "keyLocation": "https://{}/{}.txt".format(host, key),
    "urlList": url_list,
}))
'
  )"

  tmp="$(mktemp)"
  printf '%s' "$payload" > "$tmp"

  echo "  batch ${batch_num}: ${batch_count} URL(s)…"
  http_code="$(
    curl -sS -o /tmp/indexnow-response.json -w "%{http_code}" \
      -X POST "$ENDPOINT" \
      -H "Content-Type: application/json; charset=utf-8" \
      --data-binary @"$tmp"
  )"
  rm -f "$tmp"

  body_preview="$(head -c 500 /tmp/indexnow-response.json 2>/dev/null || true)"
  if [[ -n "$body_preview" ]]; then
    echo "  → HTTP ${http_code} — ${body_preview}"
  else
    echo "  → HTTP ${http_code}"
  fi

  case "$http_code" in
    200|202) ;;
    *)
      echo "error: IndexNow rejected batch ${batch_num} (HTTP ${http_code})" >&2
      exit 1
      ;;
  esac

  offset=$((offset + BATCH_SIZE))
done

echo "Done. Submitted ${total} URL(s) in ${batch_num} batch(es)."
