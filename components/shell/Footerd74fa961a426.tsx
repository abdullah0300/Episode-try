const season = "/dramas/mehmed-fetihler-sultani/season-4/";
export default function Footerd74fa961a426() {
  return <footer className="journal-footer">
    <div className="journal-footer-top">
      <div className="journal-footer-brand">
        <a className="logo-brand" href="/" aria-label="Episode Journal home"><img src="/assets/episode-journal-logo-480.webp" alt="Episode Journal" width={480} height={160} loading="lazy" /></a>
        <p className="journal-footer-statement">A clear guide.<br /><em>To what’s next.</em></p>
        <p className="journal-footer-description">Episode dates, subtitle updates and where to watch. Find your next chapter with Episode Journal.</p>
      </div>
      <nav className="journal-footer-nav" aria-label="Footer navigation">
        <div><h2>Explore the season</h2><a href={season}>Season 4 episode guide</a><a href={season + "urdu-subtitles/"}>Urdu subtitle guides</a><a href={season + "english-subtitles/"}>English subtitle guides</a><a href={season + "broadcast-dates/"}>Broadcast dates</a></div>
        <div><h2>A little clarity</h2><a href="/blog/">The journal · Blog</a><a href="/guides/mehmed-season-4-episode-numbers/">Episode numbering</a><a href="/guides/mehmed-season-4-story-so-far/">The story so far</a><a href="/how-we-check/">How we check our sources</a><a href="/about/">About Episode Journal</a></div>
      </nav>
    </div>
    <div className="journal-footer-bottom"><p>© 2026 Episode Journal <span>by <a href="https://webcraftio.com/" target="_blank" rel="noopener">Webcraftio</a></span></p><p className="journal-footer-credit">Series photography © TRT / respective rights holders.</p><a href="/sitemap.xml">Sitemap</a></div>
  </footer>;
}
