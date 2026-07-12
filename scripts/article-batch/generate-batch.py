#!/usr/bin/env python3
"""
Batch 3 article pipeline — Anthropic API + FAL, minimal Cursor tokens.

Architecture (run outside Cursor chat):
  1. keywords  — Haiku validates/scores topics (JSON only)
  2. content   — Haiku writes section JSON (NOT full HTML)
  3. assemble  — node generate-new-articles.mjs builds HTML from template (0 LLM)
  4. images    — FAL flux/schnell + local WebP via sharp (0 Cursor vision tokens)
  5. references — Perplexity sonar + HEAD verify, inject authoritative links into HTML

Usage:
  export ANTHROPIC_API_KEY=... FAL_KEY=... PERPLEXITY_API_KEY=...
  python scripts/article-batch/generate-batch.py --phase keywords --limit 5
  python scripts/article-batch/generate-batch.py --phase content --slug test-moca-evaluacion-cognitiva
  python scripts/article-batch/generate-batch.py --phase assemble --slug test-moca-evaluacion-cognitiva
  python scripts/article-batch/generate-batch.py --phase images --slug test-moca-evaluacion-cognitiva
  python scripts/article-batch/generate-batch.py --phase references --slug test-moca-evaluacion-cognitiva
  python scripts/article-batch/generate-batch.py --phase index --slug test-moca-evaluacion-cognitiva

Cursor role: run this script + review git diff (~5k tokens/article), NOT write HTML in chat.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import anthropic
import requests

ROOT = Path(__file__).resolve().parents[2]
BATCH_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BATCH_DIR))
OUTPUT_DIR = BATCH_DIR / "output"
IMAGES_DIR = ROOT / "assets" / "blog"
CURRENT_BATCH = "3"


def resolve_topics_path(batch: str) -> Path:
    if batch in ("3", "4", "5", "6"):
        return BATCH_DIR / f"topics-batch{batch}.json"
    return BATCH_DIR / f"topics-batch-{batch}.json"


def topics_path() -> Path:
    return resolve_topics_path(CURRENT_BATCH)

MODEL = os.environ.get("ARTICLE_MODEL", "claude-haiku-4-5-20251001")
FAL_MODEL = "fal-ai/flux/schnell"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
VERIFY_TIMEOUT_MS = 8000
ALLOWED_REFERENCE_DOMAINS = (
    "pubmed.ncbi.nlm.nih.gov",
    "apa.org",
    "psychiatry.org",
    "who.int",
    "nimh.nih.gov",
    "cochranelibrary.com",
    "scielo.org",
    "redalyc.org",
    "minsalud.gov.co",
    "gob.mx",
    "dof.gob.mx",
)

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
- Las referencias y citas deben enlazar EXCLUSIVAMENTE a dominios de alta autoridad: pubmed.ncbi.nlm.nih.gov, apa.org, psychiatry.org, who.int, nimh.nih.gov, cochranelibrary.com, scielo.org, redalyc.org. Nunca usar doi.org directo ni links a Elsevier/Springer/Tandfonline
- Antes de incluir cualquier URL, verifica mentalmente que el recurso existe en ese dominio. Si no estás seguro, omite el link y cita solo el texto de la referencia

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


def get_perplexity_key() -> str:
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        print("ERROR: PERPLEXITY_API_KEY not set")
        sys.exit(1)
    return key


def load_article_context(slug: str) -> dict | None:
    json_path = OUTPUT_DIR / f"{slug}.json"
    if not json_path.exists():
        print(f"SKIP: content JSON not found: {json_path}")
        return None

    article = json.loads(json_path.read_text(encoding="utf-8"))
    topic = next((t for t in load_topics() if t["slug"] == slug), None)
    primary_keyword = (
        (topic or {}).get("primary_keyword")
        or article.get("primary_keyword")
        or article.get("h1")
        or article.get("title")
        or slug
    )
    fallback_keyword = None
    if topic and topic.get("test_slug"):
        test_slug = str(topic["test_slug"]).upper()
        fallback_keyword = f"{test_slug} clinical assessment authoritative sources"
    return {
        "slug": article.get("slug", slug),
        "title": article.get("title") or article.get("h1") or slug,
        "primary_keyword": primary_keyword,
        "fallback_keyword": fallback_keyword,
    }


def domain_allowed(url: str) -> bool:
    host = urlparse(url).netloc.lower().removeprefix("www.")
    return any(host == domain or host.endswith(f".{domain}") for domain in ALLOWED_REFERENCE_DOMAINS)


def parse_perplexity_references(raw: str) -> list[dict]:
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    data: list | None = None
    try:
        parsed = json.loads(cleaned)
        if isinstance(parsed, list):
            data = parsed
    except json.JSONDecodeError:
        match = re.search(r"\[[\s\S]*\]", cleaned)
        if match:
            try:
                parsed = json.loads(match.group(0))
                if isinstance(parsed, list):
                    data = parsed
            except json.JSONDecodeError:
                pass

    refs: list[dict] = []
    if data:
        for item in data:
            if not isinstance(item, dict):
                continue
            url = str(item.get("url", "")).strip()
            title = str(item.get("title", "")).strip()
            source = str(item.get("source", "")).strip()
            if url and title and source:
                refs.append({"url": url, "title": title, "source": source})
    return refs


def references_from_api_metadata(api_data: dict) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    citation_urls = api_data.get("citations") or []
    search_results = api_data.get("search_results") or []
    items = list(search_results) + [{"url": url, "title": ""} for url in citation_urls]

    for item in items:
        url = str(item.get("url", "")).strip()
        if not url or url in seen or not domain_allowed(url):
            continue
        seen.add(url)
        host = urlparse(url).netloc.lower().removeprefix("www.")
        title = str(item.get("title") or url).strip()
        refs.append({"url": url, "title": title, "source": host})
        if len(refs) >= 4:
            break
    return refs


def build_references_prompt(primary_keyword: str, retry: bool = False) -> str:
    extra = ""
    if retry:
        extra = (
            "\nSearch specifically on pubmed.ncbi.nlm.nih.gov and nimh.nih.gov "
            "for peer-reviewed articles about this topic."
        )
    return f"""Find 4 real, working URLs from authoritative sources for the topic: '{primary_keyword}'.
