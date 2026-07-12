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
  panss-esquizofrenia
  ham-d-escala-hamilton-depresion
  cage-tamizaje-alcoholismo
  epds-depresion-postparto
  brief-funciones-ejecutivas
  conners-3-tdah-ninos
  neo-pi-r-personalidad
  scid-5-entrevista-clinica
  pdss-depresion-postparto
  stai-ansiedad-estado-rasgo
  nom-025-ssa2-atencion-psiquiatrica
  nom-047-ssa2-salud-mental-adolescentes
  nom-046-ssa2-violencia-familiar
  ley-2460-2025-salud-mental-colombia
  resolucion-2764-2022-riesgo-psicosocial
  politica-nacional-salud-mental-2024-2033
  ley-1616-2013-salud-mental-colombia
  sivigila-notificacion-salud-mental
  nom-035-ssa3-salud-mental-trabajo
  historia-clinica-psicologica-colombia
)

total=${#SLUGS[@]}
i=0
for slug in "${SLUGS[@]}"; do
  i=$((i + 1))
  echo "========== [$i/$total] $slug =========="
  python3 scripts/article-batch/generate-batch.py --batch 5 --phase content --slug "$slug"
  python3 scripts/article-batch/generate-batch.py --batch 5 --phase assemble --slug "$slug"
  python3 scripts/article-batch/generate-batch.py --batch 5 --phase images --slug "$slug"
done

node scripts/regenerate-sitemap.mjs
node scripts/apply-seo-improvements.mjs --index-only

echo "DONE: batch 5 generation complete"
