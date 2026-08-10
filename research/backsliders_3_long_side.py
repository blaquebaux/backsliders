#!/usr/bin/python3
# =============================================================================
# backsliders_3_long_side.py — BLAQUE BAUX BACKSLIDERS #3 (would going LONG be better?).
#
# Shorting the fallen fails (#1/#2), so: is going LONG the fallen the better bet? Directionally
# yes (long most-fallen +0.25 vs short -0.28), but it is not a strong standalone bet, and there
# is a trap:
#   - a crude threshold ("long anything down >25%") is ~0 and regime-dependent, and the edge
#     DECAYS (positive first half, negative second) — the bounce has weakened;
#   - the deepest-oversold (still falling, below 50d MA) is the BEST long (+0.11) — you buy the
#     overshoot, not the recovery;
#   - the TRAP: longing the fallen that have already STABILIZED (back above the 50d MA) is -0.83
#     — you buy AFTER the bounce and catch the fade.
# And "long the fallen" is not a new edge: it IS the drawdown-bounce the family already keeps
# (Bore / Blunt #5), which is cleaner Ulcer-ranked and beta-neutral (~+0.46) than any threshold here.
#
# RESULTS AS TESTED (80 survivors, 2016-2026, beta-neutral vs EW, net 4bp):
#   long fallen <-25%:                 Sharpe -0.06 (halves +0.39 / -0.59)  <- decays
#   long fallen & still-falling:       Sharpe +0.11 (halves +0.56 / -0.51)  <- best long, still decays
#   long fallen & stabilizing (>50dMA):Sharpe -0.83                          <- the trap: buy the fade
#   long deeply fallen <-40%:          Sharpe -0.02
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _backsliders_common import signals, sharpe

R, dd, ma50, N, T = signals(); ew = R.mean(1)
def beta(y, x): m = np.isfinite(y) & np.isfinite(x); y, x = y[m], x[m]; return np.cov(y, x)[0, 1] / np.var(x)
def longbook(mask_fn, reb=21, cost=4.0):
    wp = np.zeros(N); pnl = []; c = cost / 1e4
    for t in range(252, T - 1):
        if (t - 252) % reb == 0:
            cand = mask_fn(t); w = np.zeros(N); idx = np.where(cand)[0]
            if len(idx) > 0: w[idx] = 1.0 / len(idx)
            m = np.isfinite(dd[t]); w -= m / m.sum()      # long the fallen, minus EW (beta-neutral)
        else:
            w = wp
        pnl.append(float(np.nansum(w * R[t + 1])) - np.abs(w - wp).sum() * c); wp = w
    return np.array(pnl)

tests = {
    "long fallen (<-25% off high)":         lambda t: (dd[t] < -0.25) & np.isfinite(dd[t]),
    "long fallen & STILL falling (<50dMA)": lambda t: (dd[t] < -0.25) & (ma50[t] < 0) & np.isfinite(dd[t]),
    "long fallen & STABILIZING (>50dMA)":   lambda t: (dd[t] < -0.25) & (ma50[t] > 0) & np.isfinite(dd[t]),
    "long deeply fallen (<-40%)":           lambda t: (dd[t] < -0.40) & np.isfinite(dd[t]),
}
print("=" * 74, "\nBACKSLIDERS #3 — would going LONG the fallen be the better bet?\n" + "=" * 74)
for nm, fn in tests.items():
    p = longbook(fn); h = len(p) // 2
    print(f"  {nm:<38} Sharpe {sharpe(p):+.2f}  beta {beta(p, ew[1:len(p)+1]):+.2f}  (halves {sharpe(p[:h]):+.2f}/{sharpe(p[h:]):+.2f})")
print("\nVERDICT: long is the better SIDE (vs shorting), but a weak, decaying standalone bet —")
print("buy the deepest oversold, NEVER the already-stabilized (that -0.83 is buying the fade).")
print("And it is just the drawdown-bounce the family already keeps (Bore / Blunt #5), done better there.")
