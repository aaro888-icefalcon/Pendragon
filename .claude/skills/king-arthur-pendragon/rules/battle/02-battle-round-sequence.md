# Battle Round Sequence

The complete 5-step loop for each battle round, from determining knight status through adjusting Army Intensity. Includes First Charge special rules, Automatic Events, zone movement, Extended Melee Phases, and the conditions that end a battle.

**Use when:** Running any round of battle after initial setup.

---

## Round Structure Overview

Each round (except Round 1 First Charge) follows these five steps:

1. **Determine Player Knight Status** — check each knight's current condition
2. **Calculate Intensity** — Army Intensity, then Unit Intensity
3. **Unit Maneuver** — Unit Commander's Battle roll, choose maneuver
4. **Melee Combat** — seven sub-phases
5. **End of the Round** — Unit Results, Glory, Squire rolls, optional Extended Melee, Army Intensity adjustment

---

## STEP 1: Determine Player Knight Status

Check each player knight's current condition. Conditions may stack.

| Condition | Check |
|-----------|-------|
| Mounted / Afoot | Is knight still on horse? |
| Alone | Separated from unit? (+10 own Unit Intensity) |
| Attached / Unit Commander | What role this round? |
| Broken | Was unit destroyed last round? (Knight is now Alone) |
| Disordered | Did unit recoil last round? (+5 Unit Intensity, −10 melee) |
| Disengaged | Did unit successfully Pull Back / Withdraw last round? |
| Wounded | Took damage; apply KAP wound rules |
| Burdened / Encumbered / Guiding | Carrying extra load? |
| Squire status | Is squire still present? What age? |
| Followers remaining | How many NPC knights still with Unit Commander? |
| Passions | Any Notable (≥16) Passions triggered this round? |

---

## STEP 2: Calculate Intensity

### 2A. Calculate Army Intensity

**Army Intensity = Previous Round's Final Army Intensity + Battle Events Roll**

- **Round 1 only:** Army Intensity = Base 20 + Starting Conditions + Battle Events
- **All subsequent rounds:** Starting Conditions is NOT added again
- **Battle Events:** Roll 3d6 − 10; apply result to Army Intensity
- Battle Events can be negative (favorable) or positive (unfavorable)

### 2B. Check for Automatic Events

After calculating Army Intensity, check thresholds:

| Army Intensity | Automatic Event |
|---------------|-----------------|
| 0 or less (two consecutive rounds) | Enemy army Routs; battle effectively over |
| 10 or less (two consecutive rounds) | Enemy army Signals Retreat |
| Exactly 30 | Rally required; enemy makes desperate stand |
| 40 or more | Player army Routs; unit commanders must use Run Away or Pull Back |

- "Two consecutive rounds" means the threshold must be met at the START of the round and at the END of the previous round
- **Retreat** (Intensity ≤10 for 2 rounds): Enemy army withdraws; player may Pursue or Stop
- **Rout** (Intensity ≤0 for 2 rounds): Enemy army collapses; player enters Chase phase

### 2C. Calculate Unit Intensity

**Unit Intensity = Army Intensity + Battle Zone Modifier + Unit Cohesion Modifier(s) + Terrain Modifier(s)**

#### Battle Zone Modifiers

| Zone | Modifier |
|------|---------|
| Zones 1–2 (player rear) | −5 to −10 |
| Zone 3 (player reserve) | +0 |
| Zone 4 (starting position) | +5 |
| Zone 5 (Killing Zone) | +10 |
| Zone 6 (enemy second rank) | +10 |
| Zone 7–8 (enemy rear) | +5 to −5 |
| Zone 9 (enemy camp) | Special (see `07-battle-misc.md`) |

#### Unit Cohesion Modifiers (complete list)

| Condition | Unit Intensity Modifier | Melee Modifier | Other |
|-----------|------------------------|----------------|-------|
| Disengaged | −20 | Not applicable | Disengaged; see Zone rules |
| Disordered | +5 | −10 | None |
| Alone | +10 | None | Knight acts as own UC |
| Broken | n/a | Not applicable | Knight is Alone in battle |
| On Enemy Flank | −5 | +5 | None |
| Position of Honor | +5 | None | Increased Glory |
| Fresh Reserves (enemy) | None | −10 to UC's Battle skill | None |
| Fresh Reserves (friendly) | −10 | Enemy ×½ | Maneuver will change |
| Ambushed | Varies (+10–+20) | See ambush rules | Disordered on ambush round |

