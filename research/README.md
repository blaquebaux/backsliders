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

## Would going LONG be the better bet? (#3)

The natural follow-up: if shorting the fallen fails, is going *long* the better bet?
Directionally **yes** (long most-fallen +0.25 vs short −0.28), but it is a weak, decaying
standalone bet — and there is a trap:

| long variant (fallen, beta-neutral, net) | Sharpe | halves |
|---|---|---|
| long fallen (< −25% threshold) | −0.06 | +0.39 / −0.59 (decays) |
| long fallen & **still-falling** (< 50d MA) | **+0.11** | +0.56 / −0.51 (best, still decays) |
| long fallen & **stabilizing** (> 50d MA) | **−0.83** | the trap — buying the fade |
| long deeply-fallen (< −40%) | −0.02 | — |

- **Buy the deepest oversold, never the already-stabilized.** Longing fallen names that have
  climbed back above their 50-day MA is −0.83 — you buy *after* the bounce and catch the fade.
- **It decays** (positive first half, negative second) — the bounce has weakened.
- **It's not a new edge.** "Long the fallen" *is* the drawdown-bounce the family already keeps
  (Bore / Blunt #5), and that version is cleaner (Ulcer-ranked, beta-neutral, ~+0.46) than any
  threshold cut here.

**Verdict:** rejected as a systematic price *short* — Backsliders is the negative image of the
drawdown-bounce keeper, and shorting the fallen is shorting into the rally. Flipped **long**, it
is the better side but only re-derives (more weakly) the existing bounce keeper, with a clear
"don't buy the stabilizers" trap. A genuine terminal-decline short exists in principle (the
zeros), but it is a fundamental, specialist short obscured by survivorship, not a price sleeve.
Echoes Brute-Force (can't short with price alone) and Bottom (survivorship / untradability).

## Files
- `_backsliders_common.py` — shared helpers + the survivor universe.
- `backsliders_1_short_the_fallen.py` — long vs short the fallen, by horizon.
- `backsliders_2_no_path.py` — the trend-split ("still falling") + survivorship honesty.
- `backsliders_3_long_side.py` — would going long be the better bet? (the long-side variants).
