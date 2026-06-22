# Resolution Mechanics

Core dice-resolution rules for all rolls: success thresholds, critical/fumble triggers, opposed resolution, modifiers, experience checks, and movement.

**Use when:** adjudicating any die roll — skill check, trait roll, passion invocation, combat exchange, opposed contest, or travel.

---

## The d20 Roll

All resolution uses a single d20.

- **Success:** roll ≤ current stat value
- **Critical:** roll exactly equals stat value (counts as 20 points for non-combat Glory)
- **Fumble:** roll 20 (only possible if stat < 20)
- **Failure:** roll > stat (and not a fumble trigger)

### Stats Over 20

When a stat exceeds 20:
- Bonus to die roll = (stat value − 20); add this to the d20 result before comparing
- Any roll result of 20 or higher (after bonus) = **critical success**
- **No fumble possible** for stats ≥ 20
- Opposite trait/skill = 0 (cannot be used)

### Stats Equal to 0

- Automatic failure on all rolls
- Still roll d20 to check for fumble (roll of 20 = fumble result)

---

## Unopposed Resolution

Roll d20 against your stat:

| Roll Result | Outcome |
|---|---|
| Exactly equals stat | Critical success |
| ≤ stat (but not exact) | Success |
| > stat | Failure |
| 20 (and stat < 20) | Fumble |

---

## Opposed Resolution

Both characters roll simultaneously. Determine outcome by comparing results:

| Situation | Outcome |
|---|---|
| Only one succeeds | That character wins; other loses |
| Both succeed; one rolls higher | Higher roll wins (full success); lower roll = partial success |
| Both succeed; tie | No resolution — tied (special: sword breaks non-sword on tie) |
| Both fail | Mutual failure — no effect |
| One crits | Crit beats normal success |
| Both crit | Tie — no resolution |
| One fumbles | Fumbler suffers fumble result regardless of opponent's roll |

### Partial Success (Loser Who Succeeded)

A character who succeeded but rolled lower than the winner still succeeded — they may apply shield reduction (6 armor reduction) against combat damage.

---

## Critical Success Effects

- **Combat:** double damage (roll dice twice and add)
- **Trait/Passion roll:** character acts strongly on that trait/passion AND gains an experience check
- **Non-combat skill:** 20 Glory points; in some contexts ×2 to ×5 multiplier
- **Chirurgery critical:** patient gains double Healing Rate that week

---

## Fumble Effects

- **Weapon (sword):** weapon dropped
- **Weapon (non-sword):** weapon broken
- **First Aid:** inflicts 1d3 damage instead of healing
- **Chirurgery:** patient loses 1d3 HP immediately AND suffers deterioration at end of week
- **Trait/Passion:** opposite trait checked; character acts on opposite trait

---

## Standard Modifiers

Apply modifiers directly to the skill value before rolling:

| Modifier | Meaning |
|---|---|
| +5 / −5 | Standard advantage/disadvantage |
| +10 / −10 | Strong advantage/disadvantage |
| +15 / −15 | Extreme advantage/disadvantage |

**Reflexive modifiers:** when one side gains +X, the other side suffers −X (e.g., higher ground gives +5 to the high fighter and −5 to the low fighter).

### Common Situational Modifiers

| Situation | Modifier |
|---|---|
| Cover (ranged attacks) | −5 to attacker |
| Fatigue | −5 |
| Higher ground | +5 attacker / −5 defender |
| Immobilized target | +10 attacker / −10 target |
| Surprise (unopposed) | +5 |
| Unburdened (no armor) | +5 |
| Poor visibility | −10 (or −5 with successful Awareness roll) |
| Mounted vs. foot (melee) | +5 to mounted / −5 to foot |

---

## Experience Checks

A skill is **checked** (mark box on sheet) when:
- Used successfully in a significant situation during play
- A critical success occurs on any trait or passion roll

**Resolving checks (Winter Phase Step 2):**
- Roll d20 against current value
- If d20 **exceeds** current value → increase by +1
- Works for skills over 20 (roll d20 + (skill−20) bonus; if total exceeds skill = gain)
- Cannot fail to improve (worst case is no gain)

---

## Time Scales

| Scale | Duration | Use |
|---|---|---|
| Campaign | One scenario per year | Overall campaign structure |
| Narrative | Variable | Story scenes, travel descriptions |
| Real time | Continuous | Negotiations, conversations |
| Battle round | ~30 minutes | Mass combat |
| Melee round | Elastic (one action) | Individual combat exchanges |

---

## Movement

**Movement Rate** = (STR + DEX) / 10 (round down)

| Mode | Speed |
|---|---|
| Normal | Movement Rate yards/round |
| Running | Movement Rate × 2 |
| Sprinting | Movement Rate × 3 (requires CON roll or slow to half speed; fumble = collapse + 2d6 damage) |

Knights unencumbered (no armor) gain +2 to Movement Rate.

### Travel Rates (Miles Per Day)

| Road Type | Cautious | Leisurely | Normal | Hurried |
|---|---|---|---|---|
| Royal Road | 10 | 15 | 20 | 30 |
| Local Road | 5 | 10 | 15 | 25 |
| Path | 2 | 5 | 8 | 12 |
| Track | 1 | 2 | 3 | 4 |

**Forced March:**
- Make CON roll
- Success: +Movement Rate × 3 bonus miles
- Failure: half distance, must rest
- Fumble: injury (2d6 damage) or horse lamed

---

## DEX Rolls

### Balance (Knockdown Check)

When knocked down (damage ≥ SIZ), roll DEX (or Horsemanship if mounted):
- Success: remain standing
- Failure: fall (1d6 damage if dismounted from horse)
- Damage ≥ 2×SIZ = automatic knockdown, no roll

While knocked down: −5 to own combat rolls, enemy gains +5.
Stand up: movement phase action.

### Climb

- −5 rough vertical surface, −10 smooth vertical surface
- Rope: +5, Ladder: +10
- One roll per 30 feet climbed

### Jump

- −3 per yard beyond 1 yard

### Sneak

- Critical success always succeeds (unless opponent also crits)
- −5 modifier in metal armor
- No penalty in leather armor

