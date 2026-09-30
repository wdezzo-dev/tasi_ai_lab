from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
from typing import Any
try:
    from mcp.server import MCPServer
except ImportError:
    # Compatibility for MCP v1; pyproject pins v2 by default.
    from mcp.server.fastmcp import FastMCP as MCPServer

from .config import Settings
from .catalog import StrategyCatalog
from .data import TasiData
from .backtest import BacktestConfig, backtest
from .research import run_universe, universe_summary, candidate_from_reference
from .optimizer import optimize, render_spec

settings=Settings.from_env(Path(__file__).resolve().parents[1])
settings.results_dir.mkdir(parents=True,exist_ok=True)
catalog=StrategyCatalog(settings.reference_catalog)
data=TasiData(settings.data_dir,settings.companies_csv)
mcp=MCPServer(
    "TASI AI Research Lab",
    instructions="Research-only MCP for discovering and validating trading strategies on the user's Saudi OHLCV universe. Historical backtests are not guarantees of future profitability. Always use out-of-sample and robustness checks before treating a strategy as viable."
)

@mcp.tool()
def dataset_manifest()->dict[str,Any]:
    """Return available TASI tickers and OHLCV coverage by timeframe."""
    return {"tickers":len(data.tickers()),"timeframes":data.manifest()}

@mcp.tool()
def list_tickers(sector: str|None=None)->list[dict[str,Any]]:
    """List the supplied Saudi stock universe."""
    out=[]
    for t in data.tickers(sector): out.append(data.company(t))
    return out

@mcp.tool()
def search_reference_strategies(query: str, limit:int=10, family:str|None=None)->list[dict[str,Any]]:
    """Search the 3,811 reference strategies by name, rules, indicators, or parameters."""
    return catalog.search(query, min(max(limit,1),50), family)

@mcp.tool()
def get_reference_strategy(slug:str|None=None, strategy_id:int|None=None)->dict[str,Any]:
    """Get one reference strategy's documented logic and source paths."""
    r=catalog.get(slug, strategy_id)
    if not r: return {"error":"not_found"}
    return r

@mcp.tool()
def propose_reference_translation(strategy_id:int|None=None, slug:str|None=None)->dict[str,Any]:
    """Return a prompt-ready reference strategy for the AI to translate into the TASI DSL."""
    r=catalog.get(slug, strategy_id)
    return {"error":"not_found"} if not r else candidate_from_reference(r)

@mcp.tool()
def summarize_universe(frequency:str="Daily", min_rows:int=200)->dict[str,Any]:
    """Summarize coverage/liquidity proxies for the 222-stock universe."""
    return {"frequency":frequency,"stocks":universe_summary(data,frequency,min_rows=min_rows)[:222]}

@mcp.tool()
def backtest_strategy(ticker:str, frequency:str, strategy:dict[str,Any], initial_cash:float=100000, commission_bps:float=20, slippage_bps:float=5, direction:str="long", stop_loss_pct:float|None=None, take_profit_pct:float|None=None, use_adjusted:bool=False)->dict[str,Any]:
    """Backtest one DSL strategy on one Saudi ticker. Signals are evaluated on bar t and executed at next bar open. LONG-ONLY: direction must be "long"; non-empty entry_short/exit_short raise ValueError."""
    df=data.load_adjusted(ticker,frequency) if use_adjusted else data.load(ticker,frequency)
    cfg=BacktestConfig(initial_cash=initial_cash,commission_bps=commission_bps,slippage_bps=slippage_bps,direction=direction,stop_loss_pct=stop_loss_pct,take_profit_pct=take_profit_pct)
    r=backtest(df,strategy,cfg)
    return {"ticker":ticker,"frequency":frequency,"metrics":r["metrics"],"trades":r["trades"][:200]}

