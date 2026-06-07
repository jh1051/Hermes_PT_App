# PaulThePT Dashboard — Agent Guide

This is a personal training dashboard app. All user data lives in a single JSON file. As an AI agent, your job is to read, understand, and write data to that file in the correct structure.

## The data file: `dashboard-data.json`

The app reads everything from `dashboard-data.json`. If you need to log food, workouts, weigh-ins, or update the user's profile, you edit this file. There is no database, no API — just this one file.

Use `dashboard-data-template.json` as a reference for the exact structure. Below is a field-by-field guide.

---

## Profile

```json
"profile": {
  "name": "Jamie Harris",
  "height": "5ft 8",
  "startWeight": { "st": 10, "lb": 7, "date": "2026-05-20" },
  "currentWeight": { "st": 10, "lb": 5.7, "date": "2026-06-06" },
  "goalWeight": { "st": 10, "lb": 10 },
  "calorieTarget": { "min": 2500, "max": 2600 }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | User's full name |
| `height` | string | Height as a display string |
| `startWeight` | object | Starting weight in stones (`st`) and pounds (`lb`), with the `date` |
| `currentWeight` | object | Most recent weight in stones and pounds, with the `date` |
| `goalWeight` | object | Target/goal weight in stones and pounds |
| `calorieTarget` | object | Daily calorie target range (`min`/`max`). The app uses `max` for the progress bar |
| `proteinTargetG` | number | (Optional) Daily protein target in grams. Falls back to 150 if missing |

## Weigh-ins

```json
"weighIns": [
  { "date": "2026-05-20", "st": 10, "lb": 7, "note": "Start weight" }
]
```

Each entry:
- `date` — ISO format `YYYY-MM-DD`
- `st` — Stone component of weight
- `lb` — Pound component (can be decimal, e.g. `5.7`)
- `note` — Optional note about the weigh-in
- `kg` — (Optional) kilogram value if the scale provided it

## Days (food + workouts)

Each day has a `date` key (`YYYY-MM-DD`), a `food` array, and a `workouts` array.

### Food items

```json
{
  "name": "Greek yogurt 1.5% fat",
  "quantity": "250g",
  "kcal": 185,
  "proteinGrams": 25.0,
  "note": "On its own, no toppings.",
  "ingredients": [
    { "name": "Eggs", "quantity": "3", "kcal": 215, "proteinGrams": 18 }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Name of the food item |
| `quantity` | string | (Optional) Quantity or portion size |
| `kcal` | number | Total calories |
| `proteinGrams` | number | Total protein in grams |
| `note` | string | (Optional) Any note about the food |
| `ingredients` | array | (Optional) Breakdown of sub-ingredients. Each has `name`, `quantity`, `kcal`, `proteinGrams`. The parent `kcal` and `proteinGrams` should be the sum of ingredients |

### Workout items

```json
{
  "name": "Easy run around Haagse Bos",
  "durationMinutes": 14,
  "kcal": 0,
  "note": "2.14km in 13:37 at 6:21/km",
  "exercises": [
    { "name": "Run", "sets": 1, "reps": "13:37", "weight": "\u2014", "note": "Average pace 6:21/km" }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Name of the workout |
| `durationMinutes` | number | Total duration in minutes |
| `kcal` | number | Estimated calories burned (can be 0 if unknown) |
| `note` | string | (Optional) Note about the workout |
| `exercises` | array | List of exercises within the workout. Each has `name`, `sets`, `reps`, `weight`, and optional `note` |

## Important notes for agents

1. **Protein field name:** The JSON uses `proteinGrams` (not `proteinG` or `protein`). The app internally maps it to `proteinG` when reading.
2. **Weights are in stones and pounds** everywhere — profile, weigh-ins, goals. Do not use kg or total lbs.
3. **Dates are `YYYY-MM-DD`** format throughout.
4. **Empty arrays** are fine for days with no food or no workouts: `"food": [], "workouts": []`.
5. **The `updatedAt` field** at the top of the JSON should be updated to the current ISO datetime whenever you modify the file.
6. **Do not remove fields** from the structure even if they're empty — the app expects them.
