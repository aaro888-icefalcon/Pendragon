# Mythic State

**Engine:** mythic-gm (companion skill) · resolution Fate Chart · discipline HARDCORE (no softening; Peril Points OFF)
**Mode now:** on-script — spine follows the year brief; **482** now (Vagon, spring). Use a **Scene Test** only when the knight rides off the brief into ground the books don't cover.
**Adventure Source:** on-script GPC spine (the year brief in `campaign/`) + the Pendragon bridge; Mythic/Adventure-Crafter drives only where the books fall silent.
**Lists — machine source of truth:** `state/threads.json` · `state/characters.json` · `state/adventure.json` (the dice roll *these*, any length, via the two-stage roll). The tables below + `state/threads.md` / `state/npcs.md` are the human snapshot — keep roughly in sync; mutate the JSON with `python3 .claude/skills/mythic-gm/scripts/state.py thread|char add|weight|remove <campaign>/state "<name>"`.

## Chaos Factor: 4

**Set it at each scene's START** = previous ±1 by whether the knight **mastered the outcome** (not his composure): −1 he controlled it · +1 it got away from him · ±2 only for a decisive triumph/catastrophe · hold on a wash. Clamp 1–9; baseline 5; floors Anarchy ≥5 / battle ≥4 / faerie ≥4. The game YEAR is the master metronome — CF is scene-tempo only, never overrides the GPC schedule.

**Pace ladder:** 1 Becalmed (porridge) · 2 Quiet (gossip, hawking) · 3 Settled (a journey, a dispute) · 4 Stirring (threads tug, something brews) · 5 Balanced/baseline (live contest, outcomes uncertain) · 6 Turbulent (events outrun him) · 7 Volatile (crisis — feud/battle looms, he reacts) · 8 Chaos (betrayal/ambush, ground giving way) · 9 Cataclysm (everything at once). *Poles: 0 ≈ nothing stirs; 10 ≈ assassination + half the realm dead + poisoned + Grail loose — beyond the dice.*
<!-- … 2: Day 3 mews recovery (controlled), held through downtime.
     2 → 3 → 2: Day 5 tournament (unhorsed, then won the field & rode out Brastias).
     2 (held): Twelfth Night eve — won the King's private audience.
     2 → 4: TWELFTH NIGHT TRIAL BY COMBAT — Abisec LOST, mortal wound, maimed; Idnerth cleared & free.
     4 → 5: spring 482 — Achil abducted by the Boar.
     5 → 2: the rescue & the storm of Hindon — Achil saved, Idnerth taken alive for the King's justice, the Boar arc CLOSED. The storm has passed; Abisec on top (a friend dead, Idris, the cost).
     2 (held): the Hindon close — inventory, the guard-swap, Custennin (ExcYes ally), the Senara solar scene; Abisec steered every scene (even the unwon Senara result, Fate No); CF steady at 2.
     ⚠ RECALIBRATION (system review): CF had stuck at 2 by over-reading Abisec's *composure* as "in control." Per the rule (start 5; +1 when the PC does NOT master the scene's outcome, −1 when he does), the run of reversals on the homecoming — Senara's rejection, Idnerth withholding the truth, Gwenllian's cold rebuff, the Boar-backer dead end (none in Abisec's control) — should have driven CF back up. **Reset 2 → 4**, and moved ±1 every scene by outcome-mastery hereafter (baseline 5; floors: Anarchy/battle/faerie). At CF 4–5 honest odds breathe again (Likely 50–65%).
     4 → 5: Idris's barrow — Gwenllian rebuffed Abisec (scene not mastered).
     5 → 4: the Sarum eve — Ulfius's strategic backing won, Gwythyr met & handled, the modest "bolt" pitch shaped (mastered). -->

## Threads List — snapshot of `state/threads.json` (the dice roll the JSON; detail in `state/threads.md`)
| # | Open thread (short) | Weight |
|---|---|---|
| 11 | Hindon's disposal — a **contested** prize (rival Gwythyr of Mere; King decides) | 3 |
| 12 | Lady Senara of Hindon (heiress/ward — marriage-pawn or future enemy) | 2 |
| 9 | Marriage / the dynasty (Adwen at Wilton; Senara via Hindon) | 2 |
| 14 | Idris's death (barrow, his mother, a debt of memory) | 1 |
| 13 | The second doubted lord (never named, still hidden) | 1 |
| 4 | Old-guard friction (Caradoc, thawing) | 1 |

## Characters List — snapshot of `state/characters.json` (the dice roll the JSON; detail in `state/npcs.md`)
| NPC | Weight |
|---|---|
| King Uther (favorable; the grantor of Hindon) | 3 |
| Baron Gwythyr of Mere (Abisec's rival for Hindon) | 2 |
| Count Roderick (liege; possible backer) | 2 |
| Lady Senara of Hindon (heiress/ward) | 2 |
| Sir Ulfius, Marshal of Logres (strong ally for Hindon) | 2 |
| Lady Adwen of Wilton (marriage prospect) | 1 |
| Sir Caradoc of Tilshead (unwon, thawing) | 1 |
| Father Custennin (Senara's chaplain — Abisec's committed ally inside the old household) | 1 |

## Notes
- Nothing here overrides `state/campaign.md`, `state/threads.md`, or `state/npcs.md`. On conflict, those win.
- Save point: **Spring 482 — AT SARUM, bedded the eve of the Hindon hearing (open court at dawn)** (Idris buried on the Plain, Gwenllian's debt unpaid; Idnerth to Crown keeping; the ward Senara hostile, her father having left her the lie, her maternal refuge [wastrel uncle Cadell] hollow; **court map** — Gwythyr 3 days at the King's ear & Uther leaning him, **Ulfius strongly FOR** Abisec, an **anti-Gwythyr bloc** to court; Abisec's play = the over-mighty-lord argument, the Gwythyr-whisper sheathed). Prior: **Spring 482, HINDON (fallen) — the Boar arc CLOSED.** (Column on the road: the dead **Idris** and the rescued **Achil**; the prisoner **Idnerth** bound for Sarum→London; the ward **Senara** [met, hostile, rejects Abisec's wardship] + her chaplain **Father Custennin** [Abisec's new ally].) Earlier: **Spring 482, HINDON (fallen) — the Boar arc CLOSED.** Abisec stormed Hindon, took Idnerth alive for the King's justice (→ scaffold), rescued Achil — at the cost of **Sir Idris dead** (First Aid failed). Hindon (a ~£150 **petty** barony — re-generated; £55 caput + a Magnificent £160 hall + scattered outliers) **forfeit to the Crown** — disposal **OPEN and contested** [Fate, spring 482: King grants it out (No to "keeps it"); Roderick not grabbing it (No → a possible backer); a greater rival IS in the field (Yes) = **Baron Gwythyr of Mere**, a Council baron pressing an ancient claim to the valley]. Abisec the **junior** claimant: best case banneret + the caput, worst case thanked while Hindon goes to Gwythyr. On Uther's clock. Glory ~2,494; Valorous 16 (famous); HP 25/25. About to ride home with the dead and the rescued. **Open:** #11 Hindon's disposal — a **contested** prize (rival **Gwythyr of Mere**); #12 **Lady Senara** (heiress/ward — marriage-pawn for whichever claimant, or future enemy); #13 the **second doubted lord**; #9 marriage (Adwen at Wilton; Senara possible); ~£144 to invest; **Idris's barrow** & home to Stapleford.
