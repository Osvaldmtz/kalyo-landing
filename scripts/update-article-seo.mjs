import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const articulosDir = path.join(__dirname, '..', 'articulos');

const ARTICLES = {
  'inventario-depresion-beck-bdi.html': {
    slug: 'inventario-depresion-beck-bdi',
    title: 'Inventario de Depresión de Beck BDI-II: Interpretación y uso clínico | Kalyo',
    description:
      'Guía completa del BDI-II: puntuaciones, interpretación clínica y diferencias con el PHQ-9. Aprende a aplicarlo digitalmente con Kalyo para psicólogos.',
    keywords:
      'BDI-II, Inventario de Beck, depresión, test depresión, psicología clínica, evaluación depresiva, psicometría',
  },
  'test-beck-ansiedad-bai.html': {
    slug: 'test-beck-ansiedad-bai',
    title: 'Inventario de Ansiedad de Beck BAI: Guía clínica completa | Kalyo',
    description:
      'Todo sobre el BAI: cómo aplicarlo, interpretar puntuaciones y diferenciarlo del BDI. Test de ansiedad de Beck disponible digitalmente en Kalyo.',
    keywords:
      'BAI, Inventario de Ansiedad de Beck, ansiedad, test ansiedad, psicología clínica, evaluación ansiosa, psicometría',
  },
  'que-es-el-phq-9.html': {
    slug: 'que-es-el-phq-9',
    title: 'PHQ-9: Qué es, cómo interpretar resultados y cuándo aplicarlo | Kalyo',
    description:
      'Guía clínica del PHQ-9: escala de puntuación 0-27, interpretación por niveles de depresión y frecuencia recomendada. Aplícalo gratis en Kalyo.',
    keywords:
      'PHQ-9, test depresión, tamizaje depresión, psicología clínica, escala depresión, evaluación depresiva, DSM-5',
  },
  'que-es-el-gad-7.html': {
    slug: 'que-es-el-gad-7',
    title: 'GAD-7: Escala de ansiedad generalizada — interpretación clínica | Kalyo',
    description:
      'Guía completa del GAD-7: puntuaciones, niveles de ansiedad y cuándo preferirlo al HAM-A. Aplica el GAD-7 digitalmente con Kalyo para psicólogos.',
    keywords:
      'GAD-7, ansiedad generalizada, test ansiedad, psicología clínica, tamizaje ansiedad, evaluación ansiosa, TAG',
  },
  'escala-pcl-5-estres-postraumatico.html': {
    slug: 'escala-pcl-5-estres-postraumatico',
    title: 'PCL-5: Escala de estrés postraumático TEPT — guía clínica | Kalyo',
    description:
      'Todo sobre el PCL-5: criterios DSM-5, interpretación de puntuaciones y uso en trauma. Escala de TEPT disponible digitalmente en Kalyo para psicólogos.',
    keywords:
      'PCL-5, TEPT, PTSD, estrés postraumático, trauma, psicología clínica, evaluación trauma, DSM-5',
  },
  'escala-dass-21.html': {
    slug: 'escala-dass-21',
    title: 'DASS-21: Depresión, Ansiedad y Estrés — interpretación | Kalyo',
    description:
      'Guía del DASS-21: cómo diferencia depresión, ansiedad y estrés en una sola evaluación. Interpretación de subescalas y uso clínico. Disponible en Kalyo.',
    keywords:
      'DASS-21, depresión, ansiedad, estrés, psicología clínica, evaluación emocional, subescalas, psicometría',
  },
  'escala-hamilton-ansiedad-ham-a.html': {
    slug: 'escala-hamilton-ansiedad-ham-a',
    title: 'Escala de Hamilton para Ansiedad HAM-A: guía de aplicación | Kalyo',
    description:
      'Guía clínica del HAM-A: 14 ítems, puntuación e interpretación de ansiedad. Cuándo elegirlo sobre el GAD-7. Disponible para psicólogos en Kalyo.',
    keywords:
      'HAM-A, Hamilton ansiedad, escala ansiedad, psicología clínica, evaluación ansiosa, entrevista clínica, psicometría',
  },
  'inventario-burnout-mbi.html': {
    slug: 'inventario-burnout-mbi',
    title: 'Inventario de Burnout de Maslach MBI: guía clínica completa | Kalyo',
    description:
      'Guía del MBI: tres dimensiones del burnout, interpretación de puntuaciones y uso en profesionales de la salud. Aplícalo digitalmente con Kalyo.',
    keywords:
      'MBI, burnout, Maslach, agotamiento profesional, psicología clínica, salud mental laboral, evaluación burnout',
  },
  'resiliencia-cd-risc.html': {
    slug: 'resiliencia-cd-risc',
    title: 'Escala de Resiliencia Connor-Davidson CD-RISC: guía clínica | Kalyo',
    description:
      'Guía completa del CD-RISC: versiones de 10 y 25 ítems, puntuación e interpretación. Mide resiliencia psicológica en consulta digital con Kalyo.',
    keywords:
      'CD-RISC, resiliencia, fortalezas psicológicas, psicología clínica, evaluación resiliencia, psicometría, bienestar',
  },
  'audit-test-alcoholismo.html': {
    slug: 'audit-test-alcoholismo',
    title: 'Test AUDIT: Detección de consumo de alcohol — guía clínica | Kalyo',
    description:
      'Guía del AUDIT-10: puntuación, niveles de riesgo e interpretación clínica. Test de detección de alcoholismo disponible digitalmente en Kalyo.',
    keywords:
      'AUDIT, alcoholismo, consumo de alcohol, detección alcohol, psicología clínica, evaluación adicciones, tamizaje alcohol',
  },
  'evaluacion-riesgo-suicida.html': {
    slug: 'evaluacion-riesgo-suicida',
    title: 'Evaluación de Riesgo Suicida: protocolos y herramientas clínicas | Kalyo',
    description:
      'Guía de evaluación del riesgo suicida: protocolos SAFE-T y Columbia Scale. Herramientas clínicas digitales para psicólogos disponibles en Kalyo.',
    keywords:
      'riesgo suicida, evaluación suicida, SAFE-T, Columbia Scale, psicología clínica, protocolo clínico, seguridad paciente',
  },
  'test-vocacional-riasec.html': {
    slug: 'test-vocacional-riasec',
    title: 'Test Vocacional RIASEC: tipos Holland y orientación profesional | Kalyo',
    description:
      'Guía del test RIASEC: 6 tipos Holland, interpretación y uso en orientación vocacional. Aplica el test de Holland digitalmente con Kalyo.',
    keywords:
      'RIASEC, Holland, orientación vocacional, test vocacional, psicología vocacional, tipos profesionales, carrera',
  },
  'orientacion-vocacional-psicologia.html': {
    slug: 'orientacion-vocacional-psicologia',
    title: 'Orientación Vocacional en Psicología: guía para psicólogos | Kalyo',
    description:
      'Cómo realizar orientación vocacional con herramientas digitales. Tests RIASEC, entrevista clínica y documentación. Plataforma para psicólogos Kalyo.',
    keywords:
      'orientación vocacional, psicología vocacional, RIASEC, guía profesional, psicólogos, evaluación vocacional, carrera',
  },
  'como-interpretar-tests-psicologicos.html': {
    slug: 'como-interpretar-tests-psicologicos',
    title: 'Cómo Interpretar Tests Psicológicos: guía clínica para psicólogos | Kalyo',
    description:
      'Guía práctica para interpretar tests psicológicos: baremos, percentiles, puntuaciones T y Z. Para psicólogos clínicos en Colombia y México. Kalyo.',
    keywords:
      'interpretación tests, psicometría, baremos, percentiles, psicología clínica, puntuaciones T, evaluación psicológica',
  },
  'como-documentar-sesion-clinica.html': {
    slug: 'como-documentar-sesion-clinica',
    title: 'Cómo Documentar una Sesión Clínica: notas SOAP y formatos | Kalyo',
    description:
      'Guía completa para documentar sesiones clínicas: formato SOAP, historia clínica digital y cumplimiento NOM-004. Para psicólogos en Kalyo.',
    keywords:
      'documentación clínica, notas SOAP, historia clínica, psicología clínica, NOM-004, registro sesión, consultorio',
  },
  'consentimiento-informado-psicologia.html': {
    slug: 'consentimiento-informado-psicologia',
    title: 'Consentimiento Informado en Psicología: guía legal y clínica | Kalyo',
    description:
      'Cómo redactar y gestionar el consentimiento informado en psicología clínica. Requisitos legales en Colombia y México. Plantillas digitales en Kalyo.',
    keywords:
      'consentimiento informado, psicología clínica, ética profesional, Colombia, México, documentación legal, plantillas',
  },
  'evaluacion-psicologica-colombia-mexico.html': {
    slug: 'evaluacion-psicologica-colombia-mexico',
    title: 'Evaluación Psicológica en Colombia y México: guía clínica | Kalyo',
    description:
      'Guía de evaluación psicológica para psicólogos en Colombia y México: normativas, tests validados y documentación digital. Plataforma Kalyo.',
    keywords:
      'evaluación psicológica, Colombia, México, psicología clínica, normativas, tests validados, LATAM, documentación',
  },
  'software-para-psicologos-clinicos.html': {
    slug: 'software-para-psicologos-clinicos',
    title: 'Software para Psicólogos Clínicos: qué buscar y cómo elegir | Kalyo',
    description:
      'Guía para elegir software de gestión de consulta psicológica: agenda, tests, notas clínicas y cumplimiento normativo. Kalyo para psicólogos LATAM.',
    keywords:
      'software psicólogos, gestión consultorio, psicología clínica, plataforma digital, agenda clínica, tests digitales, LATAM',
  },
  'tests-psicologicos-digitales.html': {
    slug: 'tests-psicologicos-digitales',
    title: 'Tests Psicológicos Digitales: ventajas y cómo implementarlos | Kalyo',
    description:
      'Ventajas de los tests psicológicos digitales vs papel: precisión, tiempo y almacenamiento. 91 tests validados disponibles en Kalyo para psicólogos.',
    keywords:
      'tests digitales, psicología clínica, evaluación digital, psicometría, plataforma clínica, tests validados, telepsicología',
  },
  'alternativas-elo-psicologos-mexico.html': {
    slug: 'alternativas-elo-psicologos-mexico',
    title: 'Alternativas a ELO para Psicólogos en México: comparativa 2026 | Kalyo',
    description:
      'Las mejores alternativas a ELO para psicólogos en México: comparativa de funciones, precios y cumplimiento NOM-004. Kalyo como opción principal.',
    keywords:
      'alternativas ELO, psicólogos México, software clínico, NOM-004, gestión consultorio, Kalyo, comparativa software',
  },
};

