# Pendragon

A ready-to-run table for a **solo *King Arthur Pendragon* campaign** with Claude
as Game Master. It pairs two cooperating skills — one that *is* Pendragon, one
that supplies the solo-play oracle Pendragon never had — and gives the saga a
home to live in.

## Get playing

Open this repo with Claude Code and say something like:

> *"Be my GM — let's start a Pendragon campaign."*
> *"Continue my campaign."*

Claude reads [`CLAUDE.md`](CLAUDE.md), drives the **`king-arthur-pendragon`**
skill, and rolls every die honestly in the shell. To begin a new saga it runs
character creation and opens at Salisbury, spring **480 AD**, under King Uther.

## What's in here

```
CLAUDE.md                 the orchestration layer — how the two engines run a game together
.claude/skills/
  king-arthur-pendragon/  the driver: Pendragon 5e rules, the Great Pendragon Campaign, generators, the GM loop
  mythic-gm/              the gap-filler: Mythic GME 2e — Fate Questions, Scene Tests, Random Events, Chaos
campaigns/                your living saga state (one folder per campaign) — see campaigns/README.md
```

## How the two engines fit together

> **Pendragon drives; Mythic fills gaps; Mythic incorporates Pendragon.**

`king-arthur-pendragon` owns everything it can resolve — rules, combat,
traits/passions, Glory, the Winter Phase, the scheduled 480–566 timeline.
`mythic-gm` answers only what Pendragon leaves open: a yes/no about the world,
an off-script scene, the timing of a complication, an open NPC choice. Both
engines roll real dice in the shell and never soften the result. The full
contract is in
[`.claude/skills/king-arthur-pendragon/gm/MYTHIC.md`](.claude/skills/king-arthur-pendragon/gm/MYTHIC.md);
the wiring is in [`CLAUDE.md`](CLAUDE.md).

## A note on content & copyright

The skills repackage personal campaign material for solo play. Pendragon rules
are derived from *King Arthur Pendragon* (© Greg Stafford / Chaosium); the
generator tables are reskinned from *Worlds Without Number* (© Kevin Crawford /
Sine Nomine); the oracle tables are *Mythic GME 2e* / *The Adventure Crafter*
(© Tana Pigeon / Word Mill Games). They are condensed references bundled for
personal use with games you own — not a replacement for the published books,
and not for redistribution.
