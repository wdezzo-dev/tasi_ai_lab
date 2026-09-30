from __future__ import annotations
import json
import re
from functools import lru_cache
from pathlib import Path
import pandas as pd

TYPE_CODES = {
    "منحة اسهم": "BONUS",
    "حقوق أولوية": "RIGHTS",
    "تخفيض رأس المال": "CAPITAL_REDUCTION",
    "استحواذ": "ACQUISITION",
    "تقسيم الأسهم": "SPLIT",
    "دمج الأسهم": "REVERSE_SPLIT",
    "زيادة رأس المال": "CAPITAL_INCREASE",
    "زيادة رأس المال – تحويل الديون": "DEBT_CONVERSION",
    "زيادة رأس المال عن طريق تحويل الديون": "DEBT_CONVERSION",
    "زيادة رأس المال - طرح أسهم مع وقف العمل بحق الأولوية": "RIGHTS_WITH_PAUSE",
}

STATUS_ADJUSTED = "adjusted"
STATUS_RATIO_MISSING = "ratio_missing"
STATUS_TERMS_REQUIRED = "terms_required"
STATUS_METADATA_ONLY = "metadata_only"


def _parse_date(value) -> pd.Timestamp | None:
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    s = value.strip()
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            ts = pd.to_datetime(s, format=fmt)
            return ts
        except (ValueError, TypeError):
            continue
    try:
        return pd.Timestamp(s)
    except (ValueError, TypeError):
        return None


def _parse_capital(value) -> float | None:
    if value is None:
        return None
    s = re.sub(r"[^\d.]", "", str(value))
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _classify(type_code: str, new_capital: float | None, prev_capital: float | None) -> tuple[dict | None, str]:
    if type_code == "BONUS":
        if new_capital is not None and prev_capital is not None and new_capital > prev_capital > 0:
            ratio = new_capital / prev_capital
            return {"share_ratio": ratio, "price_factor": 1.0 / ratio, "volume_factor": ratio}, STATUS_ADJUSTED
        return None, STATUS_RATIO_MISSING
    if type_code in {"SPLIT", "REVERSE_SPLIT"}:
        return None, STATUS_RATIO_MISSING
    if type_code == "RIGHTS":
        return None, STATUS_TERMS_REQUIRED
    return None, STATUS_METADATA_ONLY


def _normalize_event(raw: dict) -> dict:
    ticker = str(raw.get("companySymbol") or "").strip().zfill(4)
    type_code = TYPE_CODES.get(str(raw.get("issueTypeDesc") or "").strip(), "UNKNOWN")
    announce = _parse_date(raw.get("announceDate"))
    effective = _parse_date(raw.get("dueDate"))
    new_cap = _parse_capital(raw.get("newCApital"))
    prev_cap = _parse_capital(raw.get("prevCApital"))
    factors, status = _classify(type_code, new_cap, prev_cap)
    ev = {
        "ticker": ticker,
        "announce_date": announce,
        "effective_date": effective,
        "type": type_code,
        "new_capital": new_cap,
        "previous_capital": prev_cap,
        "share_ratio": factors["share_ratio"] if factors else None,
        "price_factor": factors["price_factor"] if factors else None,
        "volume_factor": factors["volume_factor"] if factors else None,
        "adjustment_status": status,
        "key": None,
    }
    return ev


@lru_cache(maxsize=8)
def load_corporate_actions(data_dir: str | Path | None = None) -> list[dict]:
    root = Path(data_dir) if data_dir is not None else Path(__file__).resolve().parent.parent / "data"
    folder = root / "corporate_action"
    events: list[dict] = []
    if not folder.exists():
        return events
    files = sorted(folder.glob("*_ca.json"))
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                data = json.load(fh)
        except (json.JSONDecodeError, OSError):
            continue
        raw_list = data.get("data") or []
        for idx, raw in enumerate(raw_list):
            ev = _normalize_event(raw)
            ev["key"] = f"{ev['ticker']}:{ev['effective_date'].isoformat() if ev['effective_date'] else 'NA'}:{ev['type']}:{idx}"
            events.append(ev)
    for i, ev in enumerate(events):
        ev["_seq"] = i
    return events


def _index_by_ticker(events: list[dict]) -> dict[str, list[dict]]:
    by: dict[str, list[dict]] = {}
    for ev in events:
        by.setdefault(ev["ticker"], []).append(ev)
    for k in by:
        by[k].sort(key=lambda e: (e["effective_date"] or pd.Timestamp.max))
    return by


def get_actions(ticker: str, events: list[dict] | None = None) -> list[dict]:
    evs = events if events is not None else load_corporate_actions()
    t = str(ticker).strip().zfill(4)
    return _index_by_ticker(evs).get(t, [])


def get_actions_between(ticker: str, start, end, events: list[dict] | None = None) -> list[dict]:
    lo = pd.Timestamp(start)
    hi = pd.Timestamp(end)
    out = []
    for ev in get_actions(ticker, events):
        d = ev["effective_date"]
        if d is not None and lo <= d <= hi:
            out.append(ev)
    return out


def get_effective_actions(ticker: str, date, events: list[dict] | None = None) -> list[dict]:
    ts = pd.Timestamp(date)
    return [ev for ev in get_actions(ticker, events) if ev["effective_date"] == ts]


def apply_adjustments(df: pd.DataFrame, events: list[dict]) -> tuple[pd.DataFrame, list[str]]:
    """Return (adjusted_df, applied_event_keys).

    Bars strictly BEFORE an event's effective_date are transformed into the
    post-event share basis by that event's price factor. Bars on/after the
    effective date are treated as raw. Multiple events compose chronologically:
    each bar accumulates the product of factors for every adjusted event whose
    effective_date is AFTER that bar's date. Each event applied exactly once.
    """
    out = df.copy()
    adjusted = [ev for ev in events if ev["adjustment_status"] == STATUS_ADJUSTED
                and ev["price_factor"] is not None]
    if not adjusted:
        return out, []

    import numpy as np
    index = out.index
    fac = np.ones(len(index), dtype=float)
    for ev in adjusted:
        mask = index < ev["effective_date"]
        fac[mask] *= float(ev["price_factor"])
    fac = pd.Series(fac, index=index)

    out["open"] = out["open"] * fac
    out["high"] = out["high"] * fac
    out["low"] = out["low"] * fac
    out["close"] = out["close"] * fac
    out["volume"] = out["volume"] / fac
    applied = [ev["key"] for ev in adjusted]
    return out, applied


def summarize_events(events: list[dict] | None = None) -> dict:
    evs = events if events is not None else load_corporate_actions()
    counts = {}
    for ev in evs:
        counts[ev["adjustment_status"]] = counts.get(ev["adjustment_status"], 0) + 1
    return {
        "events_loaded": len(evs),
        "adjusted": counts.get(STATUS_ADJUSTED, 0),
        "ratio_missing": counts.get(STATUS_RATIO_MISSING, 0),
        "terms_required": counts.get(STATUS_TERMS_REQUIRED, 0),
        "metadata_only": counts.get(STATUS_METADATA_ONLY, 0),
    }


def ca_files_loaded(data_dir: str | Path | None = None) -> int:
    root = Path(data_dir) if data_dir is not None else Path(__file__).resolve().parent.parent / "data"
    folder = root / "corporate_action"
    if not folder.exists():
        return 0
    return len(list(folder.glob("*_ca.json")))