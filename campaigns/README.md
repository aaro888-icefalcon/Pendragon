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
      mythic.md        # the gap-filler's dial: Chaos Factor + scene mode + roll-snapshot
```

## Starting a new campaign

Copy every template into a fresh campaign's `state/`, then run character
creation with honest rolls:

```bash
mkdir -p campaigns/<campaign-name>/state
cp .claude/skills/king-arthur-pendragon/assets/templates/*.md campaigns/<campaign-name>/state/
```

Open at Salisbury, spring **480 AD**, under King Uther. Claude (driving the
`king-arthur-pendragon` skill) walks you through the rest per
`.claude/skills/king-arthur-pendragon/gm/GM-LOOP.md`.

## Notes

- **State files outrank memory.** If memory and a file disagree, the file wins.
- Commit your `state/` after a session — the saga is meant to be version-controlled and preserved.
- In the default mode (Pendragon drives), Pendragon's `state/` is the single
  source of truth; Mythic's bookkeeping folds into `threads.md`, `npcs.md`, and
  `mythic.md` rather than a separate file.
