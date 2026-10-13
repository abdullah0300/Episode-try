import type { Metadata, Viewport } from "next";
import { siteOrigin } from "@/lib/site";
import "./globals.css";
export const metadata: Metadata = {
  metadataBase: new URL(siteOrigin),
  icons: {
    icon: [
      { url: "/assets/favicon.svg", type: "image/svg+xml" },
      { url: "/assets/favicon-16.png", sizes: "16x16", type: "image/png" },
      { url: "/assets/favicon-32.png", sizes: "32x32", type: "image/png" },
      { url: "/assets/favicon-48.png", sizes: "48x48", type: "image/png" },
      { url: "/assets/favicon-192.png", sizes: "192x192", type: "image/png" },
      { url: "/assets/favicon-512.png", sizes: "512x512", type: "image/png" },
    ],
    shortcut: "/assets/favicon.ico",
    apple: { url: "/assets/apple-touch-icon.png", sizes: "180x180", type: "image/png" },
  },
};
export const viewport: Viewport = {themeColor: "#20362d"};
export default function RootLayout({children}: {children: React.ReactNode}) {
  return <html lang="en"><body>{children}</body></html>;
}
