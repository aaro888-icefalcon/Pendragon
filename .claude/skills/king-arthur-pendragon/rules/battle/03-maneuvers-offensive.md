# Offensive Maneuvers

Every offensive maneuver available to player units: prerequisites, opposed roll structure, opponent selection, melee skill modifiers, and full result tables (Triumph/Win/Loss/Crush) including Army Intensity and zone movement effects.

**Use when:** Unit Commander achieves a Success or Full Success on their Battle roll and wants to take aggressive action.

---

## How to Read Maneuver Entries

Each maneuver entry lists:
- **Prerequisite:** What conditions must be true to choose this maneuver
- **Opponents:** How many enemies are rolled/chosen, and from what source
- **Skill Modifier:** Any bonus or penalty applied to player knights' weapon skills this round
- **Result Table:** Triumph / Win / Loss / Crush outcomes — Army Intensity change and zone movement

Maneuver choices are constrained by the Battle roll result (see `02-battle-round-sequence.md` Step 3).

---

## Advance

**Prerequisite:** Unit is Disengaged AND in a Non-combat Zone (Zone 1–3 or 7–9)

**Opponents:** No foes — no melee this round

**Result:**
- All outcomes: Move forward 1–2 Zones; remains Disengaged next round
- No Army Intensity change

**Notes:** Used to move reserve units into combat zones, or reposition troops without fighting. No Battle roll is opposed; this is automatic if prerequisites are met.

---

## Charge

**Prerequisite:** Unit must be **Disengaged** (not Engaged in melee)

**Opponents:** 1 random foe (roll d20 on enemy table; d6+14 in Round 1)

**Skill Modifier:** +5 to Lance / Spear Expertise (Cymric) — "Charge Bonus"
- **Exception:** Enemy armed with Great Spears negates the +5 Charge Bonus (defenders lower pikes)

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −2 | Forward 2 Zones | Enemy unit may Rout |
| **Win** | −1 | Forward 1 Zone | — |
| **Loss** | 0 | Forward 1 Zone | — |
| **Crush** | +2 | Forward 1 Zone | Disordered |

**Notes:**
- The Charge is the default First Charge maneuver (Round 1)
- After a Charge (any result), unit is now Engaged unless it moved into a Non-combat Zone
- A Triumph on Charge moves the unit deep into enemy lines (Zone 5→7 or similar)
- On a Loss, knights are Engaged at their new forward zone (continued fighting next round)
- Lances that score an odd-number damage roll are broken; squire must bring replacement

---

## Attack

**Prerequisite:** None (may be used while Engaged or Disengaged)

**Opponents:** 3 random foes rolled; player chooses 1 to fight

**Skill Modifier:** None

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −2 | No movement | — |
| **Win** | −1 | No movement | — |
| **Loss** | 0 | No movement | — |
| **Crush** | +2 | No movement | — |

**Notes:**
- The standard "bread and butter" offensive maneuver when not set up for a Charge
- Player chooses the most advantageous of 3 rolled opponents
- Treat lances as spears when using Attack (no Charge bonus, no lance-specific rules)
- Can be used in any zone; does not require disengagement

---

## Attack vs. Two

**Prerequisite:** None

**Opponents:** 3 random foes rolled; player chooses 1, GM chooses 1 from remaining 2

**Skill Modifier:** None (but knight fights two opponents; see Dividing Attacks rule)

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −3 | No movement | — |
| **Win** | −1; Move forward 1 Zone | — | — |
| **Loss** | 0 | Recoil 1 Zone | — |
| **Crush** | +2 | Recoil 1 Zone | — |

**Notes:**
- High risk, high reward: potential −3 to Army Intensity on Triumph
- Knight must split attacks between two opponents (halve skill for each)
- Both results count separately toward unit tally
- GM chooses the second, less favorable opponent

---

## Attack with Another

**Prerequisite:** None

**Opponents:** 3 random foes rolled; player chooses 1; enemy at ×½ strength (half their combat skill)

**Skill Modifier:** None

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −1 | No movement | — |
| **Win** | 0 | No movement | — |
| **Loss** | 0 | No movement | — |
| **Crush** | +2 | Recoil 1 Zone | — |

**Notes:**
- "Another" is a friendly unit helping; enemy is weakened (×½ skill) because they must fight two fronts
- Lower Triumph bonus (−1 instead of −2) because the kill is shared
- Glory: same as normal, but may be split with the allied unit at GM discretion

---

## Assault vs. Position

**Prerequisite:** Enemy unit is in a prepared defensive position (earthworks, hilltop, hedgerow, dug-in)

**Opponents:** Nearby unit(s) in position (GM specifies which)

