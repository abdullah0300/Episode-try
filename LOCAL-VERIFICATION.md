# Local build verification — 13 October 2026

Project location: `D:\Webcraftio\Episode try`.
Production origin: `https://episodejournal.webcraftio.com`, configured in ignored `.env.local`.

The supplied Episode Journal project was installed directly in this folder. Its page content, CSS, imagery, fonts, metadata, provider ordering and editorial snapshot were preserved.

## Passed

- `npm ci --no-audit --no-fund`.
- `npm run check:source`: 20 content routes and 19 canonical pages.
- `npm run build` with the production origin.
- `npm run typecheck`.
- `python scripts/check-build.py`: all 21 rendered documents match the archival reference's main text, ordered links and image references. Metadata and JSON-LD match the supplied records; sitemap contains 19 distinct canonical URLs and robots references the correct domain.
- Local production HTTP checks: all 20 content routes return 200; an unknown route returns 404 with noindex; robots and sitemap return 200; `/about` redirects to `/about/` with HTTP 308.
- Browser inspection of homepage and an Urdu episode guide at desktop and mobile widths. The checked mobile episode page has no document-level horizontal overflow and all its images load.
- Mobile menu opening and closing; episode search by original number; empty search results; subtitle filtering; local preference save and honest email-delivery message.
- Countdown expiry shows zero and a passed-schedule message without changing episode release status.
- No browser warning/error logs were reported during the checked production episode-page visit.

## Local compatibility fixes

- Set `turbopack.root` to the project directory so the parent folder's unrelated lockfile is not selected.
- Make the Python fidelity checker read files as UTF-8, including Urdu content, on Windows.

## Use

Run `npm run dev -- --port 3107` for development.
Run `npm run build` followed by `npm run start -- --port 3108` for a production preview.
Set the same `SITE_ORIGIN` environment variable on the deployment host and build there.

## Remaining limits

The site has not been deployed. Public DNS, TLS, preferred-host redirects, CDN crawler access, Search Console, indexing and field Core Web Vitals remain production checks. Browser inspection is representative, not a pixel-by-pixel comparison of every route or a full accessibility audit. No ranking or AI-citation outcome is guaranteed. Email delivery and automated editorial publishing are not connected.

SEO and AI-search work retains crawlable server-rendered content, direct answers, useful source attribution and accurate structured data. Google's guidance continues to emphasize the same foundational SEO practices for AI features: https://developers.google.com/search/docs/appearance/ai-features .

## Subtitle countdown update

Added separate Urdu and English expected-release timers on the homepage, season page, subtitle hubs and upcoming Episode 88 guides. Both target Wednesday, 14 October 2026 at 12:00 noon PKT, derived from the episode broadcast calendar. The wording says "expected by" and does not mention a Makki TV conversation. Expiry does not verify availability. Upcoming guide FAQs, descriptions and titles now include release-date intent; the expected date remains readable without JavaScript. Existing canonical paths and episode broadcast facts are preserved.

The fidelity checker now explicitly allows the approved timer sections and FAQ edits while checking every timer's language/deadline and retaining original link/image/schema validation. Previously documented full text equality applies to the original build; the updated check compares the remaining text after these approved additions.

## Episode 6 update — 14 October 2026

Published local pre-release guides for Season 4 Episode 6 / original Episode 89 in both subtitle editions. Homepage and season feature now show Episode 6, with expected Turkish broadcast on 20 October at 20:00 Turkey time and separate subtitle deadlines on 21 October at noon UTC+5, displayed in each visitor's local timezone. These are weekly schedule estimates, not independently confirmed episode-specific announcements.

TRT's official series page was checked and shows Tuesday 20:00. No Episode 89 synopsis was verified, so its guides contain honest pending-preview sections, numbering/language help, previous-episode context, provider options, FAQs and sources. Existing TRT series photography is labelled as a series illustration, not Episode 89 artwork. No provider episode URL or release confirmation was invented. Episode 5 availability was preserved.

Added Episode 6 links to the subtitle hubs, broadcast calendar and Episode 5 navigation. There are now 22 content routes and 21 unique canonical sitemap URLs. Current route inventory is in data/route-manifest.json; the archival reference remains unchanged. New metadata uses unique titles/descriptions, original number 89, within-season episodeNumber 6, and genuine 14 October page publication dates.

Source, production build, TypeScript and updated rendered-output checks passed. All 22 local production content routes returned HTTP 200; missing routes returned 404. Browser verification confirmed both homepage subtitle timers and the new Urdu guide, with no captured console errors. Publishing automation is not included.

## Episode 5 release confirmation — 14 October 2026

The publisher confirmed both Urdu and English editions of Season 4 Episode 5 / original Episode 88 released on Great Nation, Makki TV, Niazi TV and Historical Point. Both guides, platform statuses, FAQs, availability history, homepage rows, subtitle hubs, calendar and metadata were updated. Confirmation is publisher-supplied; no assistant playback test or exact upload timestamp is claimed. Episode 5 countdowns were removed. Episode 6 remains featured and upcoming. Source, production build and rendered-output validation passed.

## Episode 6 researched preview — 14 October 2026

TRT now lists its official Episode 89 trailer. DiziKonusu coverage and DiziFragman's published transcript were read and cross-checked for the eastern confrontation, Bayezid's frontier order and reports of a fortress raid. The transcript warns of errors, so precise disputed fortress spelling and final battle outcomes are not asserted. Niazi's current Episode 88 Urdu guide was read for previous-episode context; no Episode 89 Niazi listing was verified.

Both Episode 89 editions now contain original, distinct summaries, language-specific reading help, cast/character context, terminology and an episode-specific FAQ. Story details are clearly labelled as trailer reports, not a full watched recap. Source links and Article citations are updated. Build, source and rendered-output validation passed.

## Episode 5 story research — 14 October 2026

Read TRT's official Episode 88 synopsis (including its embedded page content) and both language-specific Niazi listings, IDs 40941 and 40942. Updated both guides with distinct original summaries, sourced story developments, character context, language aids and a new episode-specific FAQ. Added observed Niazi viewing links in the correct editions. SEO descriptions and Article citations match the revised content. No copied dialogue, final-scene claim or complete watched recap was added. Build, source and rendered-output validation passed.
