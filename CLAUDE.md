# Pendragon — Solo Play Environment

This repository is a ready-to-run table for a **solo King Arthur Pendragon
campaign** with Claude as Game Master. It runs on the **mythic-gm v2
architecture**: a content-free **engine** plus a **companion** that fills the
engine's hooks through a `bridge/`. This file is the orchestration layer that
wires them together.

## The architecture: engine + companion (bridge)

| Skill | Role | Lives in |
|---|---|---|
| **`mythic-gm`** | **The engine (the driver).** Mythic GME 2e + The Adventure Crafter: it runs the scene / Chaos / Fate-Question / Random-Event / Turning-Point loop, the no-softening discipline, and all oracle tables. Content-free and shared. | `.claude/skills/mythic-gm/` |
| **`king-arthur-pendragon`** | **The companion (the world).** The full Pendragon 5e ruleset, the Great Pendragon Campaign (480–566), Arthurian generators, and prose laws — exposed to the engine through `bridge/`. | `.claude/skills/king-arthur-pendragon/` |

Both roll **real dice in the shell and never fudge** (`python3 …`). The engine
verifies clean (`python3 .claude/skills/mythic-gm/scripts/build_data.py`), and
the bridge validates clean
(`python3 .claude/skills/mythic-gm/scripts/bridge.py validate .claude/skills/king-arthur-pendragon/bridge`).

## The one rule of integration

> **Mythic drives the loop; the Pendragon bridge fills every hook; Pendragon
> supplies the substance, Mythic the structure.**

The engine owns the *machinery* — scenes, the Scene Test, Chaos math, Fate
Questions, Random Events, Turning Points, the seed/list machinery, the
discipline. The companion owns the *world* — how things resolve, how NPCs think,
what advances at scene's end, what content fills a result. When the engine asks a
hook, it reads the bridge override (below) and uses **Pendragon's answer**; only
where the bridge is silent does it fall to the Mythic/AC default. Whether / when /
what-kind comes from Mythic; the *face* of it comes from Pendragon first — a
rule, the year brief, a statted NPC, a generator — and only falls to Mythic's
Meaning Tables when Pendragon has nothing.

## Default operating mode: **Mythic drives, Pendragon companion (strong)**

When the user says *"play Pendragon," "be my GM," "start/continue my campaign,"*
or anything Arthurian:

1. **Invoke the `mythic-gm` skill** and run it as the engine (`mythic-gm/SKILL.md`).
2. **Load the companion bridge** at session start:
   `python3 .claude/skills/mythic-gm/scripts/bridge.py summary .claude/skills/king-arthur-pendragon/bridge`
   — use a bridge override where present, else the engine default.
3. **Boot / Session Zero, then run THE TURN** (`mythic-gm/SKILL.md`): frame → Scene Test → play (resolve via the bridge) → advance plot → **bookkeep, firing the Pendragon world-tick** → repeat.

The companion is **strong**: the engine reads `bridge/interpretation.md` on every
oracle/NPC moment, fires `bridge/subsystems.md` (the game-year metronome,
scheduled GPC events, thread pressure, Winter Phase, Glory) at every bookkeeping
step via `tick.py`, and can frame Expected Scenes from the ingested Pendragon
content in `bridge/adventures/`.

## The resolution ladder (inside the engine's TURN)

Never resolve by vibes what a procedure resolves. The engine runs the loop;
within it, resolve each uncertain moment by walking this ladder — Pendragon
(substance, rungs 1–3) always outranks the Mythic default (structure, rung 4):

1. A specific **rule** → `bridge/system-profile.md` → roll it on `king-arthur-pendragon/gm/roll.py` (d20 roll-under; combat; traits/passions; Winter Phase; battle).
2. The **year brief / adventure** → `king-arthur-pendragon/campaign/` and the ingested `bridge/adventures/`.
3. A roll on a **generator** → `bridge/generators/registry.md` (120 verified tables), rolled with `dice.py table <path>`.
4. A **Mythic oracle** for what Pendragon leaves open — a yes/no Fate Question, an off-script Scene Test, the timing/lever of a complication, a genuinely open NPC choice. Read it through `bridge/interpretation.md`.
5. A **GM ruling** — state it, log it in `state/session-log.md`, keep it forever.