const INTERNAL_LINKS = {
  'que-es-el-phq-9.html': [
    [
      'El PHQ-9 completo, en cambio, es preferible en psicolog&iacute;a cl&iacute;nica',
      'El PHQ-9 completo, en cambio, es preferible en psicolog&iacute;a cl&iacute;nica; para evaluaciones m&aacute;s profundas, el <a href="/articulos/inventario-depresion-beck-bdi.html">Inventario de Beck (BDI-II)</a> ofrece mayor detalle',
    ],
  ],
  'inventario-depresion-beck-bdi.html': [],
  'escala-dass-21.html': [
    ['como el PHQ-9 (depresi&oacute;n) o el GAD-7 (ansiedad)', 'como el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> (depresi&oacute;n) o el <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> (ansiedad)'],
    ['instrumento espec&iacute;fico (PHQ-9 para depresi&oacute;n, GAD-7 para ansiedad)', 'instrumento espec&iacute;fico (<a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> para depresi&oacute;n, <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> para ansiedad)'],
  ],
  'que-es-el-gad-7.html': [
    [
      'como la Escala de Hamilton para Ansiedad (HAM-A), que requiere administraci&oacute;n',
      'como la <a href="/articulos/escala-hamilton-ansiedad-ham-a.html">Escala de Hamilton para Ansiedad (HAM-A)</a>, que requiere administraci&oacute;n',
    ],
  ],
  'escala-pcl-5-estres-postraumatico.html': [
    [
      'debe ser confirmado mediante una entrevista cl&iacute;nica estructurada.',
      'debe ser confirmado mediante una entrevista cl&iacute;nica estructurada. En pacientes con hiperactivaci&oacute;n persistente, conviene complementar con el <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> para evaluar comorbilidad ansiosa.',
    ],
  ],
};

