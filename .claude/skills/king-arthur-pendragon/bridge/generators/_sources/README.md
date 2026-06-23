# `_sources/` — human-authored generator source, compiled to verified JSON

These files are the **input** to `../build_generators.py`. Each describes the
rollable oracle tables of one `generators/NN-*.md` file as ordered value-lists;
the builder computes the contiguous d100/d10 ranges and writes verified
`../<id>.json` tables (the engine rolls those with `dice.py table <path>`).

One file per source generator, named to match (e.g. `03-npcs.json`). Schema:

```json
{
  "file": "generators/03-npcs.md",
  "tables": [
    {
      "id": "pendragon.npcs.gentry_type",
      "title": "NPC Type — Gentry (one-roll)",
      "source": "generators/03-npcs.md#one-roll-npc-table",
      "die": "d100",
      "values": ["Abbot or prior of a monastery", "Court enchanter or learned mage", "..."]
    }
  ]
}
```

- **`id`** — `pendragon.<file-slug>.<table-slug>`, globally unique, snake_case.
- **`values`** — the table's results **in order**, verbatim (already reskinned to
  Arthurian Britain in the source; copy faithfully, do not re-word). The builder
  assigns ranges: 10 values → `list_d10`; otherwise an even split across `1d100`.
- **`die`** — informational only (the native die in the book).
- For a d100 table whose rows have **non-uniform** ranges, give `entries`
  (`[{"min","max","value"}]`, covering 1..100) verbatim instead of `values`.

Only convert tables you actually **roll a die on**. Skip pure reference/lookup
tables (stat legends, HP-by-rating, tag-effect glossaries, "key" tables) — those
belong in `system-profile.md`/`subsystems.md`, not here.
