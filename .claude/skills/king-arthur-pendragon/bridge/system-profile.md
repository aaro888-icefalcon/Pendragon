# System Profile — King Arthur Pendragon (5th ed.)   (hook: resolve)

How the engine resolves tasks when Pendragon is the ruleset. **Pendragon owns
task resolution and combat; Mythic asks the narrative questions around them.**
Pendragon rolls through its **own** roller, not `dice.py`. Full rules in this
skill's `rules/`; this is the lean profile the engine needs.

- **Dice convention:** d20 **roll-under** for all skills, traits, passions, and
  combat; `NdM` for damage and random tables. Apply situational modifiers to the
  skill value **before** rolling.
- **Express a roll as:**
  - Skill/trait/passion check → `python3 gm/roll.py check <effective skill>` (returns success / critical / fumble / failure).
  - Opposed → `python3 gm/roll.py opposed <PC skill> <NPC skill>`.
  - Damage / random → `python3 gm/roll.py 4d6` (or any `NdM`).
  - Pendragon dice are `gm/roll.py …`; the engine's `dice.py` is for Fate Questions, Scenes, and oracle tables only — the two never collide because they answer different questions.
- **Core resolution:** roll d20 ≤ skill = **success**; roll **exactly** = skill = **critical**; natural 20 = **fumble**. For skill > 20, add (skill − 20) to the roll: a modified total ≥ 20 = critical, else success, no fumble. **Opposed:** critical beats success beats failure beats fumble; at equal level the higher qualifying roll wins, loser may get a partial success.
- **Degrees of success?** **Yes** — critical / success / failure / fumble. In **rule-mode** Fate Questions (`dice.py fate <odds> <cf> --mode rule`): map **Exceptional Yes → critical-grade**, **Exceptional No → fumble-grade**. Prefer rolling the actual Pendragon check whenever one exists; use rule-mode Fate Questions only when statting the check would stall play.
- **Stats / skills:** Attributes SIZ, DEX, STR, CON, APP. Skills are d20 roll-under (Awareness, Courtesy, Intrigue, First Aid, Hunting, Falconry, Orate, Heraldry…). Combat skills: Sword, Lance, Spear, Dagger, Horsemanship, plus **Battle** (mass-combat command). Thirteen personality **trait** pairs (each pair sums to 20; e.g. Valorous/Cowardly) and **passions** (Loyalty, Love, Hospitality, Honor, Hate…). Both are rolled and **bind the player knight**, not just NPCs. **Glory** accrues and drives advancement (`rules/core/07-glory.md`).
- **Defenses / health:** Total **HP = CON + SIZ**. **Unconscious** at current HP ≤ ¼ total (round). **Major Wound** when a single hit's damage (after armor) ≥ **CON**. **Knockdown** when damage ≥ **SIZ**. **Healing Rate** = (CON+SIZ)/10. Armor = points subtracted from each hit (chainmail 10, +6 shield if used). Death at 0 HP or by Major-Wound complications (`rules/core/06-injury-death-healing.md`).
- **Combat:** statement of intent, then resolve each exchange as an **opposed weapon-skill roll** (attacker vs defender); the winner strikes. **Damage** = weapon dice (e.g. Sword 4d6 including the SIZ+STR damage bonus) minus armor; remainder is HP loss. Initiative by DEX/situation. **Defeat is real:** death, Major Wound/maiming, capture-and-ransom (the genre's survival valve, not GM mercy). Mass battle uses the Battle skill and `rules/battle/`. A doubles-≤-CF Fate Question mid-fight can still fire a Random Event — the combat math is Pendragon's; the interruption is Mythic's.
- **NPC stat units:** key skill values (combat skill + significant skills), Damage `NdM`, armor points, HP, Move, notable traits/passions, Glory. Stat on the fly from `rules/core/11-gm-reference.md`. **On-the-fly NPC Statistics mapping** (engine asks a Fate Question about an NPC's competence → read against your expected value): **Yes** = as expected · **Exc Yes** +25% · **No** −25% · **Exc No** −50% (apply to the key skill or HP). Famous NPCs use their canon stat blocks (`campaign/uther/03-npcs-royal.md`, `campaign/gpc/09-gpc-appendices.md`).
- **Routing default:** Pendragon resolves **all** task / skill / combat / trait / passion checks, Winter Phase, aging, healing, estate, and mass battle. Defer to **Mythic Fate Questions** only for world yes/no questions, off-script scene framing, complication timing, and genuinely open NPC choices (see `interpretation.md`). If a rule, stat block, or scheduled GPC event already decides something, the engine **adopts that answer** instead of rolling.
- **Subsystems as Fate Questions:** faerie / Otherworld weirdness and omens where no rule applies → a Fate Question "in the tone of the genre." Everything mechanical stays in `rules/`. The estate, faction, Glory, and year subsystems are world-tick items (`subsystems.md`), not Fate Questions.
- **House rule (binding):** honest dice, rolled in the shell and shown, applied as rolled, never fudged (`gm/LETHALITY.md`). Player knights can die; the saga continues through the heir.
