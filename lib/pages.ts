import type { Metadata } from "next";
import snapshot from "@/data/page-metadata.json";
import { siteOrigin } from "./site";
export type PagePath = keyof typeof snapshot;
export const routes = Object.keys(snapshot).filter(p => p !== "/404/") as PagePath[];
export function pageData(path: PagePath) {
  return JSON.parse(JSON.stringify(snapshot[path]).replaceAll("__SITE_ORIGIN__", siteOrigin)) as typeof snapshot[PagePath];
}
export function pageMetadata(path: PagePath): Metadata {
  const p = pageData(path);
  const index = !p.robots.includes("noindex");
  return {
    title: p.title, description: p.description,
    alternates: { canonical: p.canonical },
    robots: { index, follow: true, "max-image-preview": "large" },
    openGraph: { title: p.title, description: p.description, type: "website", url: p.canonical,
      siteName: "Episode Journal", locale: "en_US", images: [{url: p.image, alt: p.title}] },
    twitter: { card: "summary_large_image", title: p.title, description: p.description, images: [p.image] },
  };
}
