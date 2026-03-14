"""
Kalyo Social Post Generator
Generates content with Claude, creates image with Templated.io, publishes via Late.
"""

import os
import json
import time
import tempfile
import datetime
import anthropic
import requests

# ─── Config ───────────────────────────────────────────────────────────────────

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
TEMPLATED_API_KEY = os.environ["TEMPLATED_API_KEY"]
LATE_API_KEY = os.environ["LATE_API_KEY"]
FAL_KEY = os.environ["FAL_KEY"]
UNSPLASH_ACCESS_KEY = os.environ["UNSPLASH_ACCESS_KEY"]
LATE_PROFILE_ID = os.environ["LATE_PROFILE_ID"]
LATE_IG_ACCOUNT_ID = os.environ["LATE_IG_ACCOUNT_ID"]
LATE_FB_ACCOUNT_ID = os.environ["LATE_FB_ACCOUNT_ID"]

# Templated.io template IDs
TEMPLATE_OVERLAY = "528e6dad-126a-4edc-9f5c-a0dc2390ddf7"   # Layout 0: overlay
TEMPLATE_SPLIT = "2aa508b9-d30a-4a9a-840d-26cdd3ff5804"     # Layout 1: split
TEMPLATE_MINIMAL = "60d757a9-e7ec-4ff4-92ac-47e2655c2c43"   # Layout 2: minimal
TEMPLATE_FOTO = "528e6dad-126a-4edc-9f5c-a0dc2390ddf7"      # Layout 3: reuses overlay

TEMPLATES = [TEMPLATE_OVERLAY, TEMPLATE_SPLIT, TEMPLATE_MINIMAL, TEMPLATE_FOTO]

LOGO_WHITE = "https://raw.githubusercontent.com/Osvaldmtz/kalyo-landing/main/assets/logo-white.svg"
LOGO_PURPLE = "https://raw.githubusercontent.com/Osvaldmtz/kalyo-landing/main/assets/logo-purple.svg"

SYSTEM_PROMPT = """\
Eres el community manager de Kalyo (kalyo.io), plataforma SaaS B2B para psicólogos clínicos en Latinoamérica.

PRODUCTO:
- Kalyo permite aplicar 91 tests psicológicos digitalmente (PHQ-9, GAD-7, BAI, RIASEC, PCL-5, MBI y más)
- Genera reportes clínicos con IA en segundos, no en horas
- Gestión de pacientes con expediente digital, notas SOAP y mapa de riesgo
- Interpretación automática DSM-5
- Plan Pro: $29 USD/mes
- Tagline: "Evalúa más. Documenta menos. Trata mejor."

AUDIENCIA:
Psicólogos clínicos latinoamericanos, 28-45 años, práctica privada o institucional.
Frustrados con el papeleo, quieren ser más eficientes sin perder rigor clínico.

TONO:
- Empático y directo, de igual a igual con el profesional
- Clínico sin ser frío
- Orientado a resultados concretos con datos específicos
- Español latinoamericano neutro, sin regionalismos
- Sin hype ("revolucionario", "disruptivo", "game-changer")
- Sin tuteo excesivo

EJEMPLOS DE POSTS BUENOS:
Ejemplo 1 (educativo):
"El PHQ-9 tiene una sensibilidad del 88% para detectar depresión mayor con un punto de corte de 10.
Ese número que ves en pantalla no es solo un score — es la diferencia entre intervenir a tiempo o no.
Kalyo lo califica automáticamente. Tú decides qué hacer con el resultado.
kalyo.io 🔗
#psicologiaclinica #evaluacionpsicologica #PHQ9 #psicologos #saludmental"

Ejemplo 2 (dolor del psicólogo):
"3 horas semanales en promedio.
Eso es lo que un psicólogo pasa corrigiendo tests en papel, calculando puntajes y escribiendo reportes.
12 horas al mes que podrías estar en sesión.
Con Kalyo: aplicas el test por link, el reporte llega solo.
kalyo.io
#psicologos #evaluacionpsicologica #eficienciaclinica #saludmental #latam"

Ejemplo 3 (producto):
"El GAD-7 en Kalyo no es solo un formulario.
Es un formulario + calificación automática + interpretación DSM-5 + comparativa con sesión anterior + alerta si el score sube.
Todo en 3 minutos.
Pruébalo gratis: kalyo.io
#ansiedadgeneralizada #GAD7 #psicologiaclinica #psicologos"

REGLAS:
- Máximo 280 caracteres para el caption principal (sin contar hashtags)
- Incluir siempre kalyo.io
- 4-6 hashtags relevantes, sin inventar
- El título para la imagen debe ser máximo 6 palabras, impactante
- Nunca usar emojis en exceso — máximo 2 por post
- Siempre incluir un dato clínico concreto o estadística real cuando sea posible
"""

