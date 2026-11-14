import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const ARTICULOS_DIR = path.join(ROOT, 'articulos');
const OUT = path.join(ROOT, 'sitemap.xml');

const TODAY = new Date().toISOString().slice(0, 10);

/** Dirs that exist but should not be submitted for indexing. */
const LANDING_EXCLUDES = new Set([
  'embajadores', // robots.txt disallow + redirects home
  'precios', // soft stub → precios-software-psicologos
  'demo',
  'about',
  'privacy',
  'terms',
  'kalyo-psicologos-mockup',
]);

const HIGH_PRIORITY_LANDINGS = new Set([
  'articulos',
  'plataforma-psicologos-mexico',
  'plataforma-psicologos-colombia',
  'expediente-clinico-psicologico',
  'agenda-whatsapp-psicologos',
  'heiko-vs-kalyo',
  'terapia-online-vs-kalyo',
  'software-rips-psicologos-colombia',
  'tests-psicologicos-digitales',
  'precios-software-psicologos',
]);

function urlEntry({ loc, priority, changefreq }) {
  return `  <url>
    <loc>${loc}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
}

function discoverLandings() {
  return fs
    .readdirSync(ROOT, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .filter((name) => !name.startsWith('.') && !LANDING_EXCLUDES.has(name))
    .filter((name) => fs.existsSync(path.join(ROOT, name, 'index.html')))
    .sort();
}

const STATIC_PAGES = [
  { loc: 'https://kalyo.io/', priority: '1.0', changefreq: 'weekly' },
  ...discoverLandings().map((name) => ({
    loc: `https://kalyo.io/${name}/`,
    priority: HIGH_PRIORITY_LANDINGS.has(name) ? '0.9' : '0.8',
    changefreq: 'weekly',
  })),
  { loc: 'https://kalyo.io/sobre-kalyo.html', priority: '0.7', changefreq: 'monthly' },
  { loc: 'https://kalyo.io/contacto.html', priority: '0.6', changefreq: 'monthly' },
];

/** Legacy URLs that 308 to newer pages — keep out of sitemap. */
const SITEMAP_EXCLUDES = new Set([
  'alternativas-a-doctoralia-para-psicologos.html',
  'mejor-software-para-psicologos-clinicos.html',
  'teleconsulta-para-psicologos-latinoamerica.html',
  'como-reducir-inasistencias-consulta-psicologica.html',
  'c-ssrs-escala-columbia-suicidio.html',
  'escala-pcl-5-estres-postraumatico.html',
  'cage-alcoholismo-test.html',
  'que-es-el-phq-9.html',
  'dast-10-deteccion-drogas.html',
  'que-es-el-gad-7.html',
  'who-5-bienestar-psicologico.html',
  'evaluacion-psicologica-clinica.html',
  'test-defensas-psicologicas.html',
  'trastorno-bipolar.html',
  'terapia-cognitivo-conductual.html',
  'ghq-12-salud-general.html',
  'resiliencia-cd-risk.html',
  'riasec.html',
  'test-riasec.html',
  'nom-004-mexico.html',
  'abrir-consulta-privada-mexico.html',
  'escala-yale-brown-toc.html',
  'trastornos-alimentarios.html',
]);

const articles = fs
  .readdirSync(ARTICULOS_DIR)
  .filter((f) => f.endsWith('.html') && f !== 'index.html' && !SITEMAP_EXCLUDES.has(f))
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
console.log(
  `sitemap.xml: ${STATIC_PAGES.length} static + ${articles.length} articles = ${STATIC_PAGES.length + articles.length} URLs`,
);
