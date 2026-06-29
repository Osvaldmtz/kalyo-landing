#!/usr/bin/env python3
"""
Batch 3 article pipeline — Anthropic API + FAL, minimal Cursor tokens.

Architecture (run outside Cursor chat):
  1. keywords  — Haiku validates/scores topics (JSON only)
  2. content   — Haiku writes section JSON (NOT full HTML)
  3. assemble  — node generate-new-articles.mjs builds HTML from template (0 LLM)
  4. images    — FAL flux/schnell + local WebP via sharp (0 Cursor vision tokens)

Usage:
  export ANTHROPIC_API_KEY=... FAL_KEY=...
  python scripts/article-batch/generate-batch.py --phase keywords --limit 5
  python scripts/article-batch/generate-batch.py --phase content --slug test-moca-evaluacion-cognitiva
  python scripts/article-batch/generate-batch.py --phase images --slug test-moca-evaluacion-cognitiva
  python scripts/article-batch/generate-batch.py --phase index --slug test-moca-evaluacion-cognitiva

Cursor role: run this script + review git diff (~5k tokens/article), NOT write HTML in chat.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import anthropic
import requests

ROOT = Path(__file__).resolve().parents[2]
BATCH_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BATCH_DIR))
OUTPUT_DIR = BATCH_DIR / "output"
IMAGES_DIR = ROOT / "assets" / "blog"
CURRENT_BATCH = "3"


def resolve_topics_path(batch: str) -> Path:
    if batch in ("3", "4"):
        return BATCH_DIR / f"topics-batch{batch}.json"
    return BATCH_DIR / f"topics-batch-{batch}.json"


def topics_path() -> Path:
    return resolve_topics_path(CURRENT_BATCH)

MODEL = os.environ.get("ARTICLE_MODEL", "claude-haiku-4-5-20251001")
FAL_MODEL = "fal-ai/flux/schnell"

HERO_PROMPT_SUFFIX = (
    "Minimal flat digital illustration for psychology blog hero, purple and white palette, "
    "clinical wellness aesthetic, tablet with assessment UI, no text, no watermark, no faces"
)
INLINE_PROMPT_SUFFIX = (
    "Simple infographic style illustration, purple clinical theme, chart or scale visualization, "
    "minimal flat design, no text, white background"
)

# LLM sometimes drops tildes in meta fields while using entities elsewhere.
META_ACCENT_REPLACEMENTS = (
    ("deteccin", "detecci&oacute;n"),
    ("Deteccin", "Detecci&oacute;n"),
    ("deteccion", "detecci&oacute;n"),
    ("Deteccion", "Detecci&oacute;n"),
    ("evaluacion", "evaluaci&oacute;n"),
    ("Evaluacion", "Evaluaci&oacute;n"),
    ("interpretacion", "interpretaci&oacute;n"),
    ("Interpretacion", "Interpretaci&oacute;n"),
    ("aplicacion", "aplicaci&oacute;n"),
    ("Aplicacion", "Aplicaci&oacute;n"),
    ("administracion", "administraci&oacute;n"),
    ("Administracion", "Administraci&oacute;n"),
    ("psicologia", "psicolog&iacute;a"),
    ("Psicologia", "Psicolog&iacute;a"),
    ("geriatrica", "geri&aacute;trica"),
    ("Geriatrica", "Geri&aacute;trica"),
)


def fix_meta_spanish(text: str) -> str:
    if not text:
        return text
    for plain, entity in META_ACCENT_REPLACEMENTS:
        if plain in text and entity not in text:
            text = text.replace(plain, entity)
    return text


def normalize_article_meta(article: dict) -> dict:
    for field in ("title", "description", "h1", "intro", "heroAlt", "inlineAlt", "ctaTitle"):
        if field in article and isinstance(article[field], str):
            article[field] = fix_meta_spanish(article[field])
    for section in article.get("sections", []):
        if isinstance(section.get("title"), str):
            section["title"] = fix_meta_spanish(section["title"])
    return article


def topic_slice(limit: int, offset: int) -> list[dict]:
    return load_topics()[offset : offset + limit]


def load_topics() -> list[dict]:
    data = json.loads(topics_path().read_text(encoding="utf-8"))
    return data["topics"]


def get_client() -> anthropic.Anthropic:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)
    return anthropic.Anthropic(api_key=key)


def phase_keywords(limit: int, offset: int = 0) -> None:
    """Score topics for SEO priority — GSC real queries + Haiku JSON."""
    from gsc_client import fetch_search_queries, match_queries_to_topics, save_gsc_snapshot

    client = get_client()
    topics = topic_slice(limit, offset)
    gsc_queries = fetch_search_queries()
    gsc_matches = match_queries_to_topics(topics, gsc_queries) if gsc_queries else {}

    if gsc_queries:
        gsc_path = save_gsc_snapshot(gsc_queries, gsc_matches, OUTPUT_DIR)
        print(f"GSC: {len(gsc_queries)} queries loaded -> {gsc_path}")
    else:
        print(
            "WARN: No GSC data — set GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "
            "GOOGLE_REFRESH_TOKEN and GSC_SITE_URL=https://kalyo.io/ in .env.local "
            "(see scripts/article-batch/README-GSC.md)"
        )

    top_site_queries = []
    if gsc_queries:
        top_site_queries = sorted(gsc_queries, key=lambda q: q.get("impressions", 0), reverse=True)[:30]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_results: list[dict] = []
    chunk_size = 10

    for start in range(0, len(topics), chunk_size):
        chunk = topics[start : start + chunk_size]
        topics_with_gsc = [{**t, "gsc_matches": gsc_matches.get(t["slug"], [])} for t in chunk]
        gsc_block = ""
        if top_site_queries:
            gsc_block = f"""
