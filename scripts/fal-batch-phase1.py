#!/usr/bin/env python3
"""Batch FAL image generation — Phase 1 articles (7 slugs). Run from repo root."""
import subprocess
import sys

ARTICLES = [
    (
        "test-vocacional-psicologia-clinica",
        "Clinical psychologist reviewing vocational career assessment forms with a teenager in a modern purple-toned office, warm professional photography, Latin American setting",
        "Flat lay of Holland RIASEC hexagon diagram and aptitude test answer sheets on a desk, clean editorial style, psychology career guidance",
    ),
    (
        "estilos-de-aprendizaje-evaluacion-clinica",
        "Psychologist explaining learning styles assessment to a student with visual diagrams on tablet, modern clinical setting, soft natural light",
        "VARK learning styles chart with icons for visual auditory reading kinesthetic, minimalist educational illustration on white background",
    ),
    (
        "arquetipos-jung-aplicacion-clinica",
        "Symbolic Jungian archetypes collage with shadow and anima motifs, artistic editorial style, muted purple and gold tones, psychology concept",
        "Open clinical notebook with Jungian archetype symbols sketched beside therapy session notes, warm desk lamp light, professional photography",
    ),
    (
        "inteligencias-multiples-evaluacion-clinica",
        "Child completing multiple intelligences assessment with psychologist observing, colorful Gardner theory icons, bright clinical educational setting",
        "Infographic showing Gardner nine multiple intelligences in a circular diagram, clean modern illustration, psychology education theme",
    ),
    (
        "cie-11-trastornos-mentales-psicologos",
        "Clinical psychologist coding mental health diagnosis using ICD-11 reference on laptop, modern healthcare office, professional documentary style",
        "WHO ICD-11 classification manual open beside clinical chart with diagnostic codes, top-down flat lay, clean medical photography",
    ),
    (
        "ley-20584-derechos-paciente-chile",
        "Chilean healthcare patient rights document with stethoscope and pen on desk, legal medical context, professional editorial photography",
        "Psychologist explaining informed consent form to patient in Chilean clinical setting, warm trustworthy atmosphere, natural light",
    ),
    (
        "cie-11-vs-dsm-5-diferencias",
        "Two diagnostic classification manuals side by side ICD-11 and DSM-5 on psychologist desk, comparison concept, clean professional photography",
        "Split screen visual comparing WHO and APA diagnostic systems with clinical notes, modern infographic style, purple accent colors",
    ),
]

SCRIPT = "scripts/fal-generate-one.py"
total = len(ARTICLES)

for i, (slug, hero_prompt, inline_prompt) in enumerate(ARTICLES, 1):
    print(f"\n[{i}/{total}] === {slug} ===")
    for kind, prompt in [("hero", hero_prompt), ("inline", inline_prompt)]:
        print(f"  → {kind}")
        result = subprocess.run(
            [sys.executable, SCRIPT, "--slug", slug, "--kind", kind, "--prompt", prompt],
            capture_output=False,
        )
        if result.returncode != 0:
            print(f"  ✗ ERROR on {slug} {kind}", file=sys.stderr)
            sys.exit(1)
    print("  ✓ done")

print(f"\n✅ All {total} articles generated ({total * 2} images).")
