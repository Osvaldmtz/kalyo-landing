import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import sharp from 'sharp';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const blogDir = path.join(__dirname, '..', 'assets', 'blog');
const THRESHOLD = 0.85;

async function hash8x8(filePath) {
  const { data } = await sharp(filePath)
    .resize(8, 8, { fit: 'fill' })
    .grayscale()
    .raw()
    .toBuffer({ resolveWithObject: true });

  const avg = data.reduce((s, v) => s + v, 0) / data.length;
  let bits = '';
  for (const v of data) {
    bits += v >= avg ? '1' : '0';
  }
  return bits;
}

function similarity(a, b) {
  let same = 0;
  for (let i = 0; i < a.length; i += 1) {
    if (a[i] === b[i]) same += 1;
  }
  return same / a.length;
}

function listImages(suffix) {
  return fs
    .readdirSync(blogDir)
    .filter((f) => f.endsWith(`${suffix}.jpg`))
    .sort()
    .map((f) => ({
      file: f,
      slug: f.replace(`${suffix}.jpg`, ''),
      path: path.join(blogDir, f),
    }));
}

function findDuplicates(images) {
  const pairs = [];
  const flagged = new Set();

  for (let i = 0; i < images.length; i += 1) {
    for (let j = i + 1; j < images.length; j += 1) {
      pairs.push([images[i], images[j]]);
    }
  }

  return pairs;
}

async function analyzeGroup(suffix) {
  const images = listImages(suffix);
  const hashes = new Map();

  for (const img of images) {
    hashes.set(img.slug, await hash8x8(img.path));
  }

  const duplicates = [];
  const flagged = new Set();

  for (let i = 0; i < images.length; i += 1) {
    for (let j = i + 1; j < images.length; j += 1) {
      const a = images[i];
      const b = images[j];
      const sim = similarity(hashes.get(a.slug), hashes.get(b.slug));
      if (sim > THRESHOLD) {
        duplicates.push({
          a: a.slug,
          b: b.slug,
          similarity: Math.round(sim * 1000) / 10,
          regenerate: b.slug,
        });
        flagged.add(b.slug);
      }
    }
  }

  return { suffix, total: images.length, duplicates, flagged: [...flagged].sort() };
}

const hero = await analyzeGroup('-hero');
const inline = await analyzeGroup('-inline');

const report = { threshold: THRESHOLD * 100, hero, inline };
console.log(JSON.stringify(report, null, 2));

const allFlagged = [...new Set([...hero.flagged, ...inline.flagged])].sort();
fs.writeFileSync(
  path.join(__dirname, 'duplicate-images-report.json'),
  JSON.stringify({ ...report, allFlagged }, null, 2),
);

console.log(`\nFlagged slugs (${allFlagged.length}):`, allFlagged.join(', '));
