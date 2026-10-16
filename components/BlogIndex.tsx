import Header from "./shell/Headerae0b46724a56";
import Footer from "./shell/Footerd74fa961a426";
import BlogCover from "./BlogCover";
import { publishedPosts, postReadingMinutes } from "@/lib/posts";

const season = "/dramas/mehmed-fetihler-sultani/season-4/";
const featured = publishedPosts[0];

export default function BlogIndex() {
  return <>
    <a className="skip" href="#main">Skip to content</a>
    <Header />
    <main id="main" className="blog-index">
      <section className="blog-intro" aria-labelledby="blog-heading">
        <div className="blog-masthead"><span className="eyebrow">THE EPISODE JOURNAL</span><span>Stories · Context · Viewing guides</span></div>
        <div className="blog-intro-grid"><h1 id="blog-heading">Beyond the<br /><em>episode.</em></h1><p>Meet the characters, understand the story and find your next chapter. Episode Journal connects original articles with episode details, release dates and Urdu and English viewing guides.</p></div>
      </section>

      <section className="blog-feature" aria-labelledby="featured-heading">
        <a className="blog-feature-image" href={"/blog/" + featured.slug + "/"} aria-label="Read the Season 4 cast guide">
          <BlogCover post={featured} />
        </a>
        <div className="blog-feature-copy"><span className="eyebrow">FEATURED READING / SEASON 4</span><h2 id="featured-heading"><a href={"/blog/" + featured.slug + "/"}>Know the faces.<br /><em>Follow the story.</em></a></h2><p>Match the actor to the character, untangle similar names and find your way through the Season 4 ensemble with our sourced cast guide.</p><a className="blog-read-link" href={"/blog/" + featured.slug + "/"}>Read the cast guide <span aria-hidden="true">↗</span></a></div>
      </section>

      <section className="blog-reading" aria-labelledby="latest-heading">
        <div className="blog-section-heading"><h2 id="latest-heading">Questions worth answering.</h2><span>SEVEN NOTES FROM THE JOURNAL</span></div>
        <div className="journal-post-grid">{publishedPosts.map((post, i) => <article className={"journal-post-card journal-post-card--" + post.layout} key={post.slug}><a href={"/blog/" + post.slug + "/"}><div className="journal-post-card-cover"><BlogCover post={post} card /></div><div className="journal-post-card-top"><span className="eyebrow">{post.category}</span><span aria-hidden="true">0{i + 1}</span></div><h3>{post.title}</h3><p>{post.description}</p><div className="journal-post-card-bottom"><span><time dateTime={post.publishedAt}>17 October 2026</time> · {postReadingMinutes(post)} min read</span><span aria-hidden="true">↗</span></div></a></article>)}</div>
      </section>

      <section className="blog-reading" aria-labelledby="reading-heading">
        <div className="blog-section-heading"><h2 id="reading-heading">Find your way into the story.</h2><span>THE READING DESK</span></div>
        <div className="blog-card-grid">
          <article className="blog-card"><a href="/guides/mehmed-season-4-episode-numbers/" className="blog-card-link"><div className="blog-number-art" aria-hidden="true"><span>01<span className="blog-number-divider">/</span>84</span><small>ONE EPISODE. TWO WAYS TO COUNT.</small></div><div className="blog-card-copy"><span className="eyebrow">THE ESSENTIALS / NUMBERING</span><h3>One episode.<br /><em>Two numbers.</em></h3><p>Season 4 Episode 1 or original Episode 84? Understand the numbering and choose the right guide before you watch.</p><span className="blog-read-link">Explore the numbering guide <span aria-hidden="true">↗</span></span></div></a></article>
          <article className="blog-card"><a href={season + "broadcast-dates/"} className="blog-card-link"><div className="blog-card-image"><img src="/assets/frame-3-960.webp" srcSet="/assets/frame-3-480.webp 480w, /assets/frame-3-960.webp 960w" sizes="(max-width: 760px) 100vw, 45vw" width={960} height={540} loading="lazy" alt="Series scene from Mehmed: Fetihler Sultani" /></div><div className="blog-card-copy"><span className="eyebrow">THE VIEWING GUIDE / RELEASE DATES</span><h3>Make time for<br /><em>the next chapter.</em></h3><p>Follow Turkish broadcast dates and expected Urdu and English subtitle releases in the Season 4 calendar.</p><span className="blog-read-link">Open the release calendar <span aria-hidden="true">↗</span></span></div></a></article>
        </div>
      </section>

      <aside className="blog-editorial-note"><div><span className="eyebrow">A NOTE FROM THE JOURNAL</span><h2>Good stories deserve<br /><em>clear sources.</em></h2></div><div><p>Our guides draw on official episode information and clearly identified viewing sources. We distinguish the drama’s story from historical fact, and expected releases from confirmed availability.</p><a className="blog-read-link" href="/how-we-check/">How we check our sources <span aria-hidden="true">↗</span></a></div></aside>
    </main>
    <Footer />
  </>;
}

