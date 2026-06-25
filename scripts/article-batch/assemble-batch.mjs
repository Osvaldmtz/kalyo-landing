import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { buildArticle, countWords, ensureMinWords } from '../generate-new-articles.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '../..');
const OUTPUT_DIR = path.join(__dirname, 'output');
const ARTICULOS_DIR = path.join(ROOT, 'articulos');
const TOPICS_PATH = path.join(__dirname, 'topics-batch3.json');
const MIN_WORDS = 1500;

const FALLBACK_RELATED = [
  ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
  ['como-interpretar-tests-psicologicos', 'C&oacute;mo interpretar tests psicol&oacute;gicos'],
  ['tests-psicologicos-digitales', 'Tests psicol&oacute;gicos digitales'],
];

function p(text) {
  return `<p>\n      ${text}\n    </p>`;
}

function sectionsToBody(sections, faq) {
  let html = sections
    .map((section) => {
      const paragraphs = section.paragraphs.map((para) => p(para)).join('\n\n    ');
      return `<h2>${section.title}</h2>\n    ${paragraphs}`;
    })
    .join('\n\n    ');

  if (faq?.length) {
    html += `\n\n    <h2>Preguntas frecuentes</h2>\n    `;
    html += faq.map((item) => `<h3>${item.q}</h3>\n    ${p(item.a)}`).join('\n\n    ');
  }

  return html;
}

function resolveRelated(relatedSlugs) {
  const related = [];
  for (const slug of relatedSlugs || []) {
    const filePath = path.join(ARTICULOS_DIR, `${slug}.html`);
    if (!fs.existsSync(filePath)) continue;
    const html = fs.readFileSync(filePath, 'utf8');
    const h1 = html.match(/<h1>([^<]+)<\/h1>/)?.[1] || slug;
    related.push([slug, h1]);
    if (related.length >= 3) break;
  }
  return related.length ? related : FALLBACK_RELATED;
}

function jsonToConfig(article, topics) {
  const topic = topics.find((t) => t.slug === article.slug);
  const bodyHtml = sectionsToBody(article.sections, article.faq);

  return {
    slug: article.slug,
    filename: `${article.slug}.html`,
    title: article.title,
    description: article.description,
    keywords: article.keywords,
    metaLabel: 'Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026',
    h1: article.h1,
    intro: article.intro,
    heroAlt: article.heroAlt,
    inlineAlt: article.inlineAlt,
    ctaTitle: article.ctaTitle || 'Aplica el test en Kalyo',
    ctaText: `Administra, califica e interpreta ${topic?.primary_keyword || 'este instrumento'} de forma digital en Kalyo.`,
    ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
    related: resolveRelated(article.related_slugs),
    bodyHtml,
  };
}

function parseArgs(argv) {
  let slug = null;
  let limit = Infinity;
  let offset = 0;
  for (let i = 0; i < argv.length; i += 1) {
    if (argv[i] === '--limit') {
      limit = parseInt(argv[i + 1], 10);
      i += 1;
    } else if (argv[i] === '--offset') {
      offset = parseInt(argv[i + 1], 10);
      i += 1;
    } else if (!argv[i].startsWith('--')) {
      slug = argv[i];
    }
  }
  return { slug, limit, offset };
}

const { slug: slugFilter, limit, offset } = parseArgs(process.argv.slice(2));
const topics = JSON.parse(fs.readFileSync(TOPICS_PATH, 'utf8')).topics;

let jsonFiles = fs
  .readdirSync(OUTPUT_DIR)
  .filter((file) => file.endsWith('.json') && file !== 'keyword-scores.json')
  .sort();

if (slugFilter) {
  jsonFiles = jsonFiles.filter((file) => file === `${slugFilter}.json`);
}
jsonFiles = jsonFiles.slice(offset, offset + limit);

if (!jsonFiles.length) {
  console.error('ERROR: no article JSON files found in output/');
  process.exit(1);
}

for (const file of jsonFiles) {
  const article = JSON.parse(fs.readFileSync(path.join(OUTPUT_DIR, file), 'utf8'));
  const config = jsonToConfig(article, topics);
  const paddedConfig = {
    ...config,
    bodyHtml: ensureMinWords(config.bodyHtml, MIN_WORDS, config.h1.replace(/<[^>]+>/g, '')),
  };
  const html = buildArticle(paddedConfig);
  const wrapperMatch = html.match(/<article class="article-wrapper">([\s\S]*?)<\/article>/);
  const wordCount = countWords(wrapperMatch ? wrapperMatch[1] : html);
  const outPath = path.join(ARTICULOS_DIR, config.filename);
  fs.writeFileSync(outPath, html, 'utf8');
  console.log(`Assembled: ${config.filename} (${wordCount} words)`);
}