Datos reales de Google Search Console (últimos 90 días, top queries del sitio):
{json.dumps(top_site_queries, ensure_ascii=False, indent=2)}
"""

        prompt = f"""Eres SEO strategist para kalyo.io (psicólogos MX/CO).
Evalúa estos {len(chunk)} temas de artículos clínicos.
{gsc_block}
Para cada uno devuelve JSON array con:
- slug
- priority_score (1-10)
- suggested_title (max 60 chars)
- meta_description (max 155 chars)
- long_tail_variants (3 frases en español)
- gsc_opportunity (query real + impresiones, o "sin datos GSC")

Temas:
{json.dumps(topics_with_gsc, ensure_ascii=False, indent=2)}

Responde SOLO JSON array válido, sin markdown."""

        msg = client.messages.create(
            model=MODEL,
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        chunk_result = json.loads(raw)
        all_results.extend(chunk_result)
        print(
            f"  scored {len(chunk_result)} topics "
            f"(tokens in={msg.usage.input_tokens} out={msg.usage.output_tokens})"
        )

    out = OUTPUT_DIR / "keyword-scores.json"
    out.write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {out} ({len(all_results)} topics scored)")


def phase_content(slug: str) -> None:
    """Generate article body as structured JSON — Haiku, not HTML."""
    client = get_client()
    topic = next((t for t in load_topics() if t["slug"] == slug), None)
    if not topic:
        print(f"ERROR: slug not found: {slug}")
        sys.exit(1)

    prompt = f"""Eres redactor clínico para kalyo.io (psicólogos Colombia/México).
Escribe contenido SEO en español para el test/instrumento:
{json.dumps(topic, ensure_ascii=False)}

Devuelve SOLO JSON con esta estructura:
{{
  "slug": "...",
  "title": "Título SEO max 60 chars | Kalyo al final opcional",
  "description": "meta description max 155 chars",
  "keywords": "comma separated",
  "h1": "título H1 con entidades HTML (&iacute; etc)",
  "intro": "párrafo intro HTML entities",
  "heroAlt": "alt text hero imagen",
  "inlineAlt": "alt text imagen inline",
  "ctaTitle": "título CTA Kalyo",
  "sections": [
    {{"title": "H2", "paragraphs": ["p1 html entities", "p2"]}}
  ],
  "faq": [{{"q": "...", "a": "..."}}],
  "related_slugs": ["slug-articulo-existente", "..."]
}}

