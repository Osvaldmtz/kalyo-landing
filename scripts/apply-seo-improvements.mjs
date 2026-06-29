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

const TEST_SUBCATEGORIES = {
  'Depresi&oacute;n y &aacute;nimo': [
    'inventario-depresion-beck-bdi',
    'test-beck-ansiedad-bai',
    'que-es-el-phq-9',
    'escala-dass-21',
    'epds-depresion-postnatal-edimburgo',
  ],
  Ansiedad: ['que-es-el-gad-7', 'escala-hamilton-ansiedad-ham-a', 'pss-10-escala-estres-percibido', 'isi-indice-severidad-insomnio'],
  'Trauma y riesgo': ['escala-pcl-5-estres-postraumatico', 'c-ssrs-escala-columbia-suicidio', 'aces-adversidad-infantil'],
  'Conductas adictivas': ['audit-test-alcoholismo', 'cage-alcoholismo-test', 'dast-10-deteccion-drogas'],
  Otros: ['inventario-burnout-mbi', 'resiliencia-cd-risc', 'phq-15-sintomas-somaticos', 'scoff-trastornos-alimentarios', 'y-bocs-escala-yale-brown-toc'],
};

const TOPICS_BATCH3_PATH = path.join(__dirname, 'article-batch', 'topics-batch3.json');
const TOPICS_BATCH4_PATH = path.join(__dirname, 'article-batch', 'topics-batch4.json');

const BATCH3_CATEGORY_LABELS = {
  tests_cognitivos: 'Cognici&oacute;n y neuropsicolog&iacute;a',
  tests_depresion: 'Depresi&oacute;n — escalas adicionales',
  tests_ansiedad: 'Ansiedad — escalas adicionales',
  tests_estado_animo: 'Estado de &aacute;nimo y bipolar',
  tests_neurodesarrollo: 'Neurodesarrollo y TEA',
  tests_infantil: 'Evaluaci&oacute;n infantil',
  tests_alimentarios: 'Trastornos alimentarios — escalas adicionales',
  tests_sueno: 'Sue&ntilde;o y somnolencia',
  tests_sustancias: 'Sustancias — tamizaje adicional',
  tests_riesgo: 'Riesgo y seguridad cl&iacute;nica',
  tests_trauma: 'Trauma — escalas adicionales',
  tests_outcomes: 'Resultados de tratamiento',
  tests_sintomatologia: 'Sintomatolog&iacute;a amplia',
  tests_vinculo: 'Apego y v&iacute;nculo',
  tests_familia: 'Terapia familiar',
  tests_pareja: 'Terapia de pareja',
  tests_general: 'Salud mental general',
};

const BATCH4_CATEGORY_LABELS = {
  tests_tamizaje_breve: 'Tamizajes breves y atenci&oacute;n primaria',
  tests_ansiedad_ampliada: 'Ansiedad — inventarios adicionales',
  tests_depresion_suicidio_bipolar: 'Depresi&oacute;n, suicidio y bipolaridad',
  tests_infantil_adolescente: 'Infantil y adolescente — ampliado',
  tests_sustancias_ampliado: 'Sustancias — escalas adicionales',
  tests_toc_trauma_disociacion: 'TOC, trauma y disociaci&oacute;n',
  tests_bienestar_personalidad: 'Bienestar y personalidad',
  tests_proceso_terapeutico: 'Proceso terap&eacute;utico y alianza',
  practica_clinica: 'Pr&aacute;ctica cl&iacute;nica — gu&iacute;as',
};

function buildBatchSubcategories(topicsPath, labels) {
  if (!fs.existsSync(topicsPath)) return {};
  const { topics } = JSON.parse(fs.readFileSync(topicsPath, 'utf8'));
  const groups = {};
  for (const topic of topics) {
    const label = labels[topic.category] || topic.category;
    if (!groups[label]) groups[label] = [];
    groups[label].push(topic.slug);
  }
  return groups;
}

function buildBatch3Subcategories() {
  return buildBatchSubcategories(TOPICS_BATCH3_PATH, BATCH3_CATEGORY_LABELS);
}

