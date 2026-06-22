# Pendragon — Solo Play Environment

This repository is a ready-to-run table for a **solo King Arthur Pendragon
campaign** with Claude as Game Master. It bundles two cooperating skills and a
place to keep the living saga. When the user wants to play, this file is the
orchestration layer that wires the two engines together so the game runs
smoothly.

## The two engines

| Skill | Role | Lives in |
|---|---|---|
| **`king-arthur-pendragon`** | **The driver.** The full Pendragon 5e engine: rules, traits/passions, combat, Glory, Winter Phase, the Great Pendragon Campaign (480–566), Arthurian generators, and the year-based GM loop. | `.claude/skills/king-arthur-pendragon/` |
| **`mythic-gm`** | **The gap-filler oracle.** Mythic GME 2e + The Adventure Crafter: yes/no Fate Questions, Scene Tests, Random Events, Chaos Factor — the questions Pendragon has no native answer for. | `.claude/skills/mythic-gm/` |

Both roll **real dice in the shell and never fudge**. Both are already
installed and verified to run from this repo (`python3 …`).

## The one rule of integration

> **Pendragon drives; Mythic fills gaps; Mythic incorporates Pendragon.**

Resolve every uncertain moment by walking this ladder top to bottom; never
resolve by vibes what a procedure resolves (full text in
`.claude/skills/king-arthur-pendragon/gm/GM-LOOP.md` §3 and `gm/MYTHIC.md`):

1. A specific **rule** in `king-arthur-pendragon/rules/` (core first, then the supplement).
2. The **year brief / adventure text** in `king-arthur-pendragon/campaign/`.
3. A roll on a **generator** table in `king-arthur-pendragon/generators/`.
4. A **Mythic oracle** — *only* for what Pendragon leaves open: a yes/no Fate
   Question, an off-script Scene Test, the timing of a complication, or a
   genuinely open NPC choice.
5. A **GM ruling** — state it, log it in `state/session-log.md`, keep it forever.

Steps 1–3 (Pendragon) always outrank step 4 (Mythic). If a rule, stat block,
canon fact, or scheduled GPC event already decides something, Mythic adopts
that answer instead of rolling. Mythic supplies *structure* (whether / when /
what kind); Pendragon's generators and canon supply the *substance*.

## Default operating mode: **A — Pendragon drives**

This is the recommended mode and the default for this repo. When the user says
*"play Pendragon," "be my GM," "start/continue my campaign,"* or anything
Arthurian:

1. **Invoke the `king-arthur-pendragon` skill** and run it as the GM. It owns
   the loop, the laws, and the dice.
2. Keep `mythic-gm` available as **rung 4** of the ladder above. When you hit
   one of the four gaps, call its scripts (concrete commands below) and show
   the roll, exactly like a Pendragon roll.

> Mode B (Mythic drives, Pendragon is just its ruleset+setting via
> `king-arthur-pendragon/compat/`) exists but is **not** the default here. Use
> it only if the user explicitly asks to run the Mythic engine with Pendragon
> as content. See `king-arthur-pendragon/compat/README.md`.

## Resolving the `<mythic>` path

`king-arthur-pendragon/gm/MYTHIC.md` calls the oracle as `<mythic>/scripts/…`.
In this repo, `<mythic>` is a fixed path — use it verbatim:

```
.claude/skills/mythic-gm/scripts/
```

| Gap (rung 4) | Command |
|---|---|
| Fate Question (yes/no) | `python3 .claude/skills/mythic-gm/scripts/dice.py fate <odds> <CF>` |
| Scene Test (off-script scene) | `python3 .claude/skills/mythic-gm/scripts/dice.py scene <CF> --mode pure` |
| Random Event lever / Meaning | `python3 .claude/skills/mythic-gm/scripts/oracle.py event-focus` then `… oracle.py pair actions` |
| Pick an open thread/NPC at random | `python3 .claude/skills/mythic-gm/scripts/oracle.py list <count>` |
| Chaos Factor up/down after a scene | `python3 .claude/skills/mythic-gm/scripts/state.py chaos <+1\|-1> <CF>` |

