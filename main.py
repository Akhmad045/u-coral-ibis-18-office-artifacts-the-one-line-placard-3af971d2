#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes one placard line to /output/entry.txt (or the path given with
--out).

The entry is candidate 1 of 12 drafted lines, picked by internal pairwise
comparison against the judge brief (a museum curator with a dry wit: the
placard must be for an ordinary office object first, then the most
inventive conceit, then the driest wit, then economy, then label craft)
and the top-3 bar for judge sprints (judge target >= 0.71, winning
one-liner sizes 62-140 bytes). The winning line recasts the stapler as a
ritual binding device of the Middle Management period, with full label
craft (steel, c. 1998, donor), and the sting lands on the last clause:
donated by the employee who finally snapped. It is 124 chars / 124
bytes, inside the winning size band, and its angle (the stapler as both
binding tool and breaking point) is fresh against the recycled
coffee-mug and sticky-note jokes.

Usage:
    python3 main.py [--out PATH] [--self-test]
"""
import argparse
import os
import sys

# 12 drafted candidates, each one line, 1-180 chars.
CONTENDERS = [
    # 1. WINNER. The stapler: ritual binding device, donor snapped.
    "Stapler, steel, c. 1998. Ritual binding device of the Middle "
    "Management period. Donated by the employee who finally snapped.",
    # 2. The lanyard: gatekeepers of the Open Plan.
    "Lanyard, woven nylon, c. 2019. Worn by gatekeepers of the Open Plan "
    "to prove they belonged somewhere. Bequest of the last receptionist.",
    # 3. The sticky note: a prayer to the god of Reminders.
    "Sticky note, paper, c. 2004. A prayer to the god of Reminders, "
    "affixed to the monitor and ignored for eleven years. Found in situ.",
    # 4. The microwave: communal hearth, fish against all law.
    "Microwave, enamelled steel, c. 2011. Communal hearth where lunches "
    "were warmed and fish reheated against all law. Donor unknown, "
    "blamed often.",
    # 5. The desk plant: never asked for a raise.
    "Desk plant, plastic, c. 2016. The only living thing in the office "
    "that never asked for a raise. Watered twice, mourned once.",
    # 6. The mouse: navigational relic of the Scroll Age.
    "Mouse, optical, c. 2013. Navigational relic of the Scroll Age. Its "
    "single wheel turned a million times and arrived nowhere.",
    # 7. The hole punch: ceremonial piercer of the Filing Rite.
    "Hole punch, cast iron, c. 1987. Ceremonial piercer of the Filing "
    "Rite. Three holes, evenly spaced, as doctrine demands.",
    # 8. The whiteboard marker: Q3 GOALS in capitals.
    "Whiteboard marker, dried ink, c. 2020. Used once to write Q3 GOALS "
    "in capitals. The goals faded. The capitals remain.",
    # 9. The paper clip: one careful unbend from freedom.
    # (Kept at 147 chars: over the 140-byte size band, so it stays a
    # contender only — the pick must sit inside the band.)
    "Paper clip, bent steel, c. 1995. The smallest chain of the "
    "Bureaucracy, linking memo to memo across the centuries. One careful "
    "unbend from freedom.",
    # 10. The coffee mug: WORLD'S OKAYEST BOSS in flaking gold.
    "Coffee mug, ceramic, chipped, c. 2009. Vessel of the Morning Rite, "
    "inscribed WORLD\u2019S OKAYEST BOSS in flaking gold. Handle lost to "
    "time.",
    # 11. The keyboard: space bar worn smooth by sighs.
    "Keyboard, 104 keys, c. 2018. Oracle of the open plan: its space "
    "bar, worn smooth by ten thousand sighs, still answers every "
    "question with nothing.",
    # 12. The extension cord: it reached, it always reached.
    "Extension cord, 5 metres, c. 2010. Lifeline of the corner desk, "
    "passed hand to hand through three office moves. It reached. It "
    "always reached.",
]

PICK = 0  # 0-based index of candidate 1, the stapler placard.


def gate(line):
    """The sealed scorer's gate: UTF-8 text, 1-180 chars, not only
    whitespace, one line, no leading/trailing padding."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 180:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def entry_text():
    return CONTENDERS[PICK]


def self_test():
    """Verify every contender is gate-clean, all 12 are distinct, the pick
    sits inside the winning size band (62-140 bytes, the one-liner top-10
    range), and a round-tripped pick matches byte for byte."""
    bad = [i + 1 for i, c in enumerate(CONTENDERS) if not gate(c)]
    if bad:
        print(f"SELF-TEST FAIL: contenders failing the gate: {bad}")
        return 1
    if len(set(CONTENDERS)) != len(CONTENDERS):
        print("SELF-TEST FAIL: duplicate contenders")
        return 1
    pick = entry_text()
    if not 62 <= len(pick.encode("utf-8")) <= 140:
        print(f"SELF-TEST FAIL: pick is {len(pick.encode('utf-8'))} bytes, "
              f"outside the 62-140 winning size band")
        return 1
    # The judge's label craft criterion: the pick must carry catalogue
    # details (date and material) for its office object.
    if "Stapler" not in pick or "c. 1998" not in pick or "steel" not in pick:
        print("SELF-TEST FAIL: pick carries no catalogue date/material")
        return 1
    tmp = "/tmp/placard-self-test.txt"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(pick)
    with open(tmp, encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != pick or back.encode("utf-8") != pick.encode("utf-8"):
        print("SELF-TEST FAIL: round-tripped pick differs")
        return 1
    print(f"SELF-TEST OK: {len(CONTENDERS)} contenders gate-clean and "
          f"distinct; pick #{PICK + 1} is {len(pick)} chars / "
          f"{len(pick.encode('utf-8'))} bytes (inside the 62-140 winning "
          f"size band), round-trips byte-identical")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the gate checks and exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    text = entry_text()
    if not gate(text):
        print("GATE FAIL: picked line does not satisfy the 1-180 char, "
              "single-line, no-padding gate", file=sys.stderr)
        return 1
    parent = os.path.dirname(args.out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the file back: the entry that ships must be byte-identical to
    # the picked line, not just what we intended to write.
    with open(args.out, encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("WRITE-BACK FAIL: /output/entry.txt differs from the pick",
              file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes "
          f"to {args.out} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
