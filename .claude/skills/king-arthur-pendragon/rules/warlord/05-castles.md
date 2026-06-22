# Castles

Covers all castle types, Defensive Values (DV) for each component, construction costs and time, garrison requirements, siege-relevant stats, and the Castle Damage table.

**Use when:** Determining a castle's DV for a siege, generating a new castle, calculating garrison size, or adjudicating castle damage after an assault.

---

## Castle Types and Base Defensive Values

Defensive Values are written as a slash-separated sequence: **Wall/Tower/Gate/Keep/[Sally port]**. Each component has its own DV. The attacker must breach each component in sequence (or select a weak point). A missing component is marked N/A or omitted.

### Earthwork Enclosure
A ditch + earthen bank with palisade. Simplest fortification.
- DV: **5/2** (bank+palisade / entrance)
- No tower; no stone
- Construction time: weeks to months
- Cost: £5–£20 depending on size

### Motte-and-Bailey
An earthen mound (motte) with a timber tower, adjacent to an enclosed yard (bailey) with palisade.
- DV: **5/11/2** (bailey wall / motte tower / gate)
- The motte tower is the last refuge; highest DV component
- Construction time: 1–3 months (timber); longer for earthwork preparation
- Cost: £20–£60

**Variants:**
- Double motte: two mottes with linked baileys → **5/5/11/2**
- Motte with double ditch: +1 DV to the bank component
- Motte-and-bailey with wet moat: +2 DV to the palisade/wall component

### Shell Keep
A stone wall around the top of the motte, replacing the timber tower.
- DV: **5/13/2** (bailey / shell keep / gate)
- Shell keeps are permanent stone constructions
- Construction time: 1–2 years
- Cost: £100–£200

### Partial Stone
A combination of earthwork/timber and stone elements (stone curtain wall, stone great tower, or stone gatehouse, but not fully stone).
- DV: **5/13** to **9/13/2** depending on which elements are stone
- Typical: motte with stone-lined ditch + timber hall → **6–9/13/2**

### Stone Castle (Full)
All major defensive elements in stone.
- DV varies widely by design: **10–26/5–20/11–24**
- The strongest component is usually the great tower or keep
- Construction time: 5–20 years
- Cost: £500–£5,000+

### Specific Stone Castle Subtypes

| Subtype | Description | Typical DV |
|---------|-------------|------------|
| Stone shell keep on motte | Shell wall around motte; bailey still earthwork | 8–10/13–16/2 |
| Stone great tower (square) | Square keep with thick walls; no motte | 14–20/11/2–3 |
| Stone great tower (round/cylindrical) | Round keep; more defensible | 16–22/13/2 |
| Stone curtain wall + tower | Multiple towers on curtain; proper castle | 12–18/13–20/11/2 |
| Concentric plan | Two rings of walls; inner higher than outer | 16–26/15–24/13–18/2 |
| City walls integrated | Castle inside or using Roman city walls | +2–8 DV to any component using the walls |

---

## Four Example Estates (from Chapter IV)

### Slayersfort (Wuerensis County)
- Type: Fortified manor within a walled town
- DV: **5/5/2**
- Notes: Low DV; the walled town provides the outer layer; manor is the inner keep

### Sentinel Ridge (Tribruit County)
- Type: Motte and three baileys, riverside
- DV: **12/5/5/11/2** (outer wall / first bailey tower / second bailey tower / motte tower / gate)
- Notes: Multiple concentric baileys provide layered defense

### Roaring Stream (Ascalon County)
- Type: Stone square keep (built during Anarchy by King Idres)
- DV: **9/11/2** (Uther); expanded to **9/10** after Idres adds three-story rectangular great tower and palisade
- Notes: Alternatively, Player-knight actions determine events

### Castle of the Pinnacle (Jagent County)
- Type: Motte with ditch around motte, another around bailey
- DV: **12/4/13/2** (Uther Period)
- Anarchy Period: **12/4/13/2** (unchanged or determined by player actions)
- Boy King Period: **12/4/13/2** or Gamemaster's choice

---

## Defensive Value Reference

The DV of each component is the number that must be beaten in a siege assault check (or overcome in siege operations).

| DV | Fortification Quality |
|----|----------------------|
| 1–4 | Minimal: simple earthworks, wooden stockade |
| 5–9 | Light: motte, simple earthwork enclosure |
| 10–15 | Moderate: shell keep, partial stone, strong motte |
| 16–20 | Strong: full stone castle, city walls |
| 21–30 | Very strong: major fortresses, multi-tower stone |
| 31+ | Exceptional: legendary fortresses (White Tower = 26/15/24) |

---

## Garrison Requirements

**Minimum garrison** = enough to man the walls and respond to assault.

**Formula:** 1 Foot Soldier per £10 of Customary Revenue of the honour (from the servitium debitum calculation).

| Honour CR | Min Garrison Foot | Permanent Garrison |
|-----------|-----------------|-------------------|
| £50 | 5 | 3 |
| £100 | 10 | 5 |
| £200 | 20 | 10 |
| £300 | 30 | 15 |
| £500 | 50 | 25 |
| £1,000 | 100 | 50 |
| £1,574 (Roderick) | 157 | 78 |

**Note:** "Minimum" = siege-viable defense. "Permanent" = peacetime standing garrison (roughly half the minimum). Additional garrison can be drawn from the field army if needed.

**Castellan:** Required for any castle held as a stronghold. Must have Battle or Siege skill. Pay bonus: see Table 3.4.

