# Battle Setup

Covers all pre-battle configuration: army and battle sizing, unit organization, troop categories, commander types, follower rules, passion triggers, and the complete Opening Army Intensity calculation procedure.

**Use when:** Starting any battle, or when players are appointed as Unit Commander or Army Commander.

---

## Army Size and Battle Type

| Army Size | # of Knights | Type Name | Commander Title |
|-----------|--------------|-----------|-----------------|
| 10–50 | | Clash | Baron |
| 100–500 | | Battle | Count |
| 1000–5000 | | Campaign | Duke or King |

Battle size affects Glory multipliers (see `06-battle-aftermath.md`).

---

## Army Organization (Feudal Structure)

**Hierarchy (smallest to largest):**

1. **Lance / Conroi** — 5–10 knights; a knight + his famuli (personal attendants)
2. **Eschille / Company** — 10–40 knights; the basic tactical unit; led by a Unit Commander
3. **Battalion (Bataille)** — 3–6 eschilles; commanded by a Battalion Commander; the three standard battalions are Vanguard (right flank), Center, Rearguard (left flank)
4. **Army** — all battalions; commanded by the Army Commander

**Pendragon Banner:** The Army Commander carries the Pendragon banner; its capture or fall is a Scripted Event (GM discretion, typically +5–10 to Army Intensity).

**Flags by rank:**
- Knight: pennocel (small triangular pennant)
- Leader of company: pennon (swallow-tailed)
- Battalion Commander: standard
- Army Commander: banner

---

## Unit Composition: Player Knight's Eschille

| Role | Who | Notes |
|------|-----|-------|
| Unit Commander | Player knight with Battle skill | Leads the eschille; makes all Battle rolls |
| Attached knight | Player knight NOT the Unit Commander | Fights individually; no Battle roll |
| Leader | Player knight Attached but with own followers | Has Followers of his own |
| Follower | NPC knight or man-at-arms | Fights for the Unit Commander |
| Squire | Player knight's personal squire | Makes Squire rolls each round |

**Followers (NPC knights):**
- Default combat skill: 15
- Default damage dice: 5d6
- Default armor: 16 (Chainmail + Shield)
- Receive the same maneuver bonuses/penalties as the unit
- A player knight may have Followers if they have a Loyalty (Vassals) or Loyalty (Lord) passion
- Types: vassal knights, hired mercenaries, family members, assigned retainers
- **Bodyguard Bonus:** If Unit Commander has 5+ Followers, once per round, when the Unit Commander would be critically hit or killed, Followers sacrifice themselves to cancel the result. Roll 2d6−4 Followers are lost (minimum 0).

---

## Commander Types

### Army Commander
- One per army; commands from the Reserve or Center battalion
- Makes one Battle roll per battle: the **Army Commander's Battle Roll** in Round 1 (First Charge only)
- If engaged in personal combat (e.g. bodyguard unit attacked), acts as a Unit Commander for that eschille
- Does NOT make Battle rolls in subsequent rounds unless personally leading a unit

### Unit Commander
- One per eschille; always a player knight (or Sir Elad / NPC in tutorial)
- Makes a Battle roll every round (Step 3)
- Chooses the maneuver the unit performs
- Earns +15 Glory bonus at end of battle (small battle) to +30 (large battle) — see `06-battle-aftermath.md`

### Battalion Commander
- Leads a major segment (Vanguard, Center, Rearguard)
- Normally ignored in the battle game; appears as an **Opportunity** target (p.78 rules, see `06-battle-aftermath.md`)
- Killing/capturing a Battalion Commander: −10 Army Intensity immediately

---

## Player Knight Status Categories

Check at the start of every round (Step 1). A knight may be in multiple states simultaneously.

| Status | Definition | Key Mechanical Effect |
|--------|-----------|----------------------|
| Normal | Mounted, armed, with unit | No modifier |
| Attached | Following a Unit Commander | Uses UC's maneuver results |
| Alone | Separated from unit, typically unhorsed | +10 to that knight's Unit Intensity; acts as own UC |
| Mounted | On horseback | +5 vs. infantry in melee |
| Afoot | Not on horseback | −5 vs. mounted in melee |
| Burdened | Carrying an unconscious person on horseback | −5 Horsemanship |
| Encumbered | Horse loaded with two mounted riders | −5 to rider's Horsemanship |
| Guiding | Leading a riderless horse on foot | −5 Squire roll; −5 Horsemanship |
| Leading | Guiding from horseback | Same as Guiding penalties |
| Wounded | Taken damage in melee | Standard KAP wound rules apply |
| Disordered | Unit result caused disorder | −10 to melee skill; +5 to Unit Intensity |
| Broken | Unit destroyed/routed | Knight is now Alone |

---

## Passions in Battle

### Involuntary Passion Roll (Notable Passions ≥ 16)
- A notable Passion (value ≥ 16) with an appropriate trigger **must** be rolled the first time a knight enters combat with that trigger present (unless player actively suppresses)
- On **success:** knight is Impassioned; +10 to weapon skill for the rest of that combat round
- On **failure:** no bonus
- On **critical:** double weapon skill for that round
- On **fumble:** Melancholy; knight is effectively out of the battle (GM discretion)

### Voluntary Passion Roll (Any Passion)
- Player may choose to roll any appropriate Passion at any time before melee resolution
- Same effects as Involuntary

### NPC Enemy Passions
- Enemy units with Passions listed (e.g., Hate Britons 20) may invoke them during melee
- Roll 1d6 for each elapsed round at the time of melee; on a 6, the NPC has invoked their Passion this battle. If round 4 or later, roll 3d6 and check for any showing 6
- Invoked NPC Passion: +10 to their combat skill