**Rule:** If Unit Intensity calculates to 0 or negative, treat as 1 for all roll purposes.

---

## STEP 3: Unit Maneuver

### 3A. Unit Commander's Battle Roll

The Unit Commander (UC) makes an opposed roll:
- **UC rolls:** d20 vs. Battle skill (lower = better)
- **Opposed by:** Unit Intensity (treated as a skill: roll d20 + bonus matching intensity value, or use intensity directly as difficulty)

**Interpreting the opposed result:**

| UC Result vs. Unit Intensity | Outcome |
|------------------------------|---------|
| UC Critical, any Intensity result | UC Full Success: full choice of maneuver; Opportunity roll |
| UC Success vs. Intensity Success (UC higher) | UC Success: choose from success maneuvers |
| UC Success vs. Intensity Critical | Partial Success: limited maneuver choices |
| UC Failure | UC Failure: GM chooses maneuver from failure list |
| UC Fumble | UC Fumble: worst options; unit may be Charged |

### Opportunity (on UC Critical Success)

When the UC scores a Critical, roll d20 on the Opportunity Table:

| d20 | Opportunity |
|-----|-------------|
| 1–5 | No opportunity this round |
| 6–10 | Mystery Unit: face unknown enemy, chance for a surprise |
| 11–15 | Enemy on the flank: +5 melee next round |
| 16–18 | Attack Enemy Rear: ignore normal zone restrictions |
| 19 | Attack Battalion Commander (Extended Melee required) |
| 20 | Attack Army Commander (Extended Melee required) |

### 3B. Choose a Maneuver

Based on the Battle roll result, choose from available maneuvers. Full maneuver tables in `03-maneuvers-offensive.md` and `04-maneuvers-defensive-retreat.md`.

**Maneuver Choices by Result:**

| UC Battle Result | Maneuvers Available |
|-----------------|---------------------|
| Full Success | Any maneuver; may also take Opportunity |
| Success | Most maneuvers except the most aggressive options |
| Partial Success | Stand Fast, Pull Back, Run Away, Stand vs. Two |
| Failure | Stand Fast, Run Away, or GM chooses |
| Fumble | Stand vs. Charge, Run Away, or GM chooses worst option |

---

## STEP 4: Melee Combat

Seven sub-phases, in order:

### 4.1 Determine Opponent(s)
- Roll d20 on the enemy army's unit table
- Number of opponents determined by maneuver chosen (see maneuver tables)
- First Charge (Round 1): roll d6+14 (tougher units are at the front)
- Subsequent rounds: roll d20

### 4.2 Calculate Player Knight Melee Skill
Base skill = highest applicable weapon skill (Lance for Charge, Spear Expertise for Cymric, Sword if dismounted, etc.)

Apply all modifiers:

| Modifier Source | Effect |
|----------------|--------|
| Mounted vs. infantry | +5 to player's attack |
| Infantry vs. mounted | −5 to player's attack |
| First Charge bonus (Army Commander won) | +5 to Lance/Spear Expertise |
| Lance Charge bonus (maneuver) | +5 to Lance/Spear Expertise |
| Maneuver penalty (Pull Back, Withdraw) | −5 to all weapon skills |
| Disordered | −10 to all weapon skills |
| Passion (Impassioned) | +10 to weapon skill for this round |
| Passion (Critical) | Double weapon skill for this round |
| Enemy Great Spear cancels Charge bonus | Charge +5 bonus negated |
| Defense tactic | Results count as Loss for unit tallying, but prevents Crush |

### 4.3 Missile Phase
- If any opposing unit has missile weapons (archers, crossbowmen, javelineers) and is NOT engaged in melee, they may fire
- Missile unit vs. non-engaged player unit: roll on "Missile Fire from Non-Engaged Units" table
- Player in Zone X, missile unit in Zone Y: roll 1d6; fire on 1–4 (if zones are adjacent/close)
- Knight targeted by missiles may split attacks between missile unit and melee opponent (halving skill for each)
- Against missile units: **Win** = missile unit loses; **Loss** = missile unit wins; **Tie** = tie
- Glory for being shot at: equal to missile unit's Glory value (even without winning)

