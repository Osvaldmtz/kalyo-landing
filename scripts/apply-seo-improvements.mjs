import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const ARTICULOS_DIR = path.join(ROOT, 'articulos');
const TEMPLATE_PATH = path.join(ARTICULOS_DIR, 'que-es-el-phq-9.html');

const templateHtml = fs.readFileSync(TEMPLATE_PATH, 'utf8');
const styleMatch = templateHtml.match(/<style>([\s\S]*?)<\/style>/);
const INLINE_STYLE = styleMatch[1];

const GTAG = `<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-RTBRDTN5BK');
</script>`;

const INDEX_TITLE = 'Recursos para Psicólogos — Guías Clínicas y Normativas | Kalyo';
const INDEX_DESCRIPTION =
  'Biblioteca de recursos para psicólogos clínicos en Colombia y México: guías de tests clínicos, normativa legal y práctica clínica. Todo disponible digitalmente en Kalyo.';

const ARTICLE_BATCH_DIR = path.join(__dirname, 'article-batch');
const HOME_INDEX_PATH = path.join(ROOT, 'index.html');
const HOME_INDEX_HTML = fs.readFileSync(HOME_INDEX_PATH, 'utf8');

const TOP_LEVEL = {
  ESCALAS: 'Escalas Cl&iacute;nicas',
  NORMATIVAS: 'Normativas y Leyes',
  SOFTWARE: 'Software y Tecnolog&iacute;a',
  PRACTICA: 'Pr&aacute;ctica Cl&iacute;nica',
};

const TOP_LEVEL_ORDER = [
  TOP_LEVEL.ESCALAS,
  TOP_LEVEL.NORMATIVAS,
  TOP_LEVEL.SOFTWARE,
  TOP_LEVEL.PRACTICA,
];

const TOP_LEVEL_IDS = {
  [TOP_LEVEL.ESCALAS]: 'escalas-clinicas',
  [TOP_LEVEL.NORMATIVAS]: 'normativas-leyes',
  [TOP_LEVEL.SOFTWARE]: 'software-tecnologia',
  [TOP_LEVEL.PRACTICA]: 'practica-clinica',
};

const CATEGORY_TO_TOP = {
  evaluacion_tea: TOP_LEVEL.ESCALAS,
  normativa_tea_colombia: TOP_LEVEL.NORMATIVAS,
  guias_legales_mx: TOP_LEVEL.NORMATIVAS,
  guias_legales_co: TOP_LEVEL.NORMATIVAS,
  comparativas: TOP_LEVEL.SOFTWARE,
  guias_practica_clinica: TOP_LEVEL.PRACTICA,
  practica_clinica: TOP_LEVEL.PRACTICA,
  practica_neuropsicologia: TOP_LEVEL.PRACTICA,
  inclusion_tea: TOP_LEVEL.PRACTICA,
  neurodesarrollo_tea: TOP_LEVEL.PRACTICA,
  guias_evaluacion: TOP_LEVEL.ESCALAS,
  tests_bienestar: TOP_LEVEL.ESCALAS,
};

function loadTopicCategoryMap() {
  const map = {};
  if (!fs.existsSync(ARTICLE_BATCH_DIR)) return map;

  for (const filename of fs.readdirSync(ARTICLE_BATCH_DIR)) {
    if (!filename.startsWith('topics') || !filename.endsWith('.json')) continue;
    const { topics } = JSON.parse(fs.readFileSync(path.join(ARTICLE_BATCH_DIR, filename), 'utf8'));
    for (const topic of topics) {
      map[topic.slug] = topic.category;
    }
  }
  return map;
}

const TOPIC_CATEGORY_MAP = loadTopicCategoryMap();

