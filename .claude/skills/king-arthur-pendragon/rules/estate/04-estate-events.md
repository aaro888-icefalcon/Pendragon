# Estate Events: Damage and Recovery

The Lots system for estate damage, all damage types and their effects, all recovery methods, and the procedures for applying damage and reconstruction during the Winter Phase.

**Use when:** An estate is raided, pillaged, plundered, or ravaged; weather damage occurs; applying recovery actions; determining how long reconstruction takes.

---

## The Lots System

**1 Lot = £1 of annual income.**

Lots represent units of estate productivity. A £10 manor has 10 Lots. A £50 estate has 50 Lots.

Lots come in two types:

| Type | Symbol | Meaning |
|------|--------|---------|
| Temporary (T) | T | Lost income this year only; recovers automatically next year |
| Permanent (P) | P | Reduced annual income until repaired; does NOT self-recover |

**Effect of damage:** Each Temporary Lot lost = £1 less income this year. Each Permanent Lot lost = £1 less income every year until repaired.

**Repairing Permanent Lots:** See Recovery Methods below.

---

## Damage Events

### Military Damage

| Action | Temporary Lots Lost | Permanent Lots Lost | Notes |
|--------|--------------------|--------------------|-------|
| Raid | 3T | 0P | Cattle and livestock driven off; no structures damaged |
| Pillage | 3T | 2P | Buildings damaged, crops burned |
| Plunder | 3T | 4P | Systematic destruction of productive capacity |
| Ravage | 3T | 6P | Total devastation; structures destroyed |

**Who inflicts each:**
- **Raid:** Fast-moving attackers; take portable goods and animals.
- **Pillage:** Attackers with time; burn fields and break tools.
- **Plunder:** Attackers with intent to cripple; destroy infrastructure.
- **Ravage:** Full army with orders to lay waste; maximum destruction.

A knight may also use these actions against his own estate (desperation income). See `02-estate-economics.md`.

---

### Weather Damage

Weather damage is determined by a random roll each Winter Phase (GM may use this as an optional rule or mandate it each year).

| Roll (d20 or narrative) | Category | Temporary Lots | Permanent Lots |
|------------------------|----------|---------------|----------------|
| Normal year | None | 0 | 0 |
| Moderate hardship (result 4–6) | Bad harvest | 1T–2T | 0P |
| Significant hardship (result 7–9) | Flooding/drought | 3T–4T | 1P |
| Severe hardship (result 10+) | Catastrophe | 4T–6T | 2P–3P |

Specific weather events (flood, drought, blight, pestilence) are adjudicated by the GM based on regional conditions and story context.

---

## Recovery Methods

All recovery applies during the **Winter Phase Step 4** (Economic Check), after damage is noted.

### Automatic Recovery: Gentlewoman (Lady of the Estate)

A competent gentlewoman (knight's wife or female estate manager) overseeing the household provides automatic recovery each year, no roll required:

- Recovers **1 Temporary Lot** per year automatically.
- Recovers **1 Permanent Lot** per year automatically.

**Condition:** The gentlewoman must be present on the estate and actively managing it.

---

### Stewardship Recovery (Steward's Skill Roll)

The estate's Steward makes a Stewardship skill roll each Winter Phase.

| Result | Recovery |
|--------|---------|
| Critical Success | 2T recovered |
| Success | 1T recovered |
| Failure | No recovery this method |
| Fumble | GM may apply -1T (mismanagement worsens condition) |

---

### Stewardship Rebuild (Steward's Skill Roll: Permanent Damage)

To repair Permanent Lots, the Steward makes a separate Rebuild roll. This requires actual expenditure of funds.

**Cost:** Half the Lot's original value (£0.5 per £1 of annual income being restored), paid in cash from the estate's resources.

| Result | Recovery |
|--------|---------|
| Success | 1 Permanent Lot repaired |
| Failure | Money spent; no repair this year |
| Critical Success | 1 Permanent Lot repaired; no additional effect |
| Fumble | Money spent; 1 additional Temporary Lot of damage from botched repairs |

---

### Reconstruct (Knight's Personal Action)

The knight himself may oversee reconstruction as a personal project during the year. This is a directed action, not a passive roll.

| Result | Recovery |
|--------|---------|
| Critical Success | 2 Permanent Lots repaired |
| Success | 1 Permanent Lot repaired |
| Failure | No repair; time spent |
| Fumble | -1 Permanent Lot (further damage from poor oversight) |

**Limitation:** The knight may only Reconstruct if he is present on the estate for the majority of the year (not away on campaign for more than a season).

---

### Russet Monk (Spiritual/Agricultural Advisor)

A monk or friar with agricultural knowledge assists in recovery. Requires the estate to have a chapel, hermitage, or other religious presence.

| Result | Recovery |
|--------|---------|
| Success | 1 Temporary Lot recovered |
| Failure | No effect |

The monk's Stewardship (or equivalent skill) is used for this roll, not the knight's.

---

## Recovery Summary Table

| Method | Action Type | Recovers | Roll Required | Cost |
|--------|------------|---------|---------------|------|
| Gentlewoman (present) | Automatic | 1T + 1P per year | None | None |
| Stewardship (T) | Passive officer roll | 1T on success | Stewardship | None |
| Stewardship Rebuild (P) | Active + expenditure | 1P on success | Stewardship | ½ Lot value in cash |
| Reconstruct (P) | Knight's personal action | 2P crit / 1P success / -1P fumble | Knight roll | None |
| Russet Monk | Religious assistant | 1T on success | Monk's skill | None |

Multiple methods may be applied in the same Winter Phase; each recovers independently.

---

## Applying Damage and Recovery: Step-by-Step

This is the full procedure for Winter Phase economic damage/recovery:

1. **Note all damage events** that occurred during the year (raids, weather, self-inflicted).
2. **Tally total Temporary Lots lost** and **total Permanent Lots lost**.
3. **Subtract Temporary Lots** from this year's income calculation (£1 per T lost).
4. **Subtract Permanent Lots** from the estate's base annual income (permanent adjustment).
5. **Apply Gentlewoman recovery** first (automatic, if eligible): remove 1T and 1P from the tally.
6. **Roll Stewardship** for remaining Temporary Lots: on success, remove 1T.
7. **Roll Stewardship Rebuild** if attempting Permanent repair (costs cash): on success, remove 1P.
8. **Resolve Reconstruct** if the knight took this action: apply result.
9. **Resolve Russet Monk** if applicable: on success, remove 1T.
10. **Record remaining damage.** Permanent Lots that are not repaired reduce next year's base income.

---

## Estate Recovery Limits

- A single estate cannot recover more Permanent Lots in one year than it lost in the previous year (you cannot "bank" recovery against future damage).
- Temporary Lots that are not recovered in the year they were incurred are simply lost; they do not carry forward.
- If an estate's Permanent Lots lost equals or exceeds its total Lots (i.e., total permanent damage ≥ annual income), the estate is **ruined** and generates no income until reconstruction brings it above zero.

---

## Ruined Estate

If an estate reaches 0 annual income due to Permanent damage:

1. The estate generates no income this year or any subsequent year until repaired.
2. The family must be supported from other sources or falls into Shortage (see `02-estate-economics.md`).
3. Reconstruction still follows the normal rules; each Permanent Lot repaired restores £1 of annual income.
4. A ruined estate may be abandoned: the knight gives it up and the liege lord re-grants it (or keeps it as waste land).
