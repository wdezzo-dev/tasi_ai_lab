from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
import pandas as pd
from .dsl import evaluate

@dataclass
class BacktestConfig:
    initial_cash: float = 100_000.0
    commission_bps: float = 20.0
    slippage_bps: float = 5.0
    direction: str = "long"
    stop_loss_pct: float | None = None
    take_profit_pct: float | None = None
    max_positions: int = 1
    position_fraction: float = 1.0
    execution: str = "next_open"
    intrabar_priority: str = "stop_first"
    window: tuple[str, str] | None = None

    def __post_init__(self):
        if self.direction != "long":
            raise ValueError(
                f"this engine is long-only; expected direction='long', got '{self.direction}'"
            )


def _annual_factor(index):
    if len(index)<2: return 252
    days=max((index[-1]-index[0]).total_seconds()/86400, 1)
    return 365*len(index)/days


def _simulate(df: pd.DataFrame, spec: dict, cfg: BacktestConfig) -> tuple[pd.Series, list[dict]]:
    if spec.get("entry_short") or spec.get("exit_short"):
        raise ValueError("short signals are not supported: this engine is long-only")
    df=df.copy().sort_index()
    entry_long=evaluate(spec["entry_long"],df) if spec.get("entry_long") else pd.Series(False,index=df.index)
    exit_long=evaluate(spec["exit_long"],df) if spec.get("exit_long") else pd.Series(False,index=df.index)
    el=entry_long.values.astype(bool); xl=exit_long.values.astype(bool)
    O,H,L,C=df[["open","high","low","close"]].values.T
    cash=float(cfg.initial_cash); qty=0.0; side=0; entry=0.0; entry_time=None
    equity=[]; trades=[]
    fee_rate=cfg.commission_bps/10000; slip_rate=cfg.slippage_bps/10000
    sl_pct=cfg.stop_loss_pct; tp_pct=cfg.take_profit_pct
    ipo=cfg.intrabar_priority; pos_frac=cfg.position_fraction
    abs_=abs; eq_append=equity.append; tr_append=trades.append
    n=len(df); index=df.index
    for i in range(n):
        o,h,l,c=O[i],H[i],L[i],C[i]
        # manage existing position at this bar's high/low, then close-on-signal
        if side:
            stop_hit=target_hit=False; exit_px=None; reason=None
            sl = entry*(1-sl_pct/100) if sl_pct is not None else None
            tp = entry*(1+tp_pct/100) if tp_pct is not None else None
            if sl is not None and o <= sl:
                exit_px=o; reason="stop"
            elif tp is not None and o >= tp:
                exit_px=o; reason="target"
            if reason is None:
                if sl is not None:
                    if l <= sl: stop_hit=True; exit_px=sl
                if tp is not None:
                    if h >= tp: target_hit=True; tpx=tp
                if stop_hit and target_hit:
                    do_target=(ipo=="target_first")
                    exit_px=tpx if do_target else exit_px; reason="target" if do_target else "stop"
                elif stop_hit:
                    reason="stop"
                elif target_hit:
                    exit_px=tpx; reason="target"
            if reason is None:
                if xl[i]: exit_px=o; reason="signal"
            if exit_px is not None:
                exec_px=exit_px*(1-slip_rate)
                pnl=qty*(exec_px-entry)
                fees=fee_rate*(abs_(qty*entry)+abs_(qty*exec_px))
                cash += qty * exec_px - fee_rate * abs_(qty * exec_px)
                tr_append({"entry_time":entry_time,"exit_time":index[i],"side":"long","entry":entry,"exit":exec_px,"qty":qty,"pnl":pnl-fees,"gross_pnl":pnl,"fees":fees,"reason":reason})
                qty=0; side=0; entry=0; entry_time=None
        # generate new position from previous-bar signal at current open
        if side==0 and i>0:
            if el[i-1]:
                exec_px=o*(1+slip_rate)
                alloc=max(0.0, cash*pos_frac)
                qty=math.floor(alloc/exec_px)
                if qty>=1:
                    side=1
                    fees=fee_rate*abs_(qty*exec_px)
                    cash -= qty * exec_px + fees
                    entry=exec_px; entry_time=index[i]
        mark=cash + qty*c
        eq_append(mark)
    if side:
        ts=index[-1]; c=C[-1]; exec_px=c*(1-slip_rate)
        pnl=qty*(exec_px-entry); fees=fee_rate*(abs_(qty*entry)+abs_(qty*exec_px))
        cash += qty * exec_px - fee_rate * abs_(qty * exec_px)
        tr_append({"entry_time":entry_time,"exit_time":ts,"side":"long","entry":entry,"exit":exec_px,"qty":qty,"pnl":pnl-fees,"gross_pnl":pnl,"fees":fees,"reason":"end"})
        equity[-1]=cash
    eq=pd.Series(equity,index=df.index,dtype=float)
    return eq, trades


