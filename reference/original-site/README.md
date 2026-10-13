# Episode Journal — Sultan Fatih

Static responsive editorial design for Sultan Fatih Season 4. Includes a season landing page, 10 subtitle-specific episode guides, Urdu and English subtitle hubs, a drama overview, a numbering guide, an internal broadcast calendar, a spoiler-free editorial guide, and transparency pages. There are 19 canonical content pages, plus a homepage alias and a noindex 404 page.

## Rebuild and verify

Run `python build.py`, `python validate.py`, `python validate_guides.py`, `python validate_seo.py`, and `node --check dist/assets/app.js`.

## Functionality

Episode search, Urdu/English guide filters, second-by-second broadcast countdown, accessible FAQ accordions, mobile navigation and browser-local alert preferences. Email delivery and live subtitle monitoring are not connected. Released Urdu and English viewing options for Episodes 84–87 are publisher-verified as confirmed on 13 October 2026. Broadcast dates are a 13 October 2026 source-reviewed snapshot.

The generated EJ monogram and Episode Journal wordmark are integrated in the header and footer. The landing page focuses on Urdu and English subtitle searches rather than country time cards.

## Released episode guides

Season 4 Episodes 1–4 correspond to original Episodes 84–87. Eight released guides share the same ten-part structure: identity, immediate answer, release details, viewing comparison, spoiler-free overview, source-based plot details, context and characters, availability history, FAQs, and sources/navigation/notification CTA. Episode 88 now uses the same readable page structure with an upcoming status and official preview rather than a released recap. `episode_content.json` contains short original factual summaries and observed listing links; `released_guides.py` renders the common structure with separate Urdu and English viewing instructions and overview copy.

The revised episode design uses a compact image-and-title hero, a direct release answer, three clearly labelled facts, four jump buttons, a featured Great Nation card and readable platform alternatives. Body text is 17px, supporting text is at least 14px on episode pages, and action links are visible buttons with a minimum 48px height. Mobile uses a single-column layout. Breadcrumbs, edition switching, previous/next navigation and sources remain crawlable HTML links. `dist/assets/episode.css` contains the new layout and readability improvements across the wider site. Browser visual QA remains unavailable; static checks do not establish full accessibility conformance.

Current design/SEO guidance reviewed:
- https://developers.google.com/search/docs/appearance/ai-features — visible text, helpful content, internal links and schema matching visible facts.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced — comfortable action targets.

Great Nation is ranked first as requested, followed by Makki TV, Niazi TV and Historical Point. Free access, notifications and comparative ad/popup descriptions are publisher-reported, not independently tested. Direct language-specific links are included only where observed. The publisher confirmed both subtitle languages and the four providers for all four released episodes; the UI displays Verified based on that confirmation, rather than claiming an agent playback test. The publisher verification date is not an inferred upload timestamp. Episode 88 remains upcoming.

Story summaries are cross-checked against TRT’s official synopsis listing and Niazi’s episode articles. These are synopsis-based guides, not complete watched recaps; unresolved endings are not invented. Both subtitle guides remain English-language editorial pages, with no misleading translation hreflang.

Urdu guides additionally include a labelled original Urdu reading summary and Turkish-to-Urdu reading aids. English guides include episode-specific English context and term explanations. These are useful subtitle-intent pages rather than full language translations, so the English HTML language declaration and absence of translation hreflang remain deliberate.

Season episode numbers are now prominent in headings, navigation, platform buttons and the calendar. For example, Season 4 Episode 4 is displayed with original Turkish Episode 87. Search titles and stable URLs retain the original number. The numbering guide maps all five records and explains why dubbed cuts can differ.

## Design references

- https://www.awwwards.com/siena-film-foundation-case-study.html — cinematic typography, image composition and motion serving navigation.
- https://www.awwwards.com/sites/seasoned — editorial typography and restrained layout.

## Content and imagery sources

- https://www.trt1.com.tr/diziler/mehmed-fetihler-sultani
- https://www.trt1.com.tr/diziler/mehmed-fetihler-sultani/bolum
- https://www.trt1.com.tr/diziler/mehmed-fetihler-sultani/ozet/88-bolum-ozet
- https://www.trt1.com.tr/diziler/mehmed-fetihler-sultani/fotogaleri/87-bolum
- https://play.niazitv.pk/drama/82/mehmed-fetihler-sultani-season-4-urdu-english-subtitles
- https://greatnation.webcraftio.com/drama/mehmed-fetihler-sultani/season-4
- https://makkitv.com/
- https://historicalpoint.com/

