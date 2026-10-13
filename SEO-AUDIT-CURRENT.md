# Episode Journal SEO and AI-search audit

Reviewed 14 October 2026 against the current code and local production build. This is an assessment, not a ranking score or certification. No website content was changed during this audit.

## Assessment

The site has a sound technical foundation, but several content and metadata inconsistencies remain. It should not yet be described as having every best practice implemented. The immediate priority is accuracy and synchronization, followed by performance measurement and production-host validation.

## Verified strengths

- All 22 content routes return HTTP 200 locally. An unknown route returns HTTP 404 with noindex. Robots and sitemap return HTTP 200.
- The sitemap includes 21 distinct canonical URLs, excludes the error page and excludes the duplicate homepage alias. The homepage intentionally canonicalizes to the season hub.
- SITE_ORIGIN controls canonical, social-image, sitemap and entity URLs. Current rendered output uses https://episodejournal.webcraftio.com without archival preview domains or unresolved placeholders.
- All 23 rendered documents have one H1. Titles and descriptions are unique across canonical content pages.
- Core content, expected dates and links are in server-rendered HTML. Timers and timezone conversion are browser enhancements.
- The route and render checks pass. No orphan content routes, missing image alt/width/height attributes or local fragment problems were found by the additional audit scan.
- JSON-LD parses and includes publisher, website, breadcrumb, article and episode entities as appropriate. Original episode numbers are separate from within-season episodeNumber; Episode 89 has episodeNumber 6. primaryImageOfPage uses ImageObject. No hosted-playback VideoObject or invented ratings are emitted.
- English-written subtitle guides retain English document language. Urdu fragments use lang=ur and dir=rtl. Subtitle choices are not falsely presented as full translations with hreflang.
- Released guides provide source attribution, language help, episode-specific facts and verification provenance. Upcoming Episode 89 explicitly distinguishes schedule estimates from confirmed publication and does not invent its plot.
- Images have dimensions, offscreen images use lazy loading, local fonts use font-display: swap, and reduced-motion styling is present. These are implementation observations, not measured Core Web Vitals.

## Findings requiring attention

### 1. Subtitle-hub titles are stale

In data/page-metadata.json, both season subtitle hub titles still say Episodes 1–5 while their visible lists include Episode 6. Their descriptions already refer to Episode 6. Update the titles and corresponding schema names together.

### 2. Calendar metadata is stale

The broadcast calendar description still says Episodes 84–88 although the visible page includes expected Episode 89. Update the description and corresponding schema description to cover 84–89 and distinguish expected dates from historical records.

### 3. A viewing link has conflicting episode identity

The English Episode 86 guide and data/episode_content.json use https://makkitv.com/mehmed-fetihler-sultani-episode-8-in-english-subtitles/ as the direct Makki episode link. On this audit date, Makki's heading calls it Episode 86, but its body repeatedly describes Episode 8 and links to TRT Episode 8. This is not a reliable direct Episode 86 destination. Replace it only with an actually verified Episode 86 link; otherwise use a clearly labelled platform link. This finding does not invalidate historical publisher verification of the provider's release.

### 4. Modification dates are not maintained per page

app/sitemap.ts assigns dates by URL pattern rather than a page revision record. Episode 88's guides gained links to Episode 89 on 14 October but retain 13 October lastmod/dateModified. The calendar's sitemap date is 14 October while its schema dateModified remains 13 October. Store genuine substantive modification dates per page and derive sitemap and schema dates from that record. Do not refresh every page's date on each build.

### 5. Performance is unmeasured, with an obvious optimization candidate

The logo is a 410,347-byte PNG at 2172×724 served directly for the small header and footer logo. Supply an appropriately sized optimized version while preserving its appearance; keep an appropriate high-resolution asset for schema where needed. Photography is already WebP, but responsive srcset/sizes delivery is not implemented. Measure representative homepage and episode pages before claiming Core Web Vitals results. No Lighthouse or field performance score was obtained in this audit.

### 6. Source and availability freshness needs an editorial workflow

Episode 88 still reflects the earlier awaiting-release snapshot. The passage of its expected deadline cannot establish availability. Check Great Nation's actual Urdu and English publication separately. Episode 89 is a useful pre-release guide, but its story sections still await official preview material. Add verified information to the same URLs as it becomes available. Avoid cloning previous plot text to fill new pages.

### 7. Supporting numbering content still covers only five episodes

The numbering guide intentionally describes 1–5 versus 84–88. With Episode 6 now on the site, expanding its table and description to include 6/89 would improve consistency and usefulness. This is a content-coverage gap, not proof of an indexing defect.

## AI-search / GEO interpretation

The direct answers, readable HTML, explicit numbering, expected-versus-available distinction, source links and coherent entities are useful foundations. There is no special GEO schema or llms.txt requirement for Google's AI search features. Accurate, helpful information matters more than producing more near-identical pages. Separate subtitle editions should continue to offer practical language-specific help.

No claim is made that valid TVEpisode or FAQ content guarantees a Google rich result, or that this architecture guarantees AI citations. A passing local validator is not a Google Rich Results Test or an independent fact check.

## Remaining production checks

After deployment, verify public DNS/TLS, HTTP-to-HTTPS and preferred-host redirects, trailing-slash consistency, CDN/WAF access for crawlers and required assets, final-domain sitemap/robots/error responses, supported structured-data validation, Search Console/Bing setup, and actual indexing/canonical selection. Field performance requires measurements on the deployed site. These checks were not certified by the local build.

## Primary sources used

- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- Google structured-data policies: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Google sitemap and lastmod guidance: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Direct Makki destination check: https://makkitv.com/mehmed-fetihler-sultani-episode-8-in-english-subtitles/

Recommended repair order: resolve the conflicting viewing link and stale metadata, synchronize genuine revision dates, improve asset delivery, then validate production performance and indexing. Consolidating repeated episode markup and metadata around typed episode records would reduce future drift.


## Repairs completed — 14 October 2026

- All Makki viewing actions now use its homepage, with wording telling readers to select their episode/language there. The conflicting direct Episode 86 link and other Makki deep-link assumptions were removed from current components and records.
- Subtitle-hub titles now cover Episodes 1–6. Calendar metadata covers original Episodes 84–89. Schema names/descriptions agree with metadata.
- Numbering guide includes Episode 6 / original 89 and both guide links; its metadata matches the expanded table.
- Added explicit page-revisions.json records. Modified page schema dates and sitemap lastmod derive consistently from substantive revision dates. Dates do not change on each build.
- Header/footer use a 480×160 lossless WebP logo of 21,646 bytes instead of the 410,347-byte original PNG (about 95% smaller). The original high-resolution schema logo is preserved.
- Added responsive photo variants and srcset/sizes with accurate width descriptors. Image dimensions, alt text and visual content were retained.
- Great Nation's real Episode 5 listing was found and linked on both guides. Its returned playback data was inconsistent (an unverified short stream associated with Teskilat); no playable language-specific release was certified. Guides now explain that the listing exists while playback needs verification.

Production deployment checks, actual performance measurement, Episode 89 official story evidence, and Great Nation playback verification remain external checks. Code repairs do not establish rankings, indexing or Core Web Vitals results.
