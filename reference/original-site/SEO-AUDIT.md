# SEO and AI-search audit — 13 October 2026

Scope: the exported static project and its generated content, intended for the publisher’s own hosting. Preview access settings are excluded from this assessment. Checked 21 HTML files representing 19 canonical content pages, one homepage alias and one noindex error document. This audit does not promise indexing, rankings, rich results or AI citations.

## Five authoritative source groups

1. Google Search Central: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [AI features](https://developers.google.com/search/docs/appearance/ai-features), [canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions), [structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) and [helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
2. Microsoft Bing: [duplicate content and AI-search visibility](https://blogs.bing.com/webmaster/2025/12/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility/), written by Microsoft Bing product managers; the official webmaster guidelines were also retrieved through search indexing because the live help page renders a JavaScript-only shell.
3. OpenAI: [official crawler documentation](https://developers.openai.com/api/docs/bots), distinguishing OAI-SearchBot from GPTBot.
4. Schema.org: [TVEpisode](https://schema.org/TVEpisode), [episodeNumber](https://schema.org/episodeNumber) and [primaryImageOfPage](https://schema.org/primaryImageOfPage).
5. Google web.dev: [Web Vitals](https://web.dev/articles/vitals), covering LCP, INP and CLS measurement.

These are primary documentation sources, not independent SEO-agency opinions. Google Search Central and web.dev are both Google resources; the five source groups are not five independent organizations.

## Corrected code defects

### Final-domain configuration

The earlier code hardcoded the preview domain in several modules. Uploading the old generated output unchanged to a different domain would retain canonical, sitemap, social and entity references to the old origin. This was a real export defect missed by earlier source checks, which only validated the preview origin.

`site_config.py` now owns the origin. `SITE_ORIGIN` sets the final HTTPS domain. `BUILD_TARGET=self-hosted` rejects a missing domain, a non-HTTPS origin, a URL containing a path/query/credentials and reuse of the preview origin. All metadata, sitemap URLs, robots sitemap references and structured-data entities use the same origin. The final site must be rebuilt before uploading; copying the old dist folder unchanged is not the corrected deployment workflow.

An isolated export to a reserved example domain passed all three validators. Its HTML, sitemap and robots file contained no preview-domain references. Missing and invalid production-origin tests failed as intended. A second standalone project build also passed without the Sites hosting manifest. Temporary exports were removed after the checks.

### Main image schema

Episode WebPage nodes previously supplied a URL string for `primaryImageOfPage`. Its documented range is ImageObject. The nodes now provide explicit ImageObject values with url and contentUrl. Article image URLs are a separate field and remain supported URL values. This is a semantic schema correction, not a ranking guarantee.

### Calendar presentation consistency

Season-table displayed dates and upcoming flags are now derived from the calendar record rather than retaining an independently hardcoded display date. Exact historical dates and publisher verification records were not changed or newly independently certified.

## Requirement review

| Area | Finding |
|---|---|
| Crawlable HTML | Primary facts, story content, FAQs and navigation are in generated HTML; JavaScript is used for enhancement rather than fetching essential content. |
| Page intent | Drama overview, season hub, subtitle hubs, individual guides, calendar and numbering guide have distinct purposes. |
| Episode numbering | Season 4 Episode 4 and original Episode 87 are displayed together. TVEpisode episodeNumber records the season position; identifier retains the original broadcast number. Existing URLs remain stable. |
| Titles/descriptions | Unique across the 19 canonical pages. They identify the series, episode or guide purpose and subtitle edition without an unnecessary keyword meta tag. |
| Canonicals | Absolute URLs in the head; edition guides remain self-canonical. The homepage is an intentional alias of the season hub, not a second page intended for indexing. Final-origin export is tested. |
| Sitemap | Lists the canonical content URLs, excludes the 404 document and duplicate homepage alias, and uses the configured domain. |
| Internal discovery | Important pages are linked using ordinary a/href links. Source checks find no missing local links, anchors or orphan content pages. |
| Metadata/schema agreement | Episode numbers, title, subtitle intent and dates are represented visibly. Organization, WebSite, WebPage/CollectionPage, Article, TVSeries/TVEpisode and breadcrumbs match their purposes. No invented playback VideoObject or review rating is emitted. |
| Language treatment | Main editorial text is English. Urdu passages are individually marked lang=ur and dir=rtl. A subtitle edition is not automatically a page-language translation, so no misleading ur/en hreflang pair is emitted. |
| Edition similarity | Both pages cover the same episode, so overlapping facts and template text are expected. Distinct provider entries, reading notes and language help are useful. No official percentage establishes when similarity causes a ranking or indexing problem. Monitor canonical selection after launch and strengthen practical edition-specific information where possible. |
| Source transparency | TRT is the main broadcast/story source; Niazi supplies secondary story information and viewing links. Publisher verification is labelled. Story guides explicitly distinguish published synopsis details from a complete watched recap. |
| Broadcast-date evidence | Calendar records include dates and official episode links, but lack episode-specific archived announcement evidence proving every exact original airdate. This is an evidence gap, not proof the dates are false. An internal calendar is not independent confirmation of itself. |
| Date freshness | Current schema and lastmod dates match the 13 October editorial snapshot. Future substantive updates need accurate record dates; a new build or deployment alone must not create false freshness. |
| AI crawler policy | The wildcard Allow rule does not block search crawlers. Production CDN/WAF rules still need checking. OAI-SearchBot is the ChatGPT search crawler; GPTBot training permission is a separate choice. |
| Performance foundations | All images have dimensions; offscreen images are lazy-loaded, fonts use swap and JavaScript is deferred. These are helpful implementation choices, not measured Core Web Vitals results. |
| Performance optimization | The transparent logo is about 410 KB at 2172×724 while displayed much smaller. It is a reasonable image-optimization candidate; its presence alone does not prove poor performance. |
| External viewing links | Great Nation and Niazi have episode-specific links for the released editions. Some Makki/Historical entries still lead to platform homepages. Complete deep links would improve usefulness where available; no unknown episode URL was fabricated. |
| Error pages | The 404 document is noindex and excluded from the sitemap. Only the production server can establish actual HTTP 404 responses for missing URLs. |
| Author/publisher | Episode Journal and Webcraftio are identified; author and publisher entities are consistent. This is transparency, not an automatic authority score. |

## Corrections to earlier review language

An English-written page about Urdu subtitles is not inherently incorrectly configured. Full Urdu localization is a product/editorial choice. If full translations are introduced later, their language declarations and reciprocal hreflang annotations should match the actual page content.

The approximate 80–88% pair-text similarity measured earlier was an internal diagnostic, not a Google/Bing threshold or evidence of a penalty. Different subtitle intents can justify separate pages when the distinctions are useful. Template similarity alone does not prove a problem.

Google’s AI search does not require a special GEO schema or AI text file. That statement describes Google’s documented requirements, not every conceivable AI service. OpenAI documents search crawler access rather than a guaranteed method for obtaining citations. IndexNow is useful for notifying participating engines of changes; it is not an indexing or ranking guarantee and is not a Google submission mechanism.

## Checks required on the publisher’s hosting

- Rebuild with the final domain and upload the contents of the resulting dist directory.
- Verify successful 200 responses for real content, robots and sitemap; actual 404/410 for missing/removed content; and working 301/308 consolidation where variants are intentionally redirected.
- Decide on HTTPS, www/non-www and trailing-slash policy; ensure redirects, internal links, canonical URLs and sitemap agree.
- Do not apply a catch-all SPA rewrite that turns unknown routes into 200 homepage copies.
- Inspect the rendered HTML and crawler access after deploying. Validate supported rich-result types in Google’s Rich Results Test and vocabulary semantics in Schema.org Validator. Neither establishes factual accuracy by itself.
- Check CDN/WAF treatment of Googlebot, Bingbot and OAI-SearchBot and permit required assets to load.
- Measure performance on representative mobile and desktop pages. Good field targets are LCP ≤2.5 s, INP ≤200 ms and CLS ≤0.1 at the 75th percentile. Lab tests are diagnostics; initial sites may not yet have sufficient field data.
- Verify the final domain in Search Console and Bing Webmaster Tools, submit the sitemap and monitor indexing/canonical selection. Add IndexNow if useful for ongoing episode updates.
- Maintain publisher verification, broadcast evidence and content dates as episode facts change. Do not mark a subtitled release available merely because a scheduled broadcast time has passed.

Conclusion: the architecture is reasonable, and the two discovered portable/schema defects have been corrected. The export requires an explicit final-domain build. Editorial source evidence and production-host behavior remain separate matters that static validators cannot certify. No source supports promising that this setup will earn rankings or AI citations.