### 4.4 Melee Phase
- Each player knight makes an opposed roll vs. their opponent's combat skill
- Opponent's skill from their unit table entry (see `05-battle-events-tables.md` and armies files)
- **Results:**
  - **Critical vs. lower result:** Win; Glory × 2
  - **Success vs. lower success:** Win; Glory × 1
  - **Tie:** Tie; Glory × 1 (counts as Win for unit tally in most maneuvers)
  - **Loss (higher roll):** Loss; Glory × ½
  - **Opponent Critical vs. player success:** player takes damage (roll enemy damage dice; apply to armor)
- When player takes damage: roll enemy's damage dice; subtract armor total; remainder is damage taken
- Knights with ♞ symbol are mounted; charge with lance
- Knights with £ symbol may be taken prisoner for ransom

### 4.5 Bodyguard Bonus (Optional, Unit Commander only)
- Available if UC has 5+ Followers remaining
- Used when UC is about to be critically hit or killed
- Followers sacrifice themselves; UC's result is negated (re-roll or treat as Loss)
- Cost: roll 2d6−4 Followers lost (minimum 0)
- Can only be used once per round
- If Bodyguard Bonus is used, skip the Followers' Fight Phase this round

### 4.6 Followers' Fight Phase
- Occurs only if Bodyguard Bonus was NOT used this round
- UC rolls for his Followers against the same enemy type faced
- Followers use default skill 15 vs. enemy's combat skill
- Apply same maneuver modifiers as player knights
- **On Win:** No followers lost
- **On Loss or Crush:** Roll for follower losses:
  - Loss: 1d6−4 followers lost (minimum 0)
  - Crush: 2d6−4 followers lost (minimum 0)
- Followers with Loyalty (Lord) 15+ may invoke Passion for +10 to their default skill (GM discretion)

### 4.7 Dividing Attacks
A player knight may split their attack against two opponents by halving their skill (round down) for each attack. Both results count separately toward unit tally.

---

## STEP 5: End of the Round

### 5A. Determine Unit Results

