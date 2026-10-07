---
name: toll-bridge-lens
description: "Scores any business as a toll bridge: a scarce chokepoint with growing traffic, no bypass, pricing power, near-zero running costs, a hands-off government and owners who share the toll. 7 questions, 0-2 each, max 14, with red flags for bypass, government and value-trap risk. Then splits the expected return into its five sources so a great bridge bought at the wrong price doesn't fool you. Modes: company, portfolio, watchlist, founder (score your own business)."
user-invocable: true
---

# /toll-bridge-lens: is this business a toll bridge, and will the stock pay me for it?

Built on Michael Fritzell's "Toll bridge investing" (Asian Century Stocks, 25 June 2026): https://www.asiancenturystocks.com/toll-bridge-investing/. The 7-question scoring, thresholds and flags are ours. Unofficial, not affiliated with or endorsed by the author. Not investment advice.

**The one idea this skill enforces:** the best businesses own a chokepoint people must cross, again and again, at almost no cost to the owner. But the bridge is not the return. Returns come only from revenue, margins, share count, the multiple and the dividend. Every analysis answers both:
1. How good is the bridge? (7 questions)
2. Where will my return come from, at today's price? (5 sources)

`TB_HOME` = the folder you cloned this repo into (default `~/toll-bridge-lens`). The model is in `$TB_HOME/knowledge/MODEL.md`, the math in `$TB_HOME/tools/tollbridge.py`. Run `python3 $TB_HOME/tools/tollbridge.py selftest` once per session. If it fails, stop: don't trust the scores.

## Modes

| Command | What it does |
|---|---|
| `/toll-bridge-lens TICKER` | Full lens (steps 1-6), ends in a Toll Bridge Card |
| `/toll-bridge-lens portfolio` | One line per holding: score, verdict, flags, the one thing to watch. Weighted portfolio score |
| `/toll-bridge-lens watchlist` | Scores every name, ranks by score, lists the true toll bridges and every BYPASS RISK |
| `/toll-bridge-lens founder` | Score YOUR OWN business on the same 7 questions (see "Founder mode") |

## Hard rules

1. **Never invent a number.** Tolls, volumes, margins, capex and share counts come from filings, IR or a named source with the period. Missing = `NOT FOUND`.
2. **Every score gets one line of evidence.** A score with no reason is a guess. Write the reason, then the number.
3. **Look for the second bridge first.** Before scoring Q3, search: who is building a cheaper path to the same destination, and when does it open? (New entrant, open standard, regulator-approved alternative, AI tool, in-house build by the biggest customer.)
4. **Who signs the check?** Q4 is scored from the payer's side: how big is the toll in THEIR total cost, and what happened last time it went up?
5. **A red flag beats a high score.** BYPASS RISK, GOV RISK or VALUE TRAP RISK caps the verdict, whatever the total.
6. **The bridge is not the return.** Never end on the score alone. Always run step 5.

---

## Step 1. Name the bridge

One sentence each: **What is the destination? Who pays the toll? What is the toll (per unit, per crossing)? What is the traffic unit?** If you can't name the toll, it's not a toll bridge business: score it anyway, it will land low.

## Step 2. Score the 7 questions (0, 1 or 2, one line of evidence each)

| # | Question | 0 | 1 | 2 |
|---|---|---|---|---|
| Q1 | **Destination:** do payers need to get there? (function, entertainment, community, lower risk, status) | Nice-to-have | Wanted, substitutes exist | Must-have |
| Q2 | **Traffic:** is volume growing for structural reasons? | Flat/shrinking | With the economy | Structural tailwind |
| Q3 | **No bypass:** no practical alternative and nobody building one? | Real alternative exists or is being built | Competitors, but switching hurts | No practical alternative |
| Q4 | **Toll power:** toll small vs payer's cost, raised faster than inflation? | Market/regulator sets price | Some | Small toll, rising in real terms |
| Q5 | **Cheap to run:** cost per crossing and upkeep capex? | Heavy | Moderate | Near-zero, capital in "old dollars" |
| Q6 | **Government:** risk of caps, concession fees, forced access, break-up? | Toll capped or under attack | Some | Little |
| Q7 | **Owners paid:** does the toll reach minority holders? | Owner keeps it / dilutes | Some | Dividends + buybacks below value, aligned |

```bash
python3 $TB_HOME/tools/tollbridge.py score 2 2 1 2 2 1 2
```
Verdict: 12-14 TOLL BRIDGE · 9-11 STRONG TOLL · 6-8 CONTESTED · 0-5 NO TOLL. Flags: Q3=0 BYPASS RISK, Q6=0 GOV RISK, Q7=0 with 9+ VALUE TRAP RISK. Any flag caps the verdict at STRONG TOLL.

## Step 3. The four ways it dies (one line each, with a date if there is one)

- **Traffic falls:** what would make the destination less attractive? (technology shift, preference shift, shock)
- **Second bridge:** the named bypass, its price vs ours, when it opens. (The Gordie Howe test: a cheaper bridge next to Buffett's bridge opens in 2026 at half the toll.)
- **Government:** who can cap the toll, and are they saying so?
- **Owner:** does the toll come back to you? Look at 5 years of dividends, buybacks, dilution, related-party deals.

## Step 4. Moat direction

Compare this year's 7 answers with last year's. Any question that dropped is the story: say which and why. A falling Q3 or Q6 is an early warning even while earnings still beat. Earnings lag the bridge.

## Step 5. Where the return comes from (at today's price)

Estimate each source over 5 years, from filings and stated assumptions (label every assumption):
```bash
python3 $TB_HOME/tools/tollbridge.py returns --years 5 --revenue-growth 0.10 \
  --margin 0.30 0.32 --shares 100 95 --multiple 30 25 --dividend-yield 0.01
```
State which source does the work. If the answer leans on "the multiple stays high", say so: that's a bet on the market, not on the bridge. For a full reverse DCF use a valuation lens (we pair this with the Mauboussin ROIC Lens).

## Step 6. Toll Bridge Card (template: `templates/toll-bridge-card.md`)

One page: the bridge in 4 lines (destination, payer, toll, traffic), the 7 scores with evidence, total + verdict + flags, the four ways it dies, moat direction, the five return sources, and **the one signpost to watch** (the single fact that would change the score).

---

## Portfolio and watchlist modes

- Score every name with steps 1-3 in short form (one line of evidence per question).
- Portfolio: weight the score by position size. Report % of the portfolio in TOLL BRIDGE and every holding with a flag.
- Watchlist: rank by score, then list the TOLL BRIDGE names whose Step 5 return clears your hurdle. A toll bridge that doesn't clear the hurdle at today's price goes on a price alert, not a buy list.
- Re-score once a quarter, and the same day any second bridge or regulator news lands on a holding.

## Founder mode: is YOUR business a toll bridge?

Same 7 questions, about your own company:
1. **Destination:** can your buyer say in one sentence why they must get what you sell?
2. **Traffic:** is demand for that outcome growing for a structural reason?
3. **Bypass:** what does your buyer do instead of you? (Including "nothing" and "do it in-house with AI.")
4. **Toll power:** is your price small next to what the problem costs THEM, and have you raised it lately?
5. **Cheap to run:** does each new client cost you almost nothing to serve, or another hire?
6. **Government:** can a regulator change your price or your market?
7. **Owners paid:** does the business pay you, in money and in time, or does it keep the toll?

Most founders score lowest on Q4. Not because the bridge is weak, but because the buyer never put a number on what the problem costs, so any price looks big. Fix the order of the conversation (cost of doing nothing before price) and the same bridge earns a bigger toll.