function escAttr(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
}

function buildHead(meta) {
  const { slug, title, description, keywords } = meta;
  const url = `https://kalyo.io/articulos/${slug}.html`;
  const image = `https://kalyo.io/assets/blog/${slug}-hero.jpg`;
  const t = escAttr(title);
  const d = escAttr(description);

  return `  <title>${title}</title>
  <meta name="description" content="${description}">
  <meta name="keywords" content="${keywords}">
  <link rel="canonical" href="${url}">

  <link rel="preload" as="image" href="/assets/blog/${slug}-hero.webp" type="image/webp">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="${t}">
  <meta property="og:description" content="${d}">
  <meta property="og:url" content="${url}">
  <meta property="og:image" content="${image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kalyo">
  <meta property="og:locale" content="es_MX">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${t}">
  <meta name="twitter:description" content="${d}">
  <meta name="twitter:image" content="${image}">

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": ${JSON.stringify(title)},
  "description": ${JSON.stringify(description)},
  "image": "${image}",
  "author": {
    "@type": "Organization",
    "name": "Kalyo",
    "url": "https://kalyo.io"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Kalyo",
    "logo": {
      "@type": "ImageObject",
      "url": "https://kalyo.io/assets/logo.png"
    }
  },
  "datePublished": "2026-01-01",
  "dateModified": "2026-06-21",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "${url}"
  }
}
</script>
`;
}

