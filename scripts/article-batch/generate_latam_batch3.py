#!/usr/bin/env python3
"""Generate 3 LATAM/Spain clinical articles from ley-1616 template."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "articulos/ley-1616-2013-salud-mental-colombia.html"
STYLE = re.search(r"(<style>.*?</style>)", TEMPLATE.read_text(encoding="utf-8"), re.S).group(1)


def build_article(cfg: dict) -> str:
    slug = cfg["slug"]
    title = cfg["title"]
    meta_desc = cfg["meta_desc"]
    keywords = cfg["keywords"]
    canonical = f"https://kalyo.io/articulos/{slug}.html"
    og_desc = meta_desc.replace("&", "&amp;")

    faq_json = ",\n    ".join(
        '{\n      "@type": "Question",\n      "name": '
        + json.dumps(q, ensure_ascii=False)
        + ',\n      "acceptedAnswer": {\n        "@type": "Answer",\n        "text": '
        + json.dumps(a, ensure_ascii=False)
        + "\n      }\n    }"
        for q, a in cfg["faqs"]
    )

    sections_html = ""
    for h2, paras in cfg["sections"]:
        sections_html += f"    <h2>{h2}</h2>\n"
        for p in paras:
            sections_html += f"    <p>{p}</p>\n\n"

    faq_body = ""
    for q, a in cfg["faqs"]:
        q_html = (
            q.replace("¿", "&iquest;")
            .replace("á", "&aacute;")
            .replace("é", "&eacute;")
            .replace("í", "&iacute;")
            .replace("ó", "&oacute;")
            .replace("ú", "&uacute;")
            .replace("ñ", "&ntilde;")
        )
        faq_body += f"    <h3>{q_html}</h3>\n    <p>{a}</p>\n\n"

    related_items = "".join(
        f'      <li><a href="{href}" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">{label}</a></li>\n'
        for href, label in cfg.get("related", [])
    )
    related_html = f"""  <section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
    <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Art&iacute;culos relacionados</h2>
    <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
{related_items}    </ul>
  </section>
"""
    refs_items = "".join(
        f'    <li><a href="{u}" rel="nofollow noopener noreferrer" target="_blank">{t}</a></li>\n'
        for u, t in cfg.get("refs", [])
    )
    refs_html = f"""  <section class="article-references">
  <h2>Referencias</h2>
  <ul>
{refs_items}  </ul>
</section>
"""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="es" href="{canonical}">

  <link rel="preload" as="image" href="/assets/blog/{slug}-hero.webp" type="image/webp">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title.replace('&', '&amp;')}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kalyo">
  <meta property="og:locale" content="es_419">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title.replace('&', '&amp;')}">
  <meta name="twitter:description" content="{og_desc}">
  <meta name="twitter:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">

  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title.replace('&', '&amp;')}",
  "description": "{meta_desc}",
  "image": "https://kalyo.io/assets/blog/{slug}-hero.jpg",
  "author": {{
    "@type": "Organization",
    "name": "Kalyo",
    "url": "https://kalyo.io"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Kalyo",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://kalyo.io/assets/logo.png"
    }}
  }},
  "datePublished": "2026-08-01",
  "dateModified": "2026-08-01",
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{canonical}"
  }}
}}
</script>
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {faq_json}
  ]
}}
</script>
<!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">

  {STYLE}
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-RTBRDTN5BK');
  gtag('config', 'AW-18371122366');
</script>
<script src="/scripts/attribution.js"></script>
</head>
<body>

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <a href="https://app.kalyo.io/login" class="header-btn">Iniciar sesi&oacute;n</a>
    </div>
  </header>

  <article class="article-wrapper">
    <div class="article-hero-img">
      <picture>
      <source srcset="/assets/blog/{slug}-hero.webp" type="image/webp">
      <img src="/assets/blog/{slug}-hero.jpg" alt="{cfg['hero_alt']}" width="1200" height="630" loading="eager" fetchpriority="high">
    </picture>
    </div>
    <p class="article-meta">{cfg.get('meta_label', 'Gu&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026')}</p>

    <h1>{cfg['h1']}</h1>

    <h2 id="respuesta-rapida">Respuesta r&aacute;pida</h2>
    <p>{cfg['quick']}</p>

    <p class="article-intro">{cfg['intro']}</p>

{sections_html}
{cfg['tables_html']}

    <figure class="article-inline-img">
      <picture>
      <source srcset="/assets/blog/{slug}-inline.webp" type="image/webp">
      <img src="/assets/blog/{slug}-inline.jpg" alt="{cfg['hero_alt']}" width="800" height="450" loading="lazy">
    </picture>
    </figure>

    <h2>Preguntas frecuentes</h2>
{faq_body}
    <div class="cta-box">
      <h2>&iquest;Llevas tu historia cl&iacute;nica en papel o en un Google Doc?</h2>
      <p>Kalyo te permite gestionar expedientes cl&iacute;nicos digitales.</p>
      <a href="https://app.kalyo.io/login?utm_source=blog&utm_medium=article&utm_campaign={slug}" class="cta-btn">Prueba gratis &rarr;</a>
    </div>
{related_html}
{refs_html}
  </article>

  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a></p>
  </footer>

</body>
</html>
"""


