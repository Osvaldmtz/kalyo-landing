#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."

if [ -f .env.local ]; then
  set -a
  # shellcheck disable=SC1091
  source .env.local
  set +a
fi

SLUGS=(
  teleconsulta-para-psicologos-latinoamerica
  notas-clinicas-inteligencia-artificial-psicologos
  como-reducir-inasistencias-consulta-psicologica
  alternativas-a-doctoralia-para-psicologos
  mejor-software-para-psicologos-clinicos
  tests-psicologicos-de-personalidad
)

total=${#SLUGS[@]}
i=0
for slug in "${SLUGS[@]}"; do
  i=$((i + 1))
  echo "========== [$i/$total] $slug =========="
  python3 scripts/article-batch/generate-batch.py --batch 6 --phase content --slug "$slug"
  python3 scripts/article-batch/generate-batch.py --batch 6 --phase assemble --slug "$slug"
  python3 scripts/article-batch/generate-batch.py --batch 6 --phase images --slug "$slug"
done

node scripts/regenerate-sitemap.mjs
node scripts/apply-seo-improvements.mjs --index-only

echo "DONE: batch 6 generation complete"
