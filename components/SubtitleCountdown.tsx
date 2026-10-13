import { nextSubtitleEpisode, subtitleRelease, type SubtitleEdition } from "@/lib/subtitle-release";
export default function SubtitleCountdown({edition, episode = nextSubtitleEpisode, label}: {edition: SubtitleEdition; episode?: number; label?: string}) {
  const release = episode === undefined ? null : subtitleRelease(episode);
  if (!release) return null;
  return <section className="subtitle-countdown" aria-label={`${edition} subtitle expected release`}>
    <p className="subtitle-countdown-label">{label || `${edition} subtitles expected by`}</p>
    <p className="subtitle-countdown-date"><time dateTime={release.deadline} data-subtitle-local-time={release.deadline}>{release.label} · 12:00 noon Pakistan time (UTC+5)</time></p>
    <p className="subtitle-countdown-episode">Season {4} Episode {release.episode.season_episode} · Original episode {episode}</p>
    <div className="countdown-display" data-subtitle-countdown={release.deadline} data-edition={edition} role="timer" aria-label={`Time until the expected ${edition} subtitle release`}>
      <div><strong data-unit="days">--</strong><span>DAYS</span></div><b aria-hidden="true">:</b>
      <div><strong data-unit="hours">--</strong><span>HOURS</span></div><b aria-hidden="true">:</b>
      <div><strong data-unit="minutes">--</strong><span>MINUTES</span></div><b aria-hidden="true">:</b>
      <div><strong data-unit="seconds">--</strong><span>SECONDS</span></div>
    </div>
    <p className="subtitle-countdown-note" data-subtitle-status>Uploads may arrive earlier. Check the viewing guide for availability.</p>
  </section>;
}