---

## Construction Costs and Times

| Castle Type | Cost (£) | Build Time |
|-------------|----------|-----------|
| Earthwork enclosure | £5–£20 | 1–4 weeks |
| Palisade on earthwork | +£5–£15 | 2–6 weeks |
| Motte-and-bailey (timber) | £20–£60 | 1–3 months |
| Shell keep (stone, on existing motte) | £80–£200 | 1–2 years |
| Stone great tower (small) | £200–£500 | 2–5 years |
| Stone great tower (large) | £500–£1,500 | 5–10 years |
| Full stone castle (curtain wall + towers + keep) | £1,000–£5,000 | 10–20 years |
| City walls (repair or new section) | £200–£1,000/section | 2–10 years |

**Building requires:**
- Royal permission to build a new castle
- Master mason (or architect equivalent) for stone construction
- Significant labor force (funded from Discretionary Fund)
- Ongoing maintenance: typically 5–10% of construction cost per year

---

## Castle Damage (Table 5.3)

When a castle is attacked, damaged, or besieged, roll to determine the current DV reduction.

**Table 5.3: Castle Damage**

| 1d6 | Damage Level | DV Effect |
|-----|-------------|-----------|
| 1 | Light damage | −1 to one component |
| 2 | Moderate damage | −2 to one component |
| 3 | Significant damage | −3 to one component, or −1 to two |
| 4 | Heavy damage | −4 to one component, or −2 to two |
| 5 | Severe damage | −5 to one component; that component may be impassable |
| 6 | Catastrophic | −6 to primary component; secondary components also reduced |

**Notes:**
- A component reduced to DV 0 is breached/destroyed
- Damaged castles marked with * in the castle tables use this roll to determine current DV
- Repairs cost proportional to original construction costs (1/3 to full cost depending on severity)

---

## Castles of Salisbury (Key Locations)

These are the castles most relevant to a standard campaign centered on Salisbury:

| Castle | Type | Uther DV | Notes |
|--------|------|----------|-------|
| Sarum Rock | Hilltop fortified settlement (county seat) | 13/3 | Count Roderick's seat |
| Du Plain | Motte-and-bailey | 5/11/2 | Taken by West Saxons in Anarchy |
| Vagon Castle | Motte-and-bailey | 5/11/2 | Player-knight dependent in Anarchy/Boy King |
| Llud's Hall | Stone shell keep on motte | 6–8/16 | Royal treasure; heavily defended in Anarchy |
| Borders, Castle on the | Walled town + motte + two baileys | 5/3/10/11/2 | Player-knight dependent |
| Rock, Castle of the | Hillfort outer + inner defenses + tower | 13/12/3 | Player-knight dependent |
| Ford at the Pillar | Motte-and-bailey | 5/11/2 | Dependent on Player-knights |
| Frostfield | Earthwork enclosure → full stone | varies | Cerdic captures if players do nothing |
| Alder Castle | Motte-and-bailey | 5/11/2 | Attacked by Sir Blains (Steward of Levcomagus) |
| Ambrius Castle | Fortified ancient hillfort | 13/3 | Abbot Dilwyn; upgraded in Anarchy |
| Alabaster Castle | Stone shell keep, ornate alabaster | 5/13 | Demon Lord Alabaster; supernatural |
| Irontown Castle | Earthwork enclosure | 5/2 | Built by Sir Tathan; attacked by Gloom creatures |
| Woodhouse Castle | Motte-and-bailey | 5/11/2 | Taken by Djejj the Spriggan in Anarchy |
| Westfort Castle | Earthwork enclosure | 5/2 | Built by Gloomwood creatures |
| Restwell Castle | Fortified manor | 5/2 | Built by Sir Marleigh (former Thornbush vassal) |
| Shearing Castle | Motte-and-bailey | 5/11/2 | Built by Sir Landri |

---

## New Castles of Salisbury (Built During Campaign)

During the Boy King Period, new castles are built under Count Robert (heir to Roderick):
- Multiple new earthwork enclosures and motte-and-baileys
- Some existing ones upgraded to stone
- See Table A.3 for Boy King Period DVs for all Salisbury castles

---

## Siege Equipment

When assaulting a castle, the attacker needs siege equipment to overcome DV.

| Equipment | Effect |
|-----------|--------|
| Scaling ladders | Allow assault on walls; no DV reduction |
| Battering ram | Reduces gate DV by 1d6 over time |
| Siege tower | Allows assault on walls at +5 to attack |
| Trebuchet/Mangonel | Reduces wall or tower DV by 1d6 per week of bombardment |
| Mining | Undermines a wall section; if successful, collapses a section (DV to 0) |
| Starvation | No DV relevant; reduces garrison strength over time |

**Assault Gear:** A castle record sheet tracks assault gear available to the defender. Defenders with assault gear can use it offensively against besiegers.

---

## Castle Events During the Anarchy

Many castles in Logres changed hands, were damaged, or were newly built during the Anarchy Period (495–509).

**Key patterns:**
- Saxon kings (Angles, East/West/South Saxons, Kent) captured coastal and border castles
- King Idres of Cornwall seized Ascalon, Jagent, and Tintagel area castles
- King Cadwy and King Nanteleod contested Summerland and Ascalon
- Commoners built earthwork enclosures for self-defense; often fell to nearby conquerors
- Baronial Replacement Table (Table 5.1, p. 98) used when a castle's holder is unknown

For full castle tables by period, see `08-warlord-reference.md`.
