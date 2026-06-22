# Battle Events Tables and Enemy Unit Reference

The Battle Events table (rolled every round), all Automatic Event triggers, and the in-book enemy army tables used during battles (All-Knight, Beginning Saxon, Attacking Saxon, King Uther Period, British Raiding Force, Cambrian Hill Tribe, Local French Defensive). Armies from the Book of Armies are in the armies-*.md files.

**Use when:** Calculating Army Intensity each round (Step 2), and when rolling to determine enemy opponents.

---

## Table 4.1: Battle Events

Roll **3d6 − 10** each round. Apply the result as a modifier to Army Intensity. Positive values increase Intensity (bad for players); negative values reduce Intensity (favorable).

| Roll (3d6−10) | Result Range | Narrative Category |
|--------------|-------------|-------------------|
| −7 | Excellent news everywhere | Major friendly advantage |
| −6 to −5 | Good news along the line | Friendly breakthrough or enemy error |
| −4 to −3 | Favorable developments | Minor friendly advantage |
| −2 to −1 | Slight edge to players | Modest favorable development |
| 0 | Even exchange | No significant news |
| +1 to +2 | Slight edge to enemy | Minor enemy advantage |
| +3 to +4 | Unfavorable news | Enemy pressure increasing |
| +5 to +6 | Bad news along the line | Enemy breakthrough or friendly error |
| +7 to +8 | Catastrophic news | Major enemy advantage |

**Narrative examples (GM improvises appropriate flavor):**
- −5 to −7: "Our reserve cavalry just flanked their center!" / "Saxon axemen broke on the right!"
- −2 to −4: "The enemy seems hesitant and confused" / "Enemy banners are wavering"
- 0: "The fight grinds on evenly across the field"
- +2 to +4: "The Saxons are rallying! They're bashing shields!" / "Confusion in our ranks!"
- +5 to +7: "A unit on our left just broke and ran!" / "The enemy got behind our archers!"
- +8: "The enemy king has rallied his household troops and they're charging our flank!"

**Scripted Event override:** The GM may substitute a scripted result for any Battle Events roll (see below).

---

## Automatic Events

These trigger automatically when Army Intensity reaches a threshold, regardless of Battle Events.

| Army Intensity | Trigger | Effect |
|---------------|---------|--------|
| ≤ 0 for 2 consecutive rounds | Enemy army Routs | Battle ends; Decisive Victory; Chase phase begins |
| ≤ 10 for 2 consecutive rounds | Enemy Signals Retreat | Battle ends; may be Decisive or Indecisive; player may Pursue |
| Exactly 30 | Enemy makes desperate stand | GM may add a scripted event; Rally the Battalion may be used |
| ≥ 40 | Player army Routs | Battle effectively lost; units must use Run Away or Pull Back; possible Decisive Defeat |
| Any Intensity reaching 0 in 1 round | Exceptional result | GM's discretion whether to end battle or let it continue |

---

## Scripted Events

Scripted Events are predetermined modifiers the GM inserts based on the scenario (from The Great Pendragon Campaign or custom creation). They replace or supplement the Battle Events roll.

**Common Scripted Event types:**
- Fixed Army Intensity modifier (e.g., "+7 — the center battalion has collapsed")
- Zone-specific events (e.g., "enemy cavalry attacks your right flank: your unit must Stand vs. Charge")
- Named enemy appearance (e.g., "King Ælle himself leads a charge against your battalion")
- Battle ending (e.g., "Uther's horns sound the retreat — the battle is over regardless of Intensity")

**Format:** "Scripted Event: +X to Army Intensity / [narrative]" — announced during Step 2 after rolling Battle Events.

---

## Enemy Unit Table Symbols

| Symbol | Meaning |
|--------|---------|
| ♞ | Mounted; can make a Lance Charge (Charge maneuver gives them +5) |
| £ | Has ransom value; can be captured for ransom (see `06-battle-aftermath.md`) |
| << (or ≪) | Passion listed below; NPC will attempt to invoke it during melee |
| S | Sprinter; can use Sprint ability (flee on foot at listed DEX value) |
| D | Determined; will not flee; holds ground even if routed |
| F | Flee Fighting; can shoot and retreat simultaneously (mounted archers) |
| MM | Missile and Melee; unit fights with both this round |
| ×2 / ×3 | Player must fight multiple opponents from this unit simultaneously |
| Note | Special rules below the unit table; read them |

