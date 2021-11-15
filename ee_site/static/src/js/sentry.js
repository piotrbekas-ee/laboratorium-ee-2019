import * as sentry from "@sentry/browser";

const SENTRY_DSN = document.getElementById("SENTRY_DSN").textContent;
if (SENTRY_DSN) {
  sentry.init({
    dsn: SENTRY_DSN,
  });
}