function classifySlug(slug) {
  const category = TOPIC_CATEGORY_MAP[slug];
  if (category) {
    if (category.startsWith('tests_')) return TOP_LEVEL.ESCALAS;
    if (CATEGORY_TO_TOP[category]) return CATEGORY_TO_TOP[category];
  }

  if (/^(ley-|nom-|resolucion-|politica-|sivigila|rips-|historia-clinica|derechos-pacientes|ruta-atencion)/.test(slug)) {
    return TOP_LEVEL.NORMATIVAS;
  }
  if (/(software|doctoralia|teleconsulta|inteligencia-artificial|digitales|alternativas)/.test(slug)) {
    return TOP_LEVEL.SOFTWARE;
  }
  if (/^(como-|consentimiento|evaluacion-riesgo|telepsicologia|orientacion-|diagnostico-tea|evaluacion-tea-ninos|inclusion|trastornos-neurodesarrollo)/.test(slug)) {
    return TOP_LEVEL.PRACTICA;
  }

  return TOP_LEVEL.ESCALAS;
}

function discoverArticles() {
  const files = fs
    .readdirSync(ARTICULOS_DIR)
    .filter((f) => f.endsWith('.html') && f !== 'index.html')
    .sort();

  const articles = files.map((filename) => parseArticleMeta(filename));
  const articlesBySlug = Object.fromEntries(articles.map((meta) => [meta.slug, meta]));

  if (files.length !== Object.keys(articlesBySlug).length) {
    const seen = new Set();
    const duplicates = [];
    for (const meta of articles) {
      if (seen.has(meta.slug)) duplicates.push(meta.slug);
      seen.add(meta.slug);
    }
    console.warn(`Warning: duplicate slugs detected: ${duplicates.join(', ')}`);
  }

  return { files, articles, articlesBySlug };
}

function groupArticlesByTopLevel(articlesBySlug) {
  const groups = Object.fromEntries(TOP_LEVEL_ORDER.map((label) => [label, []]));
  for (const meta of Object.values(articlesBySlug)) {
    groups[classifySlug(meta.slug)].push(meta);
  }
  for (const label of TOP_LEVEL_ORDER) {
    groups[label].sort((a, b) => a.title.localeCompare(b.title, 'es'));
  }
  return groups;
}