function wrapHeroPicture(html, slug) {
  if (html.includes('<picture>')) return html;
  const re = new RegExp(
    `(<div class="article-hero-img">\\s*)<img src="/assets/blog/${slug}-hero\\.jpg"\\s+alt="([^"]*)"\\s+width="1200" height="630"\\s+loading="eager" fetchpriority="high">(\\s*</div>)`,
    's',
  );
  return html.replace(
    re,
    `$1<picture>
      <source srcset="/assets/blog/${slug}-hero.webp" type="image/webp">
      <img src="/assets/blog/${slug}-hero.jpg" alt="$2" width="1200" height="630" loading="eager" fetchpriority="high">
    </picture>$3`,
  );
}

function wrapInlinePicture(html, slug) {
  if (html.includes('article-inline-img') && html.includes('-inline.webp')) return html;
  const re = new RegExp(
    `(<figure class="article-inline-img">\\s*)<img src="/assets/blog/${slug}-inline\\.jpg"\\s+alt="([^"]*)"\\s+width="800" height="450"\\s+loading="lazy">(\\s*</figure>)`,
    's',
  );
  return html.replace(
    re,
    `$1<picture>
      <source srcset="/assets/blog/${slug}-inline.webp" type="image/webp">
      <img src="/assets/blog/${slug}-inline.jpg" alt="$2" width="800" height="450" loading="lazy">
    </picture>$3`,
  );
}

function updateSeoBlock(html, meta) {
  const headStart = html.indexOf('<title>');
  const fontsMarker = html.indexOf('<!-- Fonts -->');
  if (headStart === -1 || fontsMarker === -1) {
    throw new Error('Could not locate SEO block boundaries');
  }
  return html.slice(0, headStart) + buildHead(meta) + html.slice(fontsMarker);
}

function removeOldJsonLd(html) {
  return html.replace(/\n<script type="application\/ld\+json">[\s\S]*?<\/script>\n(?=<!-- Google Analytics|<\/head>)/g, '\n');
}

function applyInternalLinks(html, filename) {
  const links = INTERNAL_LINKS[filename] || [];
  let out = html;
  for (const [from, to] of links) {
    if (out.includes(to)) continue;
    out = out.replace(from, to);
  }
  return out;
}

let updated = 0;
for (const [filename, meta] of Object.entries(ARTICLES)) {
  const filePath = path.join(articulosDir, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing: ${filename}`);
    continue;
  }

  let html = fs.readFileSync(filePath, 'utf8');
  html = removeOldJsonLd(html);
  html = updateSeoBlock(html, meta);
  html = wrapHeroPicture(html, meta.slug);
  html = wrapInlinePicture(html, meta.slug);
  html = applyInternalLinks(html, filename);
  fs.writeFileSync(filePath, html, 'utf8');
  updated++;
  console.log(`SEO updated: ${filename}`);
}

console.log(`\nUpdated ${updated} articles.`);
