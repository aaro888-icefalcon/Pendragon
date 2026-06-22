# Mythic State

<!-- The Mythic GME layer's live state. See gm/MYTHIC.md for how it's used. Pendragon drives; this only tracks the gap-filler's bookkeeping. Update alongside the other state files. Threads/NPCs live in their own files — this holds the Chaos dial and a roll-snapshot only. Requires the companion mythic-gm skill; without it, gm/MYTHIC.md gives a standalone fallback. -->

**Engine:** mythic-gm (companion skill) · resolution Fate Chart · discipline HARDCORE (no softening; Peril Points OFF)
**Mode now:** on-script (the campaign spine follows the year brief). Use a **Scene Test** only when the knight rides off the brief into ground the books don't cover.

## Chaos Factor: 5

<!-- 1–9. −1 after a scene the knight mostly controlled, +1 after a chaotic one. Start at 5. The game year remains the master metronome (gm/PACING.md); Chaos never overrides the schedule. -->

## Threads List → `state/threads.md`

<!-- Snapshot of open threads with a rough salience weight (1–3) for Mythic list-rolls. Prose home is threads.md. -->

| # | Open thread (short) | Weight |
|---|---|---|

## Characters List → `state/npcs.md`

<!-- Most active NPCs on stage now, with a rough weight (1–3) for Mythic list-rolls. Full roster in npcs.md. -->

| NPC | Weight |
|---|---|

## Notes

- Nothing here overrides `state/campaign.md`, `state/threads.md`, or `state/npcs.md`. On conflict, those files win; this is the Chaos dial plus a roll-snapshot.
- When a thread closes or an NPC leaves the stage, drop it from the snapshot above (its prose record stays in its home file).
