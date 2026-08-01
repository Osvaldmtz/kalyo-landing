#!/usr/bin/env python3
"""Batch FAL image generation — Phase 2+3 articles (9 slugs). Run from repo root."""
import subprocess
import sys

ARTICLES = [
    (
        "ley-salud-mental-venezuela",
        "Venezuelan healthcare legal documents and psychology ethics code on desk with stethoscope, professional editorial photography, warm clinical lighting",
        "Clinical psychologist reviewing patient history folder in Venezuelan healthcare setting, documentary style photography",
    ),
    (
        "historia-clinica-ecuador-normativa",
        "Ecuador MSP health ministry clinical record forms and digital HCE system on laptop, professional healthcare office, Latin American setting",
        "Medical records archive and consent forms for clinical history Ecuador, flat lay editorial photography, clean desk",
    ),
    (
        "ley-salud-mental-uruguay-19529",
        "Uruguay mental health law document Ley 19529 with professional psychology consultation scene, Montevideo clinical setting, editorial photography",
        "Patient rights and informed consent signing in Uruguayan mental health clinic, warm trustworthy atmosphere",
    ),
    (
        "consentimiento-informado-espana-ley-41-2002",
        "Spanish Ley 41/2002 informed consent form being signed in psychology clinic Spain, professional healthcare photography",
        "Digital and paper consent forms side by side on psychologist desk Spain, GDPR healthcare compliance concept",
    ),
    (
        "cie-11-depresion-codigos-psicologos",
        "Psychologist reviewing ICD-11 depression diagnostic codes 6A70 on clinical screen with PHQ-9 questionnaire, modern office purple tones",
        "Table of ICD-11 depression codes and severity levels on clinical chart, clean medical infographic flat lay",
    ),
    (
        "cie-11-ansiedad-codigos-psicologos",
        "Clinical psychologist coding anxiety disorders ICD-11 6B00 with GAD-7 scale results, professional healthcare setting",
        "ICD-11 anxiety disorder classification chart with panic and social anxiety codes, clean clinical illustration",
    ),
    (
        "cie-11-tept-trauma-codigos",
        "Trauma therapist with ICD-11 PTSD codes 6B40 and PCL-5 assessment, compassionate clinical setting, soft lighting",
        "Complex PTSD CPSD 6B41 diagnostic framework diagram beside trauma evaluation notes, editorial psychology concept",
    ),
    (
        "cie-11-tdah-codigos-psicologos",
        "Child ADHD evaluation with Conners scale and ICD-11 code 6A05 on psychologist tablet, bright clinical pediatric setting",
        "ADHD assessment forms ASRS and SNAP-IV with ICD-11 diagnostic coding sheet, top-down clinical photography",
    ),
    (
        "cie-11-tea-autismo-codigos",
        "Autism spectrum evaluation ADOS-2 session with ICD-11 code 6A02 reference, child-friendly clinical room, professional photography",
        "ICD-11 autism spectrum disorder support levels diagram with developmental assessment tools, clean medical illustration",
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
