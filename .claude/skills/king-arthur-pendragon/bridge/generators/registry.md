# Generator Index — Arthurian Britain   (hooks: generate:character, generate:element)

Routing index for the Pendragon oracle deck: **need · when called · table(s) · mode**.
All tables are `list_d100` / `list_d10` JSON in this folder, compiled from
`generators/*.md` by `build_generators.py` (human-readable sources in `_sources/`).
Roll one honestly (from the repo root) with:

```
python3 .claude/skills/mythic-gm/scripts/dice.py table .claude/skills/king-arthur-pendragon/bridge/generators/<x>.json
```

- **mode** — `replace` (use the companion table instead of Mythic Elements),
  `conjunction` (layer the companion table on the AC Character Crafter / Mythic
  Elements), `default` (fall through to Mythic/AC).
- Anything **not** listed here → Mythic/AC default. 120 tables total; the rows
  below route by need and name the family — the individual `*.json` files are the
  authoritative list.

## People  (generate:character)

| need | when called | table(s) | mode |
|---|---|---|---|
| new NPC (generic) | any new Character, no faction tie | `npcs_type_underclass` / `npcs_type_freeman` / `npcs_type_gentry` (pick by locale) **+** AC Character Crafter | conjunction |
| NPC unexpected dimension | deepening any NPC | `npcs_characteristic_twists` | conjunction |
| NPC of a known role | the profession is already fixed | `npcs_specific_criminals` · `_merchants` · `_nobility` · `_villagers` · `_warriors` | replace |
| NPC appearance / manner | describing an NPC on stage | `npcs_physical_build` · `_differ_from_expectations` · `_way_they_move` · `_first_thing_noticed` · `_clothing_idiosyncrasies` · `_visible_mannerisms` | conjunction |
| NPC drive / wound / bond | an NPC needs a goal or depth | `npcs_ambition_*` · `npcs_tragedy_*` · `npcs_friendship_*` · `npcs_romance_*` | conjunction |

## Places & organizations  (generate:element)

| need | when called | table(s) | mode |
|---|---|---|---|
| a court / power-center | a noble, church, criminal, or clan court is needed | `courts_aristocratic_*` / `courts_religious_*` / `courts_criminal_*` / `courts_familial_*` **+** `courts_court_tags` (×2) | replace (tags conjunction) |
| a settlement | the PC arrives at a village / town / tribe | `communities_village_*` / `communities_city_*` / `communities_tribe_*` **+** `communities_community_tags` (×2) | replace |
| a ruin / site | a barrow, Roman ruin, hermitage, faerie place | `sites_ruin_type` / `sites_general_place` **+** `sites_ruin_tags` (×2) | replace (tags conjunction) |
| a wilderness hex | open-country travel point of interest | `sites_wilderness_tags` (×2) | replace |
| a travel encounter | something met on the road | `sites_encounter_human` / `_nonhuman` / `_beasts` **+** `sites_encounter_happening_sapients` / `_beasts` | replace |
| a faith / temple / cult | a British church, pagan cult, mystery religion | `religions_who_leads` · `_gods_origin` · `_why_matters` · `_faith_wants` · `_portfolio_*` · `_temple_*` · `_cult_*` | replace |
| a faction | building / advancing an off-screen political force | `factions_faction_tag` · `factions_faction_goal` (also used by the world-tick Faction Turn) | replace |

## Story pressure  (meaning / Random-Event content lever)

| need | when called | table(s) | mode |
|---|---|---|---|
| an adventure premise | need a hook or scenario | `adventure_seeds_all` (one-roll d100; or per-slot `adventure_seeds_enemy/friend/complication/thing/place`) | replace |
| a complication / reversal | **Random-Event content (first source)**, a stall-breaker, a mid-scene wrinkle | `complications_sudden_complications` · `complications_betrayal_*` · `complications_betrayer_motive` · `complications_problem_officials` · `complications_government_struggle` | replace |
| period twist | a Saxon/Pictish, Church-vs-pagan, or faerie beat | `complications_saxon_pictish_complications` · `complications_church_pagan_complications` · `complications_faerie_otherworldly_complications` | replace |
| national / court news | year or court setup | `complications_current_national_problems` · `complications_good_things_happening` · `complications_disputes_with_neighbour` · `complications_positive_ties_with_neighbour` · `complications_recent_governmental_events` | replace |
| regional backstory | a region or court's past | `complications_historical_crises` · `complications_historical_events` · `complications_crisis_overcome` · `complications_crisis_failure` · `complications_region_themes` | replace |

Per `interpretation.md`: when Mythic fires a Random Event, draw its **content**
from the complications / adventure-seed tables first (Arthurian-true); Mythic's
Event Focus only chooses the lever. Famous, statted, or year-brief-specified
content always outranks a random roll.
