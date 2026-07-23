#!/usr/bin/env bash
# Batch FAL image generation — articles 6-14
# Run from repo root: bash scripts/fal-batch-6-14.sh
set -euo pipefail

SCRIPT="scripts/fal-generate-one.py"

declare -A HERO_PROMPTS=(
  ["gaslighting"]="A person looking confused at their own reflection in a cracked mirror, symbolic psychological manipulation, muted tones, editorial photography style"
  ["distorsiones-cognitivas"]="A human brain with tangled colorful thought bubbles showing distorted perceptions, minimalist illustration, clean white background, psychology concept"
  ["coeficiente-intelectual"]="A person solving puzzles and patterns on a glowing screen, intelligence test concept, modern flat illustration, blue and white tones"
  ["claustrofobia"]="A person in a narrow corridor with walls closing in, dramatic lighting, psychological thriller atmosphere, muted colors"
  ["agorafobia"]="A lone person standing at the edge of a vast empty plaza, small figure in large open space, anxiety concept, desaturated editorial style"
  ["psicologia-humanista"]="A warm glowing figure reaching upward toward light, human potential and self-actualization concept, painterly illustration, warm golden tones"
  ["violencia-psicologica"]="Two silhouettes in conversation, one casting a large intimidating shadow, emotional abuse concept, stark contrast lighting, editorial style"
  ["trastorno-de-panico"]="A person clutching their chest with swirling abstract waves around them, panic attack visualization, dark blue and white tones, expressive art"
  ["desensibilizacion-sistematica"]="A calm therapist guiding a patient through relaxation steps, peaceful clinical setting, soft natural light, warm professional photography"
)

declare -A INLINE_PROMPTS=(
  ["gaslighting"]="A notebook with words being erased and rewritten, memory manipulation concept, flat lay photography, neutral tones"
  ["distorsiones-cognitivas"]="A magnifying glass distorting text on a page, cognitive bias visualization, clean desk setup, editorial photography"
  ["coeficiente-intelectual"]="A series of geometric IQ test patterns arranged neatly on paper, top-down view, clean and minimal"
  ["claustrofobia"]="A person practicing deep breathing in an open space, calm therapeutic scene, soft natural light"
  ["agorafobia"]="A person sitting safely indoors looking out at an open street through a window, warm interior light"
  ["psicologia-humanista"]="A journal open with handwritten self-reflection notes, a plant and warm coffee mug beside it, cozy therapeutic setting"
  ["violencia-psicologica"]="A wilting plant next to a healthy thriving one in identical conditions, metaphor for emotional environment effects"
  ["trastorno-de-panico"]="A breathing exercise diagram with calm blue tones, therapeutic wellness concept, clean flat design"
  ["desensibilizacion-sistematica"]="A hierarchy ladder drawn on paper with fear levels from low to high, exposure therapy concept, clean clinical illustration"
)

SLUGS=(
  gaslighting
  distorsiones-cognitivas
  coeficiente-intelectual
  claustrofobia
  agorafobia
  psicologia-humanista
  violencia-psicologica
  trastorno-de-panico
  desensibilizacion-sistematica
)

TOTAL=${#SLUGS[@]}
COUNT=0

for slug in "${SLUGS[@]}"; do
  COUNT=$((COUNT + 1))
  echo ""
  echo "[$COUNT/$TOTAL] === $slug ==="

  echo "  → hero"
  python3 "$SCRIPT" --slug "$slug" --kind hero --prompt "${HERO_PROMPTS[$slug]}"

  echo "  → inline"
  python3 "$SCRIPT" --slug "$slug" --kind inline --prompt "${INLINE_PROMPTS[$slug]}"

  echo "  ✓ $slug done"
done

echo ""
echo "✅ All $TOTAL articles generated. Run:"
echo "   git add assets/blog && git commit -m 'feat: images batch 6-14' && git push origin main"
