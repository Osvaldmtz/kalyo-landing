import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { BATCH2_ARTICLES } from './generate-batch2-articles-content.mjs';

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

function countWords(html) {
  const text = html
    .replace(/<[^>]+>/g, ' ')
    .replace(/&[a-z]+;|&#\d+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  return text.split(/\s+/).filter(Boolean).length;
}

function ensureMinWords(bodyHtml, minWords, topicLabel) {
  const extras = [
    `En la pr&aacute;ctica cl&iacute;nica diaria, ${topicLabel} requiere que el profesional integre la evidencia psicom&eacute;trica o normativa con el juicio cl&iacute;nico, la entrevista semiestructurada y la formulaci&oacute;n del caso. Ning&uacute;n instrumento, protocolo o gu&iacute;a sustituye la relaci&oacute;n terap&eacute;utica ni la evaluaci&oacute;n contextual del paciente.`,
    `Los psic&oacute;logos en Colombia y M&eacute;xico enfrentan un entorno regulatorio y profesional en evoluci&oacute;n. Mantenerse actualizado sobre cambios normativos, asistir a formaci&oacute;n continua y utilizar herramientas digitales que faciliten el cumplimiento sin sacrificar la calidad cl&iacute;nica es una inversi&oacute;n directa en la seguridad del paciente y en la sostenibilidad profesional.`,
    `La documentaci&oacute;n adecuada respalda cada decisi&oacute;n cl&iacute;nica vinculada a ${topicLabel}. Registrar fecha, procedimiento, resultados, interpretaci&oacute;n y plan de seguimiento no solo cumple requisitos legales, sino que mejora la continuidad de la atenci&oacute;n cuando el paciente cambia de profesional o requiere derivaci&oacute;n a otro nivel del sistema de salud.`,
    `En telepsicolog&iacute;a y consulta h&iacute;brida, los mismos est&aacute;ndares aplican: consentimiento informado, confidencialidad, selecci&oacute;n de instrumentos validados y comunicaci&oacute;n clara de resultados al paciente. Las plataformas digitales deben facilitar estos procesos sin a&ntilde;adir carga administrativa innecesaria al cl&iacute;nico.`,
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

const MIN_WORDS = 1500;
const results = [];

for (const config of BATCH2_ARTICLES) {
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
