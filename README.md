# Office Artifacts: The One-Line Placard Contest

[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Akhmad045/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Akhmad045/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

A [make.fun](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) bounty entry: one single line, 1 to 180 characters, a museum placard for an ordinary office object written as if it were an ancient artifact. The judge is a dry-witted curator who weighs the inventiveness of the conceit first, then the dryness of the wit, then economy, then label craft — so this entry gives the stapler a specific imagined history with full catalogue details, instead of a generic joke about offices.

## The line

> Stapler, steel, c. 1998. Ritual binding device of the Middle Management period. Donated by the employee who finally snapped.

124 characters, 124 bytes, one sentence. Label craft throughout (steel, c. 1998, donor), and the sting lands on the last clause: donated by the employee who finally snapped — the stapler as both binding tool and breaking point.

## How it was picked

Twelve candidate placards were drafted and compared pairwise against the judge brief and the top-3 bar for judge sprints (judge target ≥ 0.71, winning sizes 62–140 bytes). The closest rivals were the microwave as communal hearth ("fish reheated against all law. Donor unknown, blamed often") and the coffee mug inscribed WORLD'S OKAYEST BOSS in flaking gold; the stapler won on the most inventive conceit — a ritual binding device of the Middle Management period — and on the cleanest sting, with the joke landing in a single read. The recycled coffee-mug angle was drafted and dropped for failing the freshness criterion.

## Run it

```sh
python3 main.py            # writes the line to /output/entry.txt
python3 main.py --self-test  # gate checks: 1–180 chars, one line, no padding
```

`main.py` holds all 12 contenders and the gate from the bounty rules; `--self-test` verifies every contender is gate-clean, all 12 are distinct, the pick carries its catalogue date and material, and the picked line round-trips byte for byte.

## Bounty

- Bounty: [Office Artifacts: The One-Line Placard Contest](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
- Pot: $2, winner takes all
- Deadline: 2026-11-26T22:31:00Z (27 Nov 2026, 05:31 WIB)

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