Odds vocabulary (9): `Certain`, `"Nearly Certain"`, `"Very Likely"`, `Likely`,
`50/50`, `Unlikely`, `"Very Unlikely"`, `"Nearly Impossible"`, `Impossible`.

Pendragon's own dice are always `python3 .claude/skills/king-arthur-pendragon/gm/roll.py …`.

## Where the saga lives — `campaigns/`

The skills are **read-only content**. A campaign's living state is written to a
working directory in this repo, never inside a skill:

```
campaigns/<campaign-name>/state/
    campaign.md      knight.md     dynasty.md
    npcs.md          threads.md    session-log.md     mythic.md
```

- **Starting a new campaign:** create `campaigns/<name>/state/` and seed it by
  copying every template from
  `.claude/skills/king-arthur-pendragon/assets/templates/`. Run character
  creation with honest rolls (`rules/core/01-character-creation.md`), then open
  at Salisbury, spring **480 AD**.
- **Continuing:** read the existing `state/` and resume per `gm/GM-LOOP.md` §0
  (recap in ≤4 sentences, then play).

**State files outrank memory.** If memory and a file disagree, the file wins.
Commit the `state/` after a session to preserve the saga (it is version-controlled on purpose).

## No duplicate bookkeeping (the seam that keeps them compatible)

Mythic's lists map onto files that already exist — do not create parallel ones:

- **Chaos Factor** → `state/mythic.md` (1–9; the year is still the master metronome).
- **Threads List** → `state/threads.md`.
- **Characters List** → `state/npcs.md`.

`state/mythic.md` holds only the Chaos dial, the current scene mode, and a
one-line snapshot of open threads/NPCs so a Mythic list-roll has something to
roll against. Everything else stays in its home file. (Mythic-gm's own
`campaign-state.md` is **not** used in Mode A — Pendragon's `state/` is the source of truth.)

## The standing laws (binding every step)

From `king-arthur-pendragon/gm/`, in priority order:

1. **Honest danger** (`LETHALITY.md`) — dice rolled in the shell and shown; outcomes as rolled; knights can die; the saga continues through the heir.
2. **Forward motion** (`PACING.md`) — the year structure is the metronome; canonical GPC events fire on schedule; stalls break with events, not atmosphere.
3. **Prose discipline** (`STYLE.md` / `VOICE.md`) — hard word budgets; one concrete detail over three adjectives; mechanics in one bracketed line; dialogue over narration.

Mythic adds its own spine when invoked (`mythic-gm/references/discipline/`):
honor the oracle, NPCs act to win, never soften an honest result, Peril Points OFF.

## Quick directory map (load only the file you need — never whole directories)

```
.claude/skills/king-arthur-pendragon/
  SKILL.md                operating manual (laws, loop, ladder, modes)
  gm/                     GM-LOOP.md · LETHALITY/PACING/STYLE/VOICE · DICE.md+roll.py · MYTHIC.md (the contract)
  rules/                  core/ · battle/ · estate/ · warlord/ · entourage/
  campaign/               uther/ (480–495 in depth) · gpc/ (485–566 year briefs + appendices)
  generators/             Arthurian oracle tables (courts, factions, NPCs, sites, seeds, complications)
  compat/                 Pendragon reshaped for Mode B (Mythic-driven)
  assets/templates/       blank state/ files for a new campaign

.claude/skills/mythic-gm/
  SKILL.md                play loop, discipline, routing, script commands
  scripts/                dice.py · oracle.py · adventure_crafter.py · state.py · system.py · build_data.py
  data/                   verified machine-rollable JSON tables
  references/             playloop · discipline · mythic/ · adventure-crafter/ · adapting/ · genres/ · canon/

campaigns/                living saga state (one folder per campaign) — see campaigns/README.md
```

## Session checklist

1. Identify the campaign under `campaigns/` (or start a new one).
2. Invoke `king-arthur-pendragon`; run its boot sequence (`gm/GM-LOOP.md` §0).
3. Play the loop: court → adventures → battle → Winter Phase → state update.
4. Adjudicate down the ladder; reach for `mythic-gm` only at rung 4.
5. Roll every die in the shell and show it. Update `state/` on material changes.
6. At session end, write `state/` and commit so the saga is preserved.