**Skill Modifier:** −15 to attackers; +10 to defenders (from earthworks/position)

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −2 | Move forward 1 Zone; Special! | Defenders driven out |
| **Win** | 0 | Enemy holds; Normal | — |
| **Loss** | 0 | Enemy holds; Recoil 1 Zone | — |
| **Crush** | +2 | Recoil 1 Zone | — |

**Notes:**
- "Special!" on Triumph means the position is breached; enemy unit loses Dug-In status
- Successful Horsemanship roll required before melee when attacking earthworks
- Cannot use Lance Charge against a Dug-In position
- See `07-battle-misc.md` for full terrain modifiers on different position types

---

## Attack Enemy Rear

**Prerequisite:** Unit is in a non-combat zone behind enemy lines (Zone 7–9), typically from Opportunity result or a deep Charge/Push Deeper result

**Opponents:** 1 random foe; enemy at ×½ strength (unshielded side, surprised)

**Skill Modifier:** +5 (rear attack advantage)

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −3 | No movement | Enemy unit may Rout |
| **Win** | −2 | No movement | — |
| **Loss** | 0 | Recoil 1 Zone | — |
| **Crush** | +2 | Recoil 1 Zone | Disordered |

**Notes:**
- Very powerful when available; the exposed flank and surprise give significant advantages
- Requires unit to have reached enemy rear zones through prior maneuvers or Opportunity

---

## Push Deeper

**Prerequisite:** None

