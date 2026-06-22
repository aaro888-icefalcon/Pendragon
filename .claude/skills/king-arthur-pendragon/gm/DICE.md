# Dice: Honest Rolls Only

Every roll is made with real RNG in the shell, shown to the player in the mechanics line, and applied as rolled. An unrolled outcome is a lie; a rolled-then-ignored outcome is worse. See LETHALITY.md.

## How to roll

Use the roller script at `gm/roll.py` (run it via the shell from the project folder):

```
python3 gm/roll.py d20              # raw d20
python3 gm/roll.py 5d6+2            # damage-style rolls
python3 gm/roll.py check 15         # Pendragon resolution vs skill 15
python3 gm/roll.py check 24         # handles skills over 20
python3 gm/roll.py opposed 15 12    # opposed: player skill 15 vs NPC 12
```

Apply situational modifiers to the skill value *before* rolling (state them: `[Sword 15, -5 darkness → check 10]`).

Inline fallback if the script is unavailable:
```
python3 -c "import random; print(random.randint(1,20))"
```

## Resolution reference (full rules: rules/core/04-resolution.md)

| Skill ≤ 20 | Result |
|---|---|
| roll = skill | Critical |
| roll < skill | Success |
| roll = 20 | Fumble |
| otherwise | Failure |

Skill > 20: add (skill − 20) to the roll; modified 20+ = critical; everything else succeeds; no fumble.

Opposed: both roll; criticals beat successes; if both succeed, higher roll wins and the loser gets a partial success; both fail = no result; ties per rules/core/04-resolution.md.

## When to roll

- Whenever a rule calls for it, including against the player's interest: trait checks, passion invocations, aging, family events, horse survival, Chirurgery.
- On oracle tables (`generators/`): roll the stated die, take the result, interpret it in fiction. Don't browse tables for the entry you like.
- **Don't roll** for what's certain, trivial, or already determined by fiction — no roll to mount a horse in peacetime. Rolls mark risk.

## Batch rolling

Winter Phase and battles need many rolls. Roll them in one shell call where convenient (e.g. `python3 gm/roll.py d20` repeated, or several `check` calls), but every result must still be individually shown and applied. Never "assume average."