ARTICLES = [
    {
        "slug": "consentimiento-informado-psicologia-latam",
        "title": "Consentimiento Informado en Psicolog&iacute;a: Gu&iacute;a para Am&eacute;rica Latina | Kalyo",
        "meta_desc": "Qu&eacute; debe incluir el consentimiento informado en psicolog&iacute;a seg&uacute;n la normativa de M&eacute;xico, Colombia, Argentina y Per&uacute;. Formato y gu&iacute;a cl&iacute;nica.",
        "keywords": "consentimiento informado psicolog&iacute;a, consentimiento informado terapia, formato consentimiento informado, psicolog&iacute;a cl&iacute;nica",
        "h1": "Consentimiento Informado en Psicolog&iacute;a: Gu&iacute;a para Am&eacute;rica Latina",
        "hero_alt": "Consentimiento informado en psicolog\u00eda gu\u00eda Am\u00e9rica Latina",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "quick": "El <strong>consentimiento informado</strong> es el acuerdo libre y documentado del paciente tras comprender el proceso terap&eacute;utico, sus riesgos, beneficios y l&iacute;mites de confidencialidad. Es obligatorio en consulta privada e institucional en M&eacute;xico (NOM-004), Colombia (Ley 1090), Argentina (Ley 26657) y Per&uacute; (Ley 29889). Debe incluir identificaci&oacute;n, descripci&oacute;n del servicio, derecho a retirarse y firma fechada; puede ser digital con trazabilidad.",
        "intro": "El consentimiento informado no es un formulario accesorio: es el mecanismo &eacute;tico y legal que protege la autonom&iacute;a del paciente y delimita la responsabilidad del psic&oacute;logo. En Am&eacute;rica Latina, cada pa&iacute;s regula el tema desde la salud, la deontolog&iacute;a profesional y la protecci&oacute;n de datos. Esta gu&iacute;a unifica criterios cl&iacute;nicos pr&aacute;cticos y referencias normativas para M&eacute;xico, Colombia, Argentina y Per&uacute;, incluyendo menores, telepsicolog&iacute;a y excepciones a la confidencialidad.",
        "sections": [
            ("Qu&eacute; es el consentimiento informado y por qu&eacute; es obligatorio", [
                "El consentimiento informado en psicolog&iacute;a es el proceso mediante el cual una persona, con capacidad suficiente, acepta participar en evaluaci&oacute;n o tratamiento psicol&oacute;gico despu&eacute;s de recibir informaci&oacute;n clara, comprensible y suficiente sobre qu&eacute; implica la intervenci&oacute;n. No basta con firmar un documento gen&eacute;rico: la ley y los c&oacute;digos deontol&oacute;gicos exigen que el paciente comprenda prop&oacute;sito, m&eacute;todos, duraci&oacute;n estimada, alternativas razonables, riesgos previsibles y l&iacute;mites de confidencialidad.",
                "Su obligatoriedad deriva de tres ejes convergentes: (1) <strong>derechos del paciente</strong> a decidir sobre su salud; (2) <strong>deber profesional</strong> de no imponer intervenciones sin acuerdo; y (3) <strong>exigencia documental</strong> en historia cl&iacute;nica y auditor&iacute;as. En consulta privada, muchos psic&oacute;logos subestiman el riesgo legal de iniciar terapia sin consentimiento archivado, especialmente cuando aplican tests, graban sesiones o comparten informaci&oacute;n con terceros (escuela, empleador, aseguradora).",
                "Un consentimiento bien dise&ntilde;ado tambi&eacute;n es herramienta cl&iacute;nica: reduce ambig&uumde;edades sobre frecuencia, cancelaciones, honorarios, comunicaci&oacute;n entre sesiones y protocolos de crisis. Para modelos base, revisa <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado en psicolog&iacute;a</a> y la gu&iacute;a espec&iacute;fica de <a href=\"/articulos/consentimiento-informado-psicologia-mexico.html\">M&eacute;xico</a>.",
            ]),
            ("Elementos m&iacute;nimos del consentimiento informado", [
                "Aunque cada pa&iacute;s detalla requisitos en normativa propia, en la pr&aacute;ctica cl&iacute;nica latinoamericana conviene incluir los elementos de la tabla siguiente. Su presencia facilita cumplimiento transfronterizo y defensa &eacute;tica ante colegios profesionales.",
            ]),
            ("Diferencias normativas por pa&iacute;s", [
                "La tabla comparativa resume marcos legales centrales. Siempre verifica actualizaciones locales y regulaciones profesionales (colegios, ministerios de salud, protecci&oacute;n de datos).",
            ]),
            ("L&iacute;mites de la confidencialidad", [
                "La confidencialidad es pilar del secreto profesional, pero no es absoluta. El consentimiento debe explicar con claridad cu&aacute;ndo el psic&oacute;logo puede o debe divulgar informaci&oacute;n sin autorizaci&oacute;n previa del paciente.",
                "<strong>Riesgo de vida:</strong> ideaci&oacute;n suicida con plan viable, intento en curso o peligro grave para terceros suele activar deber de protecci&oacute;n, contacto con red de apoyo o derivaci&oacute;n urgente. Documenta evaluaci&oacute;n y acciones (ver <a href=\"/articulos/evaluacion-riesgo-suicida.html\">evaluaci&oacute;n del riesgo suicida</a>).",
                "<strong>Menores de edad:</strong> sospecha fundada de maltrato, abuso o negligencia puede imponer deber de denuncia seg&uacute;n legislaci&oacute;n de infancia de cada pa&iacute;s. Informa al representante legal sobre l&iacute;mites legales al inicio del proceso.",
                "<strong>Mandato judicial u orden de autoridad:</strong> citaciones, pericias ordenadas por tribunal o requerimientos legales v&aacute;lidos pueden obligar a aportar informaci&oacute;n en el marco procesal. El paciente debe conocer estas excepciones antes de iniciar tratamiento.",
            ]),
            ("Consentimiento informado con menores de edad", [
                "En menores intervienen padres, madres o tutores legales como titulares del consentimiento sustituto, pero la pr&aacute;ctica cl&iacute;nica contempor&aacute;nea promueve la <strong>autonom&iacute;a progresiva</strong>: explicar al ni&oacute; o adolescente, en lenguaje adecuado, qu&eacute; ocurrir&aacute; en terapia y solicitar su asentimiento cuando sea posible.",
                "En adolescentes, conviene distinguir qu&eacute; temas se mantendr&aacute;n confidenciales respecto de los adultos responsables (p. ej., sexualidad, sustancias) dentro de l&iacute;mites legales. Esta cl&aacute;usula debe estar escrita para evitar conflictos familiares y rupturas terap&eacute;uticas.",
                "En evaluaciones escolares o institucionales, aclara qui&eacute;n solicita el servicio, qu&eacute; informe se entregar&aacute; y qu&eacute; permanecer&aacute; en expediente cl&iacute;nico reservado.",
            ]),
            ("Consentimiento en telepsicolog&iacute;a", [
                "La telepsicolog&iacute;a exige consentimiento espec&iacute;fico o cl&aacute;usula ampliada que cubra: plataforma utilizada, medidas de seguridad (cifrado, contrase&ntilde;as), riesgos de interrupci&oacute;n t&eacute;cnica, ubicaci&oacute;n del paciente, protocolo ante descompensaci&oacute;n a distancia y almacenamiento digital de datos.",
                "Si la sesi&oacute;n se graba para supervisi&oacute;n cl&iacute;nica o IA asistida, se requiere consentimiento expl&iacute;cito adicional, indicando finalidad, acceso, plazo de conservaci&oacute;n y derecho de revocaci&oacute;n. Consulta <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta para psic&oacute;logos</a> para buenas pr&aacute;cticas operativas.",
                "En pacientes transfronterizos, indica jurisdicci&oacute;n aplicable y normativa de protecci&oacute;n de datos (p. ej., Ley 1581 en Colombia).",
            ]),
            ("Buenas pr&aacute;cticas de archivo y renovaci&oacute;n", [
                "Archiva el consentimiento firmado en la historia cl&iacute;nica o expediente digital con fecha de inicio. Renueva cuando cambie sustancialmente el tratamiento (nuevas t&eacute;cnicas, grupos, evaluaciones, derivaciones, grabaci&oacute;n) o tras pausas prolongadas.",
                "Usa lenguaje claro, evita jerga legal innecesaria y ofrece tiempo para preguntas. Registra en nota cl&iacute;nica breve que se explic&oacute; el documento y que el paciente manifest&oacute; comprensi&oacute;n.",
                "Integrar consentimientos en software cl&iacute;nico como Kalyo reduce p&eacute;rdida documental y facilita firma digital con trazabilidad.",
            ]),
        ],
        "tables_html": """
    <table class="items-table">
      <thead>
        <tr><th>Elemento</th><th>Contenido m&iacute;nimo</th></tr>
      </thead>
      <tbody>
        <tr><td>Datos del paciente</td><td>Nombre, identificaci&oacute;n, contacto, representante legal si aplica.</td></tr>
        <tr><td>Datos del psic&oacute;logo</td><td>Nombre, matr&iacute;cula/colegiatura, t&iacute;tulo, consultorio o instituci&oacute;n.</td></tr>
        <tr><td>Descripci&oacute;n del proceso</td><td>Evaluaci&oacute;n, psicoterapia, tests, duraci&oacute;n estimada, frecuencia.</td></tr>
        <tr><td>Riesgos y beneficios</td><td>Beneficios esperados y malestares posibles (p. ej., activaci&oacute;n emocional).</td></tr>
        <tr><td>Confidencialidad y l&iacute;mites</td><td>Secreto profesional y excepciones legales (riesgo, menores, orden judicial).</td></tr>
        <tr><td>Derecho a retirarse</td><td>Libertad de suspender o terminar sin perder dignidad ni atenci&oacute;n urgente debida.</td></tr>
        <tr><td>Firma y fecha</td><td>Firma del paciente/representante y del profesional; fecha de otorgamiento.</td></tr>
      </tbody>
    </table>

    <table class="severity-table">
      <thead>
        <tr><th>Pa&iacute;s</th><th>Marco normativo principal</th><th>Notas cl&iacute;nicas</th></tr>
      </thead>
      <tbody>
        <tr><td>M&eacute;xico</td><td>NOM-004-SSA3-2012 + Ley General de Salud</td><td>Consentimiento en expediente; ver <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>.</td></tr>
        <tr><td>Colombia</td><td>Ley 1090 + Res. 1995/1999</td><td>Historia cl&iacute;nica + &eacute;tica profesional; ver <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a>.</td></tr>
        <tr><td>Argentina</td><td>Ley 26657 + Ley 26529</td><td>Derechos del paciente y salud mental; consentimiento expreso.</td></tr>
        <tr><td>Per&uacute;</td><td>Ley 29889 + LGS art. 15</td><td>Informaci&oacute;n y autorizaci&oacute;n previa; ver <a href="/articulos/ley-salud-mental-peru-29889.html">Ley 29889</a>.</td></tr>
      </tbody>
    </table>
""",
        "faqs": [
            ("¿Es obligatorio el consentimiento informado en consulta privada?", "Sí. Aplica en consultorio privado e institucional. Es requisito ético y, en la mayoría de países latinoamericanos, exigencia legal vinculada a historia clínica y derechos del paciente."),
            ("¿Puede ser digital o debe ser en papel?", "Puede ser digital si garantiza autenticidad, integridad, firma identificable y archivo seguro (firmas electrónicas, plataformas clínicas). El papel sigue siendo válido; lo crítico es documentar acuerdo y comprensión."),
            ("¿Qué pasa si el paciente se niega a firmarlo?", "No debes iniciar evaluación o tratamiento que requiera consentimiento. Puedes ofrecer información, responder dudas y, si persiste la negativa, no prestar el servicio clínico electivo. En urgencias psicológicas, prioriza seguridad y protocolos legales."),
            ("¿Cada cuánto debo renovarlo?", "Al inicio del proceso y cuando cambien objetivos, métodos, confidencialidad, modalidad (presencial a tele), aplicación de tests o participantes (pareja, familia). Tras pausas prolongadas (>6–12 meses) conviene reconfirmar acuerdos."),
        ],
        "related": [
            ("/articulos/consentimiento-informado-psicologia.html", "Consentimiento informado en psicolog\u00eda"),
            ("/articulos/historia-clinica-colombia-resolucion-1995.html", "Historia cl\u00ednica Colombia Res. 1995"),
            ("/articulos/ley-salud-mental-argentina-26657.html", "Ley 26657 salud mental Argentina"),
        ],
        "refs": [
            ("https://www.who.int/ethics/publications/en/patient_safety/en/", "OMS \u2014 Seguridad del paciente y consentimiento"),
        ],
    },
    {
        "slug": "gad-7-espana-ansiedad-generalizada",
        "title": "GAD-7 en Espa&ntilde;a: Escala de Ansiedad Generalizada para Psic&oacute;logos | Kalyo",
        "meta_desc": "Gu&iacute;a cl&iacute;nica del GAD-7 para psic&oacute;logos en Espa&ntilde;a. Interpretaci&oacute;n, puntos de corte, validaci&oacute;n en poblaci&oacute;n espa&ntilde;ola y descarga del formulario.",
        "keywords": "gad-7 espa&ntilde;a, escala ansiedad generalizada espa&ntilde;a, gad-7 espa&ntilde;ol, ansiedad generalizada psicolog&iacute;a",
        "h1": "GAD-7 en Espa&ntilde;a: Escala de Ansiedad Generalizada",
        "hero_alt": "GAD-7 Espa\u00f1a escala ansiedad generalizada psic\u00f3logos",
        "meta_label": "Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "quick": "El <strong>GAD-7</strong> es un cuestionario breve de 7 &iacute;tems para tamizaje de ansiedad generalizada (puntuaci&oacute;n 0&ndash;21). En Espa&ntilde;a, Garc&iacute;a-Campayo et al. (2010) reportaron sensibilidad <strong>86%</strong> y especificidad <strong>93%</strong> en atenci&oacute;n primaria. Puntos de corte habituales: 0&ndash;4 m&iacute;nima, 5&ndash;9 leve, 10&ndash;14 moderada, 15&ndash;21 severa. Es tamizaje, no diagn&oacute;stico definitivo.",
        "intro": "El Generalized Anxiety Disorder scale (GAD-7) es uno de los instrumentos m&aacute;s utilizados en atenci&oacute;n primaria y salud mental por su brevedad, gratuidad y solidez psicom&eacute;trica. Para psic&oacute;logos en Espa&ntilde;a —Sistema Nacional de Salud (SNS) o consulta privada— dominar su administraci&oacute;n, interpretaci&oacute;n y l&iacute;mites cl&iacute;nicos es esencial. Esta gu&iacute;a integra evidencia internacional con la validaci&oacute;n espa&ntilde;ola y comparaciones pr&aacute;cticas con GAD-2 y HAM-A.",
        "sections": [
            ("Qu&eacute; es el GAD-7 y para qu&eacute; sirve", [
                "El GAD-7 eval&uacute;a s&iacute;ntomas nucleares del trastorno de ansiedad generalizada durante las &uacute;ltimas dos semanas: preocupaci&oacute;n excesiva, dificultad para controlarla, inquietud, fatiga, tensi&oacute;n, irritabilidad y alteraciones del sue&oacute;o. Se autorresponde en menos de tres minutos y se integra f&aacute;cilmente en consulta psicol&oacute;gica o m&eacute;dica.",
                "Cl&iacute;nicamente sirve para: (1) <strong>tamizaje</strong> inicial; (2) <strong>cuantificar severidad</strong>; (3) <strong>monitorear respuesta</strong> al tratamiento sesi&oacute;n a sesi&oacute;n. No reemplaza entrevista diagn&oacute;stica ni evaluaci&oacute;n de comorbilidades (depresi&oacute;n, p&aacute;nico, TOC). Complementa con <a href=\"/articulos/que-es-el-gad-7.html\">qu&eacute; es el GAD-7</a> y el PDF en <a href=\"/articulos/gad-7-espanol-pdf.html\">espa&ntilde;ol</a>.",
            ]),
            ("Los 7 &iacute;tems del GAD-7", [
                "Cada &iacute;tem se punt&uacute;a de 0 (nada) a 3 (casi todos los d&iacute;as). La suma total va de 0 a 21.",
            ]),
            ("Puntos de corte y niveles de severidad", [
                "Los rangos est&aacute;ndar derivan del estudio original de Spitzer et al. y se replicaron en la validaci&oacute;n espa&ntilde;ola. Un punto de corte &ge;10 suele usarse para sospecha cl&iacute;nica significativa; &ge;15 sugiere ansiedad severa que requiere evaluaci&oacute;n ampliada y posible derivaci&oacute;n.",
                "Interpreta siempre en contexto: comorbilidad depresiva infla puntuaciones; contexto vital agudo (duelo, estr&eacute;s laboral) puede elevar transitoriamente el puntaje. Registra en historia cl&iacute;nica puntuaci&oacute;n, fecha y decisiones cl&iacute;nicas tomadas.",
            ]),
            ("Validaci&oacute;n en Espa&ntilde;a: Garc&iacute;a-Campayo et al. (2010)", [
                "Garc&iacute;a-Campayo, Zamorano, Ruiz et al. (2010) validaron la versi&oacute;n espa&ntilde;ola del GAD-7 en <em>Atenci&oacute;n Primaria</em>, con muestra de pacientes de centros de salud. Reportaron <strong>sensibilidad 86%</strong> y <strong>especificidad 93%</strong> para detectar trastorno de ansiedad generalizada, con buena consistencia interna (alfa de Cronbach &asymp; 0,90).",
                "Estos datos respaldan su uso en atenci&oacute;n primaria espa&ntilde;ola y apoyan extensi&oacute;n a consulta privada de psicolog&iacute;a cl&iacute;nica, siempre integrando entrevista cl&iacute;nica estructurada. La versi&oacute;n castellana mantiene equivalencia sem&aacute;ntica con el original ingl&eacute;s.",
            ]),
            ("GAD-7 vs GAD-2 vs HAM-A", [
                "<strong>GAD-2</strong> (primeros dos &iacute;tems del GAD-7): ultrabreve para tamizaje masivo; punto de corte &ge;3 sugiere continuar con GAD-7 completo. <strong>HAM-A</strong> (Hamilton): escala heteroaplicada m&aacute;s larga, com&uacute;n en investigaci&oacute;n y psiquiatr&iacute;a; requiere entrevista cl&iacute;nica. El GAD-7 equilibra brevedad y utilidad en consulta psicol&oacute;gica ambulatoria.",
                "En Espa&ntilde;a, el GAD-7 se prefiere en atenci&oacute;n primaria por costo-efectividad; el HAM-A persiste en ensayos cl&iacute;nicos y algunos servicios especializados. Ver <a href=\"/articulos/phq9-vs-gad7-diferencias.html\">PHQ-9 vs GAD-7</a> para uso combinado con depresi&oacute;n.",
            ]),
            ("Uso en el SNS y consulta privada en Espa&ntilde;a", [
                "En el SNS, el GAD-7 se emplea en dispositivos de salud mental comunitaria, atenci&oacute;n primaria y programas de trastornos ansioso-depresivos, frecuentemente junto al PHQ-9. En consulta privada de psicolog&iacute;a, permite estandarizar seguimiento y comunicar progreso objetivo al paciente.",
                "Registra resultados en expediente cl&iacute;nico conforme a normativa de protecci&oacute;n de datos (RGPD) y deontolog&iacute;a del Colegio Oficial de Psic&oacute;logos correspondiente. Si compartes datos con m&eacute;dicos de familia, obt&eacute;n consentimiento expl&iacute;cito.",
            ]),
            ("Diferencias de uso cl&iacute;nico: Espa&ntilde;a vs LATAM", [
                "En LATAM (M&eacute;xico, Colombia, Chile, Argentina), el GAD-7 tambi&eacute;n es ampliamente usado, pero los baremos suelen importarse de validaciones internacionales o locales heterog&eacute;neas. Espa&ntilde;a cuenta con validaci&oacute;n primaria publicada en atenci&oacute;n primaria; en LATAM conviene citar estudio local cuando exista.",
                "Acceso a derivaci&oacute;n psiqui&aacute;trica, cobertura de medicaci&oacute;n y tiempos de espera difieren entre SNS, FONASA/ISAPRE o seguros privados latinoamericanos. Ajusta umbrales de derivaci&oacute;n seg&uacute;n recursos disponibles y gravedad funcional, no solo puntaje.",
            ]),
            ("Administraci&oacute;n, registro e interpretaci&oacute;n en consulta", [
                "Administra el GAD-7 al inicio del proceso y en intervalos definidos (p. ej., cada 4&ndash;8 semanas) para objetivar cambio cl&iacute;nico. Evita leer los &iacute;tems en voz alta salvo que haya dificultad lectora; en telepsicolog&iacute;a, comparte enlace seguro o pantalla con instrucciones escritas.",
                "Registra puntuaci&oacute;n total, subescalas relevantes si usas GAD-2 previo, contexto vital concurrente y plan de acci&oacute;n. Un descenso &ge;5 puntos suele considerarse cambio cl&iacute;nicamente notable en investigaci&oacute;n, pero interpreta junto a funcionalidad y metas del paciente.",
                "Para descarga del formulario en espa&ntilde;ol y aplicaci&oacute;n digital integrada, consulta <a href=\"/articulos/gad-7-espanol-pdf.html\">GAD-7 PDF en espa&ntilde;ol</a> y la gu&iacute;a general <a href=\"/articulos/gad-7-escala-ansiedad-generalizada.html\">GAD-7 escala de ansiedad generalizada</a>.",
            ]),
            ("Errores frecuentes al usar el GAD-7 en Espa&ntilde;a", [
                "Confundir tamizaje positivo con diagn&oacute;stico de TAG sin entrevista cl&iacute;nica. Usar un &uacute;nico puntaje aislado sin tendencia longitudinal. No indagar comorbilidad depresiva (PHQ-9). Omitir evaluaci&oacute;n de consumo de alcohol o benzodiacepinas que modulan s&iacute;ntomas ansiosos.",
                "Otro error es no adaptar lenguaje a pacientes con baja escolaridad o no castellanohablantes; ofrece aclaraci&oacute;n de &iacute;tems. Finalmente, olvidar consentimiento informado cuando compartes resultados con m&eacute;dico de familia o psiquiatra del SNS.",
            ]),
        ],
        "tables_html": """
    <table class="items-table">
      <thead>
        <tr><th>&Iacute;tem</th><th>Pregunta (resumen)</th><th>0</th><th>1</th><th>2</th><th>3</th></tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>Nerviosismo, ansiedad o tensi&oacute;n</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
        <tr><td>2</td><td>Imposibilidad de dejar de preocuparse</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
        <tr><td>3</td><td>Preocupaci&oacute;n excesiva</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
        <tr><td>4</td><td>Dificultad para relajarse</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
        <tr><td>5</td><td>Inquietud / no poder quedarse quieto</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
        <tr><td>6</td><td>Irritabilidad</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
        <tr><td>7</td><td>Miedo a que ocurra algo malo</td><td>Nada</td><td>Varios d&iacute;as</td><td>M&aacute;s de la mitad</td><td>Casi todos</td></tr>
      </tbody>
    </table>

    <table class="severity-table">
      <thead>
        <tr><th>Puntuaci&oacute;n total</th><th>Nivel de severidad</th><th>Acci&oacute;n cl&iacute;nica sugerida</th></tr>
      </thead>
      <tbody>
        <tr><td>0&ndash;4</td><td>Ansiedad m&iacute;nima</td><td>Psicoeducaci&oacute;n; reevaluar si persiste queja cl&iacute;nica.</td></tr>
        <tr><td>5&ndash;9</td><td>Ansiedad leve</td><td>Vigilancia, intervenci&oacute;n breve, re-test en 2&ndash;4 semanas.</td></tr>
        <tr><td>10&ndash;14</td><td>Ansiedad moderada</td><td>Plan terap&eacute;utico activo; considerar derivaci&oacute;n si no respuesta.</td></tr>
        <tr><td>15&ndash;21</td><td>Ansiedad severa</td><td>Evaluaci&oacute;n ampliada; derivaci&oacute;n psiqui&aacute;trica si indicado.</td></tr>
      </tbody>
    </table>
""",
        "faqs": [
            ("¿El GAD-7 está validado para población española?", "Sí. García-Campayo et al. (2010) validaron la versión española en atención primaria con sensibilidad 86% y especificidad 93% para TAG, respaldando su uso clínico en España."),
            ("¿Puedo usar el GAD-7 en telepsicología?", "Sí, es autorresponde y se adapta bien a formularios digitales o aplicación guiada en videollamada. Asegura confidencialidad, explica instrucciones y archiva puntuación en expediente."),
            ("¿Qué punto de corte usar para derivar a psiquiatría?", "Un GAD-7 ≥10 justifica evaluación clínica ampliada; ≥15, deterioro funcional marcado o ausencia de respuesta terapéutica son criterios habituales de derivación, junto con entrevista clínica."),
            ("¿El GAD-7 sirve para diagnóstico o solo tamizaje?", "Principalmente tamizaje y medición de severidad. El diagnóstico requiere entrevista clínica según DSM-5 o CIE-11, evaluación diferencial y criterios de duración/funcionalidad."),
        ],
        "related": [
            ("/articulos/que-es-el-gad-7.html", "Qu\u00e9 es el GAD-7"),
            ("/articulos/gad-7-escala-ansiedad-generalizada.html", "GAD-7 gu\u00eda cl\u00ednica"),
            ("/articulos/escala-hamilton-ansiedad-ham-a.html", "Escala Hamilton ansiedad HAM-A"),
        ],
        "refs": [
            ("https://pubmed.ncbi.nlm.nih.gov/20138495/", "Garc\u00eda-Campayo et al. (2010) \u2014 validaci\u00f3n GAD-7 Espa\u00f1a"),
        ],
    },
    {
        "slug": "test-ansiedad-chile-psicologos",
        "title": "Test de Ansiedad para Psic&oacute;logos en Chile: GAD-7, BAI y STAI | Kalyo",
        "meta_desc": "Gu&iacute;a de los principales tests de ansiedad usados en Chile: GAD-7, BAI y STAI. Validaci&oacute;n, puntos de corte y uso cl&iacute;nico para psic&oacute;logos chilenos.",
        "keywords": "test de ansiedad chile, gad-7 chile, escala ansiedad chile, evaluaci&oacute;n ansiedad psicolog&iacute;a chile",
        "h1": "Test de Ansiedad para Psic&oacute;logos en Chile: GAD-7, BAI y STAI",
        "hero_alt": "Tests de ansiedad Chile GAD-7 BAI STAI psic\u00f3logos",
        "meta_label": "Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "quick": "En Chile, los tests de ansiedad m&aacute;s usados en salud mental son el <strong>GAD-7</strong> (tamizaje TAG), el <strong>BAI</strong> (s&iacute;ntomas som&aacute;ticos de ansiedad) y el <strong>STAI</strong> (ansiedad estado vs rasgo). La ENS y el MINSAL documentan alta carga de trastornos ansioso-depresivos. Marco legal: <strong>Ley 20.584</strong> y Programa Nacional de Salud Mental.",
        "intro": "Chile enfrenta una creciente demanda de servicios por ansiedad, con cobertura mixta entre sistema p&uacute;blico (FONASA) e instituciones privadas (ISAPRE). Para psic&oacute;logos cl&iacute;nicos, elegir el instrumento adecuado —y interpretarlo con baremos y contexto— condiciona calidad asistencial y derivaciones oportunas. Esta gu&iacute;a compara GAD-7, BAI y STAI en el escenario chileno.",
        "sections": [
            ("Panorama de la ansiedad en Chile", [
                "La Encuesta Nacional de Salud (ENS) y reportes del Ministerio de Salud (MINSAL) han mostrado prevalencias elevadas de s&iacute;ntomas ansioso-depresivos en poblaci&oacute;n adulta, con incremento post-pandemia. Factores como estr&eacute;s econ&oacute;mico, violencia urbana, cambios laborales y acceso dispar a salud mental explican parte de la demanda en consulta psicol&oacute;gica.",
                "El Programa Nacional de Salud Mental promueve detecci&oacute;n temprana en atenci&oacute;n primaria y dispositivos comunitarios (SAPU, CESFAM, consultorios). En ISAPRE y consulta privada, el psic&oacute;logo suele ser primera l&iacute;nea evaluadora, lo que hace imprescindible tamizajes validados y documentados.",
            ]),
            ("Comparativa de instrumentos: GAD-7, BAI y STAI", [
                "Ning&uacute;n test sustituye la entrevista cl&iacute;nica. La tabla resume cu&aacute;ndo preferir cada instrumento en Chile.",
            ]),
            ("GAD-7 en Chile", [
                "El GAD-7 es el tamizaje m&aacute;s extendido por brevedad y utilidad en atenci&oacute;n primaria. En Chile se utiliza en programas de salud mental comunitaria y consulta privada, apoyado en validaciones internacionales en espa&ntilde;ol. Puntos de corte est&aacute;ndar: &ge;10 sospecha cl&iacute;nica; &ge;15 severidad alta.",
                "Ventajas: seguimiento num&eacute;rico del tratamiento, compatibilidad con telepsicolog&iacute;a, integraci&oacute;n con PHQ-9. Limitaciones: menos sensible a ataques de p&aacute;nico puro o fobias espec&iacute;ficas sin preocupaci&oacute;n generalizada.",
            ]),
            ("BAI (Inventario de Ansiedad de Beck) en Chile", [
                "El BAI mide s&iacute;ntomas som&aacute;ticos y cognitivos de ansiedad (21 &iacute;tems). Es &uacute;til cuando predominan quejas corporales (palpitaciones, mareo, tensi&oacute;n muscular) y para diferenciar ansiedad de cuadros m&eacute;dicos. Puntos de corte cl&aacute;sicos de Beck: 0&ndash;7 m&iacute;nima, 8&ndash;15 leve, 16&ndash;25 moderada, 26&ndash;63 severa.",
                "En Chile se emplea en servicios cl&iacute;nicos y universitarios; verifica si usas baremo local o internacional al informar resultados. Complementa con evaluaci&oacute;n m&eacute;dica si s&iacute;ntomas som&aacute;ticos son at&iacute;picos.",
            ]),
            ("STAI en Chile", [
                "El STAI diferencia <strong>ansiedad estado</strong> (reactiva al momento) y <strong>ansiedad rasgo</strong> (propensi&oacute;n estable). La versi&oacute;n adaptada al espa&ntilde;ol latinoamericano es frecuente en investigaci&oacute;n y evaluaci&oacute;n psicol&oacute;gica chilena.",
                "Cl&iacute;nicamente ayuda a separar crisis situacional de patr&oacute;n temperamental ansioso. Es m&aacute;s largo que GAD-7; ideal en evaluaciones iniciales completas o periciales.",
            ]),
            ("Marco normativo en Chile", [
                "La <strong>Ley 20.584</strong> regula derechos y deberes de las personas en relaci&oacute;n con acciones de salud: informaci&oacute;n, consentimiento, confidencialidad y acceso a la historia cl&iacute;nica. Todo test aplicado debe estar consignado en expediente con interpretaci&oacute;n profesional.",
                "El Programa Nacional de Salud Mental del MINSAL establece l&iacute;neas de cuidado para depresi&oacute;n y ansiedad en red p&uacute;blica. Psic&oacute;logos en convenio deben alinear documentaci&oacute;n con protocolos institucionales.",
            ]),
            ("Cu&aacute;ndo derivar a psiquiatr&iacute;a", [
                "Deriva cuando: (1) GAD-7 &ge;15 o BAI en rango severo con deterioro marcado; (2) comorbilidad depresiva mayor; (3) s&iacute;ntomas psic&oacute;ticos o bipolaridad; (4) riesgo suicida; (5) ausencia de respuesta a psicoterapia tras periodo razonable; (6) solicitud de medicaci&oacute;n o indicaci&oacute;n cl&iacute;nica de f&aacute;rmacos.",
                "Documenta derivaci&oacute;n, comparte informe con consentimiento y mant&eacute;n continuidad psicoterap&eacute;utica cuando corresponda.",
            ]),
            ("GAD-7, BAI y STAI en FONASA, ISAPRE y consulta privada", [
                "En el sistema p&uacute;blico chileno (FONASA), el acceso a psicolog&iacute;a cl&iacute;nica depende de derivaci&oacute;n desde atenci&oacute;n primaria y disponibilidad en SAPU o dispositivos de salud mental. El GAD-7 facilita priorizar casos en listas de espera cuando se estandariza en triage psicosocial.",
                "En ISAPRE y consulta privada, los pacientes suelen llegar sin evaluaci&oacute;n previa; aplicar GAD-7 en primera sesi&oacute;n establece l&iacute;nea base y justifica plan de tratamiento ante aseguradoras si requieren informes.",
                "El BAI es preferible cuando el paciente describe s&iacute;ntomas corporales y teme enfermedad m&eacute;dica; el STAI aporta distinci&oacute;n estado/rasgo en perfiles de alta reactividad. Combina instrumentos solo si hay tiempo cl&iacute;nico y prop&oacute;sito claro; evita fatiga por exceso de tests.",
            ]),
            ("Documentaci&oacute;n cl&iacute;nica y protecci&oacute;n de datos en Chile", [
                "La Ley 20.584 garantiza acceso del paciente a su historia cl&iacute;nica y exige registro de procedimientos. Los resultados de tests deben incluir fecha, versi&oacute;n del instrumento, puntuaci&oacute;n, interpretaci&oacute;n profesional y recomendaciones, evitando copiar &iacute;tems sin contexto.",
                "Almacena datos en sistemas con respaldo y control de acceso; en telepsicolog&iacute;a, utiliza plataformas conformes a pol&iacute;ticas del Colegio de Psic&oacute;logos de Chile y normativa de protecci&oacute;n de datos personales.",
            ]),
        ],
        "tables_html": """
    <table class="items-table">
      <thead>
        <tr><th>Instrumento</th><th>&Iacute;tems / tiempo</th><th>Constructo</th><th>Uso principal en Chile</th></tr>
      </thead>
      <tbody>
        <tr><td>GAD-7</td><td>7 &iacute;tems / 2&ndash;3 min</td><td>Ansiedad generalizada (TAG)</td><td>Tamizaje en APS, salud mental, consulta privada</td></tr>
        <tr><td>BAI</td><td>21 &iacute;tems / 5&ndash;10 min</td><td>S&iacute;ntomas som&aacute;ticos-cognitivos de ansiedad</td><td>Evaluaci&oacute;n cl&iacute;nica con queja som&aacute;tica</td></tr>
        <tr><td>STAI</td><td>40 &iacute;tems / 10&ndash;15 min</td><td>Ansiedad estado vs rasgo</td><td>Evaluaci&oacute;n inicial amplia, investigaci&oacute;n</td></tr>
      </tbody>
    </table>
""",
        "faqs": [
            ("¿Qué test de ansiedad es más usado en el sistema público de Chile?", "El GAD-7 es el más extendido en tamizaje por brevedad e integración con programas de salud mental en atención primaria y dispositivos comunitarios del MINSAL."),
            ("¿El GAD-7 está validado en población chilena?", "Se usa ampliamente apoyado en validaciones internacionales en español; consulta literatura local cuando publiques informes. La interpretación clínica debe complementarse con entrevista y contexto chileno."),
            ("¿Puedo aplicar estos tests en telepsicología?", "Sí. GAD-7 y BAI son autorresponde; STAI también. Envía formulario seguro antes de sesión o supervisa aplicación en videollamada; archiva resultados en expediente conforme Ley 20.584."),
            ("¿Cuál es la diferencia entre el BAI y el GAD-7?", "El GAD-7 tamiza ansiedad generalizada con foco en preocupación y tensión; el BAI cuantifica síntomas somáticos y cognitivos de ansiedad más amplios. Son complementarios, no excluyentes."),
        ],
        "related": [
            ("/articulos/que-es-el-gad-7.html", "Qu\u00e9 es el GAD-7"),
            ("/articulos/test-beck-ansiedad-bai.html", "Test Beck ansiedad BAI"),
            ("/articulos/stai-ansiedad-estado-rasgo.html", "STAI ansiedad estado-rasgo"),
        ],
        "refs": [
            ("https://www.minsal.cl/", "MINSAL Chile \u2014 Salud mental"),
        ],
    },
]


def main() -> None:
    out = ROOT / "articulos"
    for cfg in ARTICLES:
        path = out / f"{cfg['slug']}.html"
        html = build_article(cfg)
        path.write_text(html, encoding="utf-8")
        body = re.search(r"<article class=\"article-wrapper\">(.*)</article>", html, re.S).group(1)
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        print(f"OK {path.name} ({words} body words)")


if __name__ == "__main__":
    main()
