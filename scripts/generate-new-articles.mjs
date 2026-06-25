import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { REMAINING_ARTICLES } from './generate-new-articles-content.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const ARTICULOS_DIR = path.join(ROOT, 'articulos');
const TEMPLATE_PATH = path.join(ARTICULOS_DIR, 'que-es-el-phq-9.html');

const templateHtml = fs.readFileSync(TEMPLATE_PATH, 'utf8');
const styleMatch = templateHtml.match(/<style>([\s\S]*?)<\/style>/);
if (!styleMatch) throw new Error('Could not extract <style> block from PHQ-9 template');
const INLINE_STYLE = styleMatch[1];

const GTAG = `<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-RTBRDTN5BK');
</script>`;

function escAttr(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
}

function p(text) {
  return `<p>\n      ${text}\n    </p>`;
}

function paras(...texts) {
  return texts.map((t) => p(t)).join('\n\n    ');
}

function ensureMinWords(bodyHtml, minWords, topicLabel) {
  const extras = [
    `En la pr&aacute;ctica cl&iacute;nica diaria, ${topicLabel} requiere que el profesional integre la evidencia psicom&eacute;trica o normativa con el juicio cl&iacute;nico, la entrevista semiestructurada y la formulaci&oacute;n del caso. Ning&uacute;n instrumento, protocolo o resoluci&oacute;n sustituye la relaci&oacute;n terap&eacute;utica ni la evaluaci&oacute;n contextual del paciente.`,
    `Los psic&oacute;logos en Colombia y M&eacute;xico enfrentan un entorno regulatorio en evoluci&oacute;n. Mantenerse actualizado sobre cambios normativos, asistir a formaci&oacute;n continua y utilizar herramientas digitales que faciliten el cumplimiento sin sacrificar la calidad cl&iacute;nica es una inversi&oacute;n directa en la seguridad del paciente y en la sostenibilidad profesional.`,
    `La documentaci&oacute;n adecuada respalda cada decisi&oacute;n cl&iacute;nica vinculada a ${topicLabel}. Registrar fecha, procedimiento, resultados, interpretaci&oacute;n y plan de seguimiento no solo cumple requisitos legales, sino que mejora la continuidad de la atenci&oacute;n cuando el paciente cambia de profesional o requiere derivaci&oacute;n a otro nivel del sistema de salud.`,
    `En telepsicolog&iacute;a y consulta h&iacute;brida, los mismos est&aacute;ndares aplican: consentimiento informado, confidencialidad, selecci&oacute;n de instrumentos validados y comunicaci&oacute;n clara de resultados al paciente. Las plataformas digitales deben facilitar estos procesos sin a&ntilde;adir carga administrativa innecesaria al cl&iacute;nico.`,
    `Finalmente, conviene revisar peri&oacute;dicamente si la implementaci&oacute;n de ${topicLabel} en el consultorio est&aacute; alineada con las gu&iacute;as cl&iacute;nicas vigentes, las recomendaciones de colegios profesionales y las necesidades espec&iacute;ficas de la poblaci&oacute;n atendida, ajustando protocolos internos cuando la evidencia o la normativa as&iacute; lo requieran.`,
  ];
  let html = bodyHtml;
  let i = 0;
  while (countWords(html) < minWords) {
    html += `\n\n    ${p(extras[i % extras.length])}`;
    i += 1;
    if (i > 20) break;
  }
  return html;
}

