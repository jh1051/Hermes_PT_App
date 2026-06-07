# Hermes PT App

Working copy of the PaulThePT dashboard app for local development.

This repo is a copy — the live/source-of-truth versions still live on the Hermes host at:
- `/root/dashboard/index.html` (served via symlink from `/root/PaulThePT/dashboard-index.html`)
- `/root/PaulThePT/dashboard-data.json` (source of truth, symlinked into `/root/dashboard/`)
- `/root/PaulThePT/server.py` (the no-cache HTTP server, port 8000)

## Files

- `index.html` — full dashboard UI (1120 lines, self-contained, vanilla JS)
- `dashboard-data.json` — source of truth data file (meals, workouts, water, weight, etc.)
- `server.py` — minimal `http.server` wrapper that disables caching so edits show up live

## Running locally

```bash
cd hermes-pt-app
python3 server.py     # serves on :8000, cwd must be the folder containing index.html
```

Or any other static server, e.g. `python3 -m http.server 8000`.

## Live server (Tailscale)

The production version is reachable at http://100.109.250.77:9119/ when bound to host 100.109.250.77.

## Editing

The dashboard reads `dashboard-data.json` on every page load. Edits to the JSON appear immediately (hard refresh if the page is cached). Edits to `index.html` likewise — no rebuild step.

A watchdog cron restarts `server.py` if it goes down.