Requisitos:
- Mínimo 8 secciones H2, ~1800-2200 palabras total
- Tono profesional, no sensacionalista
- Mencionar interpretación clínica, limitaciones, cuándo derivar
- NO inventar normas específicas sin cautela; usar "consultar normativa vigente"
- HTML entities para acentos (&aacute; &eacute; &iacute; &oacute; &uacute;)
- En title, description y h1 NUNCA omitir tildes: mal "deteccin", bien "detecci&oacute;n"
- related_slugs deben ser artículos reales de kalyo.io/articulos/

Responde SOLO JSON, sin markdown."""

    max_tokens = 16384
    last_err: Exception | None = None
    for attempt in range(3):
        msg = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        try:
            article = json.loads(raw)
            break
        except json.JSONDecodeError as exc:
            last_err = exc
            print(f"  JSON parse attempt {attempt + 1}/3 failed: {exc}")
            time.sleep(2)
    else:
        print(f"ERROR: invalid JSON for {slug}")
        raise last_err or RuntimeError("JSON parse failed")

    article = normalize_article_meta(article)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{slug}.json"
    out.write_text(json.dumps(article, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {out}")
    print(f"Tokens: input={msg.usage.input_tokens} output={msg.usage.output_tokens}")
    est_cost = (msg.usage.input_tokens * 0.8 + msg.usage.output_tokens * 4) / 1_000_000
    print(f"Est. cost Haiku: ~${est_cost:.3f} USD")


def fal_generate(prompt: str, retries: int = 3) -> bytes:
    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("ERROR: FAL_KEY not set")
        sys.exit(1)
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            resp = requests.post(
                f"https://queue.fal.run/{FAL_MODEL}",
                headers={"Authorization": f"Key {fal_key}", "Content-Type": "application/json"},
                json={
                    "prompt": prompt,
                    "image_size": "landscape_4_3",
                    "num_images": 1,
                    "num_inference_steps": 4,
                    "output_format": "jpeg",
                },
                timeout=60,
            )
            resp.raise_for_status()
            poll_url = resp.json().get("response_url") or resp.json().get("status_url")
            for _ in range(40):
                time.sleep(2)
                poll = requests.get(poll_url, headers={"Authorization": f"Key {fal_key}"}, timeout=60)
                poll.raise_for_status()
                data = poll.json()
                if data.get("images"):
                    url = data["images"][0]["url"]
                    img = requests.get(url, timeout=120)
                    img.raise_for_status()
                    return img.content
                if data.get("status") in ("FAILED", "ERROR"):
                    raise RuntimeError(data)
            raise TimeoutError("FAL image generation timed out")
        except Exception as exc:
            last_err = exc
            print(f"  FAL attempt {attempt + 1}/{retries} failed: {exc}")
            time.sleep(3)
    raise last_err or RuntimeError("FAL image generation failed")


def to_webp(jpeg_bytes: bytes, quality: int = 82) -> bytes:
    """Convert JPEG bytes to WebP using project sharp dependency."""
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_in:
        tmp_in.write(jpeg_bytes)
        tmp_in_path = tmp_in.name
    tmp_out_path = tmp_in_path.replace(".jpg", ".webp")
    script = f"""