**Reading combat information format:**
- "Weapon (Skill): Damage dice" — e.g., "Great Spear (15): 4d6" means skill 15, damage 4d6
- "Lance (15) Charger: 6d6 [5]" — lance skill 15, Charger horse grants 6d6, [5] = Charge bonus applied
- "Bow (12): 3d6 8" — bow skill 12, 3d6 damage, 8 = missile range/rate modifier

---

## All-Knight Army

Used for battles where the opponent is entirely mounted knights (tournaments, civil wars, late-period battles).

*Roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Squires (Young) | Spear, Sword 10 (4d6); Lance 10; Rouncy: 4d6 [5] | 14; Cuirbouilli (8), Shield (6) | 12 | 10 |
| 02 | Squires (Experienced) | Spear, Sword 15 (5d6); Lance 15; Rouncy: 4d6 [5] | 14; Cuirbouilli (8), Shield (6) | 12 | 10 |
| 03 | Squires (Veterans) | Spear, Sword 17 (5d6); Lance 17; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 04 | Knights (Young) ♞ £ | Spear, Sword 10 (4d6); Lance 10; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 05 | Knights ♞ £ | Spear, Sword 15 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 06 | Knights (Veterans) ♞ £ | Spear, Sword 20 (5d6); Lance 20; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |
| 07 | Elite Knights ♞ £ | Spear, Sword 15 (6d6); Lance 15; Large Charger: 7d6 [5] | 18; Reinf. Chain (12), Shield (6) | 14 | 15 |
| 08 | Elite Knights (Veterans) ♞ £ | Spear, Sword 20 (6d6); Lance 20; Large Charger: 7d6 [5] | 18; Reinf. Chain (12), Shield (6) | 14 | 20 |
| 09 | Household Knights ♞ £ | Spear, Sword 17 (5d6); Lance 15; Charger: 6d6 [5] | 20; Partial Plate (14), Shield (6) | 14 | 20 |
| 10 | Household Knights (Elite) ♞ £ | Spear, Sword 20 (5d6); Lance 18; Charger: 6d6 [5] | 20; Partial Plate (14), Shield (6) | 14 | 25 |
| 11 | Household Knights (Veterans) ♞ £ | Spear, Sword 22 (6d6); Lance 20; Large Charger: 7d6 [5] | 20; Partial Plate (14), Shield (6) | 14 | 25 |
| 12 | Bodyguards ♞ £ | Spear, Sword 20 (5d6); Lance 20; Charger: 6d6 [5] | 18; Reinf. Chain (12), Shield (6) | 16 | 25 |
| 13 | Bodyguards (Elite) ♞ £ | Spear, Sword 25 (6d6); Lance 25; Large Charger: 7d6 [5] | 20; Partial Plate (14), Shield (6) | 16 | 30 |
| 14 | Banner Knights ♞ £ | Spear, Sword 15 (5d6); Lance 15; Charger: 6d6 [5] | 18; Reinf. Chain (12), Shield (6) | 16 | 20 |
| 15 | Companion Knights ♞ £ | Spear, Sword 20 (5d6); Lance 20; Charger: 6d6 [5] | 20; Partial Plate (14), Shield (6) | 16 | 25 |
| 16 | Mounted Spearmen ♞ £ | Spear Expertise, Sword 15 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 17 | Mounted Spearmen (Javelin-armed) S | Javelin 10 (3d6); Sprint: Rouncy = 12 | 12; Leather (6), Shield (6) | 13 | 10 |
| 18 | Mounted Spearmen (Lancers) ♞ | Spear Expertise, Sword 16 (5d6); Lance 13; Charger: 6d6 [5] | 12; Leather (6), Shield (6) | 14 | 15 |
| 19 | Mounted Spearmen (Javelin-armed) S | Javelin 10 (3d6); Sprint: Courser = 18 | 12; Leather (6), Shield (6) | 13 | 10 |
| 20 | Knights (Veterans) ♞ £ | Spear Expertise, Sword 20 (5d6); Lance 20; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |

