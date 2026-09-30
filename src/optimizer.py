from __future__ import annotations
import re
from typing import Any
import numpy as np
import pandas as pd
import optuna
from .backtest import BacktestConfig, backtest

_PLACEHOLDER=re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")

def render_spec(spec:dict[str,Any], params:dict[str,Any])->dict[str,Any]:
    def rec(x):
        if isinstance(x,str): return x.format(**params)
        if isinstance(x,dict): return {k:rec(v) for k,v in x.items()}
        if isinstance(x,list): return [rec(v) for v in x]
        return x
    return rec(spec)

def suggest_parameter_space(trial:optuna.Trial, space:dict[str,dict[str,Any]])->dict[str,Any]:
    out={}
    for name, cfg in space.items():
        kind=cfg.get('type','int')
        if kind=='int': out[name]=trial.suggest_int(name,int(cfg['low']),int(cfg['high']),step=int(cfg.get('step',1)))
        elif kind=='float': out[name]=trial.suggest_float(name,float(cfg['low']),float(cfg['high']),step=cfg.get('step'))
        elif kind=='categorical': out[name]=trial.suggest_categorical(name,cfg['choices'])
        else: raise ValueError(f'Unsupported parameter type: {kind}')
    return out

def optimize(data, spec:dict[str,Any], space:dict[str,dict[str,Any]], frequency='Daily', tickers=None, n_trials=50, train_start=None, train_end=None, cfg:BacktestConfig|None=None):
    tickers=tickers or data.tickers()
    cfg=cfg or BacktestConfig()
    frames={}
    for t in tickers:
        try:
            df=data.load(t,frequency)
            if train_start: df=df[df.index>=pd.Timestamp(train_start)]
            if train_end: df=df[df.index<=pd.Timestamp(train_end)]
            if len(df)>=200: frames[t]=df
        except Exception: pass
    if not frames: return {"error":"No usable ticker data"}
    def objective(trial):
        params=suggest_parameter_space(trial,space)
        s=render_spec(spec,params)
        scores=[]
        for t,df in frames.items():
            try:
                m=backtest(df,s,cfg)['metrics']
                if m['trades']<5: continue
                scores.append(m)
            except Exception: pass
        if not scores: return -100.0
        x=pd.DataFrame(scores)
        # Robust objective: reward median OOS-style return and Sharpe, penalize drawdown and low breadth.
        profitable=(x['total_return']>0).mean()
        score=float(x['sharpe'].median()+0.5*x['cagr'].median()-1.0*abs(x['max_drawdown'].median())+0.75*profitable)
        trial.set_user_attr('summary',{
            'tickers':len(x),'median_return':float(x.total_return.median()),'median_cagr':float(x.cagr.median()),
            'median_sharpe':float(x.sharpe.median()),'median_drawdown':float(x.max_drawdown.median()),'profitable_fraction':float(profitable),
            'median_trades':float(x.trades.median())})
        return score
    study=optuna.create_study(direction='maximize')
    study.optimize(objective,n_trials=int(n_trials),show_progress_bar=False)
    trials=[]
    for tr in study.best_trials[:20]:
        trials.append({'number':tr.number,'value':tr.value,'params':tr.params,'summary':tr.user_attrs.get('summary',{})})
    return {'best_params':study.best_params,'best_value':study.best_value,'trials':trials}
