import SubtitleCountdown from "./SubtitleCountdown";
export default function HomepageRelease() {
  return <section className="release-schedule" aria-labelledby="release-heading">
    <header className="release-header">
      <div><span className="eyebrow">NEXT ON EPISODE JOURNAL</span><h2 id="release-heading">The next <em>chapter.</em></h2></div>
      <div className="release-identity"><span className="release-number">06</span><p>Season 4 · Episode 6<br /><span>Original Turkish episode 89</span></p></div>
    </header>
    <div className="release-timers">
      <article className="release-column">
        <span className="release-kicker">01 / ORIGINAL BROADCAST</span>
        <h3>Turkish broadcast</h3>
        <p className="release-date"><time dateTime="2026-10-20T20:00:00+03:00" data-subtitle-local-time="2026-10-20T20:00:00+03:00">Tuesday, 20 October 2026 · 20:00 Turkey time</time></p>
        <div className="countdown-display" data-countdown="2026-10-20T17:00:00Z" role="timer" aria-label="Time until the expected Turkish broadcast">
          <div><strong data-unit="days">--</strong><span>DAYS</span></div><b aria-hidden="true">:</b>
          <div><strong data-unit="hours">--</strong><span>HOURS</span></div><b aria-hidden="true">:</b>
          <div><strong data-unit="minutes">--</strong><span>MINUTES</span></div><b aria-hidden="true">:</b>
          <div><strong data-unit="seconds">--</strong><span>SECONDS</span></div>
        </div>
        <a className="release-link" href="/dramas/mehmed-fetihler-sultani/season-4/broadcast-dates/">Broadcast calendar <span aria-hidden="true">↗</span></a>
      </article>
      <article className="release-column"><span className="release-kicker">02 / EXPECTED SUBTITLES</span><SubtitleCountdown edition="Urdu" episode={89} label="Urdu subtitles" /><a className="release-link" href="/dramas/mehmed-fetihler-sultani/episodes/89/urdu-subtitles/">Explore the Urdu guide <span aria-hidden="true">↗</span></a></article>
      <article className="release-column"><span className="release-kicker">03 / EXPECTED SUBTITLES</span><SubtitleCountdown edition="English" episode={89} label="English subtitles" /><a className="release-link" href="/dramas/mehmed-fetihler-sultani/episodes/89/english-subtitles/">Explore the English guide <span aria-hidden="true">↗</span></a></article>
    </div>
    <footer className="release-footer"><span>ALL TIMES SHOWN IN YOUR LOCAL TIMEZONE</span><p data-countdown-status>Dates are expected. Subtitles may arrive earlier; availability is checked separately.</p></footer>
  </section>;
}
