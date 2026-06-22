# Injury, Death, and Healing

Hit points, wound categories, unconsciousness, death procedures, First Aid, natural healing, Chirurgery, deterioration, aggravation, and other damage types.

**Use when:** a character takes damage, needs medical treatment, or the GM must adjudicate ongoing wound recovery.

---

## Hit Points and Thresholds

| Derived Value | Formula |
|---|---|
| Total Hit Points | CON + SIZ |
| Unconscious threshold | Total HP / 4 (round down) |
| Major Wound threshold | = CON score |
| Mortal Wound threshold | = Total HP |
| Knockdown threshold | = SIZ score |

---

## Wound Categories

### Light Wound
- Single-hit damage < CON score
- Character continues normally
- No special procedure required

### Major Wound
- Single-hit damage ≥ CON score
- "Chirurgery Needed" box is checked (character becomes **Unhealthy**)
- GM rolls on **Stats Lost** table
- Character makes CON roll to remain conscious
- Character makes Valorous roll to continue fighting this round
- If character survives: First Aid may be applied

### Mortal Wound
- Single-hit damage ≥ Total HP
- Character will die unless First Aid is applied within **1 hour**
- "Chirurgery Needed" box is checked
- If First Aid succeeds: character survives (at 1 HP or Unconscious) → 3 rolls on Stats Lost table
- If First Aid fails or is not applied in time: character dies

---

## Recording Injuries (5-Step Procedure)

1. Note current HP before hit
2. Subtract armor/shield reduction from damage
3. Subtract remaining damage from current HP
4. Record each hit as a separate wound (for First Aid purposes)
5. Check thresholds: Unconscious? Major Wound? Mortal Wound?

---

## States of Health

### Healthy
- "Chirurgery Needed" box is NOT checked
- Character functions normally despite minor wounds
- Natural healing applies normally
- Aggravation possible if current HP ≤ half Total HP and character performs strenuous activity

### Unhealthy
- "Chirurgery Needed" box IS checked
- Character cannot care for themselves properly
- Deterioration may occur without Chirurgery
- Any physical exertion risks Aggravation (see below)

**Causes of Unhealthy status:**
1. Current HP drops to or below Unconscious threshold
2. Suffering a Major Wound
3. Surviving a Mortal Wound
4. Chirurgeon fumbles a First Aid roll
5. Contracting illness (dungeon conditions, poison, etc.)

---

## First Aid

Immediate emergency treatment. Must be applied within certain time limits.

**Restores:**
- Success: 1d3 HP
- Critical success: 1d3 + 3 HP
- Fumble: inflicts 1d3 HP damage

**Restrictions:**
- Only works on wounds less than 1 day old
- One application per wound (each separate wound may be treated once)
- First Aid cannot help wounds caused by Deterioration or Aggravation
- Does NOT clear the "Chirurgery Needed" status (only Chirurgery can do that over time)

---

## Natural Healing

- Healing Rate HP restored every **Sunday at noon**
- Healing Rate = (CON + STR) / 10 (round down)
- Applies to both Healthy and Unhealthy characters
- Unhealthy characters may lose HP to Deterioration on the same day (net may be negative)

---

## Chirurgery

Long-term medical care for Unhealthy characters only.

**How it works:**
- One Chirurgery roll per patient per week
- Normally made at the beginning of the week; result takes effect Sunday (same day as natural healing)
- **Success:** Deterioration does not occur this week
- **Critical success:** Deterioration prevented AND patient heals double their normal Healing Rate that week
- **Failure:** Deterioration occurs (but this effect is not apparent until Sunday)
- **Fumble:** Patient immediately loses 1d3 HP (no wound recorded; First Aid cannot help) AND suffers deterioration at end of week

**Recovery:** normally 2–3 consecutive successful Chirurgery rolls return a patient from Unhealthy to Healthy (GM discretion; more time for severe wounds).

**Modifiers:**
- Unclean/unhealthy conditions (filth, cold, disease): −5 to Chirurgery skill

