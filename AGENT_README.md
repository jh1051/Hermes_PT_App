# PT Dashboard — Agent Guide

This is a personal training dashboard app. All user data lives in a single JSON file. As an AI agent, your job is to read, understand, and write data to that file in the correct structure.

## The data file: `dashboard-data.json`

The app reads everything from `dashboard-data.json`. If you need to log food, workouts, weigh-ins, or update the user's profile, you edit this file. There is no database, no API — just this one file.

Use `dashboard-data-template.json` as a reference for the exact structure. Below is a field-by-field guide.

---

## Profile

```json
"profile": {
  "name": "Client Name",
  "avatar": "https://url.to/avatar.png",
  "coachName": "Coach Name",
  "height": "5ft 10",
  "goalBodyFatPercent": 15,
  "proteinTargetG": 150,
  "startWeight": { "st": 12, "lb": 0, "date": "2026-01-01" },
  "currentWeight": { "st": 11, "lb": 8, "date": "2026-06-01" },
  "goalWeight": { "st": 11, "lb": 0 },
  "calorieTarget": { "min": 2400, "max": 2600 }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | User's full name |
| `avatar` | string | (Optional) URL to the user's profile picture |
| `coachName` | string | (Optional) Name of the personal trainer/coach |
| `height` | string | Height as a display string |
| `goalBodyFatPercent` | number | (Optional) Target/goal body fat percentage. Used for the body fat goal wheel |
| `proteinTargetG` | number | (Optional) Daily protein target in grams. Falls back to 135 if missing |
| `startWeight` | object | Starting weight in stones (`st`) and pounds (`lb`), with the `date` |
| `currentWeight` | object | Most recent weight in stones and pounds, with the `date` |
| `goalWeight` | object | Target/goal weight in stones and pounds |
| `calorieTarget` | object | Daily calorie target range (`min`/`max`). The app uses `max` for the progress bar |

## Weigh-ins

```json
"weighIns": [
  { "date": "2026-01-01", "st": 12, "lb": 0, "note": "Starting weight" }
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
  "name": "Chicken breast with rice",
  "quantity": "200g chicken, 150g rice",
  "kcal": 450,
  "proteinGrams": 48,
  "note": "Grilled, no sauce.",
  "ingredients": [
    { "name": "Chicken breast", "quantity": "200g", "kcal": 330, "proteinGrams": 40 },
    { "name": "White rice", "quantity": "150g cooked", "kcal": 120, "proteinGrams": 8 }
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
  "name": "Upper Body Push Workout",
  "durationMinutes": 45,
  "kcal": 320,
  "note": "Felt strong, increased bench by 2.5kg.",
  "exercises": [
    { "name": "Bench Press", "sets": 4, "reps": "8-10", "weight": "60kg", "note": "Last set AMRAP - got 11" }
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
