"""
Kalyo Social Post Generator
Generates content with Claude, creates image with Placid, publishes via Late.
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
PLACID_API_KEY = os.environ["PLACID_API_KEY"]
LATE_API_KEY = os.environ["LATE_API_KEY"]
PLACID_TEMPLATE = os.environ["PLACID_TEMPLATE_POST"]
UNSPLASH_ACCESS_KEY = os.environ["UNSPLASH_ACCESS_KEY"]
LATE_PROFILE_ID = os.environ["LATE_PROFILE_ID"]
LATE_IG_ACCOUNT_ID = os.environ["LATE_IG_ACCOUNT_ID"]
LATE_FB_ACCOUNT_ID = os.environ["LATE_FB_ACCOUNT_ID"]

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

UNSPLASH_KEYWORDS = [
    "psychology",
    "productivity",
    "therapy",
    "healthcare",
]


# ─── Step 1: Generate content with Claude ─────────────────────────────────────

def generate_content() -> dict:
    week = datetime.date.today().isocalendar()[1]
    prompt_index = week % 4
    user_prompt = PROMPTS[prompt_index]

    print(f"[1/4] Generating content (week {week}, prompt #{prompt_index})...")

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
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
                    '  "caption": "caption completo para redes (máx 280 chars, incluir emojis y hashtags)",\n'
                    '  "hashtags": "#psicologia #psicologos #saludmental #kalyo #latam"\n'
                    "}"
                ),
            }
        ],
    )

    raw = message.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
        if raw.endswith("```"):
            raw = raw[:-3].strip()
    data = json.loads(raw)

    data["prompt_index"] = prompt_index

    print(f"  Title:   {data['title']}")
    print(f"  Caption: {data['caption']}")
    print(f"  Tags:    {data['hashtags']}")
    return data


# ─── Step 2: Generate image with Placid ───────────────────────────────────────

def fetch_unsplash_photo(keywords: str) -> str | None:
    # Replace commas with spaces for Unsplash query format
    query = keywords.replace(",", " ").strip()
    print(f"  Fetching Unsplash photo: {query}")
    try:
        resp = requests.get(
            "https://api.unsplash.com/photos/random",
            params={
                "query": query,
                "orientation": "squarish",
                "client_id": UNSPLASH_ACCESS_KEY,
            },
        )
        resp.raise_for_status()
        photo_url = resp.json()["urls"]["regular"]
        print(f"  Unsplash URL: {photo_url}")
        return photo_url
    except requests.HTTPError:
        # Fallback: try a simpler query
        print(f"  Unsplash failed for '{query}', trying fallback 'therapy'")
        resp = requests.get(
            "https://api.unsplash.com/photos/random",
            params={
                "query": "therapy",
                "orientation": "squarish",
                "client_id": UNSPLASH_ACCESS_KEY,
            },
        )
        if resp.ok:
            photo_url = resp.json()["urls"]["regular"]
            print(f"  Unsplash fallback URL: {photo_url}")
            return photo_url
        print("  Unsplash fallback also failed, skipping background")
        return None


def generate_image(title: str, unsplash_keywords: str) -> str:
    print("[2/5] Generating image with Placid...")

    background_url = fetch_unsplash_photo(unsplash_keywords)

    layers = {"title": {"text": title}}
    if background_url:
        layers["background"] = {"image": background_url}

    resp = requests.post(
        "https://api.placid.app/api/rest/images",
        headers={
            "Authorization": f"Bearer {PLACID_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "template_uuid": PLACID_TEMPLATE,
            "layers": layers,
        },
    )
    resp.raise_for_status()
    job = resp.json()

    image_url = job.get("image_url")
    poll_url = job.get("id")
    elapsed = 0

    while not image_url and elapsed < 60:
        time.sleep(5)
        elapsed += 5
        poll = requests.get(
            f"https://api.placid.app/api/rest/images/{poll_url}",
            headers={"Authorization": f"Bearer {PLACID_API_KEY}"},
        )
        poll.raise_for_status()
        poll_data = poll.json()
        status = poll_data.get("status")
        image_url = poll_data.get("image_url")
        print(f"  Poll {elapsed}s: status={status}")

    if not image_url:
        raise TimeoutError("Placid image generation timed out after 60s")

    print(f"  Image URL: {image_url}")
    return image_url


# ─── Step 3: Publish with Late ────────────────────────────────────────────────

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
    keywords = UNSPLASH_KEYWORDS[content["prompt_index"]]
    image_url = generate_image(content["title"], keywords)
    media = upload_media(image_url)
    result = publish(content["caption"], media)

    print("\n[5/5] Done!")
    print(f"  Caption:  {content['caption']}")
    print(f"  Image:    {image_url}")
    print(f"  Result:   {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    main()
