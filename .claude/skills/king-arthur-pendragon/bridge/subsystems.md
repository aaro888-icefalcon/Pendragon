# World Subsystems — Arthurian Britain   (hook: world-tick; fired by tick.py at bookkeeping)

The Pendragon companion is **strong at scene ends**: the year clock, not the
Chaos Factor, is the campaign's master metronome (`gm/PACING.md`). At every
bookkeeping step run (from the repo root)
`python3 .claude/skills/mythic-gm/scripts/tick.py .claude/skills/king-arthur-pendragon/bridge <scene#>`
and resolve each DUE / triggered row below by rolling its named table or rule
**honestly** and recording the result to the campaign's `state/`. Scheduled GPC
events fire **whether or not the player engaged** — every year brief has an "If
the player does nothing" line; use it. The world is not waiting for the knight.

**The Pendragon game year** runs in a fixed shape — **court → adventure season →
(battle, if the year brief schedules one) → Winter Phase** — and then turns to the
next year. The engine frames Expected Scenes within that shape; the rows below
fire at the year's turn. Aim to complete at least one full game year, Winter Phase
included, per session (`gm/PACING.md`).

| subsystem | cadence | advance by |
|---|---|---|
| Game-year metronome (MASTER) | on trigger: year turn / Winter Phase | Advance `state/campaign.md` to the next game year; load the new year's brief (`campaign/uther/05-timeline-480-495.md` for 480–495, `campaign/gpc/` for 496–566). The year clock outranks Chaos. |
| Scheduled GPC event | on trigger: the year clock | Fire the current year brief's canonical event as a keyed scene (it happens on schedule regardless of the PC). The GPC is a map, not a script — the dice still decide; track any divergence in `state/campaign.md`. |
| Thread pressure | every scene | Light nudge: check each open thread in `state/threads.md` against its pressure line; surface the nearest if the scene stalled. Full advance every ignored thread one step at Winter Phase — rivals gain Glory, grudges fester, opportunities expire (`gm/PACING.md` §4). |
| Glory accrual | every scene | Award Glory for the deeds of the scene per `rules/core/07-glory.md`; each 1,000 lifetime crossed grants a Bonus Point. Record to `state/knight.md`. |
| Winter Phase | on trigger: year end | Run `rules/core/08-winter-phase.md` in full — experience checks, aging roll, horse/family events, Glory tally — never skipped. Add `rules/estate/` and `rules/entourage/` steps where applicable. |
| Estate & entourage | on trigger: landed knight, at Winter Phase | Estate economics + a roll on estate events (`rules/estate/04-estate-events.md`); entourage upkeep and events (`rules/entourage/`). Record income, holdings, and people to `state/`. |
| Faction turn (off-screen) | every 3 scenes | Advance one off-screen power: roll `generators/factions_faction_goal.json` (or run a Faction Turn per `generators/02-factions.md`) plus a Mythic Move-Toward/Away an open Thread. Record standings to `state/npcs.md` / `state/threads.md`. |

Notes:
- "on trigger" rows are the **year clock's**, not the scene counter's — `tick.py` lists them as "check trigger" so the GM fires them when the fiction reaches that year/Winter Phase.
- Mythic's default offscreen-clock advance still applies underneath; these rows make the Pendragon clock explicit and authoritative.
- Everything mechanical resolves on `gm/roll.py`; only genuinely open world-questions around these subsystems use a Fate Question.