function buildBatch4Subcategories() {
  return buildBatchSubcategories(TOPICS_BATCH4_PATH, BATCH4_CATEGORY_LABELS);
}

const BATCH3_SUBCATEGORIES = buildBatch3Subcategories();
const BATCH4_SUBCATEGORIES = buildBatch4Subcategories();
const MERGED_TEST_SUBCATEGORIES = { ...TEST_SUBCATEGORIES, ...BATCH3_SUBCATEGORIES, ...BATCH4_SUBCATEGORIES };

const NORMATIVA_CO = [
  'ley-1090-psicologia-colombia',
  'rips-registros-individuales-colombia',
  'ley-1581-proteccion-datos-psicologia',
  'sivigila-psicologia-colombia',
  'resolucion-1888-salud-mental-colombia',
  'evaluacion-psicologica-colombia-mexico',
];

const NORMATIVA_MX = ['nom-004-historia-clinica-mexico', 'alternativas-elo-psicologos-mexico'];

const PRACTICA = [
  'who-5-bienestar-psicologico',
  'ghq-12-cuestionario-salud-general',
  'evaluacion-riesgo-suicida',
  'test-vocacional-riasec',
  'como-interpretar-tests-psicologicos',
  'como-documentar-sesion-clinica',
  'consentimiento-informado-psicologia',
  'software-para-psicologos-clinicos',
  'tests-psicologicos-digitales',
  'orientacion-vocacional-psicologia',
  'como-abrir-consulta-privada-colombia',
  'como-abrir-consulta-privada-mexico',
  'como-redactar-informe-psicologico',
  'telepsicologia-etica-mexico-colombia',
];

