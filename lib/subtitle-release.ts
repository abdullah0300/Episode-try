import calendar from "@/data/broadcast_calendar.json";
export type SubtitleEdition = "Urdu" | "English";
export function subtitleRelease(overallEpisode: number) {
  const episode = calendar.episodes.find(item => item.overall_episode === overallEpisode);
  if (!episode || episode.status !== "upcoming") return null;
  const date = new Date(`${episode.broadcast_date}T00:00:00Z`);
  const days = (3 - date.getUTCDay() + 7) % 7 || 7;
  date.setUTCDate(date.getUTCDate() + days);
  const day = date.toISOString().slice(0, 10);
  return { episode, deadline: `${day}T12:00:00+05:00`, label: new Intl.DateTimeFormat("en-GB", {weekday: "long", day: "numeric", month: "long", year: "numeric", timeZone: "UTC"}).format(date) };
}
export const nextSubtitleEpisode = calendar.featured_episode ?? calendar.episodes.find(item => item.status === "upcoming")?.overall_episode;
