# Codex handover: Episode Journal

## Goal

Continue this Next.js replica of the site created with ChatGPT. Preserve its visual design and content, then make episode publishing maintainable. Do not redesign it, substitute generic AI cards/shapes, or turn it into the Great Nation streaming platform. The owner wants an elegant, readable release-date and where-to-watch guide that expands from Sultan Muhammad Fateh Season 4 to other seasons and dramas.

## First steps

1. Read `README.md`, `VERIFICATION.md`, this file and `reference/original-site/SEO-AUDIT.md`.
2. Install with `npm ci`, choose the final deployment origin and run the package checks/build.
3. Compare Next.js pages against `reference/original-site/dist/` on desktop and mobile. Check forms, search, subtitle filters, FAQ details and countdown. Browser QA was not available during the export.
4. Refactor the repeated episode JSX into a shared `EpisodeGuide` component driven by typed records from `data/episode_content.json` and `data/broadcast_calendar.json`, preserving the existing ten-part structure and episode-specific information.
5. Preserve current URLs while making future routes derive from drama slug, season, original number and subtitle edition. Do not create placeholder indexable pages for dramas/seasons that have no real content.

The existing JSX pages are real React server-rendered content. They are not client-side fetched HTML or iframe copies. Header/footer are shared; episode content is still generated per page as a faithful migration snapshot. Keep the reference source unchanged for comparison.

## Visual and UX requirements

- Ivory background, forest-green details, DM Serif Display/DM Sans; original Episode Journal logo.
- Preserve layout proportions, cinematic images and restrained motion, with reduced-motion support.
- Readable copy: episode body 17px, supporting text at least 14px; proper, clearly labelled buttons and comfortable action targets.
- Keep mobile single-column flow and prominent release answer/where-to-watch actions.
- Use plain language. Avoid complicated promotional wording, vague labels and unnecessary decorative shapes.
- Identify both numbers: for example **Season 4 Episode 4 · Original Turkish episode 87**. Do not hide the original number or change stable search URLs.

## Episode facts and provider requirements

The records were last editorially reviewed on 13 October 2026. Future work must review new official sources before changing them; a schedule does not prove an episode or subtitles have been released.

| Season 4 episode | Original episode | Editorial broadcast date |
| --- | --- | --- |
| 1 | 84 | 15 September 2026 |
| 2 | 85 | 22 September 2026 |
| 3 | 86 | 29 September 2026 |
| 4 | 87 | 6 October 2026 |
| 5 | 88 | Scheduled for 13 October 2026 |

TRT's series schedule is Tuesday 20:00 Europe/Istanbul. Calendar dates are editorial records; exact historical broadcast-date announcement evidence has not all been archived. Do not claim a TRT page's posting date is automatically its broadcast date.

The owner confirmed the four released episodes and both editions for the listed providers. Preserve **Verified** for 84–87 with publisher verification provenance. Do not relabel them unverified based solely on absence of your own playback test. Do not mark 88 verified just because its scheduled time has passed.

Every episode guide must keep this viewing order:

1. Great Nation — `https://greatnation.webcraftio.com/`, featured first, free/ad-free and notifications according to owner confirmation.
2. Makki TV — `https://makkitv.com/`, includes ads.
3. Niazi TV — `https://play.niazitv.pk/`, includes ads and frequent popups according to the owner.
4. Historical Point — `https://historicalpoint.com/`, includes ads with fewer irritating popups according to the owner.

Use observed links supplied by the original site/data. Improve homepage-only links to real episode links when verified; never guess URL patterns. Preserve TRT as the primary broadcast/synopsis source and Niazi as a secondary synopsis/viewing reference. Write factual summaries in original wording. Do not invent watched recaps, endings or upload timestamps. Remove no source solely because it is another platform; the guide's value includes useful comparisons.

## Shared episode structure

Keep the same template for both subtitle editions, with original episode-specific facts:

1. Episode identity/hero and dual numbering.
2. Direct current release/availability answer.
3. Release details and broadcast facts.
4. Where to watch: Great Nation first, then the three requested alternatives.
5. Spoiler-free episode overview.
6. Source-based plot details, with spoiler labelling.
7. Characters/context and subtitle-edition reading aids.
8. Availability/checking history with accurate provenance.
9. Helpful episode-specific FAQs.
10. Sources, previous/next links, edition switching and notification call to action.

## SEO and GEO requirements

- Use server-rendered useful content and ordinary crawlable links. Keep mostly static pages and native Metadata APIs.
- `SITE_ORIGIN` must drive every canonical, sitemap, social image, schema URL and publisher ID. Fail unsafe production configuration. Rebuild when the final host changes.
- Preserve 19 canonical pages, the intentional homepage alias and real noindex 404 handling. Do not emit duplicate sitemap entries, error URLs or conflicting canonical domains.
- Every valid content page needs a unique accurate title/description, one H1, breadcrumb navigation and consistent visible/schema facts.
- The Urdu/English URLs indicate **subtitle choice**, not full page translation. Do not add `hreflang="ur"` just because a guide discusses Urdu subtitles. Tag actual Urdu fragments with `lang="ur" dir="rtl"`. Introduce reciprocal hreflang only if real translated page variants are added later.
- Schema should retain publisher/WebSite entities, breadcrumbs, applicable WebPage/TVSeries/TVSeason/TVEpisode facts, and an ImageObject for `primaryImageOfPage`.
- `episodeNumber` is the within-season number, with the original number recorded as identifier. Do not expect a TVEpisode schema type to automatically unlock a Google rich result.
- Do not claim hosted playback, full episode video or a playable VideoObject on a guide that links elsewhere.
- FAQs must help visitors; do not promise FAQ rich results. Do not invent ratings, official affiliations or source verifications.
- Use genuine editorial change dates, not a fresh `lastmod`/`dateModified` on every build. Current fixed snapshot date is 2026-10-13; future data should store per-page substantive revision dates.
- Maintain useful distinctions between subtitle editions; shared factual sections are appropriate. Do not fabricate a duplicate-content penalty or a similarity threshold.
- Preserve factual attribution and concise direct answers for search/AI use. No special GEO schema, keyword stuffing or `llms.txt` can guarantee citations.
- Test server HTTP responses, final-domain preferred-host redirects, sitemap availability, canonical metadata and mobile performance after choosing the host. The private preview audience is irrelevant to this exported project and must not be used as a blocker.

## Automation boundary

The local preference form does **not** send email. Do not replace the honest message with a false subscription confirmation. Source monitoring, editorial review, email delivery and a CMS/database are future work, not present features. Do not introduce Supabase or Sanity without the owner's choice.

First complete the typed shared episode model/template, then propose a verified update workflow. Any revalidation endpoint must authenticate publishing requests, validate input and refresh only affected routes. Preserve human verification where factual evidence is missing. Future schema/media ownership checks must use actual observations.

## Acceptance checks

- `npm ci`, `npm run check:source`, `npm run build`, `npm run typecheck` succeed with the intended origin.
- Each of the current 20 content routes renders the expected text without client JavaScript; unknown paths return a genuine 404.
- 19 unique sitemap URLs; homepage and season alias agree; 404 excluded.
- No preview origin remains in deployable metadata; preview-domain occurrences in the archival reference source are allowed.
- Original links/assets/sections/provider order/Urdu fragments/episode numbers remain intact.
- Metadata and JSON-LD parse; schema matches visible facts and accurate status.
- Browser-check desktop and mobile layout, controls, reduced motion, keyboard navigation and countdown expiry.
- Document what remains unmeasured. Do not equate successful builds with measured Core Web Vitals or guaranteed SEO/GEO performance.
