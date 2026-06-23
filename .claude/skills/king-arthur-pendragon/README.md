# king-arthur-pendragon

A self-contained solo **Game Master engine** for *King Arthur Pendragon* (5th edition). Claude runs the whole game — rolling every die honestly in the shell, enforcing traits and passions on the player knight, advancing the Great Pendragon Campaign year by year from 480 AD to 566, and continuing the saga through the dynasty when a knight falls.

It **runs standalone**, and it ships a **`bridge/`** that makes it a content companion for the **`mythic-gm`** engine — which, in this repo, is the default driver (see `/CLAUDE.md`).

## What's inside

- `SKILL.md` — the operating manual (laws, the loop, the adjudication ladder, where state lives, the two integration modes).
- `gm/` — the engine: `GM-LOOP.md` (master procedure), the three laws (`LETHALITY.md`, `PACING.md`, `STYLE.md`), the prose texture (`VOICE.md`), the dice roller (`roll.py` + `DICE.md`), and `MYTHIC.md` (the gap-filler contract with `mythic-gm`).
- `rules/` — Pendragon 5e: `core/` (chargen, skills, traits/passions, resolution, combat, injury, Glory, Winter Phase, equipment, society, GM stats), plus `battle/`, `estate/`, `warlord/`, `entourage/` supplements.
- `campaign/` — the Great Pendragon Campaign: `uther/` (480–495 in depth) and `gpc/` (485–566 year briefs + appendices).
- `generators/` — Arthurian-skinned oracle tables (courts, factions, NPCs, communities, religions, sites, adventure seeds, complications).
- `bridge/` — the **companion bridge** that exposes this skill to the `mythic-gm` engine: `system-profile`, `interpretation`, `subsystems`, `theme-weights`, `chaos-tendency`, `seeds`, `setting-canon`, `generators/` (registry + 120 verified tables), `adventures/`. Manifest: `bridge/bridge.md`.
- `assets/templates/` — blank `state/` files for starting a fresh campaign.

## How it pairs with mythic-gm

`mythic-gm` is a reusable solo-RPG engine that asks Fate Questions, runs Scene Tests, fires Random Events, and paces with a Chaos Factor. Pendragon already has its own rules, canon, generators, and a year-based loop, so the two combine under one rule:

> **Pendragon drives; Mythic fills gaps; Mythic incorporates Pendragon.**

Pendragon owns everything it resolves (rules, combat, traits/passions, Winter Phase, the scheduled GPC timeline). Mythic only answers what Pendragon leaves open — a yes/no about the world, an off-script scene, the timing of a complication, an open NPC choice — and where Mythic generates structure, Pendragon's generators and canon supply the substance. Full contract in `gm/MYTHIC.md`. The Mythic engine and its copyrighted tables are **not** bundled here; they live in the separately installed `mythic-gm` skill, which this skill calls.

## A note on content and copyright

This skill repackages a personal Pendragon campaign toolkit for the user's own solo play. The rules digests are derived from *King Arthur Pendragon* (© Greg Stafford / Chaosium), and the oracle tables are reskinned from *Worlds Without Number* (© Kevin Crawford / Sine Nomine). They are condensed references for running a game you own, **bundled for personal use** — not a replacement for the published books and not for redistribution. If you share this engine, replace the rules and generator digests with your own summaries, and keep the Mythic tables in `mythic-gm` (© Tana Pigeon / Word Mill Games), which this skill references rather than copies.