**Generic Noble Leaders Table** (use when a leader or commander is faced):

| Leader | Combat Information | Armor | MW | Glory |
|--------|--------------------|-------|----|-------|
| Young Commander £ | Spear, Sword 15 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 100 |
| Middle-aged Commander £ | Spear, Sword 20 (5d6); Lance 18; Charger: 6d6 [5] | 18; Reinf. Chain (12), Shield (6) | 15 | 100 |
| Old (Veteran) Commander £ | Spear, Sword 20 (4d6); Lance 20; Large Charger: 7d6 [5] | 20; Partial Plate (14), Shield (6) | 15 | 100 |
| Bodyguards | Spear, Sword 20 (5d6); Charger: 6d6 [5] | As commander | 18 | 50 |

---

## Saxon Army for Beginning Games

*Round 1: roll 1d6+14. Subsequent rounds: roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Elite Axemen | 2-H Axe (22): 7d6 | 16; Chainmail (10), Shield (6) | 15 | 20 |
| 02 | Veterans (Huscarls) | Sword 20 (6d6); Spear 20 (5d6) | 17; Chainmail (11), Shield (6) | 15 | 20 |
| 03 | Shield Warriors | Great Spear 17 (5d6); Shield (uses) | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 04 | Warriors (Frothing w/ Hate) << | Great Spear 17 (5d6) | 12; Chainmail (6), Shield (6) | 14 | 15 |
|    | << Hate (Britons) 20 | | | | |
| 05 | Thegns ♞ £ | Spear, Sword 17 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 20 |
| 06 | Grunting Spearmen | Great Spear 15 (4d6) | 12; Leather (6), Shield (6) | 14 | 10 |
| 07 | Spearmen | Great Spear 12 (4d6) | 10; Padding (4), Shield (6) | 12 | 8 |
| 08 | Shieldwall Spearmen | Great Spear 15 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 09 | Veteran Warriors | Great Spear 17 (5d6) | 15; Chainmail (9), Shield (6) | 14 | 15 |
| 10 | Hearthweru (Household) | Great Spear 20 (6d6) | 17; Chainmail (11), Shield (6) | 15 | 20 |
| 11 | Ordinary Axemen | 2-H Axe (15): 6d6 | 12; Leather (6), Shield (6) | 13 | 10 |
| 12 | Chanting Warriors | Great Spear 17 (5d6) | 12; Chainmail (6), Shield (6) | 14 | 15 |
| 13 | Warriors | Great Spear 10 (4d6) | 8; Padded (2), Shield (6) | 12 | 8 |
| 14 | Berserkers << | 2-H Axe (20): 7d6 | None | 16 | 20 |
|    | << Hate (All) 20 | | | | |
| 15 | Warriors (Wealthy) | Great Spear 15 (5d6); Sword 15 (4d6) | 17; Chainmail (11), Shield (6) | 14 | 15 |
| 16 | Javelineers S | Javelin 15 (3d6); Sprint: DEX = 12 | 6; Padding (3), Small Shield (3) | 11 | 8 |
| 17 | Fyrd Spearmen | Great Spear 8 (4d6) | None | 12 | 5 |
| 18 | Fyrd Spearmen (Levy) | Great Spear 10 (4d6) | 4; Padding (4) | 12 | 5 |
| 19 | Mounted Thegns ♞ £ | Spear, Sword 17 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |
| 20 | Warlord's Household ♞ £ | Spear, Sword 20 (6d6); Lance 18; Charger: 6d6 [5] | 18; Reinf. Chain (12), Shield (6) | 15 | 25 |

**Saxon Leaders:**

| Leader | Combat Information | Armor | MW | Glory |
|--------|--------------------|-------|----|-------|
| Saxons King / Chieftain £ | 2-H Axe (22): 7d6; Spear (20): 6d6 | 18; Reinf. Chain (12), Shield (6) | 18 | 150 |
| Sub-King / Warlord £ | 2-H Axe (20): 6d6; Spear (18): 5d6 | 17; Chainmail (11), Shield (6) | 16 | 100 |
| Bodyguards | 2-H Axe (20): 6d6; Spear (18): 5d6 | 17; Chainmail (11), Shield (6) | 16 | 50 |