**Restriction:** if two or more chirurgeons both attempt to treat the same patient in one week, all automatically fail.

---

## Deterioration

Affects Unhealthy characters who did NOT receive a successful Chirurgery roll during the week.

- Loses **1d6 HP** per week (Sunday at noon, same time as natural healing)
- No wound is recorded for this damage
- First Aid cannot help deterioration damage
- Net result that Sunday = Healing Rate gain − Deterioration loss (can be negative)

---

## Aggravation

Worsening a condition through excessive activity while wounded or ill.

Aggravation causes **immediate** HP loss (no wound recorded; cannot be treated by First Aid, Chirurgery, or any die roll).

### Aggravation Damage Table

| Activity Level | Healthy (HP ≤ half) | Unhealthy |
|---|---|---|
| None (resting, eating, sleeping) | 0 | 0 |
| Light (walking slowly, talking, writing) | 0 | 1 |
| Moderate (walking, riding, dancing, arguing) | 0 | 2 |
| Strenuous (fighting, running, climbing, traveling) | 1 | 3 |

**Notes:**
- Healthy characters only suffer aggravation if current HP is at half Total HP or less, AND only at GM option
- Characters at or below Unconscious threshold cannot receive aggravation (they are comatose)
- Sustained activity may increase aggravation beyond the table (GM's call; e.g., 1+ hour of light activity for an Unhealthy character might deal 2 instead of 1)

---

## Other Damage Types

### Disease
- Character becomes Unhealthy; check the "Chirurgery Needed" box
- Generally does not cause Major or Mortal Wounds
- No wound is recorded; only general HP loss
- First Aid normally does not help disease

### Poison

Target makes CON roll opposed to Potency roll (1d20 + Potency).

| CON Roll Result | Poison Effect |
|---|---|
| Critical success | No effect |
| Success | Victim becomes Unhealthy |
| Partial success | Unhealthy + damage equal to Potency − CON score |
| Failure | Unhealthy + damage equal to Potency |
| Fumble | Unhealthy + damage equal to 2 × Potency |

### Falling

| Fall Distance | Damage |
|---|---|
| Less than 3 feet | No damage |
| Each 6 feet (or fraction) beyond 3 feet | +1d6 |
| Horse (approx. 5-foot drop) | 1d6 |
| House roof (12 feet) | 2d6 |
| Cliff or castle wall (50 feet) | 8d6 |

- Armor does NOT reduce falling damage
- Magical armor effects may reduce it at GM's option
- Wounds calculated normally

**Dropped Objects:** 1 point of damage per 10 lbs + 1 point per 3 feet of drop height.
- Armor (including shields) reduces dropped object damage normally.

### Fire and Heat

- Normal fire: 1d6 damage per round
- Consecutive contact: cumulative +1d6 per round (1d6 first round, 2d6 second round, 3d6 third, etc.)
- Torch used as weapon (contact, no sustained burn): 1d6 only, no cumulative
- Hotter sources (red-hot iron, boiling lead): 2d6 cumulative per round or more
- No natural fire harms characters over 12 feet away
- **Armor (any type, not clothing) reduces fire damage by 1d6** — no damage first round; 1d6 second round of contact; etc.
- Each distinct source/application of heat = one wound (not separate wounds per round of same contact)

### Suffocation (Water, Smoke, Vapors)

- CON roll each round of exposure
- Success: no damage this round
- Failure: 1d6 damage per round thereafter while remaining exposed
- Cumulative CON penalty: −1 per round beyond the first (e.g., 7th consecutive round = −7 to CON roll)
- No actual wound recorded; recovery may be faster than from physical wounds at GM's option

---

## Unconsciousness and Recovery

- Current HP ≤ Unconscious threshold = fall unconscious
- Unconscious characters may not act
- Natural healing still applies weekly
- A Chirurgery roll can be attempted to stabilize

---

## Death

A character dies when:
- Current HP reaches 0 or below due to any damage source
- Mortal Wound was received and no successful First Aid applied within 1 hour
- Aging table reduces a key stat to 0

