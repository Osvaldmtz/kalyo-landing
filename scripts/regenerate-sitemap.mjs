import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const ARTICULOS_DIR = path.join(ROOT, 'articulos');
const OUT = path.join(ROOT, 'sitemap.xml');

const TODAY = new Date().toISOString().slice(0, 10);

const STATIC_PAGES = [
  { loc: 'https://kalyo.io/', priority: '1.0', changefreq: 'weekly' },
  { loc: 'https://kalyo.io/articulos/', priority: '0.9', changefreq: 'weekly' },
  { loc: 'https://kalyo.io/embajadores/', priority: '0.5', changefreq: 'monthly' },
  { loc: 'https://kalyo.io/sobre-kalyo.html', priority: '0.7', changefreq: 'monthly' },
  { loc: 'https://kalyo.io/contacto.html', priority: '0.6', changefreq: 'monthly' },
];

function urlEntry({ loc, priority, changefreq }) {
  return `  <url>
    <loc>${loc}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
}

const articles = fs
  .readdirSync(ARTICULOS_DIR)
  .filter((f) => f.endsWith('.html') && f !== 'index.html')
  .sort();

const articleEntries = articles.map((f) =>
  urlEntry({
    loc: `https://kalyo.io/articulos/${f}`,
    priority: '0.8',
    changefreq: 'monthly',
  }),
);

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${STATIC_PAGES.map(urlEntry).join('\n')}
${articleEntries.join('\n')}
</urlset>
`;

fs.writeFileSync(OUT, xml, 'utf8');
console.log(`sitemap.xml: ${STATIC_PAGES.length} static + ${articles.length} articles = ${STATIC_PAGES.length + articles.length} URLs`);