Official TRT series imagery remains property of its rights holders. Source credits are visible on the site. DM Sans and DM Serif Display are self-hosted font assets obtained from Google Fonts.

## SEO

HTML-rendered primary content and crawlable links, unique page titles and descriptions, canonical metadata, valid JSON-LD, sitemap and robots.txt. `seo.py` provides consistent Organization/WebSite entities, per-page schema, Open Graph and social-card metadata. Supporting pages have specific breadcrumbs and metadata; the drama hub also identifies the TVSeries, and the story guide identifies its Article. Robots permit indexing and large image previews on content pages; the 404 document is marked noindex and excluded from the sitemap. The homepage intentionally shares the season page’s canonical URL.

`validate_seo.py` checks all 19 canonical content pages, unique metadata, publisher entities, linked content, no orphan pages, social tags, numbering, subtitle-specific guidance and sitemap membership. It is a source-contract check, not Google Rich Results Test or an indexing guarantee.

Images have dimensions, episode heroes have priority hints, offscreen images are lazy-loaded, fonts use swap and interaction JavaScript is deferred. Browser control and performance tools are unavailable in the environment; no measured Core Web Vitals result is claimed.

The current publication remains owner-private. Public crawl access requires an explicit audience change. Search Console verification, sitemap submission, public HTTP/404 checks, Google rendering/schema validation and live mobile performance testing must follow public launch. No verification token or analytics account was invented, and the site does not promise rankings or AI citations.

## Verification limit

Browser control was unavailable in the managed environment. Static links, anchor targets, asset existence, heading counts, metadata, JSON-LD, XML and JavaScript syntax were checked. Live browser visual and interaction QA remains outstanding.

## Broadcast calendar and verification provenance

`broadcast_calendar.json` maintains the episode dates and TRT source links. The internal `/dramas/mehmed-fetihler-sultani/season-4/broadcast-dates/` page is generated by `broadcast_guide.py`, linked from every episode guide and included in the sitemap. TRT is the sole external broadcast-information source displayed by the site. TRT’s series page explicitly lists Tuesday 20:00; its episode-page posting timestamps are documented separately from television broadcast dates. Historical episode dates remain the editorial calendar records.

The owner explicitly confirmed verification of the released viewing options on 13 October 2026. `episode_content.json` records publisher verification for Episodes 84–87, both subtitle languages and the four requested providers. Upcoming Episode 88 remains awaiting release, without a fabricated verified status or upload date.

## Build for your own hosting

The preview origin is now centralized in `site_config.py`. Before deploying to another domain, rebuild with your actual final HTTPS origin. Do not upload an old generated dist directory without rebuilding its metadata.

Bash:

```sh
BUILD_TARGET=self-hosted SITE_ORIGIN=https://your-domain.tld python build.py
BUILD_TARGET=self-hosted SITE_ORIGIN=https://your-domain.tld python validate.py
BUILD_TARGET=self-hosted SITE_ORIGIN=https://your-domain.tld python validate_guides.py
BUILD_TARGET=self-hosted SITE_ORIGIN=https://your-domain.tld python validate_seo.py
```

PowerShell:

```powershell
$env:BUILD_TARGET = 'self-hosted'
$env:SITE_ORIGIN = 'https://your-domain.tld'
python build.py
python validate.py
python validate_guides.py
python validate_seo.py
```

Upload the contents of dist to your hosting document root. Configure directory index routes, a real error status for missing URLs, HTTPS and preferred-host redirects on that server. Environment variables must also be present when rebuilding from CI. Main content, sitemap, social metadata and schema use the same configured origin. `SITE_OUTPUT_DIR` can isolate generated output during testing.

The full five-source audit is in `SEO-AUDIT.md`. It assesses the portable project, not preview sharing. Its export test generated and validated all 19 canonical pages on a different example origin, detected no leftover preview-origin references, and checked that unsafe or missing production origin settings fail the build. Main-image WebPage schema now uses ImageObject, and calendar row dates/statuses are derived from the calendar records.

Self-hosted builds do not require the Sites .openai/hosting.json file. It can be omitted from your standalone project; it is only maintained for the preview workflow.
