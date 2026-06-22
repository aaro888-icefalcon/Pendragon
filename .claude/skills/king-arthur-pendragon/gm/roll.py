#!/usr/bin/env python3
"""Pendragon dice roller. All GM rolls go through real RNG — no exceptions.

Usage:
  roll.py d20                  raw d20
  roll.py 5d6+2                NdM(+/-K) roll (damage etc.)
  roll.py check SKILL          Pendragon d20 resolution vs effective skill
  roll.py opposed A B          opposed resolution, skill A (player) vs B (opponent)
Repeat args for batches: roll.py check 15 check 12 d20 5d6
"""
import random
import re
import sys


def resolve(skill: int):
    roll = random.randint(1, 20)
    if skill > 20:
        total = roll + (skill - 20)
        outcome = "CRITICAL" if total >= 20 else "success"
        return roll, total, outcome
    if roll == skill:
        return roll, roll, "CRITICAL"
    if roll == 20:
        return roll, roll, "FUMBLE"
    if roll < skill:
        return roll, roll, "success"
    return roll, roll, "failure"


def ndm(expr: str) -> str:
    m = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", expr)
    n = int(m.group(1) or 1)
    sides = int(m.group(2))
    mod = int(m.group(3) or 0)
    rolls = [random.randint(1, sides) for _ in range(n)]
    total = sum(rolls) + mod
    modtxt = f" {m.group(3)}" if mod else ""
    return f"{expr}: {rolls}{modtxt} = {total}"


def main(argv):
    i = 0
    rank = {"CRITICAL": 2, "success": 1, "failure": 0, "FUMBLE": -1}
    while i < len(argv):
        a = argv[i]
        if a == "check":
            skill = int(argv[i + 1]); i += 2
            roll, total, out = resolve(skill)
            extra = f" (mod total {total})" if total != roll else ""
            print(f"check {skill}: rolled {roll}{extra} -> {out}")
        elif a == "opposed":
            sa, sb = int(argv[i + 1]), int(argv[i + 2]); i += 3
            ra, ta, oa = resolve(sa)
            rb, tb, ob = resolve(sb)
            print(f"A (skill {sa}): rolled {ra} -> {oa}")
            print(f"B (skill {sb}): rolled {rb} -> {ob}")
            if rank[oa] != rank[ob]:
                win = "A" if rank[oa] > rank[ob] else "B"
                print(f"result: {win} wins")
            elif oa == "success":  # both plain successes: higher roll wins
                if ta != tb:
                    win = "A" if ta > tb else "B"
                    print(f"result: {win} wins (higher roll); loser gets partial success")
                else:
                    print("result: tie — see rules/core/04-resolution.md")
            elif oa == "CRITICAL":
                print("result: double critical — tie, see rules/core/04-resolution.md")
            else:
                print("result: no winner (both fail)")
        elif re.fullmatch(r"\d*d\d+([+-]\d+)?", a):
            print(ndm(a)); i += 1
        else:
            print(f"unrecognized: {a}"); i += 1


if __name__ == "__main__":
    main(sys.argv[1:])
