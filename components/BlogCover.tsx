import type { Post } from "@/lib/posts";

export default function BlogCover({post, card = false}: {post: Post; card?: boolean}) {
  const stem = post.image.replace(/\.webp$/, "");
  return <img src={post.image}
    srcSet={`${stem}-480.webp 480w, ${stem}-960.webp 960w, ${post.image} 1280w`}
    sizes={card ? "(max-width: 700px) 88vw, (max-width: 980px) 43vw, 28vw" : "(max-width: 760px) 88vw, 1134px"}
    width={1280} height={720} alt={post.imageAlt} loading={card ? "lazy" : "eager"} />;
}
