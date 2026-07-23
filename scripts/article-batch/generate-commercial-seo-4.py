#!/usr/bin/env python3
"""Generate 4 commercial SEO articles matching Kalyo article chrome."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "articulos"
BLOG = ROOT / "assets" / "blog"

elo = (ART / "alternativas-elo-psicologos-mexico.html").read_text(encoding="utf-8")
m_style = re.search(
    r"(<!-- Fonts -->.*?</style>\s*<!-- Google Analytics -->.*?</script>)",
    elo,
    re.S,
)
assert m_style, "shell not found"
SHELL_MID = m_style.group(1)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def cta(slug: str, h2: str, p: str, btn: str = "Probar Max 7 d&iacute;as gratis &rarr;") -> str:
    utm = f"utm_source=blog&utm_medium=article&utm_campaign={slug}"
    return f"""    <div class="cta-box">
      <h2>{h2}</h2>
      <p>{p}</p>
      <a href="https://app.kalyo.io/login?mode=register&{utm}" class="cta-btn">{btn}</a>
      <p style="margin-top:16px;margin-bottom:0;font-size:14px"><a href="/demo/?{utm}" style="color:rgba(255,255,255,0.9);text-decoration:underline">O agenda una demo</a></p>
    </div>"""


def build_article(cfg: dict) -> str:
    slug = cfg["slug"]
    title = cfg["title"]
    desc = cfg["desc"]
    assert 55 <= len(title) <= 60, (slug, len(title), title)
    assert 150 <= len(desc) <= 160, (slug, len(desc), desc)
    related_html = "\n".join(
        f'      <li><a href="{href}" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">{label}</a></li>'
        for href, label in cfg["related"]
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="keywords" content="{esc(cfg['keywords'])}">
  <link rel="canonical" href="https://kalyo.io/articulos/{slug}.html">

  <link rel="preload" as="image" href="/assets/blog/{slug}-hero.webp" type="image/webp">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="https://kalyo.io/articulos/{slug}.html">
  <meta property="og:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kalyo">
  <meta property="og:locale" content="es_MX">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">

  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{esc(cfg['headline'])}",
  "description": "{esc(desc)}",
  "image": "https://kalyo.io/assets/blog/{slug}-hero.jpg",
  "author": {{
    "@type": "Organization",
    "name": "Equipo Kalyo",
    "url": "https://kalyo.io/sobre-kalyo.html"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Kalyo",
    "url": "https://kalyo.io",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://kalyo.io/assets/logo.png"
    }}
  }},
  "datePublished": "2026-07-22",
  "dateModified": "2026-07-22",
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://kalyo.io/articulos/{slug}.html"
  }}
}}
</script>
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://kalyo.io/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Recursos para psicólogos",
      "item": "https://kalyo.io/articulos/"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{esc(cfg['crumb'])}",
      "item": "https://kalyo.io/articulos/{slug}.html"
    }}
  ]
}}
</script>
{SHELL_MID}
</head>
<body>

  <!-- Header -->
  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <div class="header-nav">
        <a href="/articulos/" class="header-link">Recursos</a>
        <a href="https://app.kalyo.io" class="header-btn">Iniciar sesi&oacute;n</a>
      </div>
    </div>
  </header>

  <!-- Article -->
  <article class="article-wrapper">
    <nav class="article-breadcrumb" aria-label="Breadcrumb">
      <a href="/">Inicio</a> &rsaquo; <a href="/articulos/">Recursos</a> &rsaquo; {esc(cfg['crumb'])}
    </nav>
    <div class="article-hero-img">
      <picture>
      <source srcset="/assets/blog/{slug}-hero.webp" type="image/webp">
      <img src="/assets/blog/{slug}-hero.jpg" alt="{esc(cfg['img_alt'])}" width="1200" height="630" loading="eager" fetchpriority="high">
    </picture>
    </div>
    <p class="article-meta">{cfg['meta_label']}</p>

    <h1>{cfg['h1']}</h1>

    <p class="article-date">Publicado el 22 de julio de 2026 &middot; Lectura: 12 min</p>

    <p class="article-intro">{cfg['intro']}</p>

{cfg['body']}

  <section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
    <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Art&iacute;culos relacionados</h2>
    <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
{related_html}
    </ul>
  </section>
  </article>

  <!-- Footer -->
    <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a> &middot; <a href="/sobre-kalyo.html">Sobre Kalyo</a> &middot; <a href="/contacto.html">Contacto</a></p>
  </footer>

</body>
</html>
"""


