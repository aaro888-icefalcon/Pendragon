# Next-Session Start Prompt

Paste the block below to begin the next session. It points Claude at the live
state and resumes at the **spring-482 save point — the Hindon arc won**.

---

> **Let's continue my solo King Arthur Pendragon campaign — Sir Abisec of Stapleford ("Shake"), now Knight Banneret of Hindon.**
>
> Invoke the `king-arthur-pendragon` skill and run as my GM on the **`mythic-gm`** engine. The living state is in `campaigns/abisec-of-stapleford/state/` — that's the source of truth. Read `mythic.md`, `campaign.md`, `knight.md`, `threads.md`, `npcs.md`, `session-log.md`; the **Lists are JSON** (`threads.json` / `characters.json` / `adventure.json`), viewed with `state.py thread|char show <C>` and the live List the dice roll. Boot per `/CLAUDE.md`: load the bridge (`bridge.py summary <B>`), read the state, give me a ≤4-sentence recap, then play.
>
> **Resolution discipline (binding — `/CLAUDE.md` + Ruling #29):** at every uncertain PC moment roll the **Pendragon check FIRST** on `gm/roll.py` (skill / trait / passion / combat); **test traits & passions when the fiction triggers them** (I may invoke a passion for inspiration: +10 success / +20 crit / madness on a fumble); **fire `tick.py` at each bookkeeping** (Glory, thread pressure, scheduled GPC events, faction turn, Winter Phase); **set CF at each scene's start = previous ±1 by outcome-mastery** (not composure). Reserve **Mythic Fate Questions** for world yes/no, off-script framing, complication timing, and genuinely-open NPC choices (rung 4 only).
>
> **Where we are — spring 482, Sarum, Chaos Factor 2.** I won the Hindon hearing on the King's floor: created **Knight Banneret**, granted **Hindon's caput** (~£55) to hold from the Crown on a sworn **perpetual-fealty vow** (mine till the line fails; the western road guarded for Uther's heirs). **Gwythyr of Mere was denied** the valley (now a smooth, slighted rival). **Lady Senara was pardoned.** I then swore the King homage — new passion **Loyalty (Uther) 10**, pointedly under **Loyalty (Roderick) 15**: the King is now legally first, Roderick still first in the heart. **Vagon reverts to Roderick**; Stapleford stays the family seat. Glory **~2,594** (next Bonus Point at 3,000).
>
> **What's open:** tell **Senara** she was pardoned at my word (she still hates me — the long game begins); **build Hindon's defenses** (~£50 plan: town enclosure + gateworks + wet moat, moat to the castle, two towers N & S — I hold ~£94); the **marriage / heir** question (Ulfius openly floated the Senara marriage that ends the whole quarrel; Lady Adwen of Wilton still waits; I've no heir and nearly died twice); **Gwythyr's grudge** + the **unproven suspicion he's the second doubted lord** (Idnerth's dying word — no proof; "mind your back with the careful man"); **Ulfius** an ailing patron to tend; **Idris's** unpaid debt (his mother **Gwenllian** rebuffed me); **Achil** mending at Stapleford. Backdrop: the GPC 482 events (Cadwy/Summerland accord, sheriffs appointed) and the game year rolling toward its adventure season and Winter Phase.
>
> Honest dice in the shell, shown, never fudged. Terse, concrete, dialogue-first voice; mechanics in one bracketed line; never narrate my interior. Commit `state/` after the session. Pick up where I name where I go first — start with the recap and my opening choice.

---

## Quick GM reference (start-of-session)

- **Knight:** Sir Abisec, **Knight Banneret of Hindon**, age 23, Glory **~2,594** (next Bonus Point at 3,000). Sword 16 · Lance 16 · Battle 18 · Horsemanship 15 · First Aid 15 · Courtesy 13 (Orate only 3). Famous traits: **Valorous 16, Honor 16**. Passions: **Loyalty (Roderick) 15 · Loyalty (Uther) 10 · Love (family) 15 · Hospitality 15 · Hate (Saxons) 14**. HP 25/25. Maimed: DEX 11 / APP 11 + chest scar. Economic grade Superlative. **Pending experience checks (WP 482): Merciful, Honor, Courtesy.**
- **Holdings:** **Hindon's caput** — Crown grant, held as banneret on the vow (shell-keep DV 9/13/2 + mill + wool-town + home manors, ~£55) · **Stapleford** (family seat, under Salisbury). Vagon returned to Roderick. **~£94 liquid** (after the ~£50 build).
- **Two lords:** King Uther (homage for Hindon; Loyalty 10; legally first) · Count Roderick (reserved liege for Stapleford + lifelong mentor; Loyalty 15; first in the heart). The gap is a live future tension.
- **Chaos Factor 2** (Quiet). Year: **spring 482** (Uther period); on-script GPC spine.
- **Don't forget:** Pendragon checks lead (Ruling #29); fire `tick.py` at bookkeeping (Glory's been owed — accrue it); state-files outrank memory; the game year is the master metronome; commit `state/` at session end.