**Opponents:** 3 random foes; GM chooses 1 (most dangerous to the GM's tactical advantage)

**Skill Modifier:** None

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −2 | Move forward 1 Zone | — |
| **Win** | −1 | Move forward 1 Zone | — |
| **Loss** | 0 | Normal; Disordered | — |
| **Crush** | +2 | Disordered | — |

**Notes:**
- Unlike Attack, GM chooses the opponent (not the player), and the unit always moves forward on a Win or Triumph
- Riskier than Attack but forces zone advancement
- An Opportunity to fight a Battalion/Army Commander often requires Push Deeper

---

## Follow

**Prerequisite:** Enemy is Withdrawing AND Army Intensity is 10 or 15 (low, enemy weakening)

**Opponents:** 1 random foe; foe receives +5 bonus to their combat skill (they're fighting while withdrawing defensively)

**Skill Modifier:** None

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −2 | Move forward 2 Zones | — |
| **Win** | 0 | Move forward 1 Zone | — |
| **Loss** | 0 | Move forward 1 Zone | — |
| **Crush** | +2 | Disengaged | — |

**Notes:**
- Used to press retreating enemies rather than letting them escape
- Enemy gets +5 because they're using controlled Withdraw while fighting
- Unit becomes Disengaged on Crush (enemy shakes them off)

---

## Pursue

**Prerequisite:** Enemy is Retreating AND Army Intensity is 14 or less

**Opponents:** 2 foes each at ×½ strength; Rearguard unit on d20 result 18–20

**Skill Modifier:** None (but Disordered on Triumph — reckless advance)

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −2 | Move forward 2 Zones; Disordered | — |
| **Win** | 0 | Move forward 2 Zones; enemy Broken | — |
| **Loss** | 0 | Move forward 1 Zone; Disengaged | — |
| **Crush** | +2 | Recoil 1 Zone; Disengaged | — |

**Notes:**
- Reckless: Triumph causes Disordered (your own troops scattered by the pursuit)
- Rearguard units (d20 18–20) are at ×½ but they are in position and ready — treat as a separate harder enemy
- Win result can Break the fleeing enemy unit

---

## Move on Flank

**Prerequisite:** None

**Opponents:** 1d6−2 foes (minimum 1)

**Skill Modifier:** +5 if successfully getting on the unshielded (right) flank of enemy

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | −1 | On flank or Charge next round | — |
| **Win** | 0 | Normal; on shielded flank | — |
| **Loss** | 0 | Normal | — |
| **Crush** | +2 | Disordered | — |

**Notes:**
- On a Triumph, the unit gains the "On Flank" position bonus next round (−5 Unit Intensity, +5 melee)
- On a Win, the unit achieves only the less advantageous shielded (left) flank
- Variable opponents (1d6−2) makes this maneuver unpredictable

---

## Run Down Sprinters

**Prerequisite:** Enemy unit has the Sprint ability (marked "S" in enemy table) and is currently fleeing/sprinting

**Opponents:** The sprinting unit itself

**Skill Modifier:** +5 (mounted pursuit advantage)

| Result | Army Intensity | Zone Movement | Other |
|--------|---------------|---------------|-------|
| **Triumph** | 0 | Move forward 2 Zones; Disordered; Check Reckless | — |
| **Win** | 0 | Move forward 1 Zone | — |
| **Loss** | 0 | Move forward 1 Zone; Disordered | — |
| **Crush** | +4 | Recoil 1 Zone; Check Cowardly | — |

**Notes:**
- Sprinters (S) have high DEX; they flee on foot and are hard to catch cleanly
- A Triumph check for Reckless: player may need to make a Reckless roll (GM discretion) or unit is scattered
- A Crush check for Cowardly: enemy sprinters successfully escape; player unit may suffer morale hit
- Sprint opponents fight at ×½ in melee (they're running away)

---

## Chase

**Prerequisite:** Enemy unit is Routing (has Broken); unit previously achieved a unit Break result

**Opponents:** 1d6 foes, each at ×½ strength; Rearguard units (d20 18–20) at full strength

**Skill Modifier:** Uses Hunting skill instead of weapon skill

| Result | Notes |
|--------|-------|
| All results | All knights are effectively Alone during a Chase; each resolves individually |

**Notes:**
- Chase replaces normal melee; uses Hunting skill
- Rearguard (18–20 on d20) represents enemy troops turning to fight to cover retreat; fight at full skill
- Glory for killing routing enemies is standard (×1 for win)
- After Chase, knights must return (Remove from Battle) or continue to Zone 8–9 (enemy camp)

---

## Stop

**Prerequisite:** Enemy is retreating and players do NOT wish to pursue

**Opponents:** None — no melee

**Result:** No movement; no Army Intensity change; unit remains Disengaged next round

**Notes:**
- Used when the battle is essentially won and further pursuit is deemed too risky or unnecessary
- Allows rest and reorganization before After the Battle phase

---

## Fancy Tactics (Optional)

Available when Unit Commander makes a Full Success AND special conditions apply (GM discretion):

- **Feigned Retreat:** Unit withdraws deliberately, drawing enemy forward into an ambush by allied units. Requires scripted setup or GM permission.
- **Double Attack:** Unit splits to engage two enemy units simultaneously. Both results count toward Army Intensity. Player splits skill (as per Dividing Attacks rule).
- **Attack vs. Reserves:** If enemy has fresh reserve units and player unit is at high intensity, this maneuver uses the fresh reserve's ×½ modifier.

---

## Maneuver Summary Table (Offensive)

| Maneuver | Prereq | Opponents | Skill Mod | Triumph ΔI | Win ΔI | Loss ΔI | Crush ΔI |
|----------|--------|-----------|-----------|-----------|--------|---------|---------|
| Advance | Disengaged, Non-combat Zone | None | — | 0 | 0 | 0 | 0 |
| Charge | Disengaged | 1 random | +5 Lance | −2 | −1 | 0 | +2 |
| Attack | None | 3→player picks 1 | None | −2 | −1 | 0 | +2 |
| Attack vs. Two | None | 3→player 1, GM 1 | None | −3 | −1 | 0 | +2 |
| Attack with Another | None | 3→player 1, enemy ×½ | None | −1 | 0 | 0 | +2 |
| Assault vs. Position | Position | Position unit(s) | −15/+10 | −2 | 0 | 0 | +2 |
| Attack Enemy Rear | In enemy rear | 1, enemy ×½ | +5 | −3 | −2 | 0 | +2 |
| Push Deeper | None | 3→GM picks 1 | None | −2 | −1 | 0 | +2 |
| Follow | Enemy Withdrawing, I≤15 | 1, foe +5 | None | −2 | 0 | 0 | +2 |
| Pursue | Enemy Retreating, I≤14 | 2 each ×½ | None | −2 | 0 | 0 | +2 |
| Move on Flank | None | 1d6−2 | +5 (flank) | −1 | 0 | 0 | +2 |
| Run Down Sprinters | Enemy Sprinting | Sprinting unit | +5 | 0 | 0 | 0 | +4 |
| Chase | Enemy Routing | 1d6 each ×½ | Hunting | All Alone | — | — | — |
| Stop | Enemy Retreating | None | — | 0 | 0 | 0 | 0 |

---

## Maneuver Choices by Battle Roll Result

| Battle Result | Offensive Options Available |
|--------------|----------------------------|
| Full Success (Critical) | All offensive maneuvers; may take Opportunity |
| Success | Charge, Attack, Attack vs. Two, Attack w/ Another, Push Deeper, Follow, Pursue, Move on Flank, Run Down Sprinters |
| Partial Success | Stand Fast, Pull Back, Run Away, Stand vs. Two (no aggressive options) |
| Failure | Stand Fast, Run Away (GM may allow Pull Back) |
| Fumble | Stand vs. Charge, Run Away (GM chooses if player doesn't) |