function countIndexLinks(indexHtml) {
  return (indexHtml.match(/href="\/articulos\/[^"]+\.html"/g) || []).length;
}

function verifyIndexCoverage(articleFiles, indexHtml) {
  const linkCount = countIndexLinks(indexHtml);
  if (linkCount !== articleFiles.length) {
    const linked = new Set([...indexHtml.matchAll(/href="\/articulos\/([^"]+\.html)"/g)].map((m) => m[1]));
    const expected = new Set(articleFiles);
    const missing = [...expected].filter((f) => !linked.has(f));
    const extra = [...linked].filter((f) => !expected.has(f));
    throw new Error(
      `Index link mismatch: ${articleFiles.length} files vs ${linkCount} links`
      + (missing.length ? `; missing: ${missing.join(', ')}` : '')
      + (extra.length ? `; extra: ${extra.join(', ')}` : ''),
    );
  }
}

const FAQ_ARTICLES = {
  'que-es-el-phq-9.html': [
    {
      q: '¿Qué puntaje es preocupante en el PHQ-9?',
      a: 'Un puntaje de 10 o más indica depresión clínicamente significativa y suele requerir evaluación ampliada y plan de tratamiento. Entre 5 y 9 sugiere sintomatología leve que conviene monitorizar. Cualquier respuesta distinta de cero en el ítem 9 (ideación suicida) requiere evaluación de riesgo, independientemente del total.',
    },
    {
      q: '¿El PHQ-9 diagnostica depresión?',
      a: 'No. El PHQ-9 es un instrumento de tamizaje y medición de severidad, no un diagnóstico formal. Los resultados deben integrarse con entrevista clínica, historia del paciente y criterios DSM-5 o CIE-11 antes de emitir un diagnóstico.',
    },
    {
      q: '¿Cada cuánto se debe aplicar el PHQ-9?',
      a: 'En tratamiento activo se recomienda cada 2 a 4 semanas para monitorizar respuesta terapéutica. En remisión o seguimiento puede aplicarse mensual o trimestral. Una reducción de al menos 5 puntos entre aplicaciones suele considerarse clínicamente relevante.',
    },
    {
      q: '¿Cuál es la diferencia entre PHQ-9 y PHQ-2?',
      a: 'El PHQ-2 incluye solo los dos primeros ítems (ánimo e interés) como tamizaje ultra breve. Si el paciente puntúa 3 o más, se administra el PHQ-9 completo para estimar severidad con mayor precisión.',
    },
  ],
  'que-es-el-gad-7.html': [
    {
      q: '¿Qué puntaje del GAD-7 indica ansiedad clínica?',
      a: 'Un puntaje de 10 o más sugiere ansiedad moderada a severa y justifica evaluación clínica ampliada. Entre 5 y 9 indica ansiedad leve; por debajo de 5, sintomatología mínima.',
    },
    {
      q: '¿El GAD-7 sirve para diagnosticar TAG?',
      a: 'No por sí solo. El GAD-7 detecta síntomas de ansiedad generalizada, pero el diagnóstico requiere entrevista clínica y verificación de criterios diagnósticos, duración e impacto funcional.',
    },
    {
      q: '¿GAD-7 o HAM-A: cuál usar?',
      a: 'El GAD-7 es autoadministrado, breve y ideal para consulta privada y telepsicología. El HAM-A requiere entrevista clínica y es preferible cuando se necesita evaluación heteroinformada o mayor detalle clínico.',
    },
    {
      q: '¿Se puede combinar GAD-7 con PHQ-9?',
      a: 'Sí. Es una práctica frecuente porque depresión y ansiedad suelen coexistir. Aplicar ambos en la evaluación inicial permite un perfil emocional más completo y mejor planificación terapéutica.',
    },
  ],
  'escala-dass-21.html': [
    {
      q: '¿Qué mide el DASS-21?',
      a: 'Evalúa tres dimensiones emocionales: depresión, ansiedad y estrés. A diferencia de escalas unidimensionales, permite identificar qué dominio predomina en el cuadro clínico del paciente.',
    },
    {
      q: '¿Cómo se interpretan las subescalas del DASS-21?',
      a: 'Cada subescala tiene puntos de corte propios para clasificar severidad en normal, leve, moderado, severo y muy severo. Conviene interpretar las tres subescalas por separado además del perfil global.',
    },
    {
      q: '¿DASS-21 o PHQ-9 para depresión?',
      a: 'Use PHQ-9 cuando el objetivo principal es tamizaje depresivo breve alineado con DSM-5. Prefiera DASS-21 cuando necesite diferenciar depresión, ansiedad y estrés en una sola batería.',
    },
    {
      q: '¿El DASS-21 sustituye una entrevista clínica?',
      a: 'No. Es un autoinforme de screening y seguimiento. La entrevista clínica sigue siendo indispensable para contextualizar resultados, explorar comorbilidades y formular el caso.',
    },
  ],
  'nom-004-historia-clinica-mexico.html': [
    {
      q: '¿Qué es la NOM-004-SSA3-2012?',
      a: 'Es la norma oficial mexicana que regula la integración, contenido y conservación del expediente clínico en instituciones y consultorios de salud, incluida la práctica psicológica privada cuando se prestan servicios clínicos.',
    },
    {
      q: '¿Los psicólogos en consulta privada deben cumplir la NOM-004?',
      a: 'Sí, cuando documentan atención clínica deben integrar un expediente con los elementos mínimos exigidos: identificación, motivo de consulta, antecedentes, exploración, diagnóstico o impresión clínica, plan terapéutico, evolución y consentimientos.',
    },
    {
      q: '¿Una historia clínica digital cumple con la NOM-004?',
      a: 'Puede cumplir si garantiza integridad, confidencialidad, respaldo, trazabilidad y conservación de registros. El soporte digital es válido si cumple los requisitos de contenido y seguridad de la norma.',
    },
    {
      q: '¿Qué pasa si no cumplo la NOM-004?',
      a: 'El incumplimiento puede derivar en sanciones administrativas, responsabilidad profesional y dificultades legales ante quejas, auditorías o continuidad de atención. Documentar correctamente protege al paciente y al profesional.',
    },
  ],
  'ley-1090-psicologia-colombia.html': [
    {
      q: '¿Qué regula la Ley 1090 de 2006?',
      a: 'Establece el Código Deontológico y Bioético del ejercicio profesional de la psicología en Colombia: deberes, derechos, confidencialidad, historia clínica, relación con usuarios y responsabilidades éticas.',
    },
    {
      q: '¿La Ley 1090 aplica a psicólogos en consulta privada?',
      a: 'Sí. Todos los psicólogos colegiados en Colombia, incluidos los de libre ejercicio, deben cumplir sus principios éticos, documentación clínica y deberes de reporte cuando la ley lo exige.',
    },
    {
      q: '¿Cuándo se puede romper la confidencialidad?',
      a: 'Existen excepciones legales como riesgo grave para la vida del paciente o terceros, mandatos judiciales, reportes SIVIGILA de eventos obligatorios y situaciones previstas expresamente por la normativa vigente.',
    },
    {
      q: '¿Qué debe incluir la historia clínica según la Ley 1090?',
      a: 'Debe documentar evaluación, diagnóstico o formulación, intervención, evolución, consentimientos, derivaciones y cierre, con registros suficientes para garantizar continuidad asistencial y responsabilidad profesional.',
    },
  ],
  'evaluacion-riesgo-suicida.html': [
    {
      q: '¿Qué se evalúa en un protocolo de riesgo suicida?',
      a: 'Se exploran ideación, plan, intentos previos, acceso a medios letales, factores precipitantes, protección social, funcionamiento y nivel de urgencia. La evaluación combina entrevista clínica y escalas estandarizadas.',
    },
    {
      q: '¿Qué hacer si un paciente tiene ideación suicida activa?',
      a: 'Activar protocolo de seguridad inmediato: evaluar plan y acceso a medios, no dejar solo al paciente si hay riesgo inminente, documentar, acordar plan de contención y derivar a urgencias o psiquiatría cuando corresponda.',
    },
    {
      q: '¿La C-SSRS reemplaza la entrevista clínica?',
      a: 'No. La C-SSRS estructura la evaluación de ideación y conducta suicida, pero la decisión clínica requiere contexto, juicio profesional y plan de seguridad personalizado.',
    },
    {
      q: '¿Debo documentar la evaluación de riesgo suicida?',
      a: 'Sí. Es un requisito ético y legal documentar preguntas realizadas, respuestas, nivel de riesgo estimado, medidas de seguridad acordadas, derivaciones y seguimiento programado.',
    },
  ],
  'consentimiento-informado-psicologia.html': [
    {
      q: '¿Es obligatorio el consentimiento informado en psicología?',
      a: 'Sí. Antes de iniciar evaluación o tratamiento, el paciente debe recibir información clara sobre objetivos, procedimientos, riesgos, confidencialidad, límites y derechos, y manifestar su aceptación.',
    },
    {
      q: '¿Qué debe incluir un consentimiento informado?',
      a: 'Identificación del profesional, naturaleza del servicio, duración estimada, confidencialidad y sus excepciones, uso de tests, telepsicología si aplica, derecho a retirar consentimiento y datos de contacto de emergencia.',
    },
    {
      q: '¿El consentimiento informado es igual al consentimiento de datos?',
      a: 'No. El consentimiento clínico autoriza la intervención psicológica; el consentimiento de datos autoriza el tratamiento de información personal, especialmente relevante bajo Ley 1581 en Colombia.',
    },
    {
      q: '¿Se puede firmar digitalmente el consentimiento?',
      a: 'Sí, si el sistema garantiza identificación, integridad, fecha y almacenamiento seguro. Plataformas clínicas como Kalyo permiten gestionar consentimientos digitales conforme a buenas prácticas y normativa local.',
    },
  ],
  'software-para-psicologos-clinicos.html': [
    {
      q: '¿Qué funciones debe tener un software para psicólogos?',
      a: 'Agenda, expediente clínico, consentimientos, aplicación de tests, gráficas de seguimiento, facturación básica y cumplimiento normativo local (NOM-004, Ley 1090, protección de datos).',
    },
    {
      q: '¿Es seguro guardar historias clínicas en la nube?',
      a: 'Puede serlo si el proveedor implementa cifrado, control de accesos, respaldos, políticas de privacidad y cumplimiento legal. Evalúe dónde se almacenan los datos y qué certificaciones ofrece la plataforma.',
    },
    {
      q: '¿Un software clínico reemplaza el criterio profesional?',
      a: 'No. Automatiza documentación, tests y seguimiento, pero la evaluación, formulación del caso e intervención siguen siendo responsabilidad exclusiva del psicólogo.',
    },
    {
      q: '¿Por qué usar tests digitales integrados?',
      a: 'Reducen errores de captura, ahorran tiempo, facilitan gráficas longitudinales y mejoran trazabilidad clínica frente al papel, especialmente en consultas con seguimiento frecuente.',
    },
  ],
  'inventario-depresion-beck-bdi.html': [
    {
      q: '¿Qué mide el BDI-II?',
      a: 'Evalúa severidad de síntomas depresivos en adultos mediante 21 ítems que cubren aspectos cognitivos, afectivos y somáticos de la depresión durante las últimas dos semanas.',
    },
    {
      q: '¿BDI-II o PHQ-9: cuál elegir?',
      a: 'Use PHQ-9 para tamizaje breve en atención primaria o seguimiento rápido. Prefiera BDI-II cuando necesite mayor detalle clínico, investigación o evaluación depresiva más exhaustiva.',
    },
    {
      q: '¿Cómo interpretar los puntos de corte del BDI-II?',
      a: 'Los rangos usuales van de depresión mínima a severa según puntuación total. Interprete siempre con entrevista clínica, especialmente si predominan síntomas somáticos o comorbilidad médica.',
    },
    {
      q: '¿El BDI-II se puede aplicar digitalmente?',
      a: 'Sí. Su formato de autoinforme lo hace apto para aplicación digital con puntuación automática, siempre respetando derechos de autor y condiciones de uso del instrumento.',
    },
  ],
  'who-5-bienestar-psicologico.html': [
    {
      q: '¿Qué mide el WHO-5?',
      a: 'Mide bienestar psicológico subjetivo en cinco ítems sobre ánimo positivo, calma, energía, descanso e interés por la vida durante las últimas dos semanas.',
    },
    {
      q: '¿Qué puntaje del WHO-5 indica bajo bienestar?',
      a: 'Por debajo de 50 (escala 0–100) sugiere bienestar reducido; por debajo de 28 aumenta la probabilidad de depresión clínica y conviene aplicar un tamizaje depresivo complementario.',
    },
    {
      q: '¿WHO-5 o PHQ-9 para seguimiento terapéutico?',
      a: 'El WHO-5 es excelente para monitorizar recuperación y bienestar entre sesiones. El PHQ-9 mide mejor severidad sintomática depresiva. Muchos clínicos usan ambos de forma complementaria.',
    },
    {
      q: '¿Cómo se calcula la puntuación del WHO-5?',
      a: 'Se suman los cinco ítems (0–25) y se multiplica por cuatro para obtener un porcentaje de 0 a 100. Documente ambos formatos para evitar confusiones en el seguimiento.',
    },
  ],
};

function parseArticleMeta(filename) {
  const html = fs.readFileSync(path.join(ARTICULOS_DIR, filename), 'utf8');
  const title = html.match(/<title>([^<]+)<\/title>/)?.[1]?.replace(' | Kalyo', '') || filename;
  const description = html.match(/<meta name="description" content="([^"]+)"/)?.[1] || '';
  const slug = filename.replace('.html', '');
  return { filename, slug, title, description, html };
}

function truncate(text, max = 110) {
  if (text.length <= max) return text;
  return `${text.slice(0, max - 1).trim()}…`;
}

function escAttr(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
}

function cardHtml(meta, tag) {
  return `      <a href="/articulos/${meta.slug}.html" class="blog-card">
        <span class="blog-card-tag">${tag}</span>
        <h3>${meta.title}</h3>
        <p>${truncate(meta.description)}</p>
      </a>`;
}

function extractHomeFragment(startMarker, endMarker) {
  const start = HOME_INDEX_HTML.indexOf(startMarker);
  const end = HOME_INDEX_HTML.indexOf(endMarker, start);
  return HOME_INDEX_HTML.slice(start, end + endMarker.length);
}

function siteHeaderForArticulos() {
  return extractHomeFragment('<!-- HEADER -->', '</header>')
    .replace(/href="#/g, 'href="/#')
    .replace(
      '<a href="/demo" style="color:var(--purple);font-weight:600">Demo</a>',
      '<a href="/articulos/" style="color:var(--purple);font-weight:600">Recursos</a>\n    <a href="/demo" style="color:var(--purple);font-weight:600">Demo</a>',
    );
}

function siteFooterForArticulos() {
  return extractHomeFragment('<!-- FOOTER -->', '</footer>').replace(/href="#/g, 'href="/#');
}

function siteHeadExtras() {
  const gaMatch = HOME_INDEX_HTML.match(/<!-- Google Analytics[\s\S]*?<\/script>\n/);
  const clarityMatch = HOME_INDEX_HTML.match(/<!-- Microsoft Clarity[\s\S]*?<\/script>\n/);
  return `${gaMatch?.[0] || ''}${clarityMatch?.[0] || ''}
<!-- Meta Pixel Code -->
<script src="/scripts/meta-pixel.js" defer></script>`;
}

function buildFaqJsonLd(faqs) {
  return `  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
${faqs
  .map(
    (f) => `    {
      "@type": "Question",
      "name": ${JSON.stringify(f.q)},
      "acceptedAnswer": {
        "@type": "Answer",
        "text": ${JSON.stringify(f.a)}
      }
    }`,
  )
  .join(',\n')}
  ]
}
</script>`;
}

function buildBreadcrumbJsonLd(title, slug) {
  return `  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://kalyo.io/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Recursos para psicólogos",
      "item": "https://kalyo.io/articulos/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": ${JSON.stringify(title.replace(' | Kalyo', ''))},
      "item": "https://kalyo.io/articulos/${slug}.html"
    }
  ]
}
</script>`;
}

function buildIndexHtml(articlesBySlug, totalArticles) {
  const groups = groupArticlesByTopLevel(articlesBySlug);
  const tagForGroup = {
    [TOP_LEVEL.ESCALAS]: 'Escala cl&iacute;nica',
    [TOP_LEVEL.NORMATIVAS]: 'Normativa',
    [TOP_LEVEL.SOFTWARE]: 'Software',
    [TOP_LEVEL.PRACTICA]: 'Gu&iacute;a cl&iacute;nica',
  };

  const categorySections = TOP_LEVEL_ORDER.map((label) => {
    const articles = groups[label];
    if (!articles.length) return '';
    const id = TOP_LEVEL_IDS[label];
    const tag = tagForGroup[label];
    return `    <section class="section-blog library-category" id="${id}">
      <div style="max-width:1100px;margin:0 auto">
        <div class="blog-header" style="margin-bottom:32px">
          <h2 class="section-headline">${label} <span style="font-size:.85em;font-weight:400;color:var(--ink-light)">(${articles.length})</span></h2>
        </div>
        <div class="blog-grid blog-grid--library">
${articles.map((meta) => cardHtml(meta, tag)).join('\n')}
        </div>
      </div>
    </section>`;
  }).filter(Boolean).join('\n\n');

  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${INDEX_TITLE}</title>
<meta name="description" content="${INDEX_DESCRIPTION}">
<meta name="keywords" content="recursos psicólogos, tests clínicos, normativa psicología Colombia México, guías clínicas, Kalyo">
<link rel="canonical" href="https://kalyo.io/articulos/">
<meta name="robots" content="index, follow">

<meta property="og:type" content="website">
<meta property="og:title" content="${escAttr(INDEX_TITLE)}">
<meta property="og:description" content="${escAttr(INDEX_DESCRIPTION)}">
<meta property="og:url" content="https://kalyo.io/articulos/">
<meta property="og:site_name" content="Kalyo">
<meta property="og:locale" content="es_MX">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${escAttr(INDEX_TITLE)}">
<meta name="twitter:description" content="${escAttr(INDEX_DESCRIPTION)}">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Recursos para Psicólogos",
  "description": ${JSON.stringify(INDEX_DESCRIPTION)},
  "url": "https://kalyo.io/articulos/",
  "numberOfItems": ${totalArticles}
}
</script>

<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/style.css">
${siteHeadExtras()}
<style>
  .library-hero { padding-top:120px; }
  .library-category { padding-top:56px; padding-bottom:56px; }
  .library-category + .library-category { border-top:1px solid var(--purple-mid); }
  .blog-grid--library { grid-template-columns:repeat(3,1fr); }
  @media (max-width:960px) {
    .blog-grid--library { grid-template-columns:repeat(2,1fr); }
  }
  @media (max-width:640px) {
    .blog-grid--library { grid-template-columns:1fr; }
    .library-hero h1 { font-size:2rem; }
  }
</style>
</head>
<body>
<script src="/scripts/tracking.js" defer></script>

${siteHeaderForArticulos()}

<main>
  <section class="section-blog library-hero">
    <div style="max-width:1100px;margin:0 auto">
      <div class="blog-header">
        <div class="section-label">Recursos</div>
        <h1 class="section-headline">Biblioteca cl&iacute;nica para psic&oacute;logos</h1>
        <p class="section-sub">${totalArticles} gu&iacute;as sobre escalas validadas, normativa legal, software cl&iacute;nico y pr&aacute;ctica de consulta en Colombia y M&eacute;xico.</p>
      </div>
    </div>
  </section>

${categorySections}

  <section class="section-cta">
    <div style="position:relative;z-index:1">
      <h2>Aplica tests y documenta tu consulta en Kalyo</h2>
      <p>91 tests validados, historia cl&iacute;nica digital y cumplimiento normativo para Colombia y M&eacute;xico.</p>
      <div class="cta-btns">
        <a href="https://app.kalyo.io" class="btn-cta-solid" data-ga-event="cta_signup_recursos">Prueba gratis 14 d&iacute;as &rarr;</a>
        <a href="/demo" class="btn-cta-outline" data-ga-event="cta_demo_recursos">Agenda tu demo &rarr;</a>
      </div>
    </div>
  </section>
</main>

${siteFooterForArticulos()}

<script src="/scripts/script.js" defer></script>
</body>
</html>
`;
}

function upsertJsonLd(html, marker, jsonLdBlock) {
  const regex = new RegExp(`\\n  <script type="application/ld\\+json">\\n\\{\\n  "@context": "https://schema.org",\\n  "@type": "${marker}"[\\s\\S]*?\\n</script>`, 'g');
  if (regex.test(html)) {
    return html.replace(regex, `\n${jsonLdBlock}`);
  }
  return html.replace('</script>\n<!-- Fonts -->', `</script>\n${jsonLdBlock}\n<!-- Fonts -->`);
}

function updateArticleHeader(html) {
  if (html.includes('header-nav')) return html;
  return html.replace(
    `<header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <a href="https://app.kalyo.io" class="header-btn">Iniciar sesi&oacute;n</a>
    </div>
  </header>`,
    `<header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <div class="header-nav">
        <a href="/articulos/" class="header-link">Recursos</a>
        <a href="https://app.kalyo.io" class="header-btn">Iniciar sesi&oacute;n</a>
      </div>
    </div>
  </header>`,
  ).replace(
    `.header-btn:hover {
      background: var(--purple);
      color: #fff;
    }`,
    `.header-btn:hover {
      background: var(--purple);
      color: #fff;
    }

    .header-nav {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .header-link {
      font-size: 14px;
      font-weight: 500;
      color: var(--ink-mid);
      text-decoration: none;
      padding: 8px 12px;
      border-radius: 8px;
      transition: color 0.2s, background 0.2s;
    }

    .header-link:hover {
      color: var(--purple);
      background: var(--purple-soft);
    }

    .article-breadcrumb {
      font-size: 14px;
      color: var(--ink-light);
      margin-bottom: 20px;
    }

    .article-breadcrumb a {
      color: var(--purple);
      text-decoration: none;
    }

    .article-breadcrumb a:hover {
      text-decoration: underline;
    }`,
  );
}

function insertBreadcrumbNav(html, title) {
  if (html.includes('<nav class="article-breadcrumb"')) return html;
  const shortTitle = title.length > 48 ? `${title.slice(0, 48)}…` : title;
  return html.replace(
    '<div class="article-hero-img">',
    `<nav class="article-breadcrumb" aria-label="Breadcrumb">
      <a href="/">Inicio</a> &rsaquo; <a href="/articulos/">Recursos</a> &rsaquo; ${shortTitle}
    </nav>
    <div class="article-hero-img">`,
  );
}

const indexOnly = process.argv.includes('--index-only');

const { files: articleFiles, articlesBySlug } = discoverArticles();
const indexHtml = buildIndexHtml(articlesBySlug, articleFiles.length);
verifyIndexCoverage(articleFiles, indexHtml);

fs.writeFileSync(path.join(ARTICULOS_DIR, 'index.html'), indexHtml, 'utf8');
console.log(`Created articulos/index.html (${articleFiles.length} articles from filesystem scan)`);

if (indexOnly) {
  process.exit(0);
}

let faqUpdated = 0;
let breadcrumbUpdated = 0;

for (const filename of articleFiles) {
  const meta = parseArticleMeta(filename);
  let html = meta.html;

  html = updateArticleHeader(html);
  html = insertBreadcrumbNav(html, meta.title);
  html = upsertJsonLd(html, 'BreadcrumbList', buildBreadcrumbJsonLd(meta.title, meta.slug));
  breadcrumbUpdated += 1;

  if (FAQ_ARTICLES[filename]) {
    html = upsertJsonLd(html, 'FAQPage', buildFaqJsonLd(FAQ_ARTICLES[filename]));
    faqUpdated += 1;
  }

  fs.writeFileSync(path.join(ARTICULOS_DIR, filename), html, 'utf8');
}

const sitemapPath = path.join(ROOT, 'sitemap.xml');
let sitemap = fs.readFileSync(sitemapPath, 'utf8');
if (!sitemap.includes('https://kalyo.io/articulos/</loc>')) {
  sitemap = sitemap.replace(
    '  <url>\n    <loc>https://kalyo.io/embajadores/</loc>',
    `  <url>
    <loc>https://kalyo.io/articulos/</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://kalyo.io/embajadores/</loc>`,
  );
  fs.writeFileSync(sitemapPath, sitemap, 'utf8');
  console.log('Updated sitemap.xml with /articulos/');
}

console.log(`FAQ schema added/updated on ${faqUpdated} articles`);
console.log(`Breadcrumb schema + nav added/updated on ${breadcrumbUpdated} articles`);
