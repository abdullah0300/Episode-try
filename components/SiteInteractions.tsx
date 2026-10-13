"use client";
import { useEffect } from "react";

/** Small enhancements only: all content and navigation are server-rendered. */
export default function SiteInteractions() {
  useEffect(() => {
    const controller = new AbortController();
    const signal = controller.signal;
    const header = document.querySelector<HTMLElement>(".site-header");
    const menu = document.querySelector<HTMLButtonElement>(".menu-button");
    menu?.addEventListener("click", () => {
      const open = menu.getAttribute("aria-expanded") !== "true";
      menu.setAttribute("aria-expanded", String(open));
      header?.classList.toggle("menu-open", open);
    }, {signal});
    header?.querySelectorAll<HTMLAnchorElement>("nav a").forEach(a => a.addEventListener("click", () => {
      menu?.setAttribute("aria-expanded", "false");
      header.classList.remove("menu-open");
    }, {signal}));

    const search = document.querySelector<HTMLInputElement>(".episode-search input");
    search?.addEventListener("input", () => {
      let count = 0;
      document.querySelectorAll<HTMLElement>("[data-episode]").forEach(row => {
        const match = (row.dataset.episode || "").split(" ").some(number => number.includes(search.value.trim()));
        row.hidden = !match;
        count += Number(match);
      });
      const message = document.querySelector<HTMLElement>(".no-results");
      if (message) message.hidden = count > 0;
    }, {signal});

    document.querySelectorAll<HTMLButtonElement>("[data-filter]").forEach(button => button.addEventListener("click", () => {
      document.querySelectorAll<HTMLButtonElement>("[data-filter]").forEach(b => {
        b.classList.toggle("active", b === button);
        b.setAttribute("aria-pressed", String(b === button));
      });
      document.querySelectorAll<HTMLElement>("[data-language]").forEach(cell => {
        cell.hidden = button.dataset.filter !== "All" && cell.dataset.language !== button.dataset.filter;
      });
    }, {signal}));

    const clock = document.querySelector<HTMLElement>("[data-countdown]");
    const status = document.querySelector<HTMLElement>("[data-countdown-status]");
    let interval: ReturnType<typeof setInterval> | undefined;
    const target = Date.parse(clock?.dataset.countdown || "");
    function tick() {
      if (!clock) return;
      if (!Number.isFinite(target)) {
        if (status) status.textContent = "Broadcast time is awaiting confirmation.";
        return;
      }
      const seconds = Math.max(0, Math.ceil((target - Date.now()) / 1000));
      const hasDays = Boolean(clock.querySelector("[data-unit=days]"));
      const values = {days: Math.floor(seconds / 86400), hours: Math.floor((hasDays ? seconds % 86400 : seconds) / 3600), minutes: Math.floor(seconds % 3600 / 60), seconds: seconds % 60};
      Object.entries(values).forEach(([unit, value]) => {
        const node = clock.querySelector<HTMLElement>(`[data-unit="${unit}"]`);
        if (node) node.textContent = String(value).padStart(2, "0");
      });
      clock.setAttribute("aria-label", seconds ? `${hasDays ? `${values.days} days, ` : ""}${values.hours} hours and ${values.minutes} minutes until the expected Turkish broadcast` : "The scheduled broadcast time has passed");
      if (!seconds) {
        if (status) status.textContent = "Scheduled broadcast time has passed. Check the subtitle guides for availability.";
        if (interval) clearInterval(interval);
      }
    }
    tick();
    if (clock && target > Date.now()) interval = setInterval(tick, 1000);

    const subtitleIntervals: ReturnType<typeof setInterval>[] = [];
    document.querySelectorAll<HTMLElement>("[data-subtitle-local-time]").forEach(node => {
      const deadline = Date.parse(node.dataset.subtitleLocalTime || "");
      if (!Number.isFinite(deadline)) return;
      try {
        const formatter = new Intl.DateTimeFormat(navigator.language || "en", {
          weekday: "long", year: "numeric", month: "long", day: "numeric",
          hour: "numeric", minute: "2-digit", timeZoneName: "long",
        });
        node.textContent = `Your local time: ${formatter.format(new Date(deadline))}`;
      } catch {
        // The server-rendered Pakistan time remains available as a fallback.
      }
    });
    document.querySelectorAll<HTMLElement>("[data-subtitle-countdown]").forEach(timer => {
      const deadline = Date.parse(timer.dataset.subtitleCountdown || "");
      const note = timer.closest(".subtitle-countdown")?.querySelector<HTMLElement>("[data-subtitle-status]");
      let subtitleInterval: ReturnType<typeof setInterval> | undefined;
      function updateSubtitleClock() {
        if (!Number.isFinite(deadline)) return;
        const remaining = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
        const values = {days: Math.floor(remaining / 86400), hours: Math.floor(remaining % 86400 / 3600), minutes: Math.floor(remaining % 3600 / 60), seconds: remaining % 60};
        Object.entries(values).forEach(([unit, value]) => {
          const node = timer.querySelector<HTMLElement>(`[data-unit="${unit}"]`);
          if (node) node.textContent = String(value).padStart(2, "0");
        });
        timer.setAttribute("aria-label", remaining ? `${values.days} days, ${values.hours} hours and ${values.minutes} minutes until the expected ${timer.dataset.edition} subtitle release` : "Expected subtitle upload window has ended");
        if (!remaining) {
          if (note) note.textContent = "Expected upload window has ended. Check the viewing guide for availability.";
          if (subtitleInterval) clearInterval(subtitleInterval);
        }
      }
      updateSubtitleClock();
      if (deadline > Date.now()) {
        subtitleInterval = setInterval(updateSubtitleClock, 1000);
        subtitleIntervals.push(subtitleInterval);
      }
    });

    const form = document.querySelector<HTMLFormElement>("#alert-form");
    form?.addEventListener("submit", event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const data = new FormData(form);
      const preferences = {email: String(data.get("email") || ""), language: String(data.get("language") || "Both")};
      const message = document.querySelector<HTMLElement>("#form-message");
      try {
        localStorage.setItem("episode-journal-alert", JSON.stringify(preferences));
        if (message) message.textContent = `${preferences.language} preference saved on this device. Email delivery is not connected.`;
      } catch {
        if (message) message.textContent = "Your selection is ready. This browser could not save it; email delivery is not connected.";
      }
    }, {signal});

    let observer: IntersectionObserver | undefined;
    if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
      observer = new IntersectionObserver(entries => entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          observer?.unobserve(entry.target);
        }
      }), {threshold: 0.08});
      document.querySelectorAll(".platform-featured .light-outline[href='https://greatnation.webcraftio.com/']").forEach(button => observer?.observe(button));
      document.querySelectorAll(".story-section,.schedule-section,.questions-section,.alerts-section").forEach(section => {
        section.classList.add("reveal-ready");
        observer?.observe(section);
      });
    }
    return () => {
      controller.abort();
      subtitleIntervals.forEach(clearInterval);
      if (interval) clearInterval(interval);
      observer?.disconnect();
      document.querySelectorAll(".reveal-ready").forEach(section => section.classList.remove("reveal-ready"));
    };
  }, []);
  return null;
}
