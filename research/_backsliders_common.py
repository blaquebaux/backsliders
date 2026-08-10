#!/usr/bin/python3
# =============================================================================
# _backsliders_common.py — shared helpers for the Blaque Baux Backsliders (short fallen) sketches.
# Alpaca SIP daily bars; reads ALPACA_KEY_ID / ALPACA_SECRET_KEY from env. Read-only.
# CAVEAT: survivors only (2016-2026). For a SHORT sleeve this cuts AGAINST the edge — the
# names that went to zero (the ideal shorts) delisted and left the sample. That is the finding.
# =============================================================================
import os, json, urllib.request, math
import numpy as np

H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
START, END = "2016-01-01", "2026-08-01"
_cache = {}

# Broad survivor universe (large + small/mid) for a real cross-section of drawdown.
UNIV = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","AVGO","JPM","V","MA","UNH","HD","PG","XOM","JNJ",
"COST","WMT","BAC","KO","PEP","CVX","MRK","CRM","ADBE","NFLX","AMD","INTC","QCOM","TXN","ORCL","DIS","GS","MS","CAT","HON","LLY","ABBV","TMO","NKE","WFC",
"CROX","DECK","RMBS","PLAB","CALX","FORM","POWI","SLAB","DIOD","VICR","OSIS","ITRI","CVLT","PRGS","MANH",
"SAIA","LSTR","WERN","MATX","RHI","ASGN","EXLS","CBZ","HURN","EXPO","JJSF","WDFC","HELE","CENT","SCSC","PLXS","BMI","KAI","SXI","AWI","TREX","SHOO","CRAI","MGPI","UFPT"]

def closes(s):
    if s in _cache: return _cache[s]
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={s}&timeframe=1Day"
         f"&start={START}&end={END}&adjustment=all&feed=sip&limit=10000")
    b = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40)).get("bars", {}).get(s, [])
    _cache[s] = {x["t"][:10]: x["c"] for x in b}
    return _cache[s]

def panel(syms):
    D = {s: closes(s) for s in syms}; D = {s: v for s, v in D.items() if len(v) > 500}
    u = list(D); ds = sorted(set.intersection(*[set(v) for v in D.values()]))
    return u, ds, np.array([[D[s][d] for s in u] for d in ds], float)

def sharpe(r):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    return r.mean() / r.std() * math.sqrt(252) if len(r) > 30 and r.std() > 0 else float('nan')

def signals():
    """Returns (R, drawdown-from-252d-high, above/below-50d-MA) for UNIV."""
    u, ds, M = panel(UNIV); R = M[1:] / M[:-1] - 1; T, N = R.shape
    dd = np.full((T, N), np.nan); ma50 = np.full((T, N), np.nan)
    for t in range(252, T):
        dd[t] = M[t] / M[t - 252:t + 1].max(0) - 1
        ma50[t] = M[t] / M[t - 50:t].mean(0) - 1
    return R, dd, ma50, N, T
