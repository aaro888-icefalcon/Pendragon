# king-arthur-pendragon

The **King Arthur Pendragon** (5th edition) **content companion** for the
**`mythic-gm`** engine — the Pendragon 5e ruleset, the Great Pendragon Campaign
(480–566 AD), the Arthurian generators, and the prose laws. Claude rolls every
die honestly in the shell, enforces traits and passions on the player knight,
advances the campaign year by year, and continues the saga through the dynasty
when a knight falls.

The engine drives the solo-play loop and reads this skill's **`bridge/`** to fill
its hooks (see `/CLAUDE.md`). Pendragon supplies the substance; Mythic the
structure. This skill does not drive on its own.

## What's inside

- `SKILL.md` — the companion manual (what it supplies, the three laws, where state lives, the directory map).
- `bridge/` — **the companion contract the engine reads**: `bridge.md` (manifest), `system-profile`, `interpretation`, `subsystems`, `theme-weights`, `chaos-tendency`, `seeds`, `setting-canon`, `generators/` (registry + 120 verified tables), `adventures/`.
- `gm/` — the Pendragon **laws** (`LETHALITY.md`, `PACING.md`, `STYLE.md`, `VOICE.md`) and the **dice roller** the bridge calls (`roll.py` + `DICE.md`).
- `rules/` — Pendragon 5e: `core/` (chargen, skills, traits/passions, resolution, combat, injury, Glory, Winter Phase, equipment, society, GM stats), plus `battle/`, `estate/`, `warlord/`, `entourage/` supplements.
- `campaign/` — the Great Pendragon Campaign: `uther/` (480–495 in depth) and `gpc/` (485–566 year briefs + appendices).
- `generators/` — the source Arthurian oracle markdown (compiled into `bridge/generators/*.json`).
- `assets/templates/` — blank `state/` files for starting a fresh campaign.

## How it pairs with mythic-gm

`mythic-gm` is the **engine**: it runs the scene / Chaos / Fate-Question /
Random-Event / Turning-Point loop, the no-softening discipline, and all the
oracle tables. This skill is the **companion**: at session start the engine loads
this skill's `bridge/` (`bridge.py summary <bridge>`) and uses a bridge override
where present, else its own default. Pendragon then owns resolution, combat,
traits/passions, the year metronome, the scheduled GPC timeline, and the
generators; the engine owns the structure (whether/when/what-kind) and pacing.
Pendragon supplies the substance; Mythic the structure. The wiring is `/CLAUDE.md`;
the manifest is `bridge/bridge.md`. The Mythic engine and its copyrighted tables
are **not** bundled here — they live in the separately installed `mythic-gm` skill.

## A note on content and copyright

This skill repackages a personal Pendragon campaign toolkit for the user's own solo play. The rules digests are derived from *King Arthur Pendragon* (© Greg Stafford / Chaosium), and the oracle tables are reskinned from *Worlds Without Number* (© Kevin Crawford / Sine Nomine). They are condensed references for running a game you own, **bundled for personal use** — not a replacement for the published books and not for redistribution. If you share this engine, replace the rules and generator digests with your own summaries, and keep the Mythic tables in `mythic-gm` (© Tana Pigeon / Word Mill Games), which this skill references rather than copies.
