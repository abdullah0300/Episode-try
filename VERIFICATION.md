# Package verification

Checked on 13 October 2026 using Node.js 24.19.0 and npm 11.9.0. The installed dependency versions are pinned by `package-lock.json`: Next.js 16.4.0, React/React DOM 19.3.0.

## Passed

- `npm install --no-audit --no-fund`: dependency installation succeeded and generated the included lockfile.
- `npm run check:source`: 20 content routes, 19 canonical pages, custom not-found source, metadata, episode numbering and asset references passed.
- `SITE_ORIGIN=https://export-check.example npm run build`: production compilation, TypeScript and static page generation succeeded. The test origin is used only for this local build; `.next` is excluded from the ZIP.
- `npm run typecheck`: TypeScript check passed after the production build.
- `python scripts/check-build.py`: all 21 emitted page documents matched the original reference's main text, ordered navigation/provider links and image references. Every page had one H1 and unique element IDs. Titles, descriptions, canonical URLs, Open Graph URL and full JSON-LD graph matched the migrated records.
- Built content pages were indexable; the generated not-found screen included noindex metadata.
- Sitemap contained exactly 19 distinct canonical URLs; the homepage alias did not create a duplicate sitemap entry. Robots referenced the same test origin.
- No preview domain or unresolved origin placeholder remained in deployable rendered page HTML, sitemap or robots. Archival reference files intentionally retain their original preview origin.

The build HTML inspection confirms that core guide content is emitted on the server and does not require client JavaScript. It does not measure search-engine ranking or indexing.

## Not checked here

Browser visual fidelity, hydration/interaction behaviour, keyboard/accessibility conformance, mobile performance and field Core Web Vitals were not measured. Live server HTTP 404/redirect behaviour, final hosting configuration, Google structured-data tools and Search Console submission remain launch checks. The countdown expiry logic was ported into TypeScript but has not been exercised in a browser in this environment.

The replica faithfully retains the editorial snapshot and its known content limitations: some provider links go to homepages, all historical broadcast-date announcement evidence has not been archived, notification delivery is not connected, and episode updates are not yet data-driven publishing.

## Re-run the fidelity check

After setting your final origin and running the production build:

```sh
python scripts/check-build.py
```

Python is optional for normal Next.js development and deployment. This script compares the migration snapshot; update or retire its exact-content expectations deliberately after approved editorial/template changes.
