# Blaque Baux Backsliders — research

First-pass Path-A research on the short-side sleeve: short stocks down ≥25% from their high
with "no path to growth." This is the honest counter-test to the family's drawdown-**bounce**
(Blunt #5 / Bore, long fallen names = +0.46). All sketches read Alpaca SIP daily bars, are
read-only, print their results.

**Data caveat (which is itself the finding):** survivors only (2016–2026). For a *short* sleeve
this cuts **against** the edge — the ideal targets (names that go to zero) delist and leave the
sample, so the survivors over-represent bouncers.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/backsliders_1_short_the_fallen.py   # shorting the fallen
python research/backsliders_2_no_path.py             # can price find "no path"?
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Does shorting the fallen pay? | short most-fallen −0.28 (vs long +0.25); negative at every horizon | ❌ you short into the bounce |
| 2 | Can price isolate the terminal decliners? | short still-falling (below 50d MA) −0.17 — *worse* | ❌ no — they bounce harder |

## The synthesis — the short side is the wrong side

- **#1 — shorting the fallen loses at every horizon.** Long the most-fallen names (the bounce)
  earns +0.25; **short** them earns **−0.28**, and it stays negative from 5-day to 126-day
  holds. Fallen names bounce more often than they keep sinking (in tradable space), so the edge
  is the **long** side (the drawdown-bounce), and its inverse is a loser.

- **#2 — price cannot find "no path."** The obvious proxy — short only the fallen names *still*
  below their 50-day MA ("still falling") — is **worse** (−0.17), because the still-falling ones
  are simply more oversold and bounce *harder*. A price screen cannot separate the terminal
  decliners from the bounce.

- **Survivorship cuts against this short** (the opposite of Bottom): the names that go to zero —
  the *ideal* backslider targets — delist and leave the sample, so the survivors over-represent
  the ones that recovered. The real terminal-decline short is thus both *invisible* in this data
  and *hard to access*: it needs **fundamental** "no path" signals (dilution, cash burn,
  going-concern) plus borrow tolerance and delisting mechanics — not a price pattern.

**Verdict:** rejected as a systematic price short. Backsliders is the negative image of the
drawdown-bounce keeper — shorting the fallen is shorting into the rally. A genuine
terminal-decline short exists in principle (the zeros), but it is a fundamental, specialist
short obscured by survivorship, not a price sleeve. Echoes Brute-Force (can't short with price
alone) and Bottom (survivorship / untradability).

## Files
- `_backsliders_common.py` — shared helpers + the survivor universe.
- `backsliders_1_short_the_fallen.py` — long vs short the fallen, by horizon.
- `backsliders_2_no_path.py` — the trend-split ("still falling") + survivorship honesty.
