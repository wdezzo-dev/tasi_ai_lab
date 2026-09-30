from __future__ import annotations
import numpy as np
import pandas as pd


def _s(x): return x.astype(float)

def sma(x, n): return _s(x).rolling(int(n), min_periods=int(n)).mean()
def ema(x, n): return _s(x).ewm(span=int(n), adjust=False, min_periods=int(n)).mean()
def rsi(x, n=14):
    n=int(n); d=_s(x).diff(); up=d.clip(lower=0); dn=-d.clip(upper=0)
    ag=up.ewm(alpha=1/n, adjust=False, min_periods=n).mean()
    al=dn.ewm(alpha=1/n, adjust=False, min_periods=n).mean()
    rs=ag/al.replace(0,np.nan)
    return 100 - 100/(1+rs)
def roc(x,n=10): return _s(x).pct_change(int(n))*100
def atr(high,low,close,n=14):
    pc=_s(close).shift(1)
    tr=pd.concat([_s(high)-_s(low), (_s(high)-pc).abs(), (_s(low)-pc).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/int(n),adjust=False,min_periods=int(n)).mean()
def std(x,n=20): return _s(x).rolling(int(n),min_periods=int(n)).std()
def zscore(x,n=20):
    m=sma(x,n); s=std(x,n); return (x-m)/s.replace(0,np.nan)
def bb_mid(x,n=20): return sma(x,n)
def bb_upper(x,n=20,k=2): return bb_mid(x,n)+k*std(x,n)
def bb_lower(x,n=20,k=2): return bb_mid(x,n)-k*std(x,n)
def donchian_high(x,n=20): return _s(x).rolling(int(n),min_periods=int(n)).max()
def donchian_low(x,n=20): return _s(x).rolling(int(n),min_periods=int(n)).min()
def donchian_high_prev(x,n=20): return _s(x).shift(1).rolling(int(n),min_periods=int(n)).max()
def donchian_low_prev(x,n=20): return _s(x).shift(1).rolling(int(n),min_periods=int(n)).min()
def crossabove(x,y):
    x=_s(x)
    if hasattr(y,'astype'):
        y=_s(y); py=y.shift(1)
    else:
        py=y
    return (x>y)&(x.shift(1)<=py)
def crossbelow(x,y):
    x=_s(x)
    if hasattr(y,'astype'):
        y=_s(y); py=y.shift(1)
    else:
        py=y
    return (x<y)&(x.shift(1)>=py)
def macd(x,fast=12,slow=26):
    f=_s(x).ewm(span=int(fast),adjust=False).mean()
    s=_s(x).ewm(span=int(slow),adjust=False).mean()
    return f-s
def macd_signal(x,fast=12,slow=26,signal=9):
    return macd(x,fast,slow).ewm(span=int(signal),adjust=False).mean()
def bars_since(x):
    b=x.astype(bool).fillna(False)
    c=(~b).cumsum()
    last_true=c.where(b).ffill()
    return c-last_true+1
def volume_ratio(v,n=20): return _s(v)/sma(v,n)
def adx(high,low,close,n=14):
    n=int(n); h=_s(high); l=_s(low); c=_s(close)
    up=h.diff(); dn=-l.diff()
    plus_dm=up.where((up>dn)&(up>0),0.0); minus_dm=dn.where((dn>up)&(dn>0),0.0)
    pc=c.shift(1); tr=pd.concat([h-l,(h-pc).abs(),(l-pc).abs()],axis=1).max(axis=1)
    atrv=tr.ewm(alpha=1/n,adjust=False,min_periods=n).mean()
    pdi=100*plus_dm.ewm(alpha=1/n,adjust=False,min_periods=n).mean()/atrv
    mdi=100*minus_dm.ewm(alpha=1/n,adjust=False,min_periods=n).mean()/atrv
    dx=100*(pdi-mdi).abs()/(pdi+mdi).replace(0,np.nan)
    return dx.ewm(alpha=1/n,adjust=False,min_periods=n).mean()
