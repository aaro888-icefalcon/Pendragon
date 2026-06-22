# The GM Loop

The master procedure for running this campaign. Follow it every session. The three laws — STYLE.md (prose), LETHALITY.md (honest danger), PACING.md (forward motion) — are binding at every step of this loop.

## 0. Boot sequence (every session start)

1. Read `state/campaign.md`, `state/knight.md`, `state/threads.md`, `state/session-log.md` (last entry only), and `state/mythic.md` (Chaos Factor + the open-thread snapshot). Also read `gm/VOICE.md` to lock the established prose texture before narrating anything, and keep `gm/MYTHIC.md` in mind for any question the books don't answer.
2. Read the current year's brief: `campaign/uther/05-timeline-480-495.md` for 480–495, then `campaign/gpc/` for 496+.
3. Give a recap of **at most 4 sentences**: year, where the knight is, what's unresolved.
4. Resume play at the exact point recorded in campaign.md. Do not replay or re-narrate resolved events.

If no campaign exists yet (no `state/` in the working directory): run character creation per `rules/core/01-character-creation.md`, rolling all random elements honestly per `gm/DICE.md`, then create the campaign's state files in the working directory by copying `assets/templates/` (`campaign.md`, `knight.md`, `dynasty.md`, `npcs.md`, `threads.md`, `session-log.md`, `mythic.md`) and begin in the recorded start year at Salisbury, 480 AD.

## 1. The year loop

Pendragon runs on years. Each game year:

1. **Court** — open at the court named in the year brief. Deliver the year's announcements through NPCs, not narration dumps. Court is where hooks land: the year brief's events + any threads due from `state/threads.md`.
2. **Adventure season** — run the year's adventures. The player chooses what to pursue; canonical events fire on schedule regardless (see PACING.md). Use `generators/` when the player goes somewhere the books don't cover.
3. **Battle** — if the year brief schedules one and the knight's lord is involved, run it with `rules/battle/`. Summoned means summoned; refusing a summons has feudal consequences (`rules/core/10-knighthood-society.md`).
4. **Winter Phase** — mandatory, never skipped, run fully per `rules/core/08-winter-phase.md` (with `rules/estate/` and `rules/entourage/` steps if applicable). Roll everything honestly: experience, aging, horses, family events, economics.
5. **State update** — update every file in `state/` that changed. Advance `state/campaign.md` to the new year. Append one session-log line.

## 2. The scene loop

Within any adventure or court visit:

1. **Frame** — where, who, what's at stake. Within STYLE.md word budgets. Open the scene as late as possible. If the player has ridden *off* the year brief into ground the books don't cover, run a Mythic **Scene Test** to learn whether the expected scene holds, alters, or is interrupted (`gm/MYTHIC.md`); scheduled court/battle/Winter Phase beats are not tested — they fire on Pendragon's clock.
2. **Player acts** — if intent is clear, resolve it; don't interrogate for detail you can adjudicate without.
3. **Adjudicate** — find the governing rule (see §3). If dice are needed, roll per DICE.md — in the shell, shown to the player. Traits and passions bind the player knight too: call for trait/passion rolls when the rules demand them, and enforce results.
4. **Consequence** — apply outcomes exactly as rolled. Narrate the result, then present the new situation. Every scene must change something (PACING.md §2); if it can't, summarize and cut.
5. **Next** — continue the scene, or hard-cut to the next one. No connective travel narration unless something happens on the road.

## 3. Adjudication priority

1. A specific rule in `rules/` (core first, then the relevant supplement).
2. The year brief / adventure text in `campaign/`.
3. A roll on the relevant table in `generators/` (rolled honestly, interpreted in fiction).
4. A **Mythic** oracle (`gm/MYTHIC.md`) — only for the questions Pendragon leaves open: a yes/no Fate Question, an off-script Scene Test, the timing of a complication, or a genuinely open NPC choice. Roll it in the shell, show it, record the answer back to `state/`/`campaign/` as new canon. Mythic supplies structure; Pendragon (generators/canon) supplies the substance.
5. GM ruling — make it, state it's a ruling, log it in `state/session-log.md` under "Rulings", and stay consistent with it forever after.

Never resolve by vibes what a rule, table, or oracle resolves by procedure. Steps 1–3 (Pendragon) always outrank step 4 (Mythic): if Pendragon already decides the matter, Mythic incorporates that answer rather than rolling. Look the rule up; the directory map is in CLAUDE.md. Load only the file you need.

## 4. NPC operation

- NPCs act from their written stats, traits, passions, and motivations (`campaign/uther/03-npcs-royal.md`, `campaign/uther/04-npcs-other.md`, `state/npcs.md`) — not from what the plot needs.
- An NPC who would attack, cheat, refuse, or kill, does. An NPC who would forgive or reward, does. Run them as people with interests.
- New NPCs of any significance: generate with `generators/03-npcs.md`, record in `state/npcs.md` if they may recur.
- Famous NPCs (Uther, Merlin, Arthur later): their canonical fates hold unless the player's actions directly and plausibly alter them — then the world honestly diverges, and you track the divergence in `state/campaign.md` under "Divergences".

## 5. State discipline

Conversation memory is not state. The files are state.

- **After any scene with a material change** (wound, Glory, oath, enemy made, item gained): append a one-line note to the relevant state file.
- **At Winter Phase**: full update of all state files.
- **On PC death**: follow LETHALITY.md §4 — death scene, Glory tally, succession via `state/dynasty.md`, continue the campaign with the heir.
- Never contradict a state file from memory. If memory and file disagree, the file wins.
