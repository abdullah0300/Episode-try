# Episode Journal — Next.js replica

This is a runnable Next.js App Router + TypeScript conversion of the Episode Journal site created in this conversation. It preserves the existing visual assets, CSS, page content, URL paths, original/season episode numbering, subtitle guides, provider order and source-based metadata.

## Run locally

Use Node.js 20.9 or newer. From this folder:

```sh
npm ci
npm run dev
```

Open http://localhost:3000. Development uses that origin unless you set `SITE_ORIGIN` in `.env.local`.

## Build for your hosting

Copy `.env.example` to `.env.local` and replace the example with your final HTTPS domain, without a path. Then:

```sh
npm run check:source
npm run build
npm run typecheck
npm start
```

The production build requires `SITE_ORIGIN`. This controls canonical URLs, social-image URLs, publisher/schema identifiers, sitemap and robots. A domain change requires a rebuild; do not deploy previously generated HTML for another domain. Set the environment variable in CI and on your hosting provider too.

This version uses normal Next.js Node hosting. It does not require Supabase, a CMS, a Sites account or any preview-service credentials. It has no database, secrets, streaming backend or notification delivery service. Basic file-upload hosting would require a deliberate static-export configuration and rebuilding for every update.

## What is included

- 20 content routes: 19 canonical pages and the original homepage alias.
- Season landing, drama overview, 10 episode subtitle guides (Episodes 84–88), Urdu/English season hubs, broadcast calendar, numbering/story guides, About and checking policy.
- Custom not-found screen, `/sitemap.xml` and `/robots.txt`.
- Original logo, imagery and locally hosted fonts.
- Server-rendered React page markup; useful content is present without JavaScript.
- Shared header/footer components, original styling and a small client enhancement component.
- Episode search, subtitle filters, mobile menu, FAQ details, countdown and browser-local alert preferences.
- Original source records, static generators, full static reference site and previous SEO audit under `reference/`.
- A Codex continuation brief in `CODEX-HANDOVER.md` and a short ready-to-paste prompt in `CODEX-PROMPT.txt`.

## Code map

| Path | Purpose |
| --- | --- |
| `app/layout.tsx`, `app/globals.css` | Root shell and original design styles |
| `app/page.tsx`, `app/[...slug]/page.tsx` | Homepage and statically generated existing routes |
| `components/pages/` | Converted server-rendered JSX for each original page |
| `components/shell/` | Shared original header/footer |
| `components/SiteInteractions.tsx` | Small browser interactions with cleanup |
| `lib/pages.ts`, `lib/site.ts` | Metadata and final-domain configuration |
| `data/page-metadata.json` | Existing titles, descriptions, canonical paths and JSON-LD |
| `data/episode_content.json`, `data/broadcast_calendar.json` | Structured editorial facts for future shared episode templates |
| `reference/route-manifest.json` | URL-to-original-page/component mapping |
| `reference/original-site/` | Original Python generator, original rendered HTML and earlier audit |

## Content and automation status

This is the **13 October 2026 editorial snapshot**, not a live source feed. Four released season episodes (original 84–87) retain the owner's Verified status. Original 88 remains awaiting release until new evidence confirms otherwise. The passage of the countdown alone never verifies a subtitle upload.

The Urdu-subtitle guides are primarily English-language reading pages with additional Urdu summaries/reading aids. They are not full Urdu translations. No translation `hreflang` is added. The separate URLs represent subtitle intent, and the existing English document language is preserved.

Great Nation is first, followed by Makki TV, Niazi TV and Historical Point. Platform labels/ad comparisons remain owner-supplied. Existing deep links are preserved; no missing episode URL has been invented. Exact subtitle upload timestamps are not fabricated.

The original one-page-per-guide markup has been converted into JSX to preserve the design closely. Codex can next refactor the repeated episode sections into a typed shared template driven by the supplied records. Editing only the JSON content records will not yet regenerate the JSX pages; the conversion preserves the original snapshot and is not an automated publishing system.

## Verification and remaining work

See `VERIFICATION.md` for checks performed on this package. The original HTML and content audit remains available under `reference/original-site/SEO-AUDIT.md`. That audit predates this Next.js conversion and does not certify it.

Browser visual QA, live-host redirects/error statuses, mobile interaction checks, measured Core Web Vitals and search-engine rendering/structured-data tools must be checked on the chosen hosting. Valid markup and metadata do not guarantee indexing, rankings or AI citations.

Series photography remains property of TRT/respective rights holders. Original credit notices are retained. This project is the independent release-date/viewing guide, distinct from Great Nation's streaming platform.
