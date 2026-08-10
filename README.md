# Blaque Baux Backsliders

**The falling knives that don't bounce — down 25%+ from the high, with no path back.**

Backsliders is a member of the Blaque Baux family. The [core repo](https://github.com/Carter-Warrens/blaquebaux)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Backsliders points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/Carter-Warrens/blaquebaux-backsliders.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

A SHORT sleeve, and an honest counter-test. The base found high-drawdown names tend to BOUNCE short-term (Blunt #5, Bore), so Backsliders' hard problem is separating that transient bounce from terminal decline: names down 25%+ with broken fundamentals and no recovery path, which keep sinking.

## Research plan (Path A — not yet built)

- Fallen-from-high screen — drawdown >=25%, then a quality filter for 'no path' (dilution, going-concern, broken growth).
- Beat the bounce — confirm these keep underperforming AFTER the short-term bounce window (else you are shorting into the Blunt #5 rally).
- Borrow / liquidity discipline — shorts cost borrow, and many are small and illiquid (Bottom's caveat).

Nothing above is implemented or validated. This is the map, not the territory.

## Research — first pass done

Full detail in [`research/README.md`](research/README.md). The scorecard:

| # | Question | Verdict |
|---|----------|---------|
| 1 | Does shorting the fallen pay? | ❌ no — short −0.28 (long +0.25); negative at every horizon |
| 2 | Can price isolate "no path"? | ❌ no — shorting "still-falling" is worse (−0.17); they bounce harder |

**The synthesis:** Backsliders is the negative image of the drawdown-bounce keeper. Fallen names
*bounce* more often than they keep sinking (in tradable space), so shorting them is shorting into
the rally — it loses at every horizon (−0.28), and a price "still-falling" filter is *worse*
(−0.17). Survivorship cuts *against* the short here (the opposite of Bottom): the ideal targets —
names that go to zero — delist and leave the sample, so this data both understates and can't
access the real terminal-decline short. That short exists in principle but is a **fundamental**,
specialist play (dilution / cash-burn / going-concern + borrow tolerance), not a price sleeve.

## Status
**Research: first pass complete — null** (`research/`). The short side is the wrong side; the
edge is the long drawdown-bounce (Bore / Blunt #5). No live driver. Nothing validated to the
spine's bar.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/Carter-Warrens/blaquebaux) is the
base/blueprint and holds the [full family roster](https://github.com/Carter-Warrens/blaquebaux#the-blaque-baux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> Carter-Warrens/blaquebaux)
research/   two Path-A sketches (short the fallen, the no-path test) + scorecard
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