---

## Attacking Saxon Army

*Used when Saxons are on the offensive. Roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Berserkers << | 2-H Axe (20): 7d6 | None | 16 | 20 |
|    | << Hate (Enemies) 20 | | | | |
| 02 | Elite Axemen | 2-H Axe (22): 7d6 | 16; Chainmail (10), Shield (6) | 15 | 20 |
| 03 | Hearthweru | Great Spear 20 (6d6) | 17; Chainmail (11), Shield (6) | 15 | 20 |
| 04 | Thegns ♞ £ | Spear, Sword 17 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |
| 05 | Warriors (Howling, Full of Hate) << | Great Spear 11 (5d6) | 12; Padded (6), Shield (6) | 14 | 15 |
|    | << Hate (Britons) 20 | | | | |
| 06 | Grunting Spearmen | Great Spear 15 (4d6) | 12; Leather (6), Shield (6) | 14 | 10 |
| 07 | Mounted Thegns ♞ £ | Spear, Sword 17 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |
| 08 | Shieldwall Spearmen | Great Spear 15 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 09 | Veteran Warriors | Great Spear 17 (5d6) | 15; Chainmail (9), Shield (6) | 14 | 15 |
| 10 | Shield Warriors | Great Spear 17 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 11 | Chanting Warriors | Great Spear 17 (5d6) | 12; Chainmail (6), Shield (6) | 14 | 15 |
| 12 | Warriors (Frothing w/ Hate) << | Great Spear 17 (5d6) | 12; Chainmail (6), Shield (6) | 14 | 15 |
|    | << Hate (Britons) 20 | | | | |
| 13 | Axemen | 2-H Axe (15): 6d6 | 12; Leather (6), Shield (6) | 13 | 10 |
| 14 | Javelineers S | Javelin 15 (3d6); Sprint: DEX = 12 | 6; Padding (3), Small Shield (3) | 11 | 8 |
| 15 | Fyrd Spearmen | Great Spear 10 (4d6) | None | 12 | 5 |
| 16 | Mounted Mercenaries ♞ £ | Spear, Sword 15 (5d6); Lance 16; War Pony: 5d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 17 | Javelineers (Mounted) S ♞ | Javelin 10 (3d6); Sprint: Pony = 15 | 10; Leather (4), Shield (6) | 12 | 10 |
| 18 | Warriors (Wealthy) | Great Spear 15 (5d6); Sword 15 (4d6) | 17; Chainmail (11), Shield (6) | 14 | 15 |
| 19 | Warlord's Household ♞ £ | Spear, Sword 20 (6d6); Lance 18; Charger: 6d6 [5] | 18; Reinf. Chain (12), Shield (6) | 15 | 25 |
| 20 | Warlord's Elite Household ♞ £ | Spear, Sword 22 (7d6); Lance 20; Large Charger: 7d6 [5] | 20; Partial Plate (14), Shield (6) | 16 | 30 |

---

## King Uther Period Army (British)

