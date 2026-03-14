"""
Kalyo Social Post Generator
Generates content with Claude, creates image with Placid, publishes via Late.
"""

import os
import json
import time
import datetime
import anthropic
import requests

# ─── Config ───────────────────────────────────────────────────────────────────

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
PLACID_API_KEY = os.environ["PLACID_API_KEY"]
LATE_API_KEY = os.environ["LATE_API_KEY"]
PLACID_TEMPLATE = os.environ["PLACID_TEMPLATE_POST"]

SYSTEM_PROMPT = (
    "Eres el community manager de Kalyo, plataforma SaaS para psicólogos "
    "clínicos en Latinoamérica. Kalyo permite aplicar tests psicológicos "
    "digitalmente, generar reportes con IA y gestionar pacientes.\n"
    "Tagline: Evalúa más. Documenta menos. Trata mejor.\n"
    "URL: kalyo.io"
)

PROMPTS = [
    "Genera un post educativo sobre tests psicológicos. Incluye dato clínico relevante.",
    "Genera un post mostrando cómo Kalyo ahorra tiempo al psicólogo.",
    "Genera un post sobre el dolor del psicólogo con papeleo y cómo Kalyo lo resuelve.",
    "Genera un post de social proof o dato de impacto de Kalyo.",
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
                    '  "title": "texto corto para imagen (máx 8 palabras)",\n'
                    '  "caption": "caption completo para redes (máx 280 chars, incluir emojis y hashtags)",\n'
                    '  "hashtags": "#psicologia #psicologos #saludmental #kalyo #latam"\n'
                    "}"
                ),
            }
        ],
    )

    raw = message.content[0].text.strip()
    data = json.loads(raw)

    print(f"  Title:   {data['title']}")
    print(f"  Caption: {data['caption']}")
    print(f"  Tags:    {data['hashtags']}")
    return data


# ─── Step 2: Generate image with Placid ───────────────────────────────────────

def generate_image(title: str) -> str:
    print("[2/4] Generating image with Placid...")

    resp = requests.post(
        "https://api.placid.app/api/rest/images",
        headers={
            "Authorization": f"Bearer {PLACID_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "template_uuid": PLACID_TEMPLATE,
            "layers": {
                "title": {"text": title},
            },
        },
    )
    resp.raise_for_status()
    job = resp.json()

    image_url = job.get("image_url")
    poll_url = job.get("id")
    elapsed = 0

    while not image_url and elapsed < 30:
        time.sleep(3)
        elapsed += 3
        poll = requests.get(
            f"https://api.placid.app/api/rest/images/{poll_url}",
            headers={"Authorization": f"Bearer {PLACID_API_KEY}"},
        )
        poll.raise_for_status()
        image_url = poll.json().get("image_url")

    if not image_url:
        raise TimeoutError("Placid image generation timed out after 30s")

    print(f"  Image URL: {image_url}")
    return image_url


# ─── Step 3: Publish with Late ────────────────────────────────────────────────

def publish(caption: str, image_url: str) -> dict:
    print("[3/4] Publishing with Late...")

    resp = requests.post(
        "https://getlate.dev/api/v1/posts",
        headers={
            "Authorization": f"Bearer {LATE_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "platforms": ["instagram", "facebook"],
            "text": caption,
            "media": [{"url": image_url}],
        },
    )
    resp.raise_for_status()
    result = resp.json()

    print(f"  Publish status: {result.get('status', 'sent')}")
    return result


# ─── Step 4: Run ──────────────────────────────────────────────────────────────

def main():
    content = generate_content()
    image_url = generate_image(content["title"])
    result = publish(content["caption"], image_url)

    print("\n[4/4] Done!")
    print(f"  Caption:  {content['caption']}")
    print(f"  Image:    {image_url}")
    print(f"  Result:   {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    main()
