import { notFound } from "next/navigation";
import { publishedPosts, getPost, postMetadata, postGraph } from "@/lib/posts";
import BlogPost from "@/components/BlogPost";

export const dynamicParams = false;
export function generateStaticParams() { return publishedPosts.map(post => ({slug: post.slug})); }
type Props = {params: Promise<{slug: string}>};
export async function generateMetadata({params}: Props) {
  const post = getPost((await params).slug);
  if (!post) notFound();
  return postMetadata(post);
}
export default async function Page({params}: Props) {
  const post = getPost((await params).slug);
  if (!post) notFound();
  return <><script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify(postGraph(post)).replace(/</g, "\\u003c")}} /><BlogPost post={post} /></>;
}