## The bridge (the companion contract)

`.claude/skills/king-arthur-pendragon/bridge/` — declared in `bridge/bridge.md`:

| Engine hook | Bridge file | What it supplies |
|---|---|---|
| `resolve` | `system-profile.md` | Pendragon 5e resolution & combat → `gm/roll.py` |
| `meaning` | `interpretation.md` | **GM/NPC lens (strong): how to read the oracle, how Logres NPCs act, prose laws** |
| `chaos` | `chaos-tendency.md` | start 5; floors for the Anarchy / battle / faerie |
| `themes` | `theme-weights.md` | fixed chivalric-tragedy theme weights |
| `generate:character` / `generate:element` | `generators/registry.md` (+ `generators/*.json`) | the Arthurian oracle deck |
| `world-tick` | `subsystems.md` | **the year metronome, GPC events, thread pressure, Winter Phase, Glory (strong)** |
| `seeds` | `seeds.md` | seed-deck sources (year brief, threads, generators) |
| `adventure-ingest` | `adventures/` | the Uther adventures as sandbox clusters |
| (ground truth) | `setting-canon.md` | Logres canon, overrides recollection |

Generators are rebuilt/verified with `python3 bridge/generators/build_generators.py`
(human-readable sources in `bridge/generators/_sources/`).

## Paths & commands

- **Engine scripts** (all oracle randomness): `.claude/skills/mythic-gm/scripts/`
  — `dice.py` · `oracle.py` · `adventure_crafter.py` · `state.py` · `tick.py` · `bridge.py` · `build_data.py`.
- **Pendragon roller** (all task/combat resolution): `python3 .claude/skills/king-arthur-pendragon/gm/roll.py …`.
- **The bridge:** `.claude/skills/king-arthur-pendragon/bridge`.

| Need | Command |
|---|---|
| Load the companion | `python3 .claude/skills/mythic-gm/scripts/bridge.py summary .claude/skills/king-arthur-pendragon/bridge` |
| Scene Test (AC always on) | `python3 .claude/skills/mythic-gm/scripts/dice.py scene <CF>` |
| Fate Question (yes/no) | `python3 .claude/skills/mythic-gm/scripts/dice.py fate <odds> <CF>` (Pendragon-replacing rule → `--mode rule`) |
| Roll a Pendragon generator | `python3 .claude/skills/mythic-gm/scripts/dice.py table .claude/skills/king-arthur-pendragon/bridge/generators/<x>.json` |
| World-tick at bookkeeping | `python3 .claude/skills/mythic-gm/scripts/tick.py .claude/skills/king-arthur-pendragon/bridge <scene#>` |
| Turning Point | `python3 .claude/skills/mythic-gm/scripts/adventure_crafter.py turning-point …` |
| Chaos up/down | `python3 .claude/skills/mythic-gm/scripts/state.py chaos <+1\|-1> <CF>` |
| Pendragon task/combat | `python3 .claude/skills/king-arthur-pendragon/gm/roll.py check <skill>` · `opposed <a> <b>` · `<NdM>` |

Odds vocabulary (9): `Certain`, `"Nearly Certain"`, `"Very Likely"`, `Likely`,
`50/50`, `Unlikely`, `"Very Unlikely"`, `"Nearly Impossible"`, `Impossible`.

## Where the saga lives — `campaigns/`

The skills are **read-only content**. A campaign's living state is written under
`campaigns/`, never inside a skill:

```
campaigns/<campaign-name>/state/
    campaign.md      knight.md     dynasty.md
    npcs.md          threads.md    session-log.md     mythic.md     seeds.md
```

- **Starting a new campaign:** create `campaigns/<name>/state/`, copy every
  template from `king-arthur-pendragon/assets/templates/`, run character creation
  with honest rolls (`rules/core/01-character-creation.md`), and open at
  Salisbury, spring **480 AD**.
