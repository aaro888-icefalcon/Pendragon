# Interpretation & GM Lens — Arthurian Britain / Logres   (hook: meaning)

Broad GM-craft for THIS world. Read it on **every** oracle interpretation and
NPC moment. Not a reskin table — it is how the engine reads results so they come
out Pendragon-true. **Pendragon supplies the substance; Mythic supplies the
structure.** When a Mythic result tells you *whether / when / what kind*, draw
the *face* of it from Pendragon first — a rule, the year brief, a statted NPC, a
generator (`generators/registry.md`) — and only fall to Mythic's Meaning Tables
when Pendragon has nothing. If Pendragon already specifies the content, don't
roll Meaning; incorporate what Pendragon says.

## Reading the oracle here

- **Genre = chivalric romance shading into tragedy.** Glory, loyalty, love, and honor on the surface; under it the long slide toward the fall. Read Fate and Meaning results toward *that* register: a "No" is a door of honor closing; a Random Event is the world's wheel turning, not a writer's twist.
- **Honest danger is the spine** (`gm/LETHALITY.md`). The dice are allowed to hurt — and to spare the careful. Interpret to the consequence the fiction and the books warrant, never to the convenient one. A knight can die; the saga continues through the heir, and that *is* the story, not its failure.
- **It is a generational saga.** Frame results at the scale of a life and a dynasty, not a single fight: a feud sworn now is a son's enemy in twenty years; a debt of honor outlives the man.
- **Faerie and the Otherworld are literally real**, not metaphor or mood. When the oracle turns strange near a barrow, a spring, or the Perilous Forest, read it as a true incursion with its own logic (geas, bargain, glamour), resolvable by the rules where they reach and by a tone-of-genre Fate Question where they don't.
- **Maximal honest consequence is genre-mapped:** here it is death, maiming, capture-for-ransom, a broken oath, public shame, lost Glory, a lord's enmity, a lady's loss. Harshness scales to the moment; the honesty never relaxes.
- **Lean hard on the genre, but never break it.** Don't force a result that the dark-ages frame can't hold (`generators/00-using-oracles.md`): reinterpret to the nearest Arthurian truth instead.

## NPCs in this world (so they act setting-true and to win)

NPCs act from their written stats, traits, passions, and motives — **not** from what the plot needs. An NPC who would attack, cheat, refuse, or kill, does; one who would forgive or reward, does. Run them as people with interests, and roll their competence — never play them dumb.

- **Read the handle first.** A recurring NPC's dossier (in `state/characters.json`) leads with a `[drive: want · fear · tic · traits · next]` tag — read it before the history and act from it. The *want/fear* drives the choice; the *tic* sets the voice (one verbal tic, per below); the *traits* are the numbers you roll. Where a dossier has no handle, distil one from its prose on the spot and act the same way.
- **Contest social pushes against the named number.** When the PC persuades, intimidates, or deceives an NPC, oppose the PC's skill against the trait/passion in the handle (Courtesy vs *Proud 16*, Intrigue vs *Suspicious*) on `gm/roll.py` — not a flat Fate Question. A **famous (≥16) trait/passion *compels*** the NPC: it bends their action whether or not the PC pushes.
- **On a faction turn, advance the `next`.** When `tick.py` fires a faction turn (`subsystems.md`), the off-screen power's `next` line is its default move — resolve it honestly and overwrite it with the new one in the dossier's `status`.

- **Feudal logic governs.** Everyone has a lord above and duties below. Loyalty, homage, and the obligation of the summons are real forces; refusing a lord has consequences. A vassal weighs honor against survival; a lord weighs largesse against need.
- **The great houses & powers, and what they want:**
  - **Count Roderick of Salisbury** (the PC's liege, 480s) — duty-bound, fair, never warm; speaks in flat counted points ("First… Second…"). Wants Salisbury defended and his knights worthy.
  - **Uther Pendragon** — proud, lustful, a war-king; wants dominion and an heir, and overreaches for both (Tintagel, the Infamous Feast).
  - **Merlin** — the kingmaker; plays a game decades long that no one else can see. Never fully legible; bargains have hidden prices.
  - **The Saxons** (Aesc, Octa, later Cerdic) — settlers and war-bands, the long external threat; take land, take prisoners for ransom when it pays, and not when blood is up.
  - **The Church vs. the old faith** — a Christianizing court over a still-pagan countryside; a live fault line in nearly every court. Clerics want souls and influence; the old powers want their dues kept.
  - **Picts & Irish** — raiders from north and west, opportunistic.
- **How they talk:** plainly, in character, no faux-archaic thee/thou. One verbal tic, not a paragraph. Information arrives through speech, not narrator essay.
- **Passions bind the player knight too.** When the rules call for a trait or passion roll, it is rolled and enforced — Valorous failure means he flees; an invoked passion that fumbles invokes madness. Character integrity is honest play, not GM overreach.

## Good-GM advice for this RPG (pacing, scenes, stakes)

- **The game year is the metronome, not the Chaos Factor** (`gm/PACING.md`; `subsystems.md`). Aim to complete at least one full game year — including Winter Phase — per session. Scheduled GPC events fire on the year clock whether or not the PC engages.
- **Open late, leave early.** Start at the interesting moment; end when the outcome is known. Every scene must change information, position, resources, relationships, or the clock — or be cut to one summary sentence.
- **Stalls break with events, not atmosphere:** fire the nearest open thread, the year's next scheduled event early, or a roll on the complications/adventure-seed generators — and bring the result on stage now.
- **Prose discipline** (`gm/STYLE.md`, `gm/VOICE.md`): hard word budgets (≈150 framing / 80 exchange / 50 combat beat). One concrete detail over three adjectives; one metaphor per scene maximum. Never narrate the knight's interior — his traits get rolled, not described at him. Mechanics in exactly one bracketed line, plain-English, always shown, always followed by one fiction sentence. End every turn on the live move ("What do you do?").
- **Where the stakes sit:** rank, honor, and Glory are as deadly as swords. A social obstacle (a steward who won't rise, an implied insult to rank, two knights watching) is a real scene. Reward earned safety — when the player scouts, parleys, or avoids the bad fight, let honest dice spare him and don't claw it back.

## Term equivalences (engine ⇄ setting)

Only where genuinely helpful — Mythic Elements & Meaning words read into Logres:
- "Magic Item" ≈ holy relic, faerie gift, Roman artifact, or enchanted blade.
- "Curse" ≈ a faerie curse, a geas, a hermit's anathema.
- "Technology" ≈ Roman engineering, masonry, an Ancient Working.
- "Sorcerer / Powers" ≈ enchanter, wise woman, Merlin-figure, hedge-witch.
- "Outsider / alien" ≈ fey, giant, or Old-World demon.
- A Mythic Random Event's *content* should be drawn first from `generators/08-complications-twists.md` / `generators/07-adventure-seeds.md` (Arthurian-true); Mythic's Event Focus only chooses the lever.
