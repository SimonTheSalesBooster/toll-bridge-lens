# Toll Bridge Lens

**Find the businesses everyone has to pay to cross.**

In 1979 Matty Moroun bought the Ambassador Bridge between Detroit and Windsor for about $30 million. The passenger toll went from $0.75 to $10. It still earns more than $60 million a year. The bridge was paid for in old dollars, costs almost nothing to run, and a quarter of the trucks crossing between the US and Canada have no better way across. Buffett's favorite kind of business. 🐬

Then a second bridge got built next door. The Gordie Howe International Bridge opens in 2026 at about half the toll. 🐯

That's the whole game. Find the chokepoint. Then sniff out the second bridge, because it rarely looks dangerous until it opens.

This free Claude Code skill does both for any company. 7 questions, 0 to 2 each, one line of evidence per score. Then it splits your expected return into its five sources, so a great bridge bought at the wrong price doesn't fool you.

We scored 115 quality stocks with this lens. 20 came out as true toll bridges. The other 95 didn't. 🌴

Not for you if you want a stock tip. It gives you a process, not a pick. Install below, then type `/toll-bridge-lens MCO`.

---

## The 7 questions

| # | Question | 2 looks like |
|---|---|---|
| Q1 | **Destination:** do payers need to get there? | Must-have: function, lower risk, status |
| Q2 | **Traffic:** is the volume growing for a structural reason? | A technology or habit shift feeding the bridge |
| Q3 | **No bypass:** no practical alternative, nobody building one? | The Gordie Howe test comes back empty |
| Q4 | **Toll power:** is the toll small next to the payer's total cost? | Raised faster than inflation, and they still pay |
| Q5 | **Cheap to run:** cost per crossing and upkeep? | Near zero. A toll booth |
| Q6 | **Government:** can someone cap or take the toll? | Little interference |
| Q7 | **Owners paid:** does the toll reach you? | Dividends, buybacks below value, aligned management |

12-14 **TOLL BRIDGE** · 9-11 STRONG TOLL · 6-8 CONTESTED · 0-5 NO TOLL.
Three red flags cap the verdict however high the total: **BYPASS RISK** (Q3 = 0), **GOV RISK** (Q6 = 0), **VALUE TRAP** (Q7 = 0).

## Then: where does the return come from?

A stock only pays you through revenue, margins, fewer shares, a higher multiple, or the dividend. The bridge alone pays you nothing if you overpay.

```bash
python3 tools/tollbridge.py returns --years 5 --revenue-growth 0.10 \
  --margin 0.30 0.32 --shares 100 95 --multiple 30 25 --dividend-yield 0.01
```

## Modes

| You type | You get |
|---|---|
| `/toll-bridge-lens MCO` | A one-page Toll Bridge Card: the bridge in 4 lines, 7 scores with evidence, the four ways it dies, moat direction, the 5 return sources, the one signpost to watch |
| `/toll-bridge-lens portfolio` | Every holding on one line, weighted score, % of the portfolio in true toll bridges, every red flag |
| `/toll-bridge-lens watchlist` | Names ranked by score; the toll bridges whose return clears your hurdle |
| `/toll-bridge-lens founder` | Score your OWN business on the same 7 questions |

## Install

```bash
git clone https://github.com/SimonTheSalesBooster/toll-bridge-lens ~/toll-bridge-lens
cp ~/toll-bridge-lens/toll-bridge-lens.md ~/.claude/commands/
python3 ~/toll-bridge-lens/tools/tollbridge.py selftest
```

The self-test runs known-good bridges that must pass and known-bad ones (a bypass, a regulator-set toll, an owner who keeps the toll, bad inputs) that must be caught. Plain Python, no dependencies.

## What's in the repo

| File | What it is |
|---|---|
| `toll-bridge-lens.md` | The skill |
| `tools/tollbridge.py` | Scoring, verdict, red flags, return sources, self-test |
| `knowledge/MODEL.md` | The model in plain words: the 4 parts, the 4 ways it dies, the 5 return sources, the research questions, our scoring |
| `examples/scored-examples.md` | The article's bridges plus five lessons from scoring 115 stocks (FICO, Apple, Arm, utilities) |
| `templates/toll-bridge-card.md` | The one-page card |

The model comes from Michael Fritzell's excellent "Toll bridge investing" (Asian Century Stocks, June 2026): https://www.asiancenturystocks.com/toll-bridge-investing/ Everything here is paraphrased in our own words. The 7-question scoring, thresholds and red flags are ours. Read the original.

---

## Who made this

**[Strategy Sprints](https://www.strategysprints.com)**, Simon Severino. Simon runs a concentrated compounding portfolio and built this lens for his own buy and sell decisions.

Our day job is sales. We help B2B founders take control of the sales conversation. 2,400+ founders have gone through our programs.

Point the same lens at your own company: `/toll-bridge-lens founder`. Watch **Q4, toll power.** That's where bigger deals at your price are won or lost. 🐯

If deals land smaller than you planned, or close only after a discount (that bitter aftertaste), that's a low Q4. You're paying the toll instead of collecting it.

Often the bridge is fine. The order of the conversation isn't. The price goes out before the buyer has said what the problem costs them. With no number on the table, any price looks big.

We fix that with the 8 Steps of the Repeatable Sale. The buyer says the cost of doing nothing out loud (Step 4) before you talk investment (Step 6). You lead the conversation. No chasing, no discount. Your toll sits next to their number. 🌴

We share our investing process on The Investing Show, and our sales tools, AI skills and a community of founders in the **Sprint Club**: https://www.strategysprints.com 🐬

Ready to accelerate now? Book a Discovery Call: https://calendly.com/strategysprint/discovery-call

Happy hunting.
Simon & The Sprinters 🐬⚡️🐆

---

*Unofficial. Not affiliated with or endorsed by Michael Fritzell or Asian Century Stocks. Educational, not investment advice.*

## License

[Apache-2.0](./LICENSE) for our code and text. The original article belongs to its author.
