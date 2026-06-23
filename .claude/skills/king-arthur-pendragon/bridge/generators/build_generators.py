#!/usr/bin/env python3
"""
build_generators.py — the companion build pass for the Pendragon bridge.

Mirrors mythic-gm/scripts/build_data.py: it turns the human-friendly *source*
descriptions of the Pendragon oracle tables (in ./_sources/*.json) into the
verified engine table schema (./<id>.json), giving them the same coverage
guarantee Mythic's own tables get. The engine can only roll list_d100 (cov 100)
and list_d10 (cov 10) tables, so every Pendragon table — whatever its native die
(d4/d6/d8/d12/d20…) — is remapped onto a d100 by an even split, or onto a d10
when it has exactly ten entries.

Source schema (./_sources/<NN-name>.json):
  {
    "file": "generators/03-npcs.md",
    "tables": [
      { "id": "pendragon.npcs.gentry_type",
        "title": "NPC Type — Gentry (one-roll)",
        "source": "generators/03-npcs.md#one-roll-npc-table",
        "die": "d100",                 # informational: the native die in the book
        "values": ["...", "...", ...]  # ordered entries; ranges are computed here
      },
      # ...or, for a d100 table whose ranges are NOT uniform, give them verbatim:
      { "id": "...", "title": "...", "source": "...",
        "entries": [ {"min":1,"max":4,"value":"..."}, ... ] }   # must cover 1..100 or 1..10
    ]
  }

Run:  python3 build_generators.py   (writes ./*.json, then verifies coverage)
"""
import json, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, "_sources")

def even_split_d100(values):
    """Distribute 1..100 across N values as evenly as possible (contiguous)."""
    n = len(values)
    base, rem = divmod(100, n)          # first `rem` buckets are one wider
    entries, cur = [], 1
    for i, v in enumerate(values):
        w = base + (1 if i < rem else 0)
        entries.append({"min": cur, "max": cur + w - 1, "value": v})
        cur += w
    return entries

def one_each_d10(values):
    return [{"min": i + 1, "max": i + 1, "value": v} for i, v in enumerate(values)]

def build_table(t):
    tid = t["id"]
    title = t.get("title", tid)
    source = t.get("source", "")
    if "entries" in t:
        entries = [{"min": int(e["min"]), "max": int(e["max"]), "value": e["value"]} for e in t["entries"]]
    else:
        values = [str(v).strip() for v in t["values"]]
        if len(values) == 10:
            entries = one_each_d10(values)
        elif 1 <= len(values) <= 100:
            entries = even_split_d100(values)
        else:
            raise ValueError(f"{tid}: {len(values)} values (must be 1..100)")
    cov = sum(e["max"] - e["min"] + 1 for e in entries)
    if cov == 100:
        ttype, dice = "list_d100", "1d100"
    elif cov == 10:
        ttype, dice = "list_d10", "1d10"
    else:
        raise ValueError(f"{tid}: coverage {cov} (must be 100 or 10)")
    # contiguity check
    cur = 1
    for e in entries:
        if e["min"] != cur:
            raise ValueError(f"{tid}: non-contiguous at {e}")
        cur = e["max"] + 1
    return {"id": tid, "title": title, "type": ttype, "dice": dice,
            "source": source, "entries": entries}

def fname(tid):
    return tid.replace("pendragon.", "").replace(".", "_") + ".json"

def main():
    if not os.path.isdir(SRC_DIR):
        sys.exit(f"No _sources/ directory at {SRC_DIR}")
    built, errors, seen = [], [], {}
    for sf in sorted(glob.glob(os.path.join(SRC_DIR, "*.json"))):
        try:
            doc = json.load(open(sf, encoding="utf-8"))
        except Exception as e:
            errors.append(f"{os.path.basename(sf)}: parse error {e}"); continue
        for t in doc.get("tables", []):
            try:
                table = build_table(t)
            except Exception as e:
                errors.append(str(e)); continue
            fn = fname(table["id"])
            if fn in seen:
                errors.append(f"duplicate output file {fn} ({table['id']} vs {seen[fn]})"); continue
            seen[fn] = table["id"]
            json.dump(table, open(os.path.join(HERE, fn), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            built.append((fn, table["type"], len(table["entries"])))
    print(f"BUILT {len(built)} generator tables")
    by_type = {}
    for _, tp, _ in built:
        by_type[tp] = by_type.get(tp, 0) + 1
    print("  by type:", by_type)
    if errors:
        print("\nERRORS:")
        for e in errors:
            print("  X", e)
        sys.exit(1)
    print("\nGENERATOR VERIFICATION PASSED ✓")

if __name__ == "__main__":
    main()
