from __future__ import annotations
import re
from functools import lru_cache
from pathlib import Path
import pandas as pd

from .corporate_actions import load_corporate_actions, get_actions, apply_adjustments

_FREQ_ALIASES = {
    "daily": "Daily", "weekly": "Weekly", "4h": "4h", "1h": "1h",
    "30m": "30min", "30min": "30min", "15m": "15min", "15min": "15min",
    "1m": "1min", "1min": "1min",
}

class TasiData:
    def __init__(self, data_dir: str | Path, companies_csv: str | Path):
        self.data_dir = Path(data_dir)
        self.companies = pd.read_csv(companies_csv, dtype={"TickerID": str})
        self.companies["TickerID"] = self.companies["TickerID"].str.strip().str.zfill(4)
        self._by_ticker = {r.TickerID: r._asdict() for r in self.companies.itertuples(index=False)}

    def tickers(self, sector: str | None = None) -> list[str]:
        df = self.companies
        if sector:
            df = df[df["Sector"].astype(str).str.contains(sector, case=False, na=False)]
        return df["TickerID"].tolist()

    def company(self, ticker: str) -> dict:
        t = str(ticker).zfill(4)
        return self._by_ticker[t]

    def _find_path(self, freq: str, ticker: str) -> Path:
        folder = _FREQ_ALIASES.get(freq.lower(), freq)
        matches = list((self.data_dir / folder).glob(f"{str(ticker).zfill(4)}_F*.csv"))
        if not matches:
            raise FileNotFoundError(f"No {folder} data for ticker {ticker}")
        return matches[0]

    @lru_cache(maxsize=64)
    def load(self, ticker: str, freq: str = "Daily") -> pd.DataFrame:
        path = self._find_path(freq, ticker)
        df = pd.read_csv(path)
        if "Time" in df.columns:
            dt = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"].astype(str), errors="coerce")
        else:
            dt = pd.to_datetime(df["Date"], errors="coerce")
        out = df.copy()
        out.index = dt
        out = out[~out.index.isna()]
        out = out[~out.index.duplicated(keep="last")].sort_index()
        out.columns = [str(c).strip().lower() for c in out.columns]
        required = ["open", "high", "low", "close", "volume"]
        missing = [c for c in required if c not in out.columns]
        if missing:
            raise ValueError(f"Missing columns {missing} in {path}")
        out[required] = out[required].apply(pd.to_numeric, errors="coerce")
        return out[required].dropna(subset=["open", "high", "low", "close"])

    @lru_cache(maxsize=64)
    def load_adjusted(self, ticker: str, freq: str = "Daily") -> pd.DataFrame:
        df = self.load(ticker, freq)
        events = get_actions(ticker, load_corporate_actions(self.data_dir))
        adjusted, _ = apply_adjustments(df, events)
        return adjusted

    def manifest(self) -> dict:
        result = {}
        for freq in _FREQ_ALIASES.values():
            files = list((self.data_dir / freq).glob("*.csv"))
            if not files:
                continue
            rows, mins, maxs = 0, [], []
            for f in files:
                df = pd.read_csv(f)
                rows += len(df)
                dt = pd.to_datetime(df["Date"].astype(str) + ((" " + df["Time"].astype(str)) if "Time" in df.columns else ""), errors="coerce")
                mins.append(dt.min()); maxs.append(dt.max())
            result[freq] = {"files": len(files), "rows": rows, "min": min(mins).isoformat(), "max": max(maxs).isoformat()}
        return result
