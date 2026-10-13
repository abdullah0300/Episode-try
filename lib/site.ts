import "server-only";
const value = process.env.SITE_ORIGIN || (process.env.NODE_ENV === "production" ? "" : "http://localhost:3000");
if (!value) throw new Error("Set SITE_ORIGIN to your final HTTPS domain before building.");
const parsed = new URL(value);
if (parsed.pathname !== "/" || parsed.search || parsed.hash || parsed.username || parsed.password || /\s/.test(value)) {
  throw new Error("SITE_ORIGIN must contain only the scheme and host.");
}
if (process.env.NODE_ENV === "production" && (parsed.protocol !== "https:" || parsed.hostname.endsWith("chatgpt.site"))) {
  throw new Error("Production SITE_ORIGIN must be your final public HTTPS origin.");
}
export const siteOrigin = parsed.origin;