PROMPTS = [
    "Crea un post educativo sobre uno de estos tests: PHQ-9, GAD-7, BAI, PCL-5, MBI o RIASEC. Incluye un dato clínico específico sobre su sensibilidad, especificidad o punto de corte validado.",
    "Crea un post mostrando el tiempo real que Kalyo ahorra al psicólogo. Usa números concretos y contrasta el antes (papel) con el después (Kalyo).",
    "Crea un post que conecte con el dolor del psicólogo ante el papeleo y la documentación. Que el psicólogo sienta que lo entiendes antes de mencionar Kalyo.",
    "Crea un post mostrando una función específica de Kalyo: reportes con IA, mapa de riesgo, interpretación DSM-5 o expediente digital. Muestra el beneficio clínico concreto.",
]

FAL_PROMPTS = [
    "A psychological assessment form and brain scan visualization, purple and violet color palette, dark moody clinical atmosphere, bokeh background, professional medical aesthetic, no people, photorealistic",
    "Hourglass with glowing purple light, digital calendar and clock elements, time concept visualization, deep purple gradient background, modern minimal, no people, photorealistic",
    None,  # Layout 2 (minimal) does not use FAL
    "Futuristic medical dashboard interface with purple glowing screens, neural network visualization, clinical AI technology concept, dark background, no people, photorealistic",
]


# ─── Step 1: Generate content with Claude ─────────────────────────────────────

def generate_content() -> dict:
    week = datetime.date.today().isocalendar()[1]
    prompt_index = week % 4
    user_prompt = PROMPTS[prompt_index]

    print(f"[1/5] Generating content (week {week}, layout #{prompt_index})...")

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    subtitle_instruction = ""
    if prompt_index in (1, 2):
        subtitle_instruction = '  "subtitle": "frase secundaria corta (máx 10 palabras)",\n'

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": (
                    f"{user_prompt}\n\n"
                    "Responde SOLO con JSON válido, sin markdown ni explicaciones:\n"
                    "{\n"
                    '  "title": "texto corto para imagen (máx 6 palabras)",\n'
                    f"{subtitle_instruction}"
                    '  "caption": "caption completo para redes (máx 280 chars)",\n'
                    '  "hashtags": "#psicologia #psicologos #saludmental #kalyo #latam"\n'
                    "}"
                ),
            }
        ],
    )

    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
        if raw.endswith("```"):
            raw = raw[:-3].strip()
    data = json.loads(raw)
    data["prompt_index"] = prompt_index

    print(f"  Title:   {data['title']}")
    if "subtitle" in data:
        print(f"  Subtitle:{data['subtitle']}")
    print(f"  Caption: {data['caption']}")
    print(f"  Tags:    {data['hashtags']}")
    return data


# ─── Step 2: Generate background ─────────────────────────────────────────────

def generate_fal_background(prompt: str) -> str | None:
    print("  Generating background with FAL.ai...")
    try:
        resp = requests.post(
            "https://queue.fal.run/fal-ai/flux/schnell",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json",
            },
            json={"prompt": prompt, "image_size": "square_hd", "num_images": 1},
        )
        resp.raise_for_status()
        response_url = resp.json()["response_url"]

        for i in range(20):
            time.sleep(3)
            result = requests.get(
                response_url,
                headers={"Authorization": f"Key {FAL_KEY}"},
            )
            result.raise_for_status()
            data = result.json()
            if "images" in data:
                url = data["images"][0]["url"]
                print(f"  FAL image URL: {url}")
                return url
            print(f"  FAL poll {(i+1)*3}s: status={data.get('status', 'unknown')}")
        print("  FAL timed out, skipping background")
        return None
    except Exception as e:
        print(f"  FAL error: {e}, skipping background")
        return None


def fetch_unsplash_photo(query: str) -> str | None:
    print(f"  Fetching Unsplash photo: {query}")
    try:
        resp = requests.get(
            "https://api.unsplash.com/photos/random",
            params={"query": query, "orientation": "squarish", "client_id": UNSPLASH_ACCESS_KEY},
        )
        resp.raise_for_status()
        url = resp.json()["urls"]["regular"]
        print(f"  Unsplash URL: {url}")
        return url
    except Exception as e:
        print(f"  Unsplash error: {e}")
        return None


