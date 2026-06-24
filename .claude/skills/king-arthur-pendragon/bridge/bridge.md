# Bridge manifest — King Arthur Pendragon (5th edition)

This companion supplies the **King Arthur Pendragon 5e ruleset**, the **Arthurian
Britain / Logres setting (480–566, the Great Pendragon Campaign)**, and a full
deck of **Arthurian oracle generators**. The `mythic-gm` engine drives the
scene / Chaos / Fate / Random-Event / Turning-Point loop and the no-softening
discipline; this bridge fills the engine's hooks so every interpretation, NPC,
resolution, world-tick, and seed comes out **setting-true and Pendragon-rules-
correct**. Pendragon supplies the *substance*; Mythic supplies the *structure*.

The companion is **strong**: the engine reads `interpretation.md` on every
oracle/NPC moment, fires `subsystems.md` (the game-year metronome, scheduled
GPC events, thread pressure, Winter Phase, Glory) at every bookkeeping step, and
frames Expected Scenes from the ingested Pendragon content in `adventures/`.

The full Pendragon rules text, setting prose, and generator tables live in the
rest of this skill (`rules/`, `campaign/`, `generators/`); this bridge points and
condenses, it does not duplicate. Resolution dice run through Pendragon's own
roller, `gm/roll.py`; all oracle/Mythic dice run through the engine's scripts.

```json
{
  "companion": "king-arthur-pendragon",
  "engine": "mythic-gm>=2",
  "overrides": ["resolve","meaning","chaos","themes","generate:character","generate:element","world-tick","seeds","adventure-ingest"],
  "generators_map": {
    "character": { "mode": "conjunction", "note": "roll the locale/role-appropriate NPC table from generators/registry.md (npcs_type_underclass|freeman|gentry, or an npcs_specific_* role table) and flesh the result from setting-canon factions and the active year brief" }
  },
  "files": {
    "system_profile": "system-profile.md",
    "interpretation": "interpretation.md",
    "chaos": "chaos-tendency.md",
    "themes": "theme-weights.md",
    "generators": "generators/registry.md",
    "subsystems": "subsystems.md",
    "seeds": "seeds.md",
    "canon": "setting-canon.md"
  }
}
```
