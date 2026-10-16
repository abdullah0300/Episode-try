import records from "@/content/posts.json";
import { siteOrigin } from "./site";
import type { Metadata } from "next";

export type Post = typeof records[number];
export const publishedPosts = records.filter(post => post.status === "published");
export function getPost(slug: string) { return publishedPosts.find(post => post.slug === slug); }
export function postUrl(post: Post) { return `${siteOrigin}/blog/${post.slug}/`; }
export function postWordCount(post: Post) {
  return [post.answer, ...post.sections.flatMap(section => section.paragraphs)].join(" ").trim().split(/\s+/).length;
}
export function postReadingMinutes(post: Post) { return Math.ceil(postWordCount(post) / 220); }
export function postMetadata(post: Post): Metadata {
  return {title: `${post.title} | Episode Journal`, description: post.description,
    alternates: {canonical: postUrl(post)}, robots: {index: true, follow: true, "max-image-preview": "large"},
    openGraph: {type: "article", title: post.title, description: post.description, url: postUrl(post), siteName: "Episode Journal", locale: "en_US", publishedTime: post.publishedAt, modifiedTime: post.modifiedAt, authors: [`${siteOrigin}/about/`], images: [{url: siteOrigin + post.image, width: 1280, height: 720, alt: post.imageAlt}]},
    twitter: {card: "summary_large_image", title: post.title, description: post.description, images: [siteOrigin + post.image]}};
}
export function postGraph(post: Post) {
  const url = postUrl(post);
  return [{"@context": "https://schema.org", "@type": "BlogPosting", "@id": url + "#article", url, headline: post.title, description: post.description,
    datePublished: post.publishedAt, dateModified: post.modifiedAt, inLanguage: "en", image: {"@type": "ImageObject", url: siteOrigin + post.image, width: 1280, height: 720, caption: post.imageAlt, creditText: post.imageCredit}, wordCount: postWordCount(post),
    author: {"@type": "Organization", name: post.author, url: siteOrigin + "/about/"},
    publisher: {"@type": "Organization", "@id": siteOrigin + "/#publisher", name: "Episode Journal", url: siteOrigin + "/about/", logo: {"@type": "ImageObject", url: siteOrigin + "/assets/episode-journal-logo.png"}},
    mainEntityOfPage: {"@type": "WebPage", "@id": url}, citation: post.sources.map(source => source.url.startsWith("/") ? siteOrigin + source.url : source.url),
    about: {"@type": "TVSeries", name: "Mehmed: Fetihler Sultanı", sameAs: "https://www.trt1.com.tr/diziler/mehmed-fetihler-sultani"}},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", itemListElement: [
      {"@type": "ListItem", position: 1, name: "Home", item: siteOrigin + "/"},
      {"@type": "ListItem", position: 2, name: "Blog", item: siteOrigin + "/blog/"},
      {"@type": "ListItem", position: 3, name: post.title, item: url}]}];
}