# ─── Step 3: Render image with Templated.io ──────────────────────────────────

def render_image(content: dict) -> str:
    idx = content["prompt_index"]
    template_id = TEMPLATES[idx]
    title = content["title"]
    subtitle = content.get("subtitle", "kalyo.io")

    print(f"[2/5] Rendering image with Templated.io (layout #{idx})...")

    # Get background image based on layout
    fal_prompt = FAL_PROMPTS[idx]
    if fal_prompt:
        bg_url = generate_fal_background(fal_prompt)
    elif idx == 3:
        bg_url = fetch_unsplash_photo("psychology therapist office")
    else:
        bg_url = None

    # Build layers based on layout
    if idx == 0:
        # Overlay: FAL background + purple overlay + logo white + title
        layers = {
            "title": {"text": title},
            "logo": {"image_url": LOGO_WHITE},
        }
        if bg_url:
            layers["background"] = {"image_url": bg_url}

    elif idx == 1:
        # Split: FAL background right + purple left + logo white + title + subtitle
        layers = {
            "title": {"text": title},
            "subtitle": {"text": subtitle},
            "logo": {"image_url": LOGO_WHITE},
        }
        if bg_url:
            layers["background"] = {"image_url": bg_url}

    elif idx == 2:
        # Minimal: white background + purple bar + logo purple + title + subtitle
        layers = {
            "title": {"text": title},
            "subtitle": {"text": subtitle},
            "logo": {"image_url": LOGO_PURPLE},
        }

    else:
        # Foto: Unsplash background + white card + logo purple + title
        layers = {
            "title": {"text": title},
            "logo": {"image_url": LOGO_PURPLE},
        }
        if bg_url:
            layers["background"] = {"image_url": bg_url}

    print(f"  Rendering template: {template_id}")
    resp = requests.post(
        "https://api.templated.io/v1/render",
        headers={
            "Authorization": f"Bearer {TEMPLATED_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "template": template_id,
            "layers": layers,
        },
    )
    if not resp.ok:
        print(f"  Templated error {resp.status_code}: {resp.text}")
    resp.raise_for_status()
    result = resp.json()
    image_url = result["render_url"]

    print(f"  Image URL: {image_url}")
    return image_url


# ─── Step 4: Publish with Late ────────────────────────────────────────────────

def upload_media(image_url: str) -> dict:
    print("[3/5] Uploading media to Late...")

    img_resp = requests.get(image_url)
    img_resp.raise_for_status()

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp.write(img_resp.content)
        tmp_path = tmp.name

    with open(tmp_path, "rb") as f:
        resp = requests.post(
            "https://getlate.dev/api/v1/media",
            headers={"Authorization": f"Bearer {LATE_API_KEY}"},
            files={"files": ("post.jpg", f, "image/jpeg")},
        )

    os.unlink(tmp_path)

    if not resp.ok:
        print(f"  Late media error {resp.status_code}: {resp.text}")
    resp.raise_for_status()
    media = resp.json()["files"][0]

    print(f"  Media URL: {media['url']}")
    return media


def publish(caption: str, media: dict) -> dict:
    print("[4/5] Publishing with Late...")

    resp = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers={
            "Authorization": f"Bearer {LATE_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "content": caption,
            "profileId": LATE_PROFILE_ID,
            "platforms": [
                {"platform": "instagram", "accountId": LATE_IG_ACCOUNT_ID},
                {"platform": "facebook", "accountId": LATE_FB_ACCOUNT_ID},
            ],
            "mediaItems": [
                {
                    "type": media["type"],
                    "url": media["url"],
                    "filename": media["filename"],
                }
            ],
            "publishNow": True,
        },
    )
    if not resp.ok:
        print(f"  Late API error {resp.status_code}: {resp.text}")
    resp.raise_for_status()
    result = resp.json()

    print(f"  Publish status: {result.get('message', 'sent')}")
    return result


# ─── Step 5: Run ──────────────────────────────────────────────────────────────

def main():
    content = generate_content()
    image_url = render_image(content)
    media = upload_media(image_url)
    result = publish(content["caption"], media)

    print("\n[5/5] Done!")
    print(f"  Caption:  {content['caption']}")
    print(f"  Image:    {image_url}")
    print(f"  Result:   {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    main()