- **Continuing:** read the existing `state/` and resume (recap in ≤4 sentences,
  then play). **State files outrank memory.** Commit `state/` after a session.

### No duplicate bookkeeping (the engine ⇄ Pendragon state mapping)

The engine's loop-state lives in Pendragon's existing files — do not create
parallel ones:

- Engine **`campaign-state.md`** (Frame · Chaos · Lists snapshot · scene recap · drift counter) → **`state/mythic.md`**.
- Engine **`character-sheet.md`** (the PC the loop tracks) → **`state/knight.md`**.
- Engine **Threads List** → **`state/threads.md`** · **Characters List** → **`state/npcs.md`**.
- Engine **seed deck** → **`state/seeds.md`** (refreshed each bookkeeping from `bridge/seeds.md` sources).
- Engine **archive** (dead PCs, resolved threads) → **`state/dynasty.md`** + the home files.

The **game year is the master metronome** (`bridge/subsystems.md`); Chaos is
scene-turbulence only and never overrides the GPC schedule.

## The standing laws (binding every step)

The engine's discipline and Pendragon's laws reinforce each other:

- **Engine discipline** (`mythic-gm/references/discipline/`): honor the oracle, roll before you narrate, NPCs act to win, never soften an honest result, **Peril Points OFF**.
- **Pendragon laws** (surfaced through `bridge/interpretation.md`, sourced in `king-arthur-pendragon/gm/`):
  1. **Honest danger** (`LETHALITY.md`) — outcomes as rolled; knights can die; the saga continues through the heir.
  2. **Forward motion** (`PACING.md`) — the year is the metronome; GPC events fire on schedule; stalls break with events, not atmosphere.
  3. **Prose discipline** (`STYLE.md` / `VOICE.md`) — hard word budgets; one concrete detail over three adjectives; mechanics in one bracketed line; dialogue over narration; never narrate the knight's interior.

## Quick directory map (load only the file you need — never whole directories)

```
.claude/skills/mythic-gm/              THE ENGINE
  SKILL.md  COMPANION-SKILLS.md  CONVERSION.md
  scripts/      dice.py · oracle.py · adventure_crafter.py · state.py · tick.py · bridge.py · build_data.py
  data/         verified machine-rollable JSON (Mythic + Adventure Crafter)
  references/   playloop · discipline · mythic/ · adventure-crafter/ · adapting/ · genres/ · canon/
  assets/       templates/ · bridge-templates/   ·   agents/mythic-scout.md

.claude/skills/king-arthur-pendragon/  THE COMPANION
  SKILL.md
  bridge/       bridge.md · system-profile · interpretation · chaos-tendency · theme-weights
                subsystems · seeds · setting-canon · generators/ (registry + 120 *.json) · adventures/
  gm/           LETHALITY/PACING/STYLE/VOICE (the Pendragon laws) · DICE.md+roll.py (the roller the bridge calls)
  rules/        core/ · battle/ · estate/ · warlord/ · entourage/
  campaign/     uther/ (480–495) · gpc/ (485–566 year briefs + appendices)
  generators/   the source Arthurian oracle markdown (compiled into bridge/generators/)
  assets/templates/   blank state/ files for a new campaign

campaigns/                              living saga state (one folder per campaign) — see campaigns/README.md
```

(How this layout was produced from the older repo: `mythic-gm/CONVERSION.md`.)

## Session checklist

1. Identify the campaign under `campaigns/` (or start a new one).
2. Invoke `mythic-gm`; load the bridge (`bridge.py summary …`); run boot / Session Zero.
3. Run THE TURN: frame → Scene Test → play (resolve via the bridge ladder) → advance → bookkeep with `tick.py` → repeat.
4. Resolve down the ladder: Pendragon rule/canon/generator (substance) before the Mythic default (structure).
5. Roll every die in the shell and show it. Update `state/` on material changes.
6. At session end, write `state/` and commit so the saga is preserved.
