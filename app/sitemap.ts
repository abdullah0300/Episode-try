import type { MetadataRoute } from "next";
import { routes, pageData } from "@/lib/pages";
import revisions from "@/data/page-revisions.json";
export default function sitemap(): MetadataRoute.Sitemap {
  const entries = new Map<string, string>();
  for (const path of routes) {
    const url = pageData(path).canonical;
    const revised = revisions[path];
    entries.set(url, revised > (entries.get(url) || "") ? revised : entries.get(url)!);
  }
  return [...entries].map(([url, lastModified]) => ({url, lastModified}));
}
