# Mythic State

<!-- The mythic-gm engine's loop-state anchor for this campaign — the engine's
`campaign-state.md` mapped onto Pendragon's `state/` (see /CLAUDE.md, "No duplicate
bookkeeping"). Overwrite at the end of every scene. The Threads/Characters Lists
(with their per-entry dossiers) live in `state/threads.json` / `state/characters.json`;
this file holds the Frame, the Chaos dial, and the scene recap — no List copy. -->

## Frame
- **Engine:** mythic-gm (drives) · companion bridge: `king-arthur-pendragon/bridge/`
- **Resolution:** Fate Chart · **Chaos flavor:** standard · **Discipline:** HARDCORE (no softening; Peril Points OFF)
- **Adventure Source mode:** Adventure Crafter (the GPC year brief seeds the Lists; scheduled events fire on the year clock)
- **Theme priority (this adventure):** _rolled from `bridge/theme-weights.md`_ — 1._ 2._ 3._ 4._ 5._
- **Mode now:** on-script (the spine follows the year brief). Use a **Scene Test** only when the knight rides off the brief into ground the books don't cover.

## Chaos Factor: 5

<!-- 1–9. −1 after a scene the knight mostly controlled, +1 after a chaotic one. Start at 5. The game year remains the master metronome (bridge/subsystems.md, gm/PACING.md); Chaos never overrides the schedule. -->

## Lists — SINGLE SOURCE: `state/threads.json` · `state/characters.json`

<!-- The dice roll the JSON directly (proportional two-stage roll, any length). Keep NO hand-copy of the Lists here.
     Each entry carries its own `dossier` (prose: status & history) + `status` field IN the JSON — there is no
     npcs.md / threads.md. The whole cast/plot is one rollable pool: dead/archived NPCs stay surfaceable; resolved
     threads sit at weight 0 (held). View: `state.py thread|char show <C>` (`--full` for whole dossiers).
     Mutate weights: `state.py thread|char add|weight|remove <C> "<name>"`; edit the JSON directly for dossiers. -->
- **View the live, generated list:** `state.py thread show <C>` · `state.py char show <C>` (`--full` for dossiers)
- **Mutate weights:** `state.py thread|char add|weight|remove <C> "<name>"`  ·  **dossier/status:** edit the JSON entry

## Scene
- **Last scene recap (2–3 sentences):** _the campaign opens here_
- **Self-audit drift counter (consecutive soft scenes):** 0
- **Seed deck:** → `state/seeds.md` _(refresh each bookkeeping from `bridge/seeds.md` sources)_

## Notes

- Nothing here overrides `state/campaign.md`, `state/threads.json`, or `state/characters.json`. On conflict, those win; this is the engine's loop-state anchor (Frame + Chaos + recap).
- When a thread closes set its `weight` to 0 in `threads.json` (held — kept for canon, surfaced only if reopened); a dead/departed NPC stays in `characters.json` at low weight so the oracle can still surface them. Update the entry's `dossier` to record what changed.
