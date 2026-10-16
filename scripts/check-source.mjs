import { readFileSync, existsSync } from "node:fs";
import assert from "node:assert/strict";
const data = JSON.parse(readFileSync("data/page-metadata.json", "utf8"));
const manifest = JSON.parse(readFileSync("data/route-manifest.json", "utf8"));
const canonicals = new Set();
for (const page of manifest) {
  assert(existsSync(page.component), page.component);
  const content = readFileSync(page.component, "utf8");
  assert.equal((content.match(/<h1[ >]/g) || []).length, 1, page.path);
  assert(!content.includes("dangerouslySetInnerHTML"), page.path);
  const meta = data[page.path];
  assert(meta.title && meta.description && meta.canonical && meta.image && meta.graph.length, page.path);
  assert(!JSON.stringify(meta).includes("chatgpt.site"), page.path);
  if (page.path !== "/404/") canonicals.add(meta.canonical);
  for (const [, asset] of content.matchAll(/(?:src|href)=\{"(\/assets\/[^"{}]+)"\}/g)) {
    assert(existsSync("public" + asset), asset);
  }
}
assert.equal(Object.keys(data).length, manifest.length);
assert.equal(canonicals.size, new Set(manifest.filter(p => p.path !== "/404/").map(p => p.canonical)).size);
for (let n = 84; n <= 89; n++) {
  for (const language of ["urdu", "english"]) {
    const path = `/dramas/mehmed-fetihler-sultani/episodes/${n}/${language}-subtitles/`;
    assert(data[path]);
    assert(data[path].title.includes(`S4 Ep ${n - 83}`));
  }
}
console.log("PASS: 23 routes, 22 canonical pages, custom 404, metadata, numbering, asset references.");

const posts = JSON.parse(readFileSync("content/posts.json", "utf8"));
const slugs = new Set();
const articleParagraphs = new Set();
const layouts = new Set();
for (const post of posts) {
 assert(!slugs.has(post.slug)); slugs.add(post.slug);
 assert(post.title && post.answer && post.sources.length && post.author);
 assert(existsSync("public" + post.image));
 const ids = new Set(post.sections.map(s => s.id));
 assert.equal(ids.size, post.sections.length);
 for (const section of post.sections) for (const id of section.sourceIds) assert(post.sources[id]);
 for (const slug of post.related) assert(posts.some(p => p.slug === slug && p.status === "published"));
 const bodyWords = [post.answer, ...post.sections.flatMap(s => s.paragraphs)].join(" ").trim().split(/\s+/).length;
 assert(bodyWords >= 2500, `${post.slug}: only ${bodyWords} body words`);
 assert(!layouts.has(post.layout), `${post.slug}: repeated article treatment`); layouts.add(post.layout);
 assert(post.fieldGuide.cards.length === 3);
 for (const section of post.sections) for (const paragraph of section.paragraphs) {
   const normalized = paragraph.toLowerCase().replace(/\s+/g, " ").trim();
   assert(!articleParagraphs.has(normalized), `${post.slug}: repeated body paragraph`);
   articleParagraphs.add(normalized);
 }
}
console.log(`PASS: ${posts.filter(p => p.status === "published").length} published articles, sources, unique slugs, images and related links.`);
console.log("PASS: each article has at least 2,500 body words, a distinct layout and no reused body paragraphs.");
