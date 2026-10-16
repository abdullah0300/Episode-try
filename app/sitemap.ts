import type { MetadataRoute } from "next";
import { routes, pageData } from "@/lib/pages";
import revisions from "@/data/page-revisions.json";
import { publishedPosts, postUrl } from "@/lib/posts";
export default function sitemap(): MetadataRoute.Sitemap {
  const entries = new Map<string, string>();
  for (const path of routes) {
    const url = pageData(path).canonical;
    const revised = revisions[path];
    entries.set(url, revised > (entries.get(url) || "") ? revised : entries.get(url)!);
  }
  for (const post of publishedPosts) entries.set(postUrl(post), post.modifiedAt);
  return [...entries].map(([url, lastModified]) => ({url, lastModified}));
}
