# compat/ — running Pendragon under the mythic-gm engine

These files rework Pendragon into the fixed shapes the **`mythic-gm`** engine reads (its `references/adapting/compatibility-spec.md`). Use this folder only for **mode B** — when the user is driving from `mythic-gm` and wants Pendragon as its ruleset + setting. For normal play, drive from this skill instead (mode A) and let `gm/MYTHIC.md` pull Mythic in as the gap-filler.

| This file | Is mythic-gm's | The engine reads it for |
|---|---|---|
| `system-profile.md` | `system-profile.md` | task resolution & combat (the RPG seam) — points at `gm/roll.py` |
| `setting-canon.md` | `setting-canon.md` | world ground truth (overrides invention) |
| `character-sheet.md` | `character-sheet.md` | the PC stats/resources the loop tracks (full sheet: `assets/templates/knight.md`) |

**Adventure source.** The Great Pendragon Campaign is Pendragon's "published adventure." Rather than rails, treat each year brief in `campaign/` as available content: seed the year's hooks onto the **Threads List** (`state/threads.md`), its NPCs onto the **Characters List** (`state/npcs.md`), and run scheduled canonical events as keyed scenes that fire on the year clock (`gm/PACING.md`). The dice still decide; the GPC is a map, not a script.

**The precedence never changes:** Pendragon drives; Mythic fills gaps; Mythic incorporates Pendragon. Even in mode B, anything Pendragon resolves (a rule, a stat block, a scheduled GPC beat) is answered by Pendragon, and Mythic only fills what's left open. Full contract: `gm/MYTHIC.md`.

**Note:** `mythic-gm`'s copyrighted tables are not bundled in this skill — they live in the separately installed `mythic-gm`. This folder only adapts Pendragon to that engine's shapes.
