#!/usr/bin/env python3
"""tollbridge.py: the scoring and return math behind the Toll Bridge Lens skill.

Plain Python 3, no dependencies. The model is Michael Fritzell's "toll bridge"
framework (Asian Century Stocks, 25 June 2026), turned into 7 scored questions
by Strategy Sprints. See knowledge/MODEL.md.

Subcommands
  score     7 answers (0, 1 or 2 each) -> total 0-14, verdict, red flags
  returns   where the return comes from: revenue, margin, share count,
            multiple, dividend (a toll bridge alone does not make a stock go up)
  selftest  known-good and known-bad fixtures (run this first)

Every rate is a decimal (0.10 = 10%).
"""
import argparse
import sys

QUESTIONS = [
    ("destination", "Destination: do payers NEED to get to the other side?"),
    ("traffic", "Traffic: is the volume over the bridge growing for structural reasons?"),
    ("no_bypass", "No bypass: is there no practical alternative, and nobody building one?"),
    ("toll_power", "Toll power: is the toll small next to the payer's total cost, and has it risen faster than inflation?"),
    ("cheap_to_run", "Cheap to run: near-zero cost per crossing and little capital to keep the bridge standing?"),
    ("government", "Government: low risk of rate caps, concession fees, forced access or break-ups?"),
    ("owners_paid", "Owners paid: does the toll reach minority shareholders (dividends, buybacks below value, aligned management)?"),
]

VERDICTS = [
    (12, "TOLL BRIDGE"),
    (9, "STRONG TOLL"),
    (6, "CONTESTED"),
    (0, "NO TOLL"),
]


def verdict(answers):
    """answers: list of 7 ints in {0,1,2}. Returns (total, verdict, flags)."""
    if len(answers) != 7:
        raise ValueError("need exactly 7 answers")
    for a in answers:
        if a not in (0, 1, 2):
            raise ValueError(f"answer {a!r} is not 0, 1 or 2")
    total = sum(answers)
    label = next(v for floor, v in VERDICTS if total >= floor)
    flags = []
    # A bridge with a bypass is not a bridge, whatever the rest scores.
    if answers[2] == 0:
        flags.append("BYPASS RISK")
    # The government can take the toll away (rate caps, concession fees).
    if answers[5] == 0:
        flags.append("GOV RISK")
    # A great bridge whose owner keeps the toll is a value trap for you.
    if answers[6] == 0 and total >= 9:
        flags.append("VALUE TRAP RISK")
    if flags and label == "TOLL BRIDGE":
        label = "STRONG TOLL"  # a red flag caps the verdict
    return total, label, flags


def return_sources(years, revenue_growth, margin_start, margin_end,
                   shares_start, shares_end, multiple_start, multiple_end,
                   dividend_yield):
    """Split an expected annual return into its five sources.

    Price = revenue x margin x multiple / shares. Returns a dict of annual
    contributions (geometric) plus the total including dividend yield.
    """
    n = float(years)
    rev = (1 + revenue_growth) - 1
    mar = (margin_end / margin_start) ** (1 / n) - 1
    sh = (shares_start / shares_end) ** (1 / n) - 1
    mult = (multiple_end / multiple_start) ** (1 / n) - 1
    price = (1 + rev) * (1 + mar) * (1 + sh) * (1 + mult) - 1
    return {
        "revenue": rev,
        "margin": mar,
        "share_count": sh,
        "multiple": mult,
        "price_cagr": price,
        "dividend": dividend_yield,
        "total": price + dividend_yield,
    }


def _selftest():
    fails = 0

    def check(name, got, want):
        nonlocal fails
        ok = got == want if not isinstance(want, float) else abs(got - want) < 1e-4
        print(("PASS " if ok else "FAIL ") + name + f": got {got!r}, want {want!r}")
        if not ok:
            fails += 1

    # Known-good: a textbook bridge (land royalties, no bypass, tiny costs).
    check("textbook bridge", verdict([2, 2, 2, 2, 2, 2, 2])[1], "TOLL BRIDGE")
    check("12 is a toll bridge", verdict([2, 2, 2, 2, 2, 1, 1])[1], "TOLL BRIDGE")
    # Known-bad: a cheaper bridge is being built next door (Gordie Howe test).
    t, v, f = verdict([2, 1, 0, 2, 2, 1, 2])
    check("bypass flagged", "BYPASS RISK" in f, True)
    check("bypass caps verdict", verdict([2, 2, 0, 2, 2, 2, 2])[1], "STRONG TOLL")
    # Known-bad: regulated utility, toll set by the regulator.
    check("gov flagged", "GOV RISK" in verdict([2, 2, 2, 0, 1, 0, 2])[2], True)
    # Known-bad: great bridge, owner keeps the toll.
    check("value trap", "VALUE TRAP RISK" in verdict([2, 2, 2, 2, 2, 2, 0])[2], True)
    check("value trap caps", verdict([2, 2, 2, 2, 2, 2, 0])[1], "STRONG TOLL")
    check("commodity", verdict([1, 2, 0, 0, 0, 0, 1])[1], "NO TOLL")
    check("contested", verdict([1, 1, 1, 1, 1, 1, 1])[1], "CONTESTED")
    # Input validation must refuse, never guess.
    for bad in ([2, 2, 2], [3, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, -1]):
        try:
            verdict(bad)
            check(f"rejects {bad}", False, True)
        except ValueError:
            check(f"rejects {bad}", True, True)
    # Return sources: 10% revenue, flat margin and multiple, 1%/yr fewer shares, 1% dividend.
    r = return_sources(5, 0.10, 0.20, 0.20, 100, 100 * 0.99 ** 5, 20, 20, 0.01)
    check("price cagr", r["price_cagr"], 1.10 / 0.99 - 1)
    check("total", r["total"], 1.10 / 0.99 - 1 + 0.01)
    # Multiple halves over 5 years: the bridge is fine, the stock is not.
    r = return_sources(5, 0.10, 0.30, 0.30, 100, 100, 40, 20, 0.0)
    check("de-rating eats growth", round(r["price_cagr"], 4), round(1.10 * 0.5 ** 0.2 - 1, 4))
    print(f"\n{'ALL PASS' if not fails else str(fails) + ' FAILED'}")
    return 1 if fails else 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("score", help="score 7 answers, e.g. score 2 2 1 2 2 1 2")
    s.add_argument("answers", nargs=7, type=int)
    r = sub.add_parser("returns", help="split expected return into its 5 sources")
    r.add_argument("--years", type=float, default=5)
    r.add_argument("--revenue-growth", type=float, required=True)
    r.add_argument("--margin", type=float, nargs=2, required=True, metavar=("START", "END"))
    r.add_argument("--shares", type=float, nargs=2, required=True, metavar=("START", "END"))
    r.add_argument("--multiple", type=float, nargs=2, required=True, metavar=("START", "END"))
    r.add_argument("--dividend-yield", type=float, default=0.0)
    sub.add_parser("selftest")
    a = p.parse_args()
    if a.cmd == "selftest":
        sys.exit(_selftest())
    if a.cmd == "score":
        total, label, flags = verdict(a.answers)
        for (key, q), ans in zip(QUESTIONS, a.answers):
            print(f"{ans}  {q}")
        print(f"\nToll Bridge score: {total}/14  {label}" + (f"  [{', '.join(flags)}]" if flags else ""))
    if a.cmd == "returns":
        out = return_sources(a.years, a.revenue_growth, *a.margin, *a.shares, *a.multiple, a.dividend_yield)
        for k, v in out.items():
            print(f"{k:12s} {v * 100:6.2f}%")


if __name__ == "__main__":
    main()