import sharp from 'sharp';
await sharp({json.dumps(tmp_in_path)}).webp({{ quality: {quality} }}).toFile({json.dumps(tmp_out_path)});
"""
    subprocess.run(
        ["node", "--input-type=module", "-e", script],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    webp = Path(tmp_out_path).read_bytes()
    Path(tmp_in_path).unlink(missing_ok=True)
    Path(tmp_out_path).unlink(missing_ok=True)
    return webp


def phase_assemble(slug: str | None, limit: int, offset: int) -> None:
    """Build HTML articles from content JSON via assemble-batch.mjs."""
    cmd = ["node", str(BATCH_DIR / "assemble-batch.mjs"), "--batch", str(CURRENT_BATCH)]
    if slug:
        cmd.append(slug)
    else:
        if offset:
            cmd.extend(["--offset", str(offset)])
        cmd.extend(["--limit", str(limit)])
    subprocess.run(cmd, cwd=ROOT, check=True)


def phase_images(slug: str) -> None:
    topic = next((t for t in load_topics() if t["slug"] == slug), None)
    if not topic:
        print(f"ERROR: slug not found: {slug}")
        sys.exit(1)
    test_name = topic.get("primary_keyword", slug)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    hero_jpg_path = IMAGES_DIR / f"{slug}-hero.jpg"
    hero_webp_path = IMAGES_DIR / f"{slug}-hero.webp"
    inline_jpg_path = IMAGES_DIR / f"{slug}-inline.jpg"
    inline_webp_path = IMAGES_DIR / f"{slug}-inline.webp"

    if hero_jpg_path.exists() and hero_webp_path.exists():
        print(f"  hero: skip (exists)")
    else:
        print(f"Generating hero for {slug}...")
        hero_jpg = fal_generate(f"{test_name}, {HERO_PROMPT_SUFFIX}")
        hero_jpg_path.write_bytes(hero_jpg)
        hero_webp_path.write_bytes(to_webp(hero_jpg))
        print(f"  hero: {hero_jpg_path.name} ({len(hero_jpg):,} B) + {hero_webp_path.name}")

    if inline_jpg_path.exists() and inline_webp_path.exists():
        print(f"  inline: skip (exists)")
    else:
        print(f"Generating inline for {slug}...")
        inline_jpg = fal_generate(f"{test_name} clinical scale chart, {INLINE_PROMPT_SUFFIX}")
        inline_jpg_path.write_bytes(inline_jpg)
        inline_webp_path.write_bytes(to_webp(inline_jpg))
        print(f"  inline: {inline_jpg_path.name} ({len(inline_jpg):,} B) + {inline_webp_path.name}")


def phase_index(slug: str | None, limit: int, offset: int) -> None:
    """Regenerate sitemap, submit to GSC, and request indexing (run after deploy)."""
    cmd = ["python3", str(BATCH_DIR / "submit-gsc.py"), "--batch", str(CURRENT_BATCH)]
    if slug:
        cmd.extend(["--slug", slug])
    else:
        slugs = [t["slug"] for t in topic_slice(limit, offset)]
        cmd.extend(["--slugs", *slugs])
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> None:
    global CURRENT_BATCH
    parser = argparse.ArgumentParser(description="Kalyo article batch pipeline")
    parser.add_argument(
        "--phase",
        choices=["keywords", "content", "assemble", "images", "index"],
        required=True,
    )
    parser.add_argument("--batch", default="3", help="Topic batch: 3, 4, or inmediato")
    parser.add_argument("--slug", help="Article slug (content/images phases)")
    parser.add_argument("--limit", type=int, default=40, help="Max topics to process")
    parser.add_argument("--offset", type=int, default=0, help="Skip first N topics in batch list")
    args = parser.parse_args()
    CURRENT_BATCH = args.batch

    if args.phase == "keywords":
        phase_keywords(args.limit, args.offset)
    elif args.phase == "content":
        if args.slug:
            phase_content(args.slug)
        else:
            for topic in topic_slice(args.limit, args.offset):
                phase_content(topic["slug"])
    elif args.phase == "assemble":
        phase_assemble(args.slug, args.limit, args.offset)
    elif args.phase == "images":
        if args.slug:
            phase_images(args.slug)
        else:
            for topic in topic_slice(args.limit, args.offset):
                phase_images(topic["slug"])
    elif args.phase == "index":
        phase_index(args.slug, args.limit, args.offset)


if __name__ == "__main__":
    main()