### Revenge Crisis (Optional Rule)
- When a close companion (follower, fellow player knight) is killed in battle, the surviving knight may be overcome
- Roll on Revenge Crisis table (GM determines result, typically Reckless charge or Melancholy)

### Battle Passions
- Passion: Hate (enemy) — most common battle passion
- Passion: Loyalty (Lord) — may trigger Bodyguard Bonus voluntarily
- Passion: Loyalty (Vassals) — may be tested when followers die in battle; on failure, Melancholy (1 week per follower lost)

---

## Step 1–3: Opening Army Intensity Calculation (Pre-Battle)

### Opening Army Intensity Base: **20**

### Step A: Add Starting Conditions Modifier

Starting Conditions reflect the relative quality of the two armies before the battle begins. Determined by the GM comparing the two forces:

| Condition | Army Intensity Modifier |
|-----------|------------------------|
| Both armies equal | +0 |
| Player army "better armed" (more mounted, better armor) | −5 |
| Player army "worse armed" | +5 |
| Player army has clear advantage (reserves, terrain, surprise) | −10 |
| Player army at serious disadvantage | +10 |
| Mercenary units present (optional rule) | Varies by GM |

### Step B: Roll Battle Events (3d6 − 10)

Roll 3d6, subtract 10. Apply the result to Army Intensity this round.

- Result is added to Army Intensity (can be negative, which lowers Intensity)
- Consult Table 4.1 (Battle Events Table) for the narrative description — see `05-battle-events-tables.md`
- Range: −7 (all 1s) to +8 (all 6s)

### Step C: Opening Army Intensity = Base + Starting Conditions + Battle Events

---

## First Charge Intensity (Round 1 Only)

**First Charge Intensity = Opening Army Intensity − Unit Cohesion Modifier + Battle Zone Modifier**

- In Round 1: all units start **Disengaged** (Unit Cohesion: −20)
- In Round 1: all units start in **Zone 4** (Battle Zone modifier: +5)
- So First Charge Intensity = Opening Army Intensity − 20 + 5 = Opening Army Intensity − 15

**Example:** Opening Army Intensity 22; First Charge Intensity = 22 − 20 + 5 = **7**

---

## Army Commander's Battle Roll (Round 1 Only)

1. Army Commander rolls Battle skill (d20 vs. skill, lower = better)
2. Opposed against: the **greater of** First Charge Intensity OR enemy Army Commander's Battle skill
3. If Army Commander wins: player knights receive **+5 First Charge Bonus** to Lance/Spear Expertise for Round 1 only
4. **Exception:** If enemy is armed with Great Spears (a two-handed polearm), the +5 Charge Bonus is cancelled out (defenders set pikes against the charge)

**Subsequent rounds:** Army Commander does not roll. Only Unit Commanders roll Battle each round.

---

## Battle Zones

The battlefield is divided into 9 zones (1 = rear of player army, 9 = rear of enemy army):

```
[1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]
 ^                   ^         ^                ^
Rear               Start    Killing           Enemy
(Safe)           Position    Zone              Rear
```

| Zone | Name | Unit Intensity Modifier |
|------|------|------------------------|
| 1 | Player Rear | −10 (or out of battle) |
| 2 | Player Second Rear | −5 |
| 3 | Player Reserve / Non-combat | +0 |
| 4 | Player Second Rank (Start) | +5 |
| 5 | Killing Zone (front line) | +10 |
| 6 | Enemy Second Rank | +10 |
| 7 | Enemy Reserve / Non-combat | +5 |
| 8 | Enemy Rear | −5 |
| 9 | Enemy Camp | Special |

- **Non-combat Zones:** 1, 2, 3 (player side) and 7, 8, 9 (enemy side) — no active enemy engagement unless scripted
- **Combat Zones:** 3–7 — where troops are always found
- **Killing Zone:** Zone 5 — most dangerous; highest intensity modifier
- All player units start in Zone 4 at Round 1 (unless otherwise specified)

---

## Ambush Rules

If the enemy sets an ambush (GM decision or scripted):

| Condition | Unit Intensity Modifier |
|-----------|------------------------|
| Ambushed (basic) | +10 |
| Ambushed from both flanks | +20 |
| Ambushed from rear | +15 |

- On the round of ambush, the ambushed unit is automatically **Disordered** (+5 Unit Cohesion, −10 melee)
- After the ambush round, treat as normal combat

---

## Terrain Effects on Setup

Terrain affects Unit Intensity (Step 2) and melee skill (Step 4). Full table in `07-battle-misc.md`. Key setup notes:

- **Rocky/marshy ground** (+5 Unit Intensity): Starting Conditions may reflect this
- **Earthworks/prepared positions:** enemy in Dug-In position means player units must use Assault vs. Position maneuver
- GM determines which zones have difficult terrain before the battle begins

---

## Pre-Battle Checklist

1. Determine army sizes and battle type (Clash/Battle/Campaign)
2. Identify Army Commander (player or NPC) and each Unit Commander
3. Record each player knight's status: weapon skills, armor, horse, Followers, Squire age, Passions
4. Calculate Opening Army Intensity (Base 20 + Starting Conditions + Battle Events)
5. Note Battle Zones; all units start in Zone 4 unless scripted otherwise
6. All units start as Disengaged for the First Charge
7. Identify any terrain, weather, or scripted event modifiers
8. Proceed to Round 1, Step 3: Army Commander's Battle Roll
