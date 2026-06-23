# Pendragon

A ready-to-run table for a **solo *King Arthur Pendragon* campaign** with Claude
as Game Master. It runs on the **mythic-gm v2 architecture** — a content-free
solo-RPG **engine** plus a Pendragon **companion** that fills the engine's hooks
through a `bridge/` — and gives the saga a home to live in.

## Get playing

Open this repo with Claude Code and say something like:

> *"Be my GM — let's start a Pendragon campaign."*
> *"Continue my campaign."*

Claude reads [`CLAUDE.md`](CLAUDE.md), drives the **`mythic-gm`** engine over the
**`king-arthur-pendragon`** companion bridge, and rolls every die honestly in the
shell. To begin a new saga it runs character creation and opens at Salisbury,
spring **480 AD**, under King Uther.

## What's in here

```
CLAUDE.md                 the orchestration layer — how the engine + companion run a game together
.claude/skills/
  mythic-gm/              THE ENGINE: Mythic GME 2e + Adventure Crafter — scenes, Fate Questions, Random Events, Chaos
  king-arthur-pendragon/  THE COMPANION: Pendragon 5e rules, the Great Pendragon Campaign, generators —
                          exposed to the engine via bridge/ (system-profile, interpretation, subsystems, generators…)
campaigns/                your living saga state (one folder per campaign) — see campaigns/README.md
```

## How the engine and companion fit together

> **Mythic drives the loop; the Pendragon bridge fills every hook; Pendragon
> supplies the substance, Mythic the structure.**

`mythic-gm` owns the *machinery* — scenes, the Scene Test, Chaos, Fate Questions,
Random Events, Turning Points, and the no-softening discipline. The
`king-arthur-pendragon` **bridge** owns the *world* — Pendragon 5e resolution and
combat, how Logres NPCs act, the year metronome and scheduled 480–566 events
(fired at every scene's end), and 120 verified Arthurian oracle tables. Both roll
real dice in the shell and never soften the result. The wiring is in
[`CLAUDE.md`](CLAUDE.md); the companion contract is in
[`.claude/skills/king-arthur-pendragon/bridge/bridge.md`](.claude/skills/king-arthur-pendragon/bridge/bridge.md),
and the migration that produced this layout is documented in
[`.claude/skills/mythic-gm/CONVERSION.md`](.claude/skills/mythic-gm/CONVERSION.md).
(The companion can also still run **standalone** as its own GM engine.)

## A note on content & copyright

The skills repackage personal campaign material for solo play. Pendragon rules
are derived from *King Arthur Pendragon* (© Greg Stafford / Chaosium); the
generator tables are reskinned from *Worlds Without Number* (© Kevin Crawford /
Sine Nomine); the oracle tables are *Mythic GME 2e* / *The Adventure Crafter*
(© Tana Pigeon / Word Mill Games). They are condensed references bundled for
personal use with games you own — not a replacement for the published books,
and not for redistribution.