*Used for Uther-era British armies (483–495). Roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Roman Infantry (Urban Elite) D | Javelin 20 (3d6); Gladius 22 (6d6) | 20; Lorica (12), Heavy Shield (8) | 18 | 20 |
| 02 | Roman Infantry (Urban) D | Javelin 10 (3d6); Gladius 15 (5d6) | 20; Lorica (12), Heavy Shield (8) | 18 | 15 |
| 03 | Archers S | Bow 15 (3d6); Sprint: DEX = 16 | None | 12 | 5 |
| 04 | Levy Spearmen | Spear 10 (4d6) | 8; Leather (2), Shield (6) | 12 | 5 |
| 05 | Levy Spearmen (Experienced) | Spear 15 (4d6) | 12; Leather (6), Shield (6) | 13 | 8 |
| 06 | Guardsmen | Spear Expertise, Sword 15 (4d6) | 16; Chainmail (10), Shield (6) | 14 | 10 |
| 07 | Armored Spearmen | Spear Expertise, Sword 15 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 08 | Elite Guardsmen | Spear Expertise, Sword 21 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 09 | Mounted Milites ♞ | Spear Expertise, Sword 15 (4d6); Rouncy: 4d6 [5] | 14; Cuirbouilli (8), Shield (6) | 12 | 12 |
| 10 | Mounted Milites (Experienced) ♞ | Spear Expertise, Sword 15 (4d6); War Pony: 5d6 [5] | 14; Cuirbouilli (8), Shield (6) | 14 | 15 |
| 11 | Spearmen (Rank & File Levy) | Spear Expertise, Sword 10 (5d6) | 8; Leather (2), Shield (6) | 14 | 5 |
| 12 | Armored Swordsmen | Spear Expertise, Sword 15 (6d6) | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 13 | Levy Spearmen | Spear Expertise, Sword 10 (5d6) | 8; Leather (2), Shield (6) | 14 | 10 |
| 14 | Mounted Milites (New) ♞ | Spear Expertise, Sword 10 (4d6); Rouncy: 4d6 [5] | 14; Cuirbouilli (8), Shield (6) | 12 | 12 |
| 15 | Mounted Milites (Exp.) ♞ | Spear Expertise, Sword 15 (4d6); War Pony: 5d6 [5] | 14; Cuirbouilli (8), Shield (6) | 14 | 15 |
| 16 | Knights (Milites) ♞ £ | Spear Expertise, Sword 15 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 17 | Mounted Spearmen (Javelin) S | Javelin 10 (3d6); Sprint: Rouncy = 12 | 12; Leather (6), Shield (6) | 13 | 10 |
| 18 | Mounted Spearmen (Lancers) ♞ | Spear Expertise, Sword 16 (5d6); Lance 13; Charger: 6d6 [5] | 12; Leather (6), Shield (6) | 14 | 15 |
| 19 | Mounted Spearmen (Javelin) S | Javelin 10 (3d6); Sprint: Courser = 18 | 12; Leather (6), Shield (6) | 13 | 10 |
| 20 | Knights (Veterans) ♞ £ | Spear Expertise, Sword 20 (5d6); Lance 20; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |

---

## British Raiding Force

