import "server-only";
// The publisher's chosen canonical domain also works on hosts without .env.local.
const productionOrigin = "https://episodejournal.webcraftio.com";
const value = process.env.SITE_ORIGIN || (process.env.NODE_ENV === "production" ? productionOrigin : "http://localhost:3000");
const parsed = new URL(value);
if (parsed.pathname !== "/" || parsed.search || parsed.hash || parsed.username || parsed.password || /\s/.test(value)) {
  throw new Error("SITE_ORIGIN must contain only the scheme and host.");
}
if (process.env.NODE_ENV === "production" && (parsed.protocol !== "https:" || parsed.hostname.endsWith("chatgpt.site"))) {
  throw new Error("Production SITE_ORIGIN must be your final public HTTPS origin.");
}
export const siteOrigin = parsed.origin;
