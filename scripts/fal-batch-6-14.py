#!/usr/bin/env python3
"""Batch FAL image generation — articles 6-14. Run from repo root."""
import subprocess, sys

ARTICLES = [
    ("gaslighting",
     "A person looking confused at their own reflection in a cracked mirror, symbolic psychological manipulation, muted tones, editorial photography style",
     "A notebook with words being erased and rewritten, memory manipulation concept, flat lay photography, neutral tones"),
    ("distorsiones-cognitivas",
     "A human brain with tangled colorful thought bubbles showing distorted perceptions, minimalist illustration, clean white background, psychology concept",
     "A magnifying glass distorting text on a page, cognitive bias visualization, clean desk setup, editorial photography"),
    ("coeficiente-intelectual",
     "A person solving puzzles and patterns on a glowing screen, intelligence test concept, modern flat illustration, blue and white tones",
     "A series of geometric IQ test patterns arranged neatly on paper, top-down view, clean and minimal"),
    ("claustrofobia",
     "A person in a narrow corridor with walls closing in, dramatic lighting, psychological thriller atmosphere, muted colors",
     "A person practicing deep breathing in an open space, calm therapeutic scene, soft natural light"),
    ("agorafobia",
     "A lone person standing at the edge of a vast empty plaza, small figure in large open space, anxiety concept, desaturated editorial style",
     "A person sitting safely indoors looking out at an open street through a window, warm interior light"),
    ("psicologia-humanista",
     "A warm glowing figure reaching upward toward light, human potential and self-actualization concept, painterly illustration, warm golden tones",
     "A journal open with handwritten self-reflection notes, a plant and warm coffee mug beside it, cozy therapeutic setting"),
    ("violencia-psicologica",
     "Two silhouettes in conversation, one casting a large intimidating shadow, emotional abuse concept, stark contrast lighting, editorial style",
     "A wilting plant next to a healthy thriving one in identical conditions, metaphor for emotional environment effects"),
    ("trastorno-de-panico",
     "A person clutching their chest with swirling abstract waves around them, panic attack visualization, dark blue and white tones, expressive art",
     "A breathing exercise diagram with calm blue tones, therapeutic wellness concept, clean flat design"),
    ("desensibilizacion-sistematica",
     "A calm therapist guiding a patient through relaxation steps, peaceful clinical setting, soft natural light, warm professional photography",
     "A hierarchy ladder drawn on paper with fear levels from low to high, exposure therapy concept, clean clinical illustration"),
]

SCRIPT = "scripts/fal-generate-one.py"
total = len(ARTICLES)

for i, (slug, hero_prompt, inline_prompt) in enumerate(ARTICLES, 1):
    print(f"\n[{i}/{total}] === {slug} ===")
    for kind, prompt in [("hero", hero_prompt), ("inline", inline_prompt)]:
        print(f"  → {kind}")
        result = subprocess.run(
            [sys.executable, SCRIPT, "--slug", slug, "--kind", kind, "--prompt", prompt],
            capture_output=False
        )
        if result.returncode != 0:
            print(f"  ✗ ERROR on {slug} {kind}", file=sys.stderr)
            sys.exit(1)
    print(f"  ✓ done")

print(f"\n✅ All {total} articles generated.")
print("Run: git add assets/blog && git commit -m 'feat: images batch 6-14' && git push origin main")