const CATEGORY_TAGS = {
  ...Object.fromEntries(
    Object.values(MERGED_TEST_SUBCATEGORIES)
      .flat()
      .map((s) => [s, 'Test cl&iacute;nico']),
  ),
  ...Object.fromEntries(NORMATIVA_CO.map((s) => [s, 'Normativa Colombia'])),
  ...Object.fromEntries(NORMATIVA_MX.map((s) => [s, 'Normativa M&eacute;xico'])),
  ...Object.fromEntries(PRACTICA.map((s) => [s, 'Pr&aacute;ctica cl&iacute;nica'])),
};

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
  return `<a class="library-card" href="/articulos/${meta.slug}.html">
            <span class="library-card-tag">${tag}</span>
            <h3 class="library-card-title">${meta.title}</h3>
            <p class="library-card-desc">${truncate(meta.description)}</p>
          </a>`;
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
  const testCount = Object.values(MERGED_TEST_SUBCATEGORIES).flat().length;
  const testSections = Object.entries(MERGED_TEST_SUBCATEGORIES)
    .map(
      ([label, slugs]) => `        <div class="library-subsection">
          <h3 class="library-subtitle">${label}</h3>
          <div class="library-grid">
${slugs.map((slug) => cardHtml(articlesBySlug[slug], CATEGORY_TAGS[slug])).join('\n')}
          </div>
        </div>`,
    )
    .join('\n');

  const section = (title, count, slugs, tag) => `      <section class="library-section" id="${title.toLowerCase().replace(/[^a-z0-9]+/g, '-')}">
        <h2 class="library-section-title">${title} <span class="library-count">(${count} art&iacute;culos)</span></h2>
        <div class="library-grid">
${slugs.map((slug) => cardHtml(articlesBySlug[slug], tag)).join('\n')}
        </div>
      </section>`;

  return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${INDEX_TITLE}</title>
  <meta name="description" content="${INDEX_DESCRIPTION}">
  <meta name="keywords" content="recursos psicólogos, tests clínicos, normativa psicología Colombia México, guías clínicas, Kalyo">
  <link rel="canonical" href="https://kalyo.io/articulos/">

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

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">

  <style>${INLINE_STYLE}

    .library-page {
      max-width: 1120px;
      margin: 0 auto;
      padding: 120px 24px 80px;
    }

    .library-hero {
      text-align: center;
      margin-bottom: 56px;
    }

    .library-hero h1 {
      font-family: 'Playfair Display', serif;
      font-size: 44px;
      line-height: 1.15;
      color: var(--ink);
      margin-bottom: 16px;
    }

    .library-hero p {
      font-size: 19px;
      color: var(--ink-mid);
      max-width: 720px;
      margin: 0 auto;
      font-weight: 300;
    }

    .library-section {
      margin-bottom: 56px;
    }

    .library-section-title {
      font-family: 'Playfair Display', serif;
      font-size: 30px;
      color: var(--ink);
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--purple-soft);
    }

    .library-count {
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 400;
      color: var(--ink-light);
    }

    .library-subsection {
      margin-bottom: 32px;
    }

    .library-subtitle {
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 600;
      color: var(--purple-dark);
      margin-bottom: 16px;
    }

    .library-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }

    .library-card {
      display: block;
      background: #fff;
      border: 1px solid rgba(124, 61, 227, 0.12);
      border-radius: 12px;
      padding: 20px;
      text-decoration: none;
      transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
    }

    .library-card:hover {
      border-color: var(--purple);
      box-shadow: 0 8px 24px rgba(124, 61, 227, 0.12);
      transform: translateY(-2px);
    }

    .library-card-tag {
      display: inline-block;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--purple);
      background: var(--purple-soft);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 12px;
    }

    .library-card-title {
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      font-weight: 600;
      line-height: 1.4;
      color: var(--ink);
      margin-bottom: 8px;
    }

    .library-card-desc {
      font-size: 14px;
      line-height: 1.55;
      color: var(--ink-light);
      margin: 0;
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

    .header-link:hover,
    .header-link.is-active {
      color: var(--purple);
      background: var(--purple-soft);
    }

    @media (max-width: 960px) {
      .library-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
    }

    @media (max-width: 640px) {
      .library-hero h1 {
        font-size: 34px;
      }

      .library-grid {
        grid-template-columns: 1fr;
      }

      .header-nav {
        gap: 8px;
      }

      .header-link {
        display: none;
      }
    }
  </style>
${GTAG}
</head>
<body>

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <div class="header-nav">
        <a href="/articulos/" class="header-link is-active">Recursos</a>
        <a href="https://app.kalyo.io" class="header-btn">Iniciar sesi&oacute;n</a>
      </div>
    </div>
  </header>

  <main class="library-page">
    <div class="library-hero">
      <h1>Biblioteca cl&iacute;nica para psic&oacute;logos</h1>
      <p>${totalArticles} gu&iacute;as sobre tests validados, normativa y pr&aacute;ctica cl&iacute;nica en Colombia y M&eacute;xico</p>
    </div>

    <section class="library-section" id="tests-evaluacion-clinica">
      <h2 class="library-section-title">Tests de evaluaci&oacute;n cl&iacute;nica <span class="library-count">(${testCount} art&iacute;culos)</span></h2>
${testSections}
    </section>

${section('Normativa Colombia', NORMATIVA_CO.length, NORMATIVA_CO, 'Normativa Colombia')}
${section('Normativa M&eacute;xico', NORMATIVA_MX.length, NORMATIVA_MX, 'Normativa M&eacute;xico')}
${section('Pr&aacute;ctica cl&iacute;nica', PRACTICA.length, PRACTICA, 'Pr&aacute;ctica cl&iacute;nica')}

    <div class="cta-box">
      <h2>Aplica tests y documenta tu consulta en Kalyo</h2>
      <p>91 tests validados, historia cl&iacute;nica digital y cumplimiento normativo para Colombia y M&eacute;xico.</p>
      <a href="https://app.kalyo.io" class="cta-btn">Prueba gratis 14 d&iacute;as &rarr;</a>
    </div>
  </main>

  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a></p>
  </footer>

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

const articleFiles = fs
  .readdirSync(ARTICULOS_DIR)
  .filter((f) => f.endsWith('.html') && f !== 'index.html')
  .sort();

const articlesBySlug = Object.fromEntries(articleFiles.map((f) => {
  const meta = parseArticleMeta(f);
  return [meta.slug, meta];
}));

fs.writeFileSync(
  path.join(ARTICULOS_DIR, 'index.html'),
  buildIndexHtml(articlesBySlug, articleFiles.length),
  'utf8',
);
console.log(`Created articulos/index.html (${articleFiles.length} articles)`);

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