def _metrics(eq: pd.Series, trades: list[dict], cfg: BacktestConfig) -> dict:
    if len(eq)==0:
        return {"total_return":0.0,"cagr":0.0,"max_drawdown":0.0,"sharpe":0.0,"volatility":0.0,"profit_factor":0.0,"trades":0,"win_rate":0.0,"final_equity":float(cfg.initial_cash)}
    idx=eq.index
    rets=eq.pct_change().replace([np.inf,-np.inf],np.nan).fillna(0)
    peak=eq.cummax(); dd=eq/peak-1
    years=max((idx[-1]-idx[0]).days/365.25, 1/365.25)
    total_ret=eq.iloc[-1]/cfg.initial_cash-1
    cagr=(eq.iloc[-1]/cfg.initial_cash)**(1/years)-1 if eq.iloc[-1]>0 else -1
    vol=rets.std(ddof=0)*math.sqrt(_annual_factor(idx)); sharpe=(rets.mean()/rets.std(ddof=0))*math.sqrt(_annual_factor(idx)) if rets.std(ddof=0)>0 else 0
    winners=[float(t["pnl"]) for t in trades if t["pnl"]>0]; losers=[float(t["pnl"]) for t in trades if t["pnl"]<0]
    pf=sum(winners)/abs(sum(losers)) if losers else float("inf") if winners else 0
    return {"total_return":float(total_ret),"cagr":float(cagr),"max_drawdown":float(dd.min()),"sharpe":float(sharpe),"volatility":float(vol),"profit_factor":float(pf),"trades":len(trades),"win_rate":float(len(winners)/len(trades)) if trades else 0,"final_equity":float(eq.iloc[-1])}


def window_metrics(eq_full: pd.Series, trades_full: list[dict], start: str, end: str, cfg: BacktestConfig) -> tuple[dict, pd.Series, list[dict]]:
    start=pd.Timestamp(start); end=pd.Timestamp(end)
    mask=(eq_full.index>=start)&(eq_full.index<=end)
    eq=eq_full[mask]
    trades=[t for t in trades_full if t["exit_time"]>=start and t["exit_time"]<=end]
    return _metrics(eq, trades, cfg), eq, trades


def backtest(df: pd.DataFrame, spec: dict, config: BacktestConfig | None = None) -> dict:
    cfg=config or BacktestConfig()
    eq_full, trades_full = _simulate(df, spec, cfg)
    if cfg.window is not None:
        metrics, eq, trades = window_metrics(eq_full, trades_full, cfg.window[0], cfg.window[1], cfg)
        return {"metrics":metrics,"trades":trades,"equity":eq}
    return {"metrics":_metrics(eq_full, trades_full, cfg),"trades":trades_full,"equity":eq_full}


def split_ohlcv(df, train_end, validation_end):
    a=df[df.index<=pd.Timestamp(train_end)].copy(); b=df[(df.index>pd.Timestamp(train_end))&(df.index<=pd.Timestamp(validation_end))].copy(); c=df[df.index>pd.Timestamp(validation_end)].copy()
    return a,b,c