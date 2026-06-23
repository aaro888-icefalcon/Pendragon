# campaigns/

The living state of every saga lives here — **one folder per campaign**. The
skills under `.claude/skills/` are read-only content; nothing is ever written
back into them. This is the working directory they write to.

## Layout

```
campaigns/
  <campaign-name>/
    state/
      campaign.md      # source of truth: year, period, situation, divergences, year log
      knight.md        # the player knight (stats, traits, passions, Glory, wounds)
      dynasty.md       # the family line and succession (the saga survives a death)
      npcs.md          # the Characters List — who's on stage, with weights
      threads.md       # the Threads List — open goals and hooks, with weights
      session-log.md   # one line per beat; GM rulings recorded here as precedent
      mythic.md        # the engine's loop-state anchor: Chaos Factor + scene mode + Lists snapshot + recap
      seeds.md         # the engine's seed deck (30–40), refreshed each bookkeeping (created on demand)
```

## Starting a new campaign

Copy every template into a fresh campaign's `state/`, then run character
creation with honest rolls:

```bash
mkdir -p campaigns/<campaign-name>/state
cp .claude/skills/king-arthur-pendragon/assets/templates/*.md campaigns/<campaign-name>/state/
```

Open at Salisbury, spring **480 AD**, under King Uther. Claude (driving the
`mythic-gm` engine over the `king-arthur-pendragon` companion bridge) walks you
through the rest — Session Zero, then THE TURN (see `/CLAUDE.md`).

## No duplicate bookkeeping (engine ⇄ Pendragon state mapping)

In the default mode (Mythic drives), the engine's loop-state lives in these
existing Pendragon files — no parallel `campaign-state.md` is created:

- engine **`campaign-state.md`** (Frame · Chaos · Lists snapshot · recap) → **`mythic.md`**
- engine **`character-sheet.md`** → **`knight.md`**
- engine **Threads List** → **`threads.md`** · **Characters List** → **`npcs.md`**
- engine **seed deck** → **`seeds.md`** · engine **archive** → **`dynasty.md`** + the home files

## Notes

- **State files outrank memory.** If memory and a file disagree, the file wins.
- Commit your `state/` after a session — the saga is meant to be version-controlled and preserved.
- The **game year is the master metronome** (`bridge/subsystems.md`); the Chaos
  Factor is scene-turbulence only and never overrides the scheduled GPC timeline.
