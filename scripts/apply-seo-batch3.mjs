import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ARTICULOS_DIR = path.join(__dirname, '..', 'articulos');

const MONTHS = [
  'enero',
  'febrero',
  'marzo',
  'abril',
  'mayo',
  'junio',
  'julio',
  'agosto',
  'septiembre',
  'octubre',
  'noviembre',
  'diciembre',
];

const AUTHOR_BLOCK = `"author": {
    "@type": "Organization",
    "name": "Equipo Kalyo",
    "url": "https://kalyo.io/sobre-kalyo.html"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Kalyo",
    "url": "https://kalyo.io",
    "logo": {
      "@type": "ImageObject",
      "url": "https://kalyo.io/assets/logo.png"
    }
  }`;

const ARTICLE_DATE_CSS = `    .article-date {
      font-size: 14px;
      color: var(--ink-light);
      margin-bottom: 24px;
      font-weight: 400;
    }`;

const NEW_FOOTER = `  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a> &middot; <a href="/sobre-kalyo.html">Sobre Kalyo</a> &middot; <a href="/contacto.html">Contacto</a></p>
  </footer>`;

function formatSpanishDate(iso) {
  const [year, month, day] = iso.split('-').map(Number);
  return `${day} de ${MONTHS[month - 1]} de ${year}`;
}

function stripHtml(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&[a-z#0-9]+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function countWords(text) {
  const words = text.match(/[\p{L}\p{N}]+/gu);
  return words ? words.length : 0;
}

function readingMinutes(html) {
  const articleMatch = html.match(/<article class="article-wrapper">([\s\S]*?)<\/article>/);
  if (!articleMatch) return 1;
  const words = countWords(stripHtml(articleMatch[1]));
  return Math.max(1, Math.ceil(words / 200));
}

function extractDatePublished(html) {
  const match = html.match(/"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"/);
  return match ? match[1] : '2026-06-21';
}

function updateAuthorSchema(html) {
  return html.replace(
    /"author"\s*:\s*\{[\s\S]*?\},\s*"publisher"\s*:\s*\{[\s\S]*?"url"\s*:\s*"https:\/\/kalyo\.io\/assets\/logo\.png"\s*\}\s*\}/,
    AUTHOR_BLOCK,
  );
}

function addArticleDateCss(html) {
  if (html.includes('.article-date')) return html;
  return html.replace(
    /\.article-meta \{[\s\S]*?\}/,
    (block) => `${block}\n\n${ARTICLE_DATE_CSS}`,
  );
}

function addArticleDate(html) {
  if (html.includes('class="article-date"')) return html;

  const datePublished = extractDatePublished(html);
  const formatted = formatSpanishDate(datePublished);
  const minutes = readingMinutes(html);
  const dateLine = `Publicado el ${formatted} &middot; Lectura: ${minutes} min`;
  const dateHtml = `<p class="article-date">${dateLine}</p>`;

  return html.replace(/(<h1>[\s\S]*?<\/h1>\s*)/, `$1\n    ${dateHtml}\n\n    `);
}

function updateFooter(html) {
  return html.replace(
    /<footer class="footer">[\s\S]*?<\/footer>/,
    NEW_FOOTER,
  );
}

const files = fs
  .readdirSync(ARTICULOS_DIR)
  .filter((f) => f.endsWith('.html') && f !== 'index.html');

let updated = 0;
for (const file of files) {
  const filePath = path.join(ARTICULOS_DIR, file);
  let html = fs.readFileSync(filePath, 'utf8');
  const original = html;

  html = updateAuthorSchema(html);
  html = addArticleDateCss(html);
  html = addArticleDate(html);
  html = updateFooter(html);

  if (html !== original) {
    fs.writeFileSync(filePath, html);
    updated++;
    console.log(`Updated ${file}`);
  }
}

console.log(`Done. ${updated} articles updated.`);
