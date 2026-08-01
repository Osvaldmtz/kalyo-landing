#!/usr/bin/env python3
"""Batch FAL image generation — Phase 2+3 part 2 (4 slugs). Run from repo root."""
import subprocess
import sys

ARTICLES = [
    (
        "normativa-psicologia-bolivia",
        "Bolivian psychology clinic with health law documents and SEDES registration forms on desk, La Paz clinical setting, professional editorial photography",
        "Psychologist reviewing clinical history folder and informed consent in Bolivian healthcare office, warm natural light",
    ),
    (
        "normativa-psicologia-paraguay",
        "Paraguayan psychology professional with Ley 3286 legal documents and MSPBS health forms, Asunción clinical office, editorial photography",
        "Clinical records and ethics code for psychologists Paraguay, flat lay on desk with stethoscope and pen",
    ),
    (
        "cie-11-toc-codigos-psicologos",
        "Psychologist reviewing ICD-11 OCD code 6B20 with Y-BOCS assessment scale on tablet, modern clinical office purple tones",
        "ICD-11 obsessive compulsive disorder classification table with related disorders 6B21-6B25, clean medical infographic",
    ),
    (
        "cie-11-trastorno-bipolar-codigos",
        "Clinical psychologist coding bipolar disorder ICD-11 6A60 with MDQ screening questionnaire, professional healthcare setting",
        "ICD-11 bipolar disorder codes table 6A60 6A61 cyclothymia with mood chart, clinical illustration flat lay",
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