@mcp.tool()
def backtest_universe(strategy:dict[str,Any], frequency:str="Daily", tickers:list[str]|None=None, initial_cash:float=100000, commission_bps:float=20, slippage_bps:float=5, direction:str="long", stop_loss_pct:float|None=None, take_profit_pct:float|None=None, use_adjusted:bool=False)->dict[str,Any]:
    """Backtest a DSL strategy across supplied tickers or all 222 tickers. LONG-ONLY: direction must be "long"; non-empty entry_short/exit_short raise ValueError."""
    cfg=BacktestConfig(initial_cash=initial_cash,commission_bps=commission_bps,slippage_bps=slippage_bps,direction=direction,stop_loss_pct=stop_loss_pct,take_profit_pct=take_profit_pct)
    return run_universe(data,strategy,frequency,tickers,cfg,use_adjusted=use_adjusted)

@mcp.tool()
def optimize_strategy(strategy_template:dict[str,Any], parameter_space:dict[str,dict[str,Any]], frequency:str="Daily", tickers:list[str]|None=None, n_trials:int=50, train_start:str|None=None, train_end:str|None=None, commission_bps:float=20, slippage_bps:float=5, direction:str="long")->dict[str,Any]:
    """Optimize a parameterized DSL strategy. Use placeholders like {fast} inside indicator arguments. Optimize only on the supplied training window. LONG-ONLY: direction must be "long"."""
    cfg=BacktestConfig(commission_bps=commission_bps,slippage_bps=slippage_bps,direction=direction)
    return optimize(data,strategy_template,parameter_space,frequency,tickers,n_trials,train_start,train_end,cfg)

@mcp.tool()
def validate_strategy(strategy:dict[str,Any], frequency:str="Daily", tickers:list[str]|None=None, train_end:str="2023-12-31", validation_end:str="2025-12-31", commission_bps:float=20, slippage_bps:float=5, direction:str="long", use_adjusted:bool=False)->dict[str,Any]:
    """Evaluate a fixed strategy across train, validation, and untouched test periods for each ticker. Windows are evaluated with warm indicators (backtest runs on the full series, results masked to each window). LONG-ONLY: direction must be "long"."""
    cfg=BacktestConfig(commission_bps=commission_bps,slippage_bps=slippage_bps,direction=direction)
    tickers=tickers or data.tickers()
    buckets={"train":[],"validation":[],"test":[]}
    windows=[
        ("train",None,train_end),
        ("validation",train_end,validation_end),
        ("test",validation_end,None),
    ]
    for t in tickers:
        try:
            df=data.load_adjusted(t,frequency) if use_adjusted else data.load(t,frequency)
            if len(df)<150: continue
            for name,start,end in windows:
                if start is None and end is None: continue
                lo=df.index.min() if start is None else pd.Timestamp(start)
                hi=df.index.max() if end is None else pd.Timestamp(end)
                n_in=int(((df.index>=lo)&(df.index<=hi)).sum())
                if n_in<100: continue
                wcfg=BacktestConfig(initial_cash=cfg.initial_cash,commission_bps=cfg.commission_bps,slippage_bps=cfg.slippage_bps,direction=cfg.direction,stop_loss_pct=cfg.stop_loss_pct,take_profit_pct=cfg.take_profit_pct,window=(lo.isoformat(),hi.isoformat()))
                m=backtest(df,strategy,wcfg)['metrics']; buckets[name].append({'ticker':t,**m})
        except Exception: continue
    summary={}
    for name,rows in buckets.items():
        if not rows: summary[name]={"tickers":0}; continue
        d=pd.DataFrame(rows)
        summary[name]={"tickers":len(rows),"median_return":float(d.total_return.median()),"median_sharpe":float(d.sharpe.median()),"median_drawdown":float(d.max_drawdown.median()),"profitable_fraction":float((d.total_return>0).mean()),"median_trades":float(d.trades.median())}
    return summary

@mcp.tool()
def save_experiment(name:str, payload:dict[str,Any])->dict[str,Any]:
    """Save a strategy/backtest experiment as JSON for later review."""
    safe=''.join(c if c.isalnum() or c in '-_' else '_' for c in name)[:120]
    path=settings.results_dir/f"{safe}.json"
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    return {"path":str(path)}

def main():
    mcp.run()

if __name__ == '__main__':
    main()