Count all individual melee results from this round (all player knights + any Followers' Fight results, if tracked):

| Result | Condition |
|--------|-----------|
| **Triumph** | All knights won their melee phase |
| **Win** | Half or more won (or tied); not all won |
| **Loss** | More than half lost |
| **Crush** | All knights lost their melee phase |

- Against missile units: Win = missile unit lost; Loss = missile unit won
- Defense tactic: always counts as a Loss for unit tally purposes (but prevents Crush)
- Knights who are Alone figure their result separately from the main unit

### 5B. Calculate Player Knight Glory

Glory per knight = (Enemy's base Glory value) × (Result multiplier) × (Critical multiplier)

| Personal Result | Glory Multiplier |
|----------------|-----------------|
| Win | ×1 |
| Tie | ×1 |
| Loss | ×½ |
| Critical (personal) | ×2 (stacks with result multiplier) |
| Inactive/Wounded (present but unable to fight) | ×½ |

- Round fractions up
- Enemy Glory values listed in their unit table entries
- Double attack enemies (×2): full Glory for each opponent if won

### 5C. Squire Roll and Actions

Each player knight with a squire makes a **Squire Roll:**
- Roll d20; target number = squire's age
- **Success:** Squire is unharmed and in position
- **Failure:** Squire may be lost, injured, or captured; roll on Squire Retreat Results table (see `06-battle-aftermath.md`)

**Squire Actions (if roll succeeded):**
- Bring replacement horse if knight's horse was killed or lost
- Bring replacement lance if lance was broken (odd damage roll = broken lance)
- Guide an extra horse (captured horse if applicable)

**Captured Horses:** If squire succeeds and enemy unit has ♞ symbol, roll on Captured Horse Table (see `06-battle-aftermath.md`).

### 5D. Extended Melee Phase (Optional)

After normal melee, unit may enter an Extended Melee for Special Actions:
- **Rescue a Friend** — retrieve an unhorsed knight from the battle
- **Take a Prisoner** — capture an enemy with £ symbol for ransom
- **Fight an Enemy Leader** — engage Battalion/Army Commander
- **Rally** — restore a routing unit

Each Extended Melee round is fought separately. Full rules in `06-battle-aftermath.md`.

### 5E. Adjust Army Intensity

Apply Unit Results to Final Army Intensity:

| Unit Result | Army Intensity Adjustment |
|-------------|--------------------------|
| Triumph | −2 |
| Win | −1 |
| Tie | 0 |
| Loss | 0 |
| Crush | +2 |

- This adjustment applies to the **entire army's** Intensity (not just the player unit)
- Killing a Battalion Commander: additional −10 to Army Intensity immediately
- Scripted Events may add or subtract additional Intensity at GM's discretion
- The result becomes the **Final Army Intensity** for this round, which is the **Starting Army Intensity** for the next round

---

## Zone Movement by Maneuver Result

| Maneuver | Triumph | Win | Loss | Crush |
|----------|---------|-----|------|-------|
| Charge | Forward 2 | Forward 1 | Forward 1 | Forward 1; Disordered |
| Attack | No move | No move | No move | No move |
| Push Deeper | Forward 1 | Forward 1 | Normal; Disordered | Disordered |
| Follow | Forward 2 | Forward 1 | Forward 1 | No move |
| Pursue | Forward 2; Disordered | Forward 2; Broken enemy | Forward 1; Disengaged | Recoil 1; Disengaged |
| Pull Back | Back 1; Disengaged; −2 | Back 1; Disengaged | Recoil 1 | +2 Intensity; Broken |
| Withdraw | Back 1; Disengaged; −2 | Back 1; Disengaged | Back 1 | Recoil 1 |
| Run Away | Back 1–2; Disengaged | Recoil 1; Disengaged | +2; Broken | +2; Broken |
| Stand Fast | Disengaged; −2 | Normal; Engaged | Recoil 1 | +2; Recoil 1 |
| Charge (Triumph) | Forward 2; enemy may Rout | | | |

Full zone movement tables by maneuver in `03-maneuvers-offensive.md` and `04-maneuvers-defensive-retreat.md`.

---

## When Battles End

A battle ends when any of the following occur:

1. **Enemy Army Intensity ≤ 0 for 2 consecutive rounds** → enemy Routs; Decisive Victory for players
2. **Enemy Army Intensity ≤ 10 for 2 consecutive rounds** → enemy Retreats; may be Decisive or Indecisive
3. **Player Army Intensity ≥ 40** → player army Routs; Decisive Defeat
4. **Scripted Event** → GM declares battle over (common for historical scenarios)
5. **All enemy units eliminated** → extremely rare; Decisive Victory
6. **Nightfall / terrain forces disengagement** → GM call; typically Indecisive result

**Indecisive Victory/Defeat:** Most battles end this way. No Loot. Victory Glory modifier applies. See `06-battle-aftermath.md`.

**Decisive Victory:** Enemy fled the field or suffered catastrophic casualties. Loot available. Maximum Glory modifiers.

---

## Long and Short Battles

- **Short battle** (fewer than 5 rounds): Unit Commander Glory bonus reduced by half
- **Long battle** (10+ rounds): Additional Scripted Events likely; GM may add +5 to Starting Conditions each additional 5 rounds
- Standard battle length: 5–8 rounds

---

## The "Alone" Knight

A knight who is Alone (unhorsed and separated, or unit Broken):
- Acts as their own Unit Commander
- +10 to their personal Unit Intensity
- Must use Run Away, Sprint, or Stand Fast (no aggressive maneuvers while Alone)
- May attempt to Rescue a Friend (Special Action, Extended Melee)
- Squire may attempt Squire Retreat to retrieve them

---

## Multiple Units in One Battle

When running multiple player units simultaneously:
1. Calculate Army Intensity once (shared)
2. Each unit calculates its own Unit Intensity separately (different zones, cohesion states)
3. Each Unit Commander makes their own Battle roll
4. Melee resolved separately per unit
5. Apply each unit's result separately to Army Intensity (can have multiple adjustments)
6. Alone knights' results are tallied separately from their former unit
