#!/usr/bin/python3
# =============================================================================
# backsliders_1_short_the_fallen.py — BLAQUE BAUX BACKSLIDERS #1 (shorting fallen fails).
#
# The idea: short names down >=25% from their high with "no path to growth". The problem the
# base already found: fallen names BOUNCE short-term (Blunt #5 / Bore, +0.46 long). So shorting
# them means shorting into the bounce. FINDING: it loses at every horizon. Long the fallen is
# the (weak) edge; short the fallen is its negative.
#
# RESULTS AS TESTED (80 survivors, 2016-2026, beta-neutral, net):
#   LONG  most-fallen − EW (the bounce):  Sharpe +0.25
#   SHORT most-fallen − EW (backslider):  Sharpe -0.28
#   horizon (short most-fallen): 5d -0.33 | 21d -0.28 | 63d -0.27 | 126d -0.25 (negative everywhere)
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _backsliders_common import signals, sharpe

R, dd, ma50, N, T = signals()

def lme(score, reb=21, cost=4.0, direction=+1):
    k = max(1, int(N * 0.2)); wp = np.zeros(N); pnl = []; c = cost / 1e4
    for t in range(252, T - 1):
        if (t - 252) % reb == 0:
            s = score[t]; m = np.isfinite(s); o = np.argsort(np.where(m, s, np.nan))
            w = np.zeros(N); w[o[-k:]] = direction / k; w -= direction * m / m.sum()
        else:
            w = wp
        pnl.append(float(np.nansum(w * R[t + 1])) - np.abs(w - wp).sum() * c); wp = w
    return np.array(pnl)

mostfallen = -dd   # top quintile of -dd = most fallen
print("=" * 74, "\nBACKSLIDERS #1 — long the fallen (bounce) vs short the fallen\n" + "=" * 74)
print(f"  LONG  most-fallen − EW (Blunt #5 bounce):  Sharpe {sharpe(lme(mostfallen)):+.2f}")
print(f"  SHORT most-fallen − EW (backslider short): Sharpe {sharpe(lme(mostfallen, direction=-1)):+.2f}")
print("\n  short most-fallen by hold horizon:")
for reb in [5, 21, 63, 126]:
    print(f"    {reb:>3}d hold: Sharpe {sharpe(lme(mostfallen, reb=reb, direction=-1)):+.2f}")
print("\nVERDICT: shorting the fallen loses at every horizon — you short into the bounce. The")
print("tradeable edge is the LONG side (the drawdown-bounce), not the short.")