*Generic attacking British army for middle and later GPC periods. Roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Infantry (Elite Mercenaries) | Halberd 25 (6d6) | 16; Chainmail (10) | 15 | 15 |
| 02 | Archers S (Mercenaries) | Bow 15 (3d6); Sprint: DEX = 10 | None | 12 | 10 |
| 03 | Crossbowmen S (Garrison) | Lt. Crossbow 10 (1d6+10); Sprint: DEX = 10 | None | 12 | 5 |
| 04 | Crossbowmen S (Mercenary) | Lt. Crossbow 15 (1d6+10); Sprint: DEX = 17 | 2; Helmet (2) | 12 | 10 |
| 05 | Infantry (Mercenary) | Great Spear 12 (5d6); Sword 12 (4d6) | 16; Chainmail (10), Shield (6) | 14 | 10 |
| 06 | Uniformed Infantry (Elite Mercenaries) | Great Spear 21 (5d6); Sword 21 (4d6) | 18; Reinf. Chainmail (12), Shield (6) | 14 | 15 |
| 07 | Crossbowmen (Mercenary) | Med. Crossbow 15 (1d6+13); Short Sword 15 (4d6) | None | 12 | 10 |
| 08 | Archers S (Garrison) | Bow 10 (3d6); Sprint: DEX = 15 | None | 10 | 5 |
| 09 | Savage Kern Swarm (Irish) MM | Javelin 12 (3d6); Knife 15 (5d6) | 4; Small Shield (4) | 12 | 5 |
| 10 | Kern Swarm S ×2 (Not-so-savage Irish) | Javelin 10 (3d6); Sprint: DEX = 12 | 4; Small Shield (4) | 12 | 5 |
| 11 | Infantry (New Mercenaries) | Great Spear 10 (5d6); Spear 10 (4d6) | 14; Cuirbouilli (8), Shield (6) | 14 | 10 |
| 12 | Infantry (Experienced Esquires) | Spear, Sword 15 (6d6) | 18; Reinf. Chainmail (12), Shield (6) | 14 | 15 |
| 13 | Spearmen (Experienced Garrison) | Spear, Sword 19 (4d6) | 16; Reinf. Chainmail (12), Shield (6) | 14 | 15 |
| 14 | Infantry (Mercenaries) | Great Spear 10 (6d6); Spear, Sword 15 (5d6) | 18; Reinf. Chainmail (12), Shield (6) | 14 | 15 |
| 15 | Mounted Sergeantry (Esquires) ♞ | Spear 19 (4d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 16 | Mounted Sergeantry (Veteran Mercenaries) ♞ | Spear, Sword 15 (5d6); Lance 16; War Pony: 5d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 17 | Knights ♞ £ | Spear, Sword 15 (5d6); Lance 15; Rouncy: 4d6 [6] | 18; Reinf. Chainmail (12), Shield (6) | 14 | 15 |
| 18 | Cymric Knights ♞ £ | Spear Expertise, Sword 16 (5d6); Charger: 6d6 [6] | 18; Reinf. Chainmail (12), Shield (6) | 14 | 15 |
| 19 | Knights (Young) ♞ | Spear, Sword 10 (4d6); Lance 10; Charger: 6d6 [6] | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 20 | Knights (Veteran) ♞ £ | Spear, Sword 20 (6d6); Lance 16; Large Charger: 7d6 [6] | 18; Reinf. Chainmail (12), Shield (6) | 14 | 20 |

---

## Cambrian Hill Tribe Army

*Suitable for Cymric tribal defense (confederation, single kingdom, or town militia). Roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Rustic Spearmen | Spear Expertise 10 (5d6) | None | 12 | 5 |
| 02 | Archers S (Trained Urban Roman) | Bow 15 (3d6); Sprint: DEX = 16 | None | 12 | 5 |
| 03 | Bowmen S (Mercenaries) | Bow 10 (3d6); Sprint: DEX = 12 | None | 12 | 5 |
| 04 | Spearmen (Guardsmen) | Spear 10 (5d6) | None | 14 | 10 |
| 05 | Guardsmen (Garrison) | Spear Expertise, Sword 15 (4d6) | 16; Chainmail (10), Shield (6) | 14 | 10 |
| 06 | Spearmen (Rank & File Levy) | Spear Expertise, Sword 10 (5d6) | 8; Leather Jack (2), Shield (6) | 14 | 5 |
| 07 | Mass Archers (Levy) ×2 S | Bow 5 (3d6); Sprint: DEX = 12 | None | 12 | 2.5 |
| 08 | Armored Spearmen (Experienced) | Spear Expertise, Sword 15 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 09 | Uniformed Infantry (Elite Guard) | Spear Expertise, Sword 21 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 10 | Infantry (Urban Roman) | Javelin 20 (3d6); Gladius & Scutum 22 (6d6) | 20; Lorica (12), Heavy Shield (8) | 18 | 15 |
| 11 | Spearmen (Levy) | Spear Expertise, Sword 10 (5d6) | 8; Leather Jack (2), Shield (6) | 14 | 12 |
| 12 | Armored Swordsmen (Big Guys) | Spear Expertise, Sword 15 (6d6) | 16; Chainmail (10), Shield (6) | 14 | 12 |
| 13 | Spearmen (Rank & File Levy) | Spear Expertise, Sword 10 (5d6) | 8; Leather Jack (2), Shield (6) | 14 | 10 |
| 14 | Mounted Spearmen (New, Young) ♞ | Spear Expertise, Sword 10 (4d6); Rouncy: 4d6 [5] | 14; Cuirbouilli (8), Shield (6) | 12 | 12 |
| 15 | Mounted Spearmen (Experienced) ♞ | Spear Expertise, Sword 15 (4d6); War Pony: 5d6 [5] | 14; Cuirbouilli (8), Shield (6) | 14 | 15 |
| 16 | Mounted Spearmen (Knights) ♞ £ | Spear Expertise, Sword 15 (5d6); Lance 15; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 17 | Mounted Spearmen (Javelin-armed) S | Javelin 10 (3d6); Sprint: Rouncy = 12 | 12; Leather (6), Shield (6) | 13 | 10 |
| 18 | Mounted Spearmen (Lancers) ♞ | Spear Expertise, Sword 16 (5d6); Lance 13; Charger: 6d6 [5] | 12; Leather (6), Shield (6) | 14 | 15 |
| 19 | Mounted Spearmen (Javelin-armed) S | Javelin 10 (3d6); Sprint: Courser = 18 | 12; Leather (6), Shield (6) | 13 | 10 |
| 20 | Knights (Veterans) ♞ £ | Spear Expertise, Sword 20 (5d6); Lance 20; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 20 |

*Note: Cymric Cultural Specialty is Spear Expertise (replaces both Spear and Lance skills for all Cymric troops).*

---

## Local French Defensive Army

*Typical French count's force defending against raiders (Tournament Period primarily). Roll 1d20.*

| d20 | Opponent | Combat Information | Armor | MW | Glory |
|-----|----------|--------------------|-------|----|-------|
| 01 | Infantry (Urban Elites) | Great Spear, Spear, Sword 19 (5d6) | 16; Chainmail (10), Shield (6) | 15 | 15 |
| 02 | Peasants (Levy) ×2 | Hoe, Shovel, or Rake 10 (3d6) | None | 10 | 5 |
| 03 | Peasants with Rocks S | Rocks 15 (3d6); Sprint: DEX 12 | 6; Shield (6) | 10 | 5 |
| 04 | Archers MS (Levy) S | Bow 10 (3d6); Sprint: DEX 13 | None | 12 | 5 |
| 05 | Footmen (Cowardly) S | Sprint: DEX 15 | 14; Cuirbouilli (8), Shield (6) | 12 | 5 |
| 06 | Footmen — Hate (Britons) 19 | Great Spear 15 (4d6) | 14; Cuirbouilli (8), Shield (6) | 14 | 10 |
| 07 | Crossbowmen (Garrison) S | Lt. Crossbow 10 (1d6+10); Sprint: DEX 14 | None | 12 | 5 |
| 08 | Archers (Franc-tenancier Yeomen) | Bow 12 (3d6); Sword 12 (4d6) | 6; Shield (6) | 12 | 5 |
| 09 | Infantry (Elite Guardsmen) | Great Spear, Spear 21 (5d6) | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 10 | Infantry (Urban Guard) | Spear, Sword 10 (4d6) | 14; Cuirbouilli (8), Shield (6) | 14 | 10 |
| 11 | Peasants with Rocks (Levy) S | Rocks 15 (3d6); Sprint: DEX 12 | 6; Shield (6) | 10 | 5 |
| 12 | Footmen (Garrison) | Great Spear 10 (4d6) | 16; Chainmail (10), Shield (6) | 12 | 5 |
| 13 | Determined Peasants ×2 — Hate (Britons) 17 | 1d6: 1–3=Spear, 4–5=Axe, 6=Hammer 10 (4d6) | 6; Shield (6) | 10 | 5 |
| 14 | Infantry (Regular Guardsmen) | Great Spear, Spear 15 (5d6) | 14; Cuirbouilli (8), Shield (6) | 12 | 10 |
| 15 | Sergeantry (Veteran) ♞ | Spear 17 (4d6); Lance 19; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 16 | Knights (Household) ♞ £ | Spear, Sword 15 (5d6); Lance 18; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 17 | Sergeantry (Garrison) ♞ | Spear, Sword 15 (4d6); Lance 12; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 18 | Knights (Poor) ♞ £ | Spear, Sword 14 (5d6); Lance 18; Rouncy: 4d6 [5] | 12; Heavy Leather (6), Shield (6) | 14 | 15 |
| 19 | Knights ♞ £ — Hate (Britons) 19 | Spear, Sword 15 (5d6); Lance 17; Charger: 6d6 [5] | 16; Chainmail (10), Shield (6) | 14 | 15 |
| 20 | Rich Knights ♞ £ — Hate (Britons) 20 | Spear, Sword 15 (5d6); Lance 17; Large Charger: 7d6 [5] | 18; Reinf. Chainmail (12), Shield (6) | 14 | 20 |

---

## Destroyed Enemy Units

When a player unit scores a **Triumph**, the enemy unit is "severely damaged." Record which units have been damaged. If the same unit entry is rolled again:
- **Once damaged:** Fight at ×½ (half their combat skill)
- **Twice damaged / Triumph vs. half-strength:** Unit eliminated; remove from table; reroll if that number comes up again

Announce to players: "That unit has been badly mauled — they won't be at full strength again."
