# Character Sheet (Mythic shape) — Pendragon knight

> What the `mythic-gm` loop tracks for a Pendragon PC. The full, canonical sheet is `assets/templates/knight.md` (built via `rules/core/01-character-creation.md`, rolled honestly). This file tells the engine which fields are live state.

**Build:** walk the player through `rules/core/01-character-creation.md` — homeland, class, family characteristic, attributes, traits, passions, skills — rolling every random element. Record into `assets/templates/knight.md` in the working directory.

**The loop tracks (the engine's "conditions/resources"):**
- **Current HP vs total** (= CON + SIZ), plus **Unconscious** (¼ total), **Major Wound** (≥ CON), **Knockdown** (≥ SIZ) thresholds.
- **Wounds & afflictions** — open wounds, Chirurgery/Healing-Rate recovery, permanent stat loss, aging effects.
- **Glory** (lifetime total; crossing each 1,000 grants a Bonus Point) and **Bonus Points** unspent.
- **Traits & passions** — these are live and **bind the PC**: when the rules call for a trait/passion check, roll it (`gm/roll.py check <value>`) and enforce the result, including against the player's wishes.
- **Skills & combat skills** with experience-check ticks (resolved at Winter Phase).
- **Horses, equipment, armor, coin.**
- **Holdings** (manor, income, military obligation, Glory/year) once landed — see `rules/estate/`.

**Seed the adventure (Session Zero):** pull 1–2 starting Threads (a liege's charge, a family matter, a rivalry) onto `state/threads.md` and any tied NPCs onto `state/npcs.md`, so Mythic's Lists have content to work with from the first scene.

**On death:** archive a copy into `state/dynasty.md`, then rebuild this sheet for the heir (`gm/LETHALITY.md` §4). The campaign continues.
