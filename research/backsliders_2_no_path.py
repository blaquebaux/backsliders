#!/usr/bin/python3
# =============================================================================
# backsliders_2_no_path.py — BLAQUE BAUX BACKSLIDERS #2 (can price find "no path"?).
#
# The thesis needs to separate terminal decliners ("no path to growth") from the oversold
# bounce. Try the obvious price proxy: among fallen names (>=25% off high), short only the ones
# STILL FALLING (below the 50-day MA). FINDING: it does not work — the still-falling fallen
# names are MORE oversold and bounce HARDER, so shorting them is worse. Price cannot isolate
# the terminal decliners.
#
# And survivorship cuts against this short (opposite of Bottom): the ideal targets — names that
# go to ZERO — delist and LEAVE the sample, so the survivors over-represent bouncers. Finding
# "no path" needs FUNDAMENTALS (dilution, cash burn, going-concern), plus borrow tolerance.
#
# RESULTS AS TESTED (80 survivors, 2016-2026, beta-hedged, net):
#   short ALL fallen (<-25% off high):            Sharpe +0.02
#   short fallen AND still below 50d MA:          Sharpe -0.17  (worse — bounces harder)
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _backsliders_common import signals, sharpe

R, dd, ma50, N, T = signals()

def short_falling(use_trend, reb=21, cost=4.0):
    wp = np.zeros(N); pnl = []; c = cost / 1e4
    for t in range(252, T - 1):
        if (t - 252) % reb == 0:
            fallen = (dd[t] < -0.25) & np.isfinite(dd[t])
            cand = fallen & (ma50[t] < 0) if use_trend else fallen
            w = np.zeros(N); idx = np.where(cand)[0]
            if len(idx) > 0: w[idx] = -1.0 / len(idx)          # short the fallen
            m = np.isfinite(dd[t]); w += m / m.sum()            # beta hedge: long EW
        else:
            w = wp
        pnl.append(float(np.nansum(w * R[t + 1])) - np.abs(w - wp).sum() * c); wp = w
    return np.array(pnl)

print("=" * 74, "\nBACKSLIDERS #2 — can price separate 'no path' from the bounce?\n" + "=" * 74)
print(f"  short ALL fallen (<-25% off high):        Sharpe {sharpe(short_falling(False)):+.2f}")
print(f"  short fallen AND still below 50d MA:      Sharpe {sharpe(short_falling(True)):+.2f}  (worse — they bounce harder)")
print("\nVERDICT: price cannot isolate terminal decliners — the 'still-falling' fallen names are")
print("just more oversold and bounce harder. And survivorship hides the true targets (the zeros")
print("delist and leave the sample). A real backslider short needs FUNDAMENTAL 'no path' signals")
print("(dilution / cash-burn / going-concern) and borrow tolerance — not a price screen.")
