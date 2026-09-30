from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import numpy as np
import pandas as pd
from .backtest import backtest, BacktestConfig
from .data import TasiData


def universe_summary(data:TasiData, frequency='Daily', tickers=None, min_rows=200, use_adjusted=False):
    tickers=tickers or data.tickers()
    rows=[]
    for t in tickers:
        try:
            df=data.load_adjusted(t,frequency) if use_adjusted else data.load(t,frequency)
            if len(df)<min_rows: continue
            rows.append({"ticker":t,"name":data.company(t)["Name"],"sector":data.company(t)["Sector"],"rows":len(df),"start":df.index.min().isoformat(),"end":df.index.max().isoformat(),"median_dollar_volume":float((df.close*df.volume).median())})
        except Exception: continue
    return sorted(rows,key=lambda x:x["median_dollar_volume"],reverse=True)


def run_universe(data, spec, frequency='Daily', tickers=None, cfg=None, min_rows=200, use_adjusted=False):
    tickers=tickers or data.tickers(); out=[]
    for t in tickers:
        try:
            df=data.load_adjusted(t,frequency) if use_adjusted else data.load(t,frequency)
            if len(df)<min_rows: continue
            r=backtest(df,spec,cfg)
            out.append({"ticker":t,"name":data.company(t)["Name"],"sector":data.company(t)["Sector"],**r["metrics"]})
        except Exception as e:
            out.append({"ticker":t,"error":str(e)})
    good=[x for x in out if "error" not in x]
    if not good: return {"results":out,"summary":{}}
    m=pd.DataFrame(good)
    summary={
        "tickers_tested":len(good),
        "median_return":float(m.total_return.median()),
        "mean_return":float(m.total_return.mean()),
        "median_sharpe":float(m.sharpe.median()),
        "median_max_drawdown":float(m.max_drawdown.median()),
        "profitable_fraction":float((m.total_return>0).mean()),
        "median_profit_factor":float(m.profit_factor.replace([np.inf,-np.inf],np.nan).median()),
        "median_trades":float(m.trades.median()),
    }
    return {"results":good,"errors":[x for x in out if "error" in x],"summary":summary}


def candidate_from_reference(ref:dict) -> dict:
    # A prompt-ready translation template. The agent uses the reference corpus as inspiration;
    # this deliberately does not claim the reference implementation is Python-engine compatible.
    return {
        "name": ref["name"],
        "family": ref["family"],
        "reference_id": ref["id"],
        "reference_slug": ref["slug"],
        "hypothesis": ref["overview"],
        "entry_long": None,
        "exit_long": None,
        "entry_short": None,
        "exit_short": None,
        "parameters": ref["parameters"],
        "translation_note": "Translate the documented rules into the TASI DSL before execution; do not execute vendor-specific StockSharp APIs directly.",
    }
