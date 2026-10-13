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
assert.equal(Object.keys(data).length, 23);
assert.equal(canonicals.size, 21);
for (let n = 84; n <= 89; n++) {
  for (const language of ["urdu", "english"]) {
    const path = `/dramas/mehmed-fetihler-sultani/episodes/${n}/${language}-subtitles/`;
    assert(data[path]);
    assert(data[path].title.includes(`S4 Ep ${n - 83}`));
  }
}
console.log("PASS: 22 routes, 21 canonical pages, custom 404, metadata, numbering, asset references.");
