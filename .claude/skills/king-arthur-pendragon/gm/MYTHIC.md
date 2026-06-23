# Mythic: The Gap-Filler

> **Scope:** this file is the contract for the **standalone mode** — when *Pendragon
> drives* and reaches down to Mythic as rung 4 (`SKILL.md` mode B). In this repo the
> **default is the reverse**: the `mythic-gm` engine drives and reads this skill's
> `bridge/` (see `/CLAUDE.md`). Both honor the same one rule below.

Mythic GME 2e is the **fourth tool** on the adjudication ladder — the oracle Pendragon never had. It does not replace any part of this engine. It runs *under* Pendragon and only where Pendragon is silent.

The companion **mythic-gm** skill supplies the Mythic engine (Fate Questions, Scene Tests, Random Events, the Meaning Tables) and rolls them honestly through its own scripts. This file is the contract between the two. Read it whenever you are about to reach past `rules/`, `campaign/`, and `generators/` for an answer.

## The one rule: Pendragon drives; Mythic fills gaps; Mythic incorporates Pendragon

1. **If Pendragon resolves it, Pendragon wins.** A rule in `rules/`, a fact in `campaign/` or `state/`, a stat block, a scheduled GPC event, a trait or passion roll — these are answered by Pendragon, rolled on `gm/roll.py`, and Mythic never touches them. There is no Fate Question about whether the Saxon's axe hits; that is a Sword-vs-axe opposed roll.
2. **Mythic answers only the open questions Pendragon leaves.** Where no rule, no canon, and no fitting generator decides the matter, Mythic decides — and the answer is recorded back to `state/` and `campaign/` as new canon (per `generators/00-using-oracles.md`: roll honestly, interpret in fiction, fix the result).
3. **When Mythic generates structure, Pendragon fills the substance.** Mythic tells you *whether* and *when* something happens and *what kind* of thing it is. The *face* of it comes from Pendragon first — a generator, a statted NPC, the year brief — and only falls through to Mythic's Meaning Tables when Pendragon has nothing. If Pendragon already specifies the content, you do not roll Meaning at all; you incorporate what Pendragon says.

The discipline of `gm/LETHALITY.md` binds every Mythic roll exactly as it binds a Pendragon roll: rolled in the shell, shown, applied as rolled, never softened. A Mythic "No" is a real No. A bad Random Event is not rescued.

## The four gaps Mythic fills (and nothing else)

**1. Yes/no world questions — the Fate Question.** When the player tests reality and neither a rule nor canon answers it: *Is the postern guarded tonight? Has word of the feud reached the next valley? Does the ferryman know the ford is watched?* Set odds from the fiction, then ask Mythic with the current Chaos Factor. Pendragon has no native yes/no oracle; this is the gap Mythic most often fills.

**2. Emergent off-script scenes — the Scene Test.** The year brief and `campaign/` schedule the campaign's spine. When the player rides off that spine into ground the books don't cover, frame the **Expected Scene**, then run a Scene Test against Chaos: it proceeds as expected, is **Altered**, or is **Interrupted** by something the world pushes in. This is the structured form of `gm/PACING.md`'s stall-breaker — use it for open exploration, not for scheduled court/battle/Winter Phase beats (those are Pendragon's and fire on their own clock).

**3. When a complication fires — the Random Event.** Mythic decides the *timing* (a Fate Question's doubles, or an Interrupt). For the *content*, go to `generators/08-complications-twists.md` or `generators/07-adventure-seeds.md` first — they are Arthurian-true; Mythic's Event Focus only chooses which lever (an NPC acts, a thread advances, a new thing enters), and its Meaning Tables are the last resort when the Pendragon generators give you nothing to seize.

**4. Genuinely open NPC choices.** `gm/GM-LOOP.md` §4 stands: NPCs act from their written stats, traits, passions, and motives — that is Pendragon, and it wins. Reach for Mythic only when a consequential NPC faces a choice the fiction genuinely leaves open. NPCs act to win; never roll Mythic to find the *convenient* option for them.

If a question is not one of these four, it is Pendragon's. Do not invent a Fate Question to avoid looking up a rule.

## How to call it

The Mythic engine lives in the installed **mythic-gm** skill, beside this campaign. Resolve its directory the same way you found this campaign's other skills (the skill loader exposes the path; it contains `scripts/dice.py`, `scripts/oracle.py`, `scripts/state.py`). Below, `<mythic>` is that directory. Every Mythic roll runs in the shell and is shown, exactly like `gm/roll.py`.

| Gap | Command |
|---|---|
| Fate Question (yes/no) | `python3 <mythic>/scripts/dice.py fate <odds> <CF>` |
| Scene Test (off-script) | `python3 <mythic>/scripts/dice.py scene <CF> --mode pure` |
| Random Event content lever | `python3 <mythic>/scripts/oracle.py event-focus` then `oracle.py meaning <table>` |
| Pick an open thread/NPC at random | `python3 <mythic>/scripts/oracle.py list <count>` (roll against the open set in `state/threads.md` / `state/npcs.md`) |

Odds vocabulary (9): `Certain`, `"Nearly Certain"`, `"Very Likely"`, `Likely`, `50/50`, `Unlikely`, `"Very Unlikely"`, `"Nearly Impossible"`, `Impossible`.

**If mythic-gm is not installed** (standalone fallback): keep playing on Pendragon alone. For a yes/no, set a rough probability from the fiction and roll d% in the shell (`python3 gm/roll.py d100` — under the probability = yes); for timing/complications, use `generators/07` and `generators/08` directly. The campaign never stalls waiting for the oracle.

## State: no duplicate lists

Mythic's bookkeeping maps onto files that already exist — do not create parallel lists.

- **Chaos Factor** lives in `state/mythic.md` (1–9; −1 after a scene the knight mostly controlled, +1 after a chaotic one). It is a scene-level turbulence dial. The **game year remains the master metronome** (`gm/PACING.md`); Chaos never overrides the schedule.
- **Threads List = `state/threads.md`.** Mythic's "Threads List" is this file. When Mythic points a Random Event at a thread, roll among the **open** threads listed there.
- **Characters List = `state/npcs.md`.** Likewise for NPCs.
- `state/mythic.md` holds only the Chaos Factor, the current scene mode, and a one-line snapshot of the open threads/NPCs so a Mythic list-roll has something to roll on. Everything else stays in its home file.

## Dice discipline (both engines, one standard)

`gm/roll.py` owns every Pendragon resolution: skills, combat, traits, passions, Winter Phase, battle, aging, healing. `<mythic>/scripts/*.py` owns the narrative oracle: yes/no, scene shape, event timing, Meaning. They never collide because they answer different questions. Both are rolled in the shell, both are shown in the bracketed mechanics line, both are applied as rolled. An unrolled Mythic answer is a lie; a rolled-then-ignored one is worse.