def main() -> None:
    articles: list[dict] = []

    slug = "doctoralia-vs-kalyo"
    body = f"""
    <h2>&iquest;Qu&eacute; compara realmente un psic&oacute;logo en 2026?</h2>
    <p>Doctoralia y Kalyo resuelven problemas distintos. Doctoralia es, ante todo, un <strong>directorio y canal de captaci&oacute;n</strong>: te ayuda a aparecer frente a pacientes que buscan psic&oacute;logo cerca. Kalyo es un <strong>consultorio digital cl&iacute;nico</strong>: agenda con WhatsApp, teleconsulta, expediente, 91+ tests y documentaci&oacute;n con IA. Si tu dolor es &ldquo;no me encuentran&rdquo;, el directorio importa. Si tu dolor es &ldquo;pierdo horas en papeleo y no-shows&rdquo;, necesitas operaci&oacute;n cl&iacute;nica.</p>
    <p>Muchos profesionales usan ambos en etapas distintas. Esta gu&iacute;a te ayuda a decidir cu&aacute;ndo conviene cada uno &mdash;y cu&aacute;ndo Kalyo reemplaza la mayor parte del stack diario. Tambi&eacute;n puedes revisar nuestra gu&iacute;a de <a href="/articulos/software-para-psicologos-clinicos.html">software para psic&oacute;logos cl&iacute;nicos</a>.</p>

    <h2>Tabla comparativa Doctoralia vs Kalyo (2026)</h2>
    <table class="items-table">
      <thead>
        <tr>
          <th>Criterio</th>
          <th>Doctoralia</th>
          <th>Kalyo</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Prop&oacute;sito principal</td><td>Directorio + citas p&uacute;blicas</td><td>Operaci&oacute;n cl&iacute;nica integral</td></tr>
        <tr><td>Modelo de precio</td><td>Planes + comisiones / leads</td><td>Suscripci&oacute;n fija; trial Max 7 d&iacute;as</td></tr>
        <tr><td>Comisi&oacute;n por consulta</td><td>S&iacute; (seg&uacute;n plan/mercado)</td><td>No</td></tr>
        <tr><td>Expediente cl&iacute;nico</td><td>B&aacute;sico / limitado</td><td>Completo (notas, evoluci&oacute;n, archivos)</td></tr>
        <tr><td>Tests psicom&eacute;tricos</td><td>No es el foco</td><td>91+ con puntuaci&oacute;n autom&aacute;tica</td></tr>
        <tr><td>Agenda + WhatsApp</td><td>Recordatorios variables</td><td>Confirmaci&oacute;n WhatsApp nativa</td></tr>
        <tr><td>Teleconsulta</td><td>Disponible en ecosistema</td><td>Kalyo Meet + transcripci&oacute;n IA</td></tr>
        <tr><td>Asistente por voz</td><td>No</td><td>Kaly (incluido en Max)</td></tr>
        <tr><td>Enfoque LATAM cl&iacute;nico</td><td>Marketplace regional</td><td>Dise&ntilde;ado para MX/CO (NOM-004, Ley 1090)</td></tr>
        <tr><td>Ideal para</td><td>Captar pacientes nuevos</td><td>Gestionar y escalar la consulta</td></tr>
      </tbody>
    </table>

    <h2>D&oacute;nde Doctoralia sigue siendo &uacute;til</h2>
    <p>Si est&aacute;s abriendo consultorio o necesitas flujo constante de primeras citas, un directorio puede acelerar la visibilidad. El perfil p&uacute;blico, rese&ntilde;as y b&uacute;squeda por zona siguen siendo ventajas reales de Doctoralia. El costo de esa visibilidad suele incluir <strong>comisiones o planes premium</strong>, y el software no reemplaza un expediente cl&iacute;nico serio ni una bater&iacute;a de tests.</p>
    <p>El riesgo habitual: el psic&oacute;logo queda atrapado en un embudo de captaci&oacute;n caro, mientras la operaci&oacute;n interna sigue en Excel, WhatsApp personal y PDFs sueltos.</p>

    <h2>Diferenciadores de Kalyo frente a un directorio</h2>
    <h3>1. Sin comisi&oacute;n por sesi&oacute;n</h3>
    <p>Kalyo no cobra un porcentaje de tus consultas. Pagas una suscripci&oacute;n predecible y usas la plataforma sin penalizar el crecimiento de tu agenda. Eso importa cuando pasas de 8 a 25 pacientes semanales.</p>
    <h3>2. Kaly, el asistente por voz</h3>
    <p>Con Kaly puedes agendar, consultar y ejecutar acciones cl&iacute;nicas por voz durante o entre sesiones. Es la diferencia entre un marketplace y un copiloto operativo. Incluido en el plan Max.</p>
    <h3>3. Tests ilimitados y reportes con IA</h3>
    <p>Aplicas instrumentos como <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a>, <a href="/articulos/que-es-el-gad-7.html">GAD-7</a>, <a href="/articulos/inventario-burnout-mbi.html">MBI</a> o <a href="/articulos/c-ssrs-escala-columbia-suicidio.html">C-SSRS</a> con puntuaci&oacute;n autom&aacute;tica y reportes editables. Un directorio no resuelve clinimetr&iacute;a.</p>
    <h3>4. Agenda con confirmaci&oacute;n WhatsApp</h3>
    <p>Los recordatorios y confirmaciones reducen inasistencias. Si ese es tu dolor principal, ve tambi&eacute;n <a href="/articulos/reducir-inasistencias-consulta-psicologica.html">c&oacute;mo reducir inasistencias</a>.</p>
    <h3>5. Cumplimiento y expediente en LATAM</h3>
    <p>Kalyo est&aacute; pensado para documentar conforme a contextos como la <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> en M&eacute;xico y la <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a> en Colombia, con expediente digital unificado.</p>

{cta(slug, 'Prueba Kalyo Max 7 d&iacute;as gratis', 'Agenda WhatsApp, 91+ tests, Kaly por voz y expediente cl&iacute;nico. Sin comisi&oacute;n por consulta.', 'Empezar trial Max gratis &rarr;')}

    <h2>Testimonios reales de psic&oacute;logos en Kalyo</h2>
    <p><strong>Rosa Isela Salazar</strong> &mdash; Fundadora, Psic&oacute;loga e Hipnoterapeuta Cl&iacute;nica (Monterrey, M&eacute;xico): &ldquo;Kalyo me ayuda a eficientizar la aplicaci&oacute;n y evaluaci&oacute;n psicom&eacute;trica de mis pacientes.&rdquo;</p>
    <p><strong>M&oacute;nica P&aacute;ez</strong> &mdash; Psic&oacute;loga Cognitivo-Conductual (Mexicali, M&eacute;xico): &ldquo;Los instrumentos de evaluaci&oacute;n han reducido significativamente el tiempo dedicado a las valoraciones. Adem&aacute;s, la transcripci&oacute;n autom&aacute;tica de las sesiones me permite estar plenamente presente con el paciente.&rdquo;</p>
    <p><strong>Ps. Carlos Mendoza</strong> (Bogot&aacute;): &ldquo;Kaly me agenda citas por voz y la confirmaci&oacute;n por WhatsApp baj&oacute; mis inasistencias. Los tests digitales son un plus.&rdquo;</p>

    <h2>&iquest;Puedo usar Doctoralia y Kalyo juntos?</h2>
    <p>S&iacute;. Un patr&oacute;n frecuente: captas con directorio (o referidos/Instagram) y operas la consulta en Kalyo. Cuando tu agenda se llena por referidos, el costo de adquisici&oacute;n del marketplace deja de justificar comisiones altas. En esa etapa, Kalyo suele convertirse en el sistema principal.</p>

    <h2>Preguntas frecuentes</h2>
    <h3>&iquest;Kalyo reemplaza por completo a Doctoralia?</h3>
    <p>Reemplaza la operaci&oacute;n cl&iacute;nica (agenda, notas, tests, teleconsulta). No es un directorio masivo de pacientes. Si necesitas SEO local de marketplace, puedes mantener un perfil externo mientras migras la operaci&oacute;n a Kalyo.</p>
    <h3>&iquest;Hay comisiones ocultas en Kalyo?</h3>
    <p>No. El modelo es suscripci&oacute;n. El trial Max de 7 d&iacute;as te deja probar el flujo completo antes de decidir.</p>
    <h3>&iquest;Sirve para M&eacute;xico y Colombia?</h3>
    <p>S&iacute;. Kalyo est&aacute; dise&ntilde;ado para psic&oacute;logos en Latinoam&eacute;rica, con &eacute;nfasis normativo en MX y CO. M&aacute;s contexto en <a href="/sobre-kalyo.html">Sobre Kalyo</a>.</p>

    <h2>Conclusi&oacute;n</h2>
    <p>Si buscas <em>aparecer</em>, un directorio puede ayudar. Si buscas <em>operar</em> una consulta moderna &mdash;sin comisi&oacute;n, con tests, voz y WhatsApp&mdash; Kalyo es la comparativa ganadora para psic&oacute;logos en 2026. Empieza con el trial Max y mide cu&aacute;nto tiempo administrativo recuperas en una semana.</p>

{cta(slug, 'Deja de pagar comisiones por crecer', 'Prueba Max 7 d&iacute;as: Kaly voz, WhatsApp, teleconsulta y 91 tests en un solo lugar.')}
"""
    articles.append(
        dict(
            slug=slug,
            title="Doctoralia vs Kalyo: Comparativa Psicólogos 2026 | Kalyo",
            desc="Compara Doctoralia y Kalyo para psicólogos: comisiones, expediente clínico, tests y agenda WhatsApp. Elige la mejor opción para tu consulta privada en LATAM.",
            h1="Doctoralia vs Kalyo: Comparativa para Psic&oacute;logos 2026",
            headline="Doctoralia vs Kalyo: Comparativa para Psicólogos 2026",
            crumb="Doctoralia vs Kalyo",
            keywords="Doctoralia vs Kalyo, alternativas Doctoralia, software psicólogos, comparativa, LATAM, agenda WhatsApp",
            meta_label="Comparativa comercial &middot; Actualizaci&oacute;n 2026",
            intro="&iquest;Doctoralia o un consultorio digital cl&iacute;nico? Esta comparativa 2026 explica diferencias de precio, comisiones, expediente, tests y agenda WhatsApp para psic&oacute;logos en Latinoam&eacute;rica &mdash;y cu&aacute;ndo conviene cada uno.",
            body=body,
            related=[
                ("/articulos/software-para-psicologos-clinicos.html", "Software para psicólogos clínicos"),
                ("/articulos/mejor-software-psicologos-2026.html", "Mejor software para psicólogos 2026"),
                ("/articulos/alternativas-elo-psicologos-mexico.html", "Alternativas a ELO en México"),
                ("/", "Landing Kalyo"),
            ],
            img_alt="Comparativa Doctoralia vs Kalyo para psicólogos",
            hero_from="alternativas-a-doctoralia-para-psicologos",
        )
    )

    slug = "mejor-software-psicologos-2026"
    body = f"""
    <h2>C&oacute;mo elegimos el ranking 2026</h2>
    <p>Evaluamos plataformas usadas por psic&oacute;logos en Latinoam&eacute;rica con cinco criterios: (1) precio predecible, (2) profundidad cl&iacute;nica (tests + expediente + notas), (3) agenda y reducci&oacute;n de inasistencias, (4) teleconsulta e IA, (5) soporte y contexto LATAM (MX/CO). No es un ranking de apps gen&eacute;ricas de citas: solo herramientas relevantes para consulta psicol&oacute;gica.</p>

    <h2>Ranking: mejor software para psic&oacute;logos en 2026</h2>
    <ol>
      <li><strong>Kalyo</strong> &mdash; consultorio digital integral (ganador)</li>
      <li><strong>Doctoralia / marketplaces</strong> &mdash; captaci&oacute;n, no operaci&oacute;n cl&iacute;nica completa</li>
      <li><strong>ELO</strong> &mdash; fuerte en tests MX, d&eacute;bil en gesti&oacute;n integral</li>
      <li><strong>Heiko / SaaS CO</strong> &mdash; agenda y consultorio en Colombia</li>
      <li><strong>Psicologistico / Terapsy Core</strong> &mdash; gesti&oacute;n cl&iacute;nica regional</li>
      <li><strong>Moodo / Aimentia</strong> &mdash; foco Europa/IA; menos encaje normativo LATAM</li>
    </ol>

    <h2>#1 Kalyo &mdash; por qu&eacute; encabeza la lista</h2>
    <p>Kalyo concentra agenda con WhatsApp, teleconsulta (Kalyo Meet), 91+ tests con puntuaci&oacute;n autom&aacute;tica, notas SOAP con IA, expediente digital y Kaly por voz. El trial Max de 7 d&iacute;as permite validar el flujo real de consulta sin compromiso. Precio por suscripci&oacute;n, sin comisi&oacute;n por sesi&oacute;n.</p>
    <ul>
      <li>Ideal si quieres <em>una</em> plataforma en lugar de cuatro herramientas sueltas</li>
      <li>Dise&ntilde;ado para psic&oacute;logos en MX y CO</li>
      <li>Escalable de consultorio individual a pr&aacute;ctica con mayor volumen</li>
    </ul>

    <h2>Comparativa r&aacute;pida por criterio</h2>
    <table class="severity-table">
      <thead><tr><th>Criterio</th><th>Kalyo</th><th>Doctoralia</th><th>ELO</th><th>Heiko/CO SaaS</th></tr></thead>
      <tbody>
        <tr><td>Agenda + WhatsApp</td><td>Excelente</td><td>Variable</td><td>Limitado</td><td>Bueno</td></tr>
        <tr><td>Tests cl&iacute;nicos</td><td>91+</td><td>No foco</td><td>~40</td><td>B&aacute;sico/variable</td></tr>
        <tr><td>Expediente + notas IA</td><td>S&iacute;</td><td>Limitado</td><td>Parcial</td><td>Parcial</td></tr>
        <tr><td>Teleconsulta + transcripci&oacute;n</td><td>S&iacute;</td><td>Parcial</td><td>No foco</td><td>Variable</td></tr>
        <tr><td>Sin comisi&oacute;n por cita</td><td>S&iacute;</td><td>No</td><td>N/A</td><td>S&iacute;</td></tr>
        <tr><td>Soporte LATAM cl&iacute;nico</td><td>Alto</td><td>Marketplace</td><td>MX tests</td><td>CO</td></tr>
      </tbody>
    </table>

{cta(slug, 'Prueba el #1 en software para psic&oacute;logos', 'Activa Max 7 d&iacute;as gratis: tests, WhatsApp, teleconsulta y Kaly voz.')}

    <h2>Kalyo vs cada competidor (resumen)</h2>
    <h3>vs Doctoralia</h3>
    <p>Doctoralia gana en discovery p&uacute;blico; Kalyo gana en operaci&oacute;n diaria y clinimetr&iacute;a. Detalle completo en <a href="/articulos/doctoralia-vs-kalyo.html">Doctoralia vs Kalyo</a>.</p>
    <h3>vs ELO</h3>
    <p>ELO es conocido en M&eacute;xico por bater&iacute;as de tests, pero el modelo por uso y la falta de gesti&oacute;n integral frenan. Kalyo ofrece m&aacute;s tests, reportes IA y expediente. Ver <a href="/articulos/alternativas-elo-psicologos-mexico.html">alternativas a ELO</a>.</p>
    <h3>vs Heiko y SaaS colombianos</h3>
    <p>Heiko y alternativas CO cubren agenda e historia. Kalyo suma bater&iacute;a amplia de tests, voz e IA de documentaci&oacute;n, &uacute;til si atiendes MX+CO o quieres clinimetr&iacute;a seria.</p>
    <h3>vs Moodo / Aimentia</h3>
    <p>Buenas en IA europea. Si tu prioridad es normativa LATAM, WhatsApp de confirmaci&oacute;n y precios pensados para la regi&oacute;n, Kalyo encaja mejor.</p>

    <h2>Criterios pr&aacute;cticos antes de pagar</h2>
    <ol>
      <li><strong>Precio anual real:</strong> suma comisiones, m&oacute;dulos extra y l&iacute;mites de tests.</li>
      <li><strong>Flujo de sesi&oacute;n:</strong> &iquest;puedes documentar sin salir de la herramienta?</li>
      <li><strong>Inasistencias:</strong> &iquest;hay WhatsApp/confirmaci&oacute;n nativa?</li>
      <li><strong>Exportaci&oacute;n:</strong> &iquest;puedes sacar PDF/CSV si migras?</li>
      <li><strong>Trial real:</strong> prueba con 2&ndash;3 pacientes piloto, no solo el tour.</li>
    </ol>
    <p>Para abrir consulta, combina esta gu&iacute;a con <a href="/articulos/como-abrir-consulta-privada-mexico.html">abrir consulta en M&eacute;xico</a> o la versi&oacute;n Colombia.</p>

    <h2>Testimonios</h2>
    <p>Psic&oacute;logos en Monterrey, Mexicali y Bogot&aacute; destacan menos tiempo en valoraciones, confirmaci&oacute;n WhatsApp y presencia plena gracias a la transcripci&oacute;n. Eso es lo que un &ldquo;mejor software&rdquo; debe demostrar en la semana 1 &mdash;no solo en la landing.</p>

    <h2>Conclusi&oacute;n</h2>
    <p>En 2026, el mejor software para psic&oacute;logos no es el que tiene m&aacute;s logos: es el que reduce papeleo, protege el expediente y escala sin comisiones. Kalyo lidera ese perfil en LATAM. Val&iacute;dalo con el trial Max de 7 d&iacute;as y compara con tu stack actual.</p>

{cta(slug, 'Elige con evidencia, no con marketing', 'Prueba Max gratis 7 d&iacute;as y mide tiempo recuperado en tu consulta.')}
"""
    articles.append(
        dict(
            slug=slug,
            title="Mejor Software para Psicólogos 2026: Guía LATAM | Kalyo",
            desc="Descubre el mejor software para psicólogos en 2026: ranking, criterios LATAM y comparativa de agenda, tests, teleconsulta y precio. Guía práctica actualizada.",
            h1="Mejor Software para Psic&oacute;logos en 2026 (Gu&iacute;a Completa)",
            headline="Mejor Software para Psicólogos en 2026 (Guía Completa)",
            crumb="Mejor software para psicólogos 2026",
            keywords="mejor software para psicólogos, ranking 2026, Kalyo, Doctoralia, ELO, Heiko, agenda clínica",
            meta_label="Gu&iacute;a comercial &middot; Ranking 2026",
            intro="Gu&iacute;a actualizada 2026 del mejor software para psic&oacute;logos en Latinoam&eacute;rica: ranking, criterios de precio/features/soporte y comparativas claras para elegir sin perder meses en pruebas fallidas.",
            body=body,
            related=[
                ("/articulos/software-para-psicologos-clinicos.html", "Cómo elegir software clínico"),
                ("/articulos/doctoralia-vs-kalyo.html", "Doctoralia vs Kalyo"),
                ("/articulos/teleconsulta-psicologos.html", "Teleconsulta para psicólogos"),
                ("/#precios", "Ver precios Kalyo"),
            ],
            img_alt="Ranking del mejor software para psicólogos en 2026",
            hero_from="mejor-software-para-psicologos-clinicos",
        )
    )

    slug = "teleconsulta-psicologos"
    body = f"""
    <h2>Por qu&eacute; la teleconsulta ya no es &ldquo;plan B&rdquo;</h2>
    <p>La atenci&oacute;n remota ampli&oacute; el radio geogr&aacute;fico del consultorio, redujo cancelaciones por traslado y permiti&oacute; continuidad terap&eacute;utica en viajes o enfermedad leve. En 2026, la pregunta no es si ofrecer teleconsulta, sino <strong>c&oacute;mo hacerlo con calidad cl&iacute;nica, privacidad y documentaci&oacute;n seria</strong>.</p>

    <h2>Beneficios frente a la modalidad 100% presencial</h2>
    <ul>
      <li><strong>Acceso:</strong> pacientes en otras ciudades o con movilidad limitada</li>
      <li><strong>Puntualidad:</strong> menos fricci&oacute;n de transporte</li>
      <li><strong>Continuidad:</strong> menos interrupciones del proceso terap&eacute;utico</li>
      <li><strong>Eficiencia:</strong> bloques h&iacute;bridos (presencial + virtual) en la misma agenda</li>
    </ul>
    <p>No sustituye toda la cl&iacute;nica presencial (evaluaciones que requieren observaci&oacute;n in situ, ciertas crisis, preferencia del paciente). El modelo h&iacute;brido suele ser el &oacute;ptimo.</p>

    <h2>Requisitos legales y &eacute;ticos (LATAM)</h2>
    <p>Sin sustituir asesor&iacute;a jur&iacute;dica, un piso m&iacute;nimo incluye:</p>
    <ol>
      <li><strong>Consentimiento informado</strong> espec&iacute;fico para modalidad remota (riesgos, l&iacute;mites, emergencias). Ver gu&iacute;a de <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a>.</li>
      <li><strong>Privacidad de datos</strong> y canal seguro (no grupos familiares de WhatsApp como expediente). En Colombia, alinea con <a href="/articulos/ley-1581-proteccion-datos-psicologia.html">Ley 1581</a>; en M&eacute;xico, considera LFPDPPP y expediente bajo <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>.</li>
      <li><strong>&Eacute;tica profesional</strong> (p. ej. marco de <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a> en CO): competencia, confidencialidad, l&iacute;mites de la telepr&aacute;ctica.</li>
      <li><strong>Protocolo de crisis:</strong> ubicaci&oacute;n del paciente, contactos de emergencia, cu&aacute;ndo derivar a presencial/urgencias.</li>
    </ol>

    <h2>Herramientas: de Zoom improvisado a Kalyo Meet</h2>
    <p>Usar videollamada gen&eacute;rica funciona al inicio, pero fragmenta la historia cl&iacute;nica: la cita vive en un calendario, la nota en Word, el test en otro link y el recordatorio en WhatsApp personal. Kalyo Meet integra la sesi&oacute;n dentro del consultorio digital.</p>
    <table class="items-table">
      <thead><tr><th>Necesidad</th><th>Zoom/Meet gen&eacute;rico</th><th>Kalyo Meet</th></tr></thead>
      <tbody>
        <tr><td>Videollamada</td><td>S&iacute;</td><td>S&iacute;</td></tr>
        <tr><td>Vinculada al expediente</td><td>No</td><td>S&iacute;</td></tr>
        <tr><td>Recordatorio WhatsApp</td><td>Manual</td><td>Automatizado en agenda</td></tr>
        <tr><td>Grabaci&oacute;n + transcripci&oacute;n IA</td><td>Add-ons / externo</td><td>Flujo cl&iacute;nico integrado</td></tr>
        <tr><td>Tests pre/post sesi&oacute;n</td><td>Otro sistema</td><td>91+ en la misma plataforma</td></tr>
      </tbody>
    </table>

{cta(slug, 'Prueba teleconsulta con Kalyo Meet', 'Trial Max 7 d&iacute;as: Meet, transcripci&oacute;n IA, agenda WhatsApp y expediente.', 'Activar trial Max &rarr;')}

    <h2>Grabaci&oacute;n y transcripci&oacute;n con IA</h2>
    <p>La transcripci&oacute;n permite estar presente con el paciente y documentar despu&eacute;s con apoyo de IA (notas SOAP). Requisitos &eacute;ticos: consentimiento expl&iacute;cito para grabar, almacenamiento seguro y pol&iacute;tica clara de retenci&oacute;n. M&oacute;nica P&aacute;ez (Mexicali) destaca que la transcripci&oacute;n autom&aacute;tica le permite &ldquo;estar plenamente presente con el paciente, sin distraerse tomando notas&rdquo;.</p>

    <h2>Checklist para lanzar teleconsulta esta semana</h2>
    <ol>
      <li>Actualiza consentimiento y aviso de privacidad</li>
      <li>Define horario h&iacute;brido en tu agenda</li>
      <li>Configura recordatorios WhatsApp (reduce no-shows remotes tambi&eacute;n)</li>
      <li>Prueba audio/video y backup de red</li>
      <li>Estandariza nota post-sesi&oacute;n (SOAP) &mdash; ver <a href="/articulos/como-documentar-sesion-clinica.html">c&oacute;mo documentar una sesi&oacute;n</a></li>
      <li>Env&iacute;a tests digitales antes de la cita cuando aplique</li>
    </ol>

    <h2>Errores comunes</h2>
    <ul>
      <li>Usar la cuenta personal de Zoom sin control de acceso</li>
      <li>No verificar identidad/ubicaci&oacute;n en primeras sesiones</li>
      <li>No documentar en expediente el mismo d&iacute;a</li>
      <li>Depender solo del chat de WhatsApp como historia cl&iacute;nica</li>
    </ul>

    <h2>Conclusi&oacute;n</h2>
    <p>La teleconsulta profesional combina legalidad, experiencia de paciente y stack integrado. Kalyo Meet + transcripci&oacute;n IA + agenda WhatsApp es el camino m&aacute;s corto para dejar de improvisar. Prueba Max 7 d&iacute;as y eval&uacute;a una semana de sesiones remotas reales.</p>

{cta(slug, 'Deja de improvisar la teleconsulta', 'Kalyo Meet, IA y expediente en un solo lugar. Trial Max 7 d&iacute;as gratis.')}
"""
    articles.append(
        dict(
            slug=slug,
            title="Teleconsulta para Psicólogos Guía Completa 2026 | Kalyo",
            desc="Aprende a ofrecer teleconsulta psicológica en 2026: beneficios, requisitos legales, herramientas y Kalyo Meet con grabación y transcripción IA para tu consulta.",
            h1="Teleconsulta para Psic&oacute;logos: Gu&iacute;a y Herramientas 2026",
            headline="Teleconsulta para Psicólogos: Guía y Herramientas 2026",
            crumb="Teleconsulta para psicólogos",
            keywords="teleconsulta psicólogos, Kalyo Meet, telepsicología, transcripción IA, requisitos legales",
            meta_label="Teleconsulta &middot; Gu&iacute;a 2026",
            intro="Gu&iacute;a pr&aacute;ctica 2026 para ofrecer teleconsulta psicol&oacute;gica con calidad: beneficios vs presencial, requisitos legales en LATAM, herramientas y c&oacute;mo Kalyo Meet + IA simplifican el flujo cl&iacute;nico.",
            body=body,
            related=[
                ("/articulos/consentimiento-informado-psicologia.html", "Consentimiento informado"),
                ("/articulos/reducir-inasistencias-consulta-psicologica.html", "Reducir inasistencias"),
                ("/articulos/mejor-software-psicologos-2026.html", "Mejor software 2026"),
                ("/demo/", "Agendar demo Kalyo"),
            ],
            img_alt="Teleconsulta psicológica con Kalyo Meet",
            hero_from="teleconsulta-para-psicologos-latinoamerica",
        )
    )

    slug = "reducir-inasistencias-consulta-psicologica"
    body = f"""
    <h2>El costo real de las inasistencias</h2>
    <p>Una falta sin aviso no es solo &ldquo;una hora libre&rdquo;: es ingreso perdido, hueco dif&iacute;cil de rellenar y desgaste emocional. En salud ambulatoria, tasas de no-show del <strong>10&ndash;30%</strong> son frecuentes seg&uacute;n contexto; en salud mental privada el impacto se siente m&aacute;s porque cada bloque es tu n&oacute;mina. Si atiendes 20 sesiones/semana y pierdes 3, est&aacute;s regalando ~15% de capacidad.</p>

    <h2>Por qu&eacute; faltan los pacientes (y qu&eacute; s&iacute; puedes controlar)</h2>
    <ul>
      <li>Olvido simple (la intervenci&oacute;n #1 es el recordatorio)</li>
      <li>Fricci&oacute;n de agenda (reprogramar es dif&iacute;cil)</li>
      <li>Ambivalencia terap&eacute;utica (aqu&iacute; el v&iacute;nculo importa m&aacute;s que el software)</li>
      <li>Barreras econ&oacute;micas o de transporte (teleconsulta ayuda; ver <a href="/articulos/teleconsulta-psicologos.html">gu&iacute;a de teleconsulta</a>)</li>
    </ul>

    <h2>Estrategias que funcionan</h2>
    <h3>1. Recordatorios multi-canal (WhatsApp primero)</h3>
    <p>WhatsApp supera al email en apertura en LATAM. Ideal: confirmaci&oacute;n 24&ndash;48 h antes + recordatorio el mismo d&iacute;a. Pide respuesta (&ldquo;confirma con 1&rdquo;) para liberar el espacio a tiempo.</p>
    <h3>2. Pol&iacute;tica de cancelaci&oacute;n clara</h3>
    <p>Incl&uacute;yela en el <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a>. Ejemplo: cancelaci&oacute;n con 24 h; de lo contrario se cobra parcial/total. La claridad reduce conflicto.</p>
    <h3>3. Dep&oacute;sito o prepago en primeras citas</h3>
    <p>Especialmente &uacute;til con pacientes nuevos o alta tasa hist&oacute;rica de no-show. No es desconfianza: es profesionalizar la agenda.</p>
    <h3>4. Lista de espera / fill-ins</h3>
    <p>Cuando alguien cancela, ofrece el hueco a 2&ndash;3 pacientes en lista. La agenda digital acelera ese ping.</p>
    <h3>5. Teleconsulta como plan B</h3>
    <p>Si el paciente no puede llegar, ofrece virtual en el mismo slot antes de perderlo.</p>

{cta(slug, 'Automatiza recordatorios WhatsApp con Kalyo', 'Trial Max 7 d&iacute;as: confirmaciones, agenda y menos huecos vac&iacute;os.', 'Probar Max gratis &rarr;')}

    <h2>C&oacute;mo Kalyo reduce inasistencias sin perseguir chats</h2>
    <p>En lugar de escribir manualmente a cada paciente desde tu WhatsApp personal, Kalyo integra <strong>confirmaci&oacute;n por WhatsApp en la agenda cl&iacute;nica</strong>. El psic&oacute;logo define la pol&iacute;tica; el sistema ejecuta. Carlos Mendoza (Bogot&aacute;) resume: &ldquo;Kaly me agenda citas por voz y la confirmaci&oacute;n por WhatsApp baj&oacute; mis inasistencias.&rdquo;</p>
    <ul>
      <li>Recordatorios ligados al expediente (no a tu chat personal)</li>
      <li>Menos olvidos operativos entre sesiones</li>
      <li>Combinable con teleconsulta y tests previos</li>
    </ul>

    <h2>Playbook de 14 d&iacute;as</h2>
    <ol>
      <li><strong>D&iacute;as 1&ndash;2:</strong> mide tu tasa actual de no-show (faltas / citas agendadas).</li>
      <li><strong>D&iacute;as 3&ndash;4:</strong> escribe pol&iacute;tica de cancelaci&oacute;n y actualiza consentimiento.</li>
      <li><strong>D&iacute;as 5&ndash;7:</strong> activa recordatorios WhatsApp (24 h + d&iacute;a de la cita).</li>
      <li><strong>D&iacute;as 8&ndash;10:</strong> prueba dep&oacute;sito en primeras evaluaciones.</li>
      <li><strong>D&iacute;as 11&ndash;14:</strong> ofrece teleconsulta como alternativa ante cancelaciones tard&iacute;as.</li>
    </ol>
    <p>Meta realista: bajar 30&ndash;50% los no-shows evitables (olvidos), no eliminar la ambivalencia cl&iacute;nica.</p>

    <h2>M&eacute;tricas a revisar cada mes</h2>
    <table class="items-table">
      <thead><tr><th>M&eacute;trica</th><th>C&oacute;mo leerla</th></tr></thead>
      <tbody>
        <tr><td>Tasa de no-show</td><td>Faltas / citas confirmadas</td></tr>
        <tr><td>% confirmaciones WhatsApp</td><td>Respuestas / recordatorios enviados</td></tr>
        <tr><td>Tiempo a rellenar hueco</td><td>Minutos desde cancelaci&oacute;n hasta nuevo booking</td></tr>
        <tr><td>Ingreso recuperado</td><td>Sesiones salvadas &times; tarifa</td></tr>
      </tbody>
    </table>

    <h2>Conclusi&oacute;n</h2>
    <p>Reducir inasistencias es 70% operaciones y 30% cl&iacute;nica. WhatsApp + pol&iacute;tica clara + teleconsulta de respaldo cambian el mes. Kalyo automatiza la parte operativa para que no vivas en el chat. Activa el trial Max y compara tu tasa de no-show en dos semanas.</p>

{cta(slug, 'Recupera horas de agenda este mes', 'Confirmaciones WhatsApp + agenda cl&iacute;nica. Trial Max 7 d&iacute;as gratis.')}
"""
    articles.append(
        dict(
            slug=slug,
            title="Reducir Inasistencias en Consulta Psicológica 2026 | Kalyo",
            desc="Aprende a reducir inasistencias en consulta psicológica: cifras del problema, recordatorios WhatsApp, depósitos y automatización con Kalyo. Guía práctica 2026.",
            h1="C&oacute;mo Reducir Inasistencias en Consulta Psicol&oacute;gica",
            headline="Cómo Reducir Inasistencias en Consulta Psicológica",
            crumb="Reducir inasistencias en consulta",
            keywords="reducir inasistencias, no-show psicología, recordatorios WhatsApp, agenda psicólogos, Kalyo",
            meta_label="Operaci&oacute;n de consulta &middot; Gu&iacute;a 2026",
            intro="Las inasistencias drenan ingresos y energ&iacute;a. Esta gu&iacute;a re&uacute;ne cifras del problema, estrategias probadas (WhatsApp, dep&oacute;sito, teleconsulta) y c&oacute;mo automatizar recordatorios con Kalyo.",
            body=body,
            related=[
                ("/articulos/teleconsulta-psicologos.html", "Teleconsulta para psicólogos"),
                ("/articulos/doctoralia-vs-kalyo.html", "Doctoralia vs Kalyo"),
                ("/articulos/consentimiento-informado-psicologia.html", "Consentimiento informado"),
                ("/", "Conocer Kalyo"),
            ],
            img_alt="Cómo reducir inasistencias en consulta psicológica con WhatsApp",
            hero_from="como-reducir-inasistencias-consulta-psicologica",
        )
    )

    for a in articles:
        html_out = build_article(a)
        path = ART / f"{a['slug']}.html"
        path.write_text(html_out, encoding="utf-8")
        text = re.sub(r"<[^>]+>", " ", html_out)
        words = len(re.findall(r"\w+", text, flags=re.UNICODE))
        src = a["hero_from"]
        for ext in (".jpg", ".webp"):
            s = BLOG / f"{src}-hero{ext}"
            d = BLOG / f"{a['slug']}-hero{ext}"
            if not s.exists():
                raise SystemExit(f"Missing hero: {s}")
            shutil.copy2(s, d)
        print(f"OK {a['slug']}: title={len(a['title'])} desc={len(a['desc'])} ~words={words}")


if __name__ == "__main__":
    main()
