"""
Kalyo Social Post Generator
Generates 4 weekly post variants as drafts, sends email notification for review.
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
RESEND_API_KEY = os.environ["RESEND_API_KEY"]
NOTIFICATION_EMAIL = os.environ["NOTIFICATION_EMAIL"]

# Templated.io template IDs
TEMPLATE_OVERLAY = "528e6dad-126a-4edc-9f5c-a0dc2390ddf7"
TEMPLATE_SPLIT = "2aa508b9-d30a-4a9a-840d-26cdd3ff5804"
TEMPLATE_MINIMAL = "60d757a9-e7ec-4ff4-92ac-47e2655c2c43"
TEMPLATE_FOTO = "528e6dad-126a-4edc-9f5c-a0dc2390ddf7"

TEMPLATES = [TEMPLATE_OVERLAY, TEMPLATE_SPLIT, TEMPLATE_MINIMAL, TEMPLATE_FOTO]

LOGO_WHITE = "https://raw.githubusercontent.com/Osvaldmtz/kalyo-landing/main/assets/logo-white.svg"
LOGO_PURPLE = "https://raw.githubusercontent.com/Osvaldmtz/kalyo-landing/main/assets/logo-purple.svg"

LAYOUT_NAMES = ["Overlay", "Split", "Minimal", "Foto"]

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
    None,
    "Futuristic medical dashboard interface with purple glowing screens, neural network visualization, clinical AI technology concept, dark background, no people, photorealistic",
]


# ─── Step 1: Generate content with Claude ─────────────────────────────────────

def generate_all_content() -> list[dict]:
    week = datetime.date.today().isocalendar()[1]
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    results = []

    for idx in range(4):
        print(f"[1/4] Generating content for layout #{idx} ({LAYOUT_NAMES[idx]})...")

        subtitle_instruction = ""
        if idx in (1, 2):
            subtitle_instruction = '  "subtitle": "frase secundaria corta (máx 10 palabras)",\n'

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"{PROMPTS[idx]}\n\n"
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
        data["prompt_index"] = idx

        print(f"  Title:   {data['title']}")
        print(f"  Caption: {data['caption'][:80]}...")
        results.append(data)

    return results


# ─── Step 2: Generate backgrounds ─────────────────────────────────────────────

def generate_fal_background(prompt: str) -> str | None:
    try:
        resp = requests.post(
            "https://queue.fal.run/fal-ai/flux/schnell",
            headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": "application/json"},
            json={"prompt": prompt, "image_size": "square_hd", "num_images": 1},
        )
        resp.raise_for_status()
        response_url = resp.json()["response_url"]

        for i in range(20):
            time.sleep(3)
            result = requests.get(response_url, headers={"Authorization": f"Key {FAL_KEY}"})
            result.raise_for_status()
            data = result.json()
            if "images" in data:
                return data["images"][0]["url"]
        return None
    except Exception as e:
        print(f"  FAL error: {e}")
        return None


def fetch_unsplash_photo(query: str) -> str | None:
    try:
        resp = requests.get(
            "https://api.unsplash.com/photos/random",
            params={"query": query, "orientation": "squarish", "client_id": UNSPLASH_ACCESS_KEY},
        )
        resp.raise_for_status()
        return resp.json()["urls"]["regular"]
    except Exception as e:
        print(f"  Unsplash error: {e}")
        return None


# ─── Step 3: Render images with Templated.io ─────────────────────────────────

def render_image(content: dict) -> str:
    idx = content["prompt_index"]
    template_id = TEMPLATES[idx]
    title = content["title"]
    subtitle = content.get("subtitle", "kalyo.io")

    print(f"[2/4] Rendering layout #{idx} ({LAYOUT_NAMES[idx]})...")

    # Get background
    fal_prompt = FAL_PROMPTS[idx]
    if fal_prompt:
        print(f"  Generating FAL background...")
        bg_url = generate_fal_background(fal_prompt)
    elif idx == 3:
        bg_url = fetch_unsplash_photo("psychology office desk minimal clean")
    else:
        bg_url = None

    if bg_url:
        print(f"  Background ready")

    # Build layers
    if idx == 0:
        layers = {"title": {"text": title}, "logo": {"image_url": LOGO_WHITE}}
        if bg_url:
            layers["background"] = {"image_url": bg_url}
    elif idx == 1:
        layers = {"title": {"text": title}, "subtitle": {"text": subtitle}, "logo": {"image_url": LOGO_WHITE}}
        if bg_url:
            layers["background"] = {"image_url": bg_url}
    elif idx == 2:
        layers = {"title": {"text": title}, "subtitle": {"text": subtitle}, "logo": {"image_url": LOGO_PURPLE}}
    else:
        layers = {
            "title": {"text": title, "x": 72, "y": 72, "width": 700, "height": 300, "horizontal_align": "left", "vertical_align": "top"},
            "overlay": {"hide": True},
            "logo": {"image_url": LOGO_WHITE, "x": 860, "y": 950, "width": 160, "height": 68},
        }
        if bg_url:
            layers["background"] = {"image_url": bg_url}

    resp = requests.post(
        "https://api.templated.io/v1/render",
        headers={"Authorization": f"Bearer {TEMPLATED_API_KEY}", "Content-Type": "application/json"},
        json={"template": template_id, "layers": layers},
    )
    if not resp.ok:
        print(f"  Templated error {resp.status_code}: {resp.text}")
    resp.raise_for_status()
    image_url = resp.json()["render_url"]
    print(f"  Image: {image_url}")
    return image_url


# ─── Step 4: Upload media & create draft in Late ─────────────────────────────

def upload_media(image_url: str) -> dict:
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
    return resp.json()["files"][0]


def create_draft(caption: str, media: dict, layout_index: int) -> dict:
    # Schedule 30 days ahead so it stays as draft for review
    scheduled = (datetime.datetime.utcnow() + datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"[3/4] Creating draft for layout #{layout_index}...")
    resp = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers={"Authorization": f"Bearer {LATE_API_KEY}", "Content-Type": "application/json"},
        json={
            "content": caption,
            "profileId": LATE_PROFILE_ID,
            "platforms": [
                {"platform": "instagram", "accountId": LATE_IG_ACCOUNT_ID},
                {"platform": "facebook", "accountId": LATE_FB_ACCOUNT_ID},
            ],
            "mediaItems": [{"type": media["type"], "url": media["url"], "filename": media["filename"]}],
            "scheduledFor": scheduled,
        },
    )
    if not resp.ok:
        print(f"  Late API error {resp.status_code}: {resp.text}")
    resp.raise_for_status()
    result = resp.json()
    print(f"  Draft created: status={result.get('post', {}).get('status')} scheduled={scheduled}")
    return result


# ─── Step 5: Send notification email ─────────────────────────────────────────

def send_notification(posts: list[dict], week: int) -> None:
    print(f"[4/4] Sending notification email to {NOTIFICATION_EMAIL}...")

    rows = ""
    for p in posts:
        idx = p["layout_index"]
        rows += f"""
        <tr>
          <td style="padding:20px; border-bottom:1px solid #eee;">
            <p style="margin:0 0 8px; font-weight:bold; color:#7C3DE3;">Layout {idx}: {LAYOUT_NAMES[idx]}</p>
            <img src="{p['image_url']}" width="400" style="border-radius:8px; margin-bottom:12px;" />
            <p style="margin:0 0 4px; font-size:14px; color:#333;">{p['caption']}</p>
            <p style="margin:0; font-size:12px; color:#888;">{p['hashtags']}</p>
          </td>
        </tr>"""

    html = f"""
    <div style="font-family:Inter,Arial,sans-serif; max-width:600px; margin:0 auto;">
      <h2 style="color:#7C3DE3;">Kalyo Social Posts - Semana {week}</h2>
      <p style="color:#666;">4 borradores listos para revision en <a href="https://getlate.dev">Late</a>.</p>
      <table width="100%" cellpadding="0" cellspacing="0">{rows}</table>
      <p style="margin-top:20px; padding:16px; background:#F8F7FF; border-radius:8px; font-size:13px; color:#666;">
        Entra a <a href="https://getlate.dev" style="color:#7C3DE3;">Late</a> para aprobar, editar o reprogramar cada post.
        Los borradores estan programados a 30 dias para darte tiempo de revisar.
      </p>
    </div>"""

    resp = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {RESEND_API_KEY}", "Content-Type": "application/json"},
        json={
            "from": "Kalyo Bot <onboarding@resend.dev>",
            "to": [NOTIFICATION_EMAIL],
            "subject": f"Kalyo Social Posts - Semana {week} - 4 borradores listos",
            "html": html,
        },
    )
    if resp.ok:
        print(f"  Email sent successfully")
    else:
        print(f"  Email error {resp.status_code}: {resp.text}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    week = datetime.date.today().isocalendar()[1]
    print(f"=== Kalyo Social Posts - Week {week} ===\n")

    all_content = generate_all_content()
    posts = []

    for content in all_content:
        idx = content["prompt_index"]
        try:
            image_url = render_image(content)
            media = upload_media(image_url)
            caption_with_tags = f"{content['caption']}\n\n{content['hashtags']}"
            result = create_draft(caption_with_tags, media, idx)
            posts.append({
                "layout_index": idx,
                "image_url": image_url,
                "caption": content["caption"],
                "hashtags": content["hashtags"],
                "draft_result": result,
            })
        except Exception as e:
            print(f"  ERROR layout #{idx}: {e}")
            posts.append({
                "layout_index": idx,
                "image_url": "",
                "caption": content.get("caption", ""),
                "hashtags": content.get("hashtags", ""),
                "error": str(e),
            })

    send_notification(posts, week)

    print(f"\n=== Done! {len([p for p in posts if 'error' not in p])}/4 drafts created ===")
    for p in posts:
        status = "ERROR" if "error" in p else "OK"
        print(f"  Layout {p['layout_index']} ({LAYOUT_NAMES[p['layout_index']]}): {status}")


if __name__ == "__main__":
    main()
