# PT Dashboard App

Personal trainer dashboard app — tracks meals, workouts, water intake, weight, and more.

This repo is a local development copy. The live version runs on a server at:
- `/root/dashboard/index.html`
- `/root/dashboard/dashboard-data.json`
- `/root/dashboard/server.py`

## Files

- `index.html` — full dashboard UI (vanilla JS, self-contained)
- `dashboard-data.json` — data file (meals, workouts, water, weight, etc.)
- `server.py` — minimal `http.server` wrapper that disables caching so edits show up live

## Running locally

```bash
python3 server.py     # serves on :8000, cwd must be the folder containing index.html
```

Or any other static server, e.g. `python3 -m http.server 8000`.

## Editing

The dashboard reads `dashboard-data.json` on every page load. Edits to the JSON or `index.html` appear immediately (hard refresh if cached). No rebuild step needed.
