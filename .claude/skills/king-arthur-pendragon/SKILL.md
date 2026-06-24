---
name: king-arthur-pendragon
description: King Arthur Pendragon (5th edition) companion for the mythic-gm engine — the Pendragon 5e ruleset, the Great Pendragon Campaign (480–566 AD), Arthurian generators, and the prose laws, exposed to the engine through bridge/. Use whenever the user wants to play, start, or continue a solo Pendragon or Arthurian-knight campaign, create a Pendragon knight, run a game year (court, adventure, battle, Winter Phase), or resolve Pendragon rules (skills, traits, passions, combat, Glory, aging, estate management, mass battle). Triggers on "Pendragon", "King Arthur Pendragon", "KAP", "play a knight", "be my GM for King Arthur", "Great Pendragon Campaign", "Knights of Logres", "Uther", "Salisbury 480", "Winter Phase", "Glory". Honest dice are rolled in the shell and never fudged; player knights can die and the saga continues through the heir. The mythic-gm engine drives the solo-play loop and reads this skill's bridge/; see /CLAUDE.md.
license: Personal-use repackaging of the user's own campaign material. See README.md.
---

# King Arthur Pendragon — the world (companion for the mythic-gm engine)

This skill is the **Pendragon companion** for the **`mythic-gm`** engine. The
engine drives the solo-play loop — scenes, the Scene Test, Chaos, Fate Questions,
Random Events, Turning Points, and the no-softening discipline. This skill
supplies the **world**: the King Arthur Pendragon (5th ed.) ruleset, the Great
Pendragon Campaign (480–566 AD from Salisbury under Uther), the Arthurian
generators, and the prose laws — all exposed to the engine through **`bridge/`**.

**It does not drive; the engine does.** Pendragon supplies the *substance*; Mythic
the *structure*. The wiring is `/CLAUDE.md`; the companion manifest is
`bridge/bridge.md`.

## How play runs

The engine loads this skill's bridge at session start
(`bridge.py summary <bridge>`) and runs **THE TURN**, resolving each uncertain
moment down the ladder — a Pendragon **rule** (`bridge/system-profile.md` →
`gm/roll.py`), then the **year brief / adventure** (`campaign/`,
`bridge/adventures/`), then a **generator** (`bridge/generators/registry.md`),
and only then a **Mythic** default — Pendragon (substance) always outranking the
Mythic default (structure). You never run a separate Pendragon loop; you supply
the answers the engine's hooks ask for, read through `bridge/interpretation.md`.
Full ladder, paths, and commands: **`/CLAUDE.md`**.

## The three laws (binding every step — surfaced through `bridge/interpretation.md`)

1. **Honest danger** (`gm/LETHALITY.md`) — all dice rolled in the shell and shown; outcomes apply as rolled; the world doesn't scale; player knights can and will die, and the campaign continues through the dynasty.
2. **Forward motion** (`gm/PACING.md`) — the game year is the metronome; canonical GPC events fire on schedule; stalls break with events, not atmosphere.
3. **Prose discipline** (`gm/STYLE.md`, texture in `gm/VOICE.md`) — hard word budgets; one concrete detail beats three adjectives; mechanics in one bracketed line; dialogue over narration; never narrate the knight's interior.

## Where the campaign state lives

Living state is written under `campaigns/<name>/state/`, never inside the skill.
The engine's loop-state maps onto these existing files (no duplicate bookkeeping
— see `/CLAUDE.md`).

- **Continuing:** the engine reads the existing `state/` and resumes (recap ≤4 sentences, then play).
- **Starting:** the engine runs character creation (`rules/core/01-character-creation.md`) with honest rolls, copies `assets/templates/` into `state/` (`campaign.md`, `knight.md`, `dynasty.md`, `session-log.md`, `mythic.md`, `seeds.md`) and scaffolds the JSON Lists (`state.py init` → `threads.json`, `characters.json`, `adventure.json` — each List entry carries its own `dossier`+`status`; there is no `npcs.md`/`threads.md`), and opens at Salisbury, 480 AD (`campaign/uther/05-timeline-480-495.md`).

State files outrank memory. If memory and a file disagree, the file wins.

## Directory map — load only the file you need, never whole directories

| Path | Contents |
|---|---|
| `bridge/` | **The companion contract the engine reads** — `bridge.md` (manifest), `system-profile`, `interpretation`, `subsystems`, `theme-weights`, `chaos-tendency`, `seeds`, `setting-canon`, `generators/` (registry + 120 verified tables), `adventures/` |
| `gm/` | The Pendragon **laws** (`LETHALITY.md`, `PACING.md`, `STYLE.md`, `VOICE.md`) and the **dice roller** the bridge calls (`roll.py` / `DICE.md`) |
| `rules/core/` | 5th ed.: chargen, skills, traits/passions, resolution, combat, injury, Glory, Winter Phase, equipment, society, GM stat blocks |
| `rules/battle/` | Book of Battle (mass combat) + Book of Armies (enemy army stat blocks) |
| `rules/estate/` | Manor economics, investments, estate events (landed knights) |
| `rules/warlord/` | Baronial play: honors, vassals, castles, baronial politics |
| `rules/entourage/` | Followers: squires, wives, mesnie, household |
| `campaign/uther/` | 480–495 in depth: court, NPCs, timeline, adventures, Logres gazetteer — **primary for 480–495** |
| `campaign/gpc/` | 485–566 year-by-year briefs by period + appendices (creatures, faerie, notable NPC stats) |
| `generators/` | The source Arthurian oracle markdown (courts, factions, NPCs, communities, religions, sites, adventure seeds, complications), compiled into `bridge/generators/*.json` by `bridge/generators/build_generators.py` |
| `assets/templates/` | Blank `state/` files for starting a fresh campaign |

## Standing orders

- State files outrank memory. Mechanics outrank vibes. The dice outrank you.
- Year briefs include "If the player does nothing" — the world advances regardless.
- Rulings made in play are precedent: log them in `state/session-log.md` and keep them.
- Traits and passions are rolled and enforced for the player knight too.
- When the books run out, roll a `bridge/generators/` table — don't improvise table results.
- Every die — Pendragon's `gm/roll.py` and the engine's oracle scripts alike — is rolled in the shell, shown, and applied as rolled.