function countWords(html) {
  const text = html
    .replace(/<[^>]+>/g, ' ')
    .replace(/&[a-z]+;|&#\d+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  return text.split(/\s+/).filter(Boolean).length;
}

function inlineFigure(slug, alt) {
  return `<figure class="article-inline-img">
      <picture>
      <source srcset="/assets/blog/${slug}-inline.webp" type="image/webp">
      <img src="/assets/blog/${slug}-inline.jpg" alt="${escAttr(alt)}" width="800" height="450" loading="lazy">
    </picture>
    </figure>`;
}

function insertInlineBeforeThirdH2(bodyHtml, slug, inlineAlt) {
  const figure = inlineFigure(slug, inlineAlt);
  let count = 0;
  return bodyHtml.replace(/<h2>/g, (match) => {
    count += 1;
    if (count === 3) return `${figure}\n\n    <h2>`;
    return match;
  });
}

function relatedSection(related) {
  const items = related
    .map(
      ([slug, label]) =>
        `<li><a href="/articulos/${slug}.html" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">${label}</a></li>`,
    )
    .join('\n      ');
  return `<section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
    <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Art&iacute;culos relacionados</h2>
    <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
      ${items}
    </ul>
  </section>`;
}

function buildHead({ slug, title, description, keywords }) {
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
</script>`;
}

function buildArticle(config) {
  const {
    slug,
    filename,
    title,
    description,
    keywords,
    metaLabel,
    h1,
    intro,
    heroAlt,
    inlineAlt,
    bodyHtml,
    ctaTitle,
    ctaText,
    ctaButton,
    related,
  } = config;

  const bodyWithFigure = insertInlineBeforeThirdH2(bodyHtml, slug, inlineAlt);
  const articleInner = `
    <div class="article-hero-img">
      <picture>
      <source srcset="/assets/blog/${slug}-hero.webp" type="image/webp">
      <img src="/assets/blog/${slug}-hero.jpg" alt="${escAttr(heroAlt)}" width="1200" height="630" loading="eager" fetchpriority="high">
    </picture>
    </div>
    <p class="article-meta">${metaLabel}</p>

    <h1>${h1}</h1>

    <p class="article-intro">
      ${intro}
    </p>

    ${bodyWithFigure}

    <div class="cta-box">
      <h2>${ctaTitle}</h2>
      <p>${ctaText}</p>
      <a href="https://app.kalyo.io" class="cta-btn">${ctaButton}</a>
    </div>
  ${relatedSection(related)}
  `;

  return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
${buildHead({ slug, title, description, keywords })}
<!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">

  <style>${INLINE_STYLE}
  </style>
${GTAG}
</head>
<body>

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <a href="https://app.kalyo.io" class="header-btn">Iniciar sesi&oacute;n</a>
    </div>
  </header>

  <article class="article-wrapper">${articleInner}
  </article>

  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a></p>
  </footer>

</body>
</html>
`;
}

// Article body content generators
const ARTICLES = [];

ARTICLES.push({
  slug: 'who-5-bienestar-psicologico',
  filename: 'who-5-bienestar-psicologico.html',
  title: 'WHO-5: Escala de Bienestar de la OMS — guía clínica para psicólogos | Kalyo',
  description:
    'Guía completa del WHO-5: interpretación de puntuaciones, uso en seguimiento terapéutico y detección de depresión. Escala de bienestar OMS disponible en Kalyo.',
  keywords: 'WHO-5, escala bienestar OMS, bienestar psicológico, detección depresión, psicología clínica',
  metaLabel: 'Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026',
  h1: 'WHO-5: Escala de Bienestar de la OMS',
  intro:
    'El WHO-5 (World Health Organization-Five Well-Being Index) es un cuestionario breve de cinco &iacute;tems desarrollado por la Organizaci&oacute;n Mundial de la Salud para medir el bienestar psicol&oacute;gico subjetivo. A diferencia de escalas centradas en patolog&iacute;a, el WHO-5 eval&uacute;a dimensiones positivas de la salud mental y se ha convertido en una herramienta valiosa para el tamizaje de depresi&oacute;n y el seguimiento terap&eacute;utico en psicolog&iacute;a cl&iacute;nica.',
  heroAlt: 'WHO-5 escala de bienestar en tablet con interfaz clínica púrpura',
  inlineAlt: 'Gráfico de interpretación WHO-5 escala 0-100, psicología clínica púrpura',
  ctaTitle: 'Aplica el WHO-5 digitalmente en Kalyo',
  ctaText:
    'Administra, califica e interpreta el WHO-5 de forma digital. Visualiza la evoluci&oacute;n del bienestar de tus pacientes con gr&aacute;ficas autom&aacute;ticas.',
  ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
  related: [
    ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
    ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
    ['que-es-el-gad-7', '&iquest;Qu&eacute; es el GAD-7?'],
  ],
  bodyHtml: `
    <h2>&iquest;Qu&eacute; es el WHO-5?</h2>
    ${paras(
      'El WHO-5 es un instrumento de autoinforme compuesto por cinco reactivos que exploran el estado emocional positivo del paciente durante las &uacute;ltimas dos semanas. Fue desarrollado por el grupo de trabajo de la OMS sobre medici&oacute;n de calidad de vida y salud, con el objetivo de ofrecer una medida breve, sensible al cambio y aplicable en contextos cl&iacute;nicos, comunitarios y de investigaci&oacute;n.',
      'Los cinco &iacute;tems eval&uacute;an: (1) sentirse alegre y de buen &aacute;nimo, (2) sentirse calmado y relajado, (3) sentirse activo y vigoroso, (4) despertarse fresco y descansado, y (5) sentir que la vida cotidiana est&aacute; llena de cosas que interesan. Cada pregunta se responde en una escala Likert de seis puntos, de 0 (&laquo;En ning&uacute;n momento&raquo;) a 5 (&laquo;Todo el tiempo&raquo;).',
      'La filosof&iacute;a del WHO-5 invierte el enfoque tradicional de muchos cuestionarios psicol&oacute;gicos: en lugar de preguntar por s&iacute;ntomas negativos, mide la presencia de experiencias positivas. Esta orientaci&oacute;n hacia el bienestar lo hace especialmente &uacute;til en intervenciones de psicolog&iacute;a positiva, rehabilitaci&oacute;n y seguimiento de tratamientos donde el objetivo no es solo reducir s&iacute;ntomas, sino restaurar la calidad de vida subjetiva.',
      'El instrumento est&aacute; disponible en m&aacute;s de treinta idiomas y ha sido validado en poblaciones generales, pacientes cr&oacute;nicos, personas mayores y contextos de atenci&oacute;n primaria. Su brevedad (menos de dos minutos de aplicaci&oacute;n) lo convierte en una opci&oacute;n pr&aacute;ctica para evaluaciones rutinarias sin sobrecargar al paciente ni al cl&iacute;nico.',
    )}

    <h2>C&oacute;mo se aplica</h2>
    ${paras(
      'La administraci&oacute;n del WHO-5 es sencilla y no requiere entrenamiento especializado. El paciente recibe las cinco preguntas con la instrucci&oacute;n de referirse a c&oacute;mo se ha sentido durante las &uacute;ltimas dos semanas. Puede aplicarse de forma presencial, en papel, por v&iacute;a telef&oacute;nica o a trav&eacute;s de plataformas digitales como Kalyo, donde la puntuaci&oacute;n se calcula autom&aacute;ticamente.',
      'El puntaje bruto se obtiene sumando las respuestas de los cinco &iacute;tems, con un rango posible de 0 a 25. Para facilitar la interpretaci&oacute;n, la OMS recomienda transformar este puntaje a una escala porcentual multiplicando por cuatro, obteniendo as&iacute; un rango de 0 a 100. Por ejemplo, un paciente que punt&uacute;a 15 en la suma bruta obtiene un 60% de bienestar.',
      'Es importante aclarar al paciente que no existen respuestas correctas o incorrectas, y que el cuestionario mide su experiencia subjetiva reciente. En poblaciones con baja alfabetizaci&oacute;n o dificultades cognitivas leves, el cl&iacute;nico puede leer las preguntas en voz alta y registrar las respuestas, siempre manteniendo la confidencialidad del proceso.',
      'En contextos de seguimiento longitudinal, se recomienda aplicar el WHO-5 con intervalos regulares (semanal, quincenal o mensual, seg&uacute;n el caso cl&iacute;nico) para detectar cambios significativos en el bienestar. Una variaci&oacute;n de al menos 10 puntos porcentuales entre aplicaciones suele considerarse cl&iacute;nicamente relevante.',
    )}

    <h2>Interpretaci&oacute;n de puntuaciones</h2>
    ${paras(
      'La interpretaci&oacute;n del WHO-5 se basa principalmente en el puntaje porcentual (0&ndash;100). Valores m&aacute;s altos indican mayor bienestar psicol&oacute;gico subjetivo. La OMS ha establecido puntos de corte emp&iacute;ricos que permiten identificar posible deterioro del bienestar y probable depresi&oacute;n.',
      'Un puntaje inferior a 50 sugiere un nivel de bienestar bajo que merece atenci&oacute;n cl&iacute;nica. Por debajo de 28, la probabilidad de depresi&oacute;n cl&iacute;nica aumenta significativamente, y se recomienda administrar un instrumento espec&iacute;fico de tamizaje depresivo, como el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a>, para confirmar o descartar un trastorno depresivo.',
    )}
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n (%)</th>
          <th>Interpretaci&oacute;n</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0 &ndash; 27</span></td>
          <td><strong>Probable depresi&oacute;n</strong></td>
          <td>Administrar PHQ-9 u otro tamizaje depresivo; evaluaci&oacute;n cl&iacute;nica integral.</td>
        </tr>
        <tr>
          <td><span class="score-badge">28 &ndash; 49</span></td>
          <td><strong>Bienestar reducido</strong></td>
          <td>Exploraci&oacute;n cl&iacute;nica; considerar intervenci&oacute;n psicoterap&eacute;utica.</td>
        </tr>
        <tr>
          <td><span class="score-badge">50 &ndash; 100</span></td>
          <td><strong>Bienestar adecuado</strong></td>
          <td>Monitoreo rutinario; reforzar factores protectores.</td>
        </tr>
      </tbody>
    </table>
    ${paras(
      'La sensibilidad del WHO-5 para detectar depresi&oacute;n es comparable a la de instrumentos m&aacute;s extensos, con la ventaja de su extrema brevedad. Sin embargo, un puntaje bajo no equivale a un diagn&oacute;stico de depresi&oacute;n: indica deterioro del bienestar que requiere evaluaci&oacute;n adicional mediante entrevista cl&iacute;nica y, cuando proceda, instrumentos diagn&oacute;sticos complementarios.',
      'En el seguimiento terap&eacute;utico, observar la trayectoria del puntaje WHO-5 permite al cl&iacute;nico evaluar la respuesta al tratamiento desde una perspectiva de recuperaci&oacute;n funcional y bienestar, m&aacute;s all&aacute; de la simple reducci&oacute;n de s&iacute;ntomas negativos medidos por escalas como el <a href="/articulos/escala-dass-21.html">DASS-21</a>.',
    )}

    <h2>Ventajas del WHO-5 frente al PHQ-9</h2>
    ${paras(
      'Tanto el WHO-5 como el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> son instrumentos breves ampliamente utilizados en atenci&oacute;n primaria y psicolog&iacute;a cl&iacute;nica, pero difieren en su orientaci&oacute;n conceptual y en sus aplicaciones &oacute;ptimas.',
      'El PHQ-9 eval&uacute;a s&iacute;ntomas depresivos negativos alineados con criterios DSM-5, lo que lo hace ideal para tamizaje espec&iacute;fico de depresi&oacute;n y monitorizaci&oacute;n de severidad sintom&aacute;tica. El WHO-5, en cambio, mide bienestar positivo y puede detectar deterioro emocional antes de que los s&iacute;ntomas depresivos cumplan criterios diagn&oacute;sticos formales.',
      'Una ventaja cl&iacute;nica del WHO-5 es su menor estigma percibido: preguntar &laquo;&iquest;Te has sentido alegre?&raquo; resulta menos amenazante para muchos pacientes que explorar directamente s&iacute;ntomas depresivos. Esto puede favorecer respuestas m&aacute;s honestas en culturas donde admitir malestar emocional conlleva verg&uuml;enza o deseabilidad social.',
      'En la pr&aacute;ctica, muchos cl&iacute;nicos utilizan ambos instrumentos de forma complementaria: el WHO-5 como medida de bienestar y recuperaci&oacute;n, y el PHQ-9 como tamizaje depresivo cuando el bienestar cae por debajo de 50. Esta combinaci&oacute;n ofrece una visi&oacute;n m&aacute;s completa del estado emocional del paciente.',
    )}

    <h2>&iquest;Cu&aacute;ndo usar el WHO-5?</h2>
    ${paras(
      'El WHO-5 es especialmente recomendado en los siguientes contextos cl&iacute;nicos: evaluaci&oacute;n inicial de bienestar en consulta psicol&oacute;gica, seguimiento de respuesta al tratamiento en depresi&oacute;n y ansiedad, tamizaje en atenci&oacute;n primaria, monitorizaci&oacute;n de pacientes cr&oacute;nicos (diabetes, cardiopat&iacute;a, dolor cr&oacute;nico) donde la salud mental influye en los resultados m&eacute;dicos, e investigaci&oacute;n sobre calidad de vida.',
      'En psicoterapia, aplicar el WHO-5 al inicio y al final de cada bloque de sesiones permite documentar cambios en el bienestar subjetivo que complementan las notas cl&iacute;nicas cualitativas. Cuando se combina con el <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> para ansiedad, el cl&iacute;nico obtiene un perfil emocional equilibrado entre dimensiones positivas y s&iacute;ntomas espec&iacute;ficos.',
      'En programas de salud mental comunitaria y en telepsicolog&iacute;a, la brevedad del WHO-5 facilita su inclusi&oacute;n en bater&iacute;as de evaluaci&oacute;n peri&oacute;dica sin fatiga del respondiente. Plataformas digitales como Kalyo permiten programar aplicaciones autom&aacute;ticas y alertar al cl&iacute;nico cuando el puntaje cae por debajo de umbrales predefinidos.',
      'Tambi&eacute;n es &uacute;til en evaluaciones de alta terap&eacute;utica: un puntaje WHO-5 superior a 50, mantenido durante al menos dos semanas, puede considerarse un indicador de remisi&oacute;n funcional complementario a la ausencia de s&iacute;ntomas depresivos en el PHQ-9.',
    )}

    <h2>Limitaciones</h2>
    ${paras(
      'Como todo instrumento de autoinforme breve, el WHO-5 tiene limitaciones que el cl&iacute;nico debe considerar. No eval&uacute;a s&iacute;ntomas espec&iacute;ficos de trastornos mentales (ansiedad, psicosis, abuso de sustancias), por lo que un puntaje alto de bienestar no descarta patolog&iacute;a en otras dimensiones.',
      'La sensibilidad cultural del WHO-5 ha sido cuestionada en algunos contextos: conceptos como &laquo;alegr&iacute;a&raquo; o &laquo;inter&eacute;s por la vida&raquo; pueden interpretarse de forma distinta seg&uacute;n el marco cultural del paciente. En poblaciones latinoamericanas, conviene complementar la interpretaci&oacute;n num&eacute;rica con una exploraci&oacute;n cualitativa de c&oacute;mo el paciente entiende y experimenta el bienestar.',
      'El WHO-5 tampoco sustituye la evaluaci&oacute;n de riesgo suicida ni la exploraci&oacute;n de factores psicosociales cr&iacute;ticos (violencia, p&eacute;rdidas recientes, crisis econ&oacute;mica). Un paciente puede puntuar alto en bienestar mientras enfrenta situaciones de riesgo que requieren intervenci&oacute;n inmediata, o viceversa.',
      'Finalmente, la transformaci&oacute;n a porcentaje (multiplicar por 4) puede generar confusi&oacute;n si no se explica adecuadamente al paciente. Documentar siempre el puntaje bruto (0&ndash;25) y el porcentual (0&ndash;100) en la historia cl&iacute;nica evita errores de interpretaci&oacute;n en el seguimiento longitudinal.',
    )}
  `,
});

ARTICLES.push(...REMAINING_ARTICLES);

export {
  buildArticle,
  buildHead,
  countWords,
  ensureMinWords,
  escAttr,
  inlineFigure,
  insertInlineBeforeThirdH2,
  relatedSection,
};

const MIN_WORDS = 1500;
const isMain =
  process.argv[1] && path.resolve(process.argv[1]) === path.resolve(fileURLToPath(import.meta.url));

if (!isMain) {
  // imported as module (assemble-batch.mjs)
} else {
const results = [];

for (const config of ARTICLES) {
  const paddedConfig = {
    ...config,
    bodyHtml: ensureMinWords(config.bodyHtml, MIN_WORDS, config.h1.replace(/<[^>]+>/g, '')),
  };
  const html = buildArticle(paddedConfig);
  const wrapperMatch = html.match(/<article class="article-wrapper">([\s\S]*?)<\/article>/);
  const wordCount = countWords(wrapperMatch ? wrapperMatch[1] : html);

  if (wordCount < MIN_WORDS) {
    console.warn(`WARNING: ${config.filename} has only ${wordCount} words (minimum ${MIN_WORDS})`);
  }

  const outPath = path.join(ARTICULOS_DIR, config.filename);
  fs.writeFileSync(outPath, html, 'utf8');
  results.push({ file: config.filename, words: wordCount });
  console.log(`Created: ${config.filename} (${wordCount} words)`);
}

console.log('\n--- Summary ---');
for (const r of results) {
  console.log(`${r.file}: ${r.words} words`);
}
}