Sources must be exclusively from: pubmed.ncbi.nlm.nih.gov, apa.org, psychiatry.org, who.int, nimh.nih.gov, cochranelibrary.com, scielo.org, redalyc.org, minsalud.gov.co, gob.mx, dof.gob.mx.
For each reference return:
- url: the exact URL
- title: the title of the article or document
- source: the domain name
Return ONLY a JSON array with these 4 objects. No markdown, no explanation.{extra}"""


def call_perplexity_references(primary_keyword: str, api_key: str, retry: bool = False) -> list[dict]:
    prompt = build_references_prompt(primary_keyword, retry=retry)
    response = requests.post(
        PERPLEXITY_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "sonar",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
        },
        timeout=120,
    )
    response.raise_for_status()
    api_data = response.json()
    content = api_data["choices"][0]["message"]["content"]
    refs = parse_perplexity_references(content)
    if not refs:
        refs = references_from_api_metadata(api_data)
    return refs


def fetch_references_from_perplexity(
    primary_keyword: str,
    api_key: str,
    fallback_keyword: str | None = None,
) -> list[dict]:
    last_err: Exception | None = None
    keywords = [primary_keyword]
    if fallback_keyword and fallback_keyword != primary_keyword:
        keywords.append(fallback_keyword)

    for keyword_index, keyword in enumerate(keywords):
        for attempt in range(3):
            try:
                refs = call_perplexity_references(keyword, api_key, retry=attempt > 0)
                if refs:
                    if keyword_index > 0:
                        print(f"  used fallback keyword: {keyword}")
                    return refs
                print(f"  Perplexity retry {attempt + 1}/3 ({keyword[:50]}...): empty result")
            except (requests.RequestException, ValueError, json.JSONDecodeError, KeyError) as exc:
                last_err = exc
                print(f"  Perplexity retry {attempt + 1}/3 ({keyword[:50]}...): {exc}")
            time.sleep(2 * (attempt + 1))
        if keyword_index < len(keywords) - 1:
            time.sleep(1)

    if last_err:
        raise last_err
    return []


def verify_reference_url(url: str) -> bool:
    try:
        response = requests.head(
            url,
            allow_redirects=True,
            timeout=VERIFY_TIMEOUT_MS / 1000,
            headers={"User-Agent": "KalyoReferences/1.0"},
        )
        return 200 <= response.status_code < 400
    except requests.RequestException:
        return False


def build_references_html(refs: list[dict]) -> str:
    items = []
    for ref in refs[:4]:
        url = html.escape(ref["url"], quote=True)
        label = html.escape(f"{ref['title']} — {ref['source']}")
        items.append(
            f'    <li><a href="{url}" rel="nofollow noopener noreferrer" target="_blank">{label}</a></li>'
        )
    joined = "\n".join(items)
    return (
        '<section class="article-references">\n'
        "  <h2>Referencias</h2>\n"
        "  <ul>\n"
        f"{joined}\n"
        "  </ul>\n"
        "</section>"
    )


def inject_references_html(slug: str, refs: list[dict]) -> bool:
    html_path = ROOT / "articulos" / f"{slug}.html"
    if not html_path.exists():
        print(f"SKIP: HTML not found: {html_path}")
        return False

    block = build_references_html(refs)
    content = html_path.read_text(encoding="utf-8")
    existing = re.search(
        r'<section class="article-references">[\s\S]*?</section>',
        content,
    )
    if existing:
        updated = content[: existing.start()] + block + content[existing.end() :]
    elif "</article>" in content:
        updated = content.replace("</article>", f"{block}\n\n  </article>", 1)
    else:
        print(f"SKIP: </article> not found in {html_path}")
        return False

    html_path.write_text(updated, encoding="utf-8")
    return True


def phase_references(slug: str) -> int:
    """Fetch verified authoritative references via Perplexity and inject into HTML."""
    context = load_article_context(slug)
    if context is None:
        return 0

    html_path = ROOT / "articulos" / f"{slug}.html"
    if not html_path.exists():
        print(f"SKIP: HTML not found: {html_path}")
        return 0

    api_key = get_perplexity_key()
    primary_keyword = context["primary_keyword"]

    print(f"Topic: {primary_keyword}")
    print("Querying Perplexity...")
    time.sleep(1)
    candidates = fetch_references_from_perplexity(
        primary_keyword,
        api_key,
        context.get("fallback_keyword"),
    )
    print(f"Perplexity returned {len(candidates)} candidate(s)")

    verified: list[dict] = []
    for ref in candidates:
        url = ref["url"]
        if not domain_allowed(url):
            print(f"  skip (domain): {url}")
            continue
        if verify_reference_url(url):
            verified.append(ref)
            print(f"  verified: {url}")
        else:
            print(f"  rejected: {url}")
        if len(verified) >= 4:
            break

    if not verified:
        print("No verified references — HTML unchanged")
        return 0

    if not inject_references_html(slug, verified):
        return 0

    print(f"OK: injected {len(verified)} reference(s) into articulos/{slug}.html")
    print("\n--- Generated references HTML ---")
    print(build_references_html(verified))
    print("--- End ---")
    return len(verified)


def main() -> None:
    global CURRENT_BATCH
    parser = argparse.ArgumentParser(description="Kalyo article batch pipeline")
    parser.add_argument(
        "--phase",
        choices=["keywords", "content", "assemble", "images", "references", "index"],
        required=True,
    )
    parser.add_argument("--batch", default="3", help="Topic batch: 3, 4, 5, 6, or inmediato")
    parser.add_argument("--slug", help="Article slug (content/images/references phases)")
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
    elif args.phase == "references":
        total_refs = 0
        injected_articles = 0
        skipped = 0
        unchanged = 0
        slugs = [args.slug] if args.slug else [t["slug"] for t in topic_slice(args.limit, args.offset)]
        for topic_slug in slugs:
            count = phase_references(topic_slug)
            if count > 0:
                total_refs += count
                injected_articles += 1
            elif (OUTPUT_DIR / f"{topic_slug}.json").exists() and (ROOT / "articulos" / f"{topic_slug}.html").exists():
                unchanged += 1
            else:
                skipped += 1
            if not args.slug:
                time.sleep(1)
        print(
            f"\nSUMMARY batch {CURRENT_BATCH}: "
            f"{injected_articles} articles updated, {total_refs} references injected, "
            f"{unchanged} unchanged, {skipped} skipped"
        )
    elif args.phase == "index":
        phase_index(args.slug, args.limit, args.offset)


if __name__ == "__main__":
    main()
