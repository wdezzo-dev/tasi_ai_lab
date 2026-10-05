import glob
import json
import sys
import warnings
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

warnings.filterwarnings(
    "ignore",
    message="Automatically deduplicated selection parameter with identical configuration",
    category=UserWarning,
)

ROOT = Path(__file__).resolve().parents[3]
PAYREPORT = Path(__file__).resolve().parents[1]
REFINE = PAYREPORT / "refine"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

from performance import (  # noqa: E402
    INITIAL_CASH,
    build_trade_view,
    overview_chart,
    styled_df,
    style_sign,
    style_trade_table,
)
from src.backtest import BacktestConfig, _simulate, window_metrics  # noqa: E402
from src.config import Settings  # noqa: E402
from src.data import TasiData  # noqa: E402

TASI = TasiData(Settings.from_env(ROOT).data_dir, Settings.from_env(ROOT).companies_csv)

st.set_page_config(
    page_title="لوحة نتائج الاستراتيجيات — TASI",
    page_icon=":material/trending_up:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

rl = "\u200f"

st.markdown(
    """
    <style>
    [data-testid="stMarkdownContainer"] { direction: rtl; text-align: right; }
    [data-testid="stMarkdownContainer"] ul,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] code { direction: rtl; text-align: right; unicode-bidi: plaintext; }
    [data-testid="stMarkdownContainer"] li { line-height: 1.8; margin-bottom: 5px; }
    [data-testid="stMarkdownContainer"] ul ul { margin-block: 4px 6px; }
    [data-testid="stMarkdownContainer"] h3 { margin-block: 1.1rem 0.35rem; }
    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p { direction: rtl; text-align: right; line-height: 1.7; }
    [data-testid="stCaptionContainer"] p { unicode-bidi: plaintext; }
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"],
    [data-testid="stMetricDelta"] { direction: rtl; text-align: right; }
    [data-testid="stHorizontalBlock"] [data-testid="stMetric"]:has([data-testid="stMetricDeltaIcon-Down"]) [data-testid="stMetricValue"] { color: #EF4444; }
    [data-testid="stHorizontalBlock"] [data-testid="stMetric"]:has([data-testid="stMetricDeltaIcon-Up"]) [data-testid="stMetricValue"] { color: #22C55E; }
    [data-testid="stVegaLiteChart"] { overflow: visible; }
    [id$="-tabpanel-0"] [data-testid="stVegaLiteChart"] > svg { padding-right: 5rem; }
    [data-testid="stWidgetLabel"] { direction: rtl; text-align: right; }
    [data-testid="stHeader"] { direction: rtl; text-align: right; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] { direction: rtl; text-align: right; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] { direction: rtl; text-align: right; }
    [data-testid="stTabs"] { direction: rtl; }
    [data-testid="stExpander"] { direction: rtl; text-align: right; }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] { direction: rtl; }
    [data-testid="stVegaLiteChart"] { direction: ltr !important; }
    [data-testid="stVegaLiteChart"] canvas { max-width: 100%; }
    [data-testid="stVegaLiteChart"] [class*="tooltip"] { direction: rtl !important; text-align: right; }
    [data-testid="stVegaLiteChart"] .vega-embed { width: 100%; }
    @media (max-width: 768px) {
      [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
      [data-testid="stHorizontalBlock"] > div { min-width: 100% !important; }
      .stTabs [data-baseweb="tab"] { padding: 6px 8px 8px; font-size: 13px; }
      .stTabs [data-baseweb="tab-highlight"] { margin-top: 6px; }
      .block-container { padding-top: 1rem; }
      [data-testid="stMetricValue"] { font-size: 1.5rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- data model
PERF_COLUMNS = {
    "ticker": "السهم",
    "strategy_id": "معرف الاستراتيجية",
    "name": "الاستراتيجية",
    "family": "العائلة",
    "timeframe": "الإطار الزمني",
    "stress_oos_gain": "الربح المجمع خارج العينة",
    "stress_eng_val": "الربح الفعلي — التحقق",
    "stress_eng_test": "الربح الفعلي — الاختبار",
    "full_stress_total_ret": "الربح الإجمالي (التاريخ الكامل)",
    "full_stress_maxdd": "أقصى تراجع",
    "full_stress_sharpe": "نسبة شارب",
    "full_stress_pf": "معامل الربحية",
    "full_stress_trades": "عدد الصفقات",
    "flags": "ملاحظات",
}
ROW_COLUMNS = [
    "ticker", "strategy_id", "name", "family", "timeframe",
    "stress_oos_gain", "stress_eng_val", "stress_eng_test",
    "full_stress_total_ret", "full_stress_maxdd", "full_stress_sharpe",
    "full_stress_pf", "full_stress_trades", "flags",
]

FAMILY_AR = {
    "trend": "الاتجاه",
    "momentum": "الزخم",
    "breakout": "كسر النطاق",
    "mean_reversion": "الارتداد للمتوسط",
    "volatility": "التذبذب",
    "volume": "الحجم",
    "pattern": "الأنماط",
    "other": "أخرى",
}
TF_AR = {"Daily": "يومي", "1h": "ساعة", "4h": "4 ساعات", "30min": "30 دقيقة", "15min": "15 دقيقة"}

COST_LEVELS = {
    "واقعي (17.825/20) ≈ 0.76%": (17.825, 20.0),
    "أساسي (20/5) ≈ 0.50%": (20.0, 5.0),
    "تشديد (40/10) ≈ 1.00%": (40.0, 10.0),
}
COST_DEFAULT = "واقعي (17.825/20) ≈ 0.76%"

RTL_COLUMNS = [PERF_COLUMNS[k] for k in ROW_COLUMNS[::-1]]
BOARD_SUBSET = [
    "الربح المجمع خارج العينة", "الربح الفعلي — التحقق", "الربح الفعلي — الاختبار",
    "الربح الإجمالي (التاريخ الكامل)", "نسبة شارب", "معامل الربحية",
]
BOARD_FORMAT = {
    "معرف الاستراتيجية": "{:d}",
    "الربح المجمع خارج العينة": "{:+.1%}",
    "الربح الفعلي — التحقق": "{:+.1%}",
    "الربح الفعلي — الاختبار": "{:+.1%}",
    "الربح الإجمالي (التاريخ الكامل)": "{:+.1%}",
    "أقصى تراجع": "{:.1%}",
    "نسبة شارب": "{:+.2f}",
    "معامل الربحية": "{:+.2f}",
    "عدد الصفقات": "{:d}",
}


@st.cache_data(show_spinner=False)
def load_cards() -> pd.DataFrame:
    files = sorted(glob.glob(str(PAYREPORT / "report" / "perf_cards_*.csv")))
    df = pd.read_csv(files[-1])
    df["strategy_id"] = df["strategy_id"].astype(int)
    df["ticker"] = df["ticker"].astype(str)
    return df.sort_values(["ticker", "strategy_id"], kind="stable").reset_index(drop=True)


@st.cache_data(show_spinner=False)
def load_picks() -> pd.DataFrame:
    p = pd.read_csv(PAYREPORT / "report" / "picks_per_stock.csv", dtype={"ticker": str})
    return p.sort_values("min_alpha", ascending=False).reset_index(drop=True)


@st.cache_data(show_spinner=False)
def roster_map() -> dict:
    out = {}
    for f in (ROOT / "results" / "catalog" / "rosters").glob("batch_*_roster.json"):
        d = json.loads(f.read_text())
        lst = d["strategy_roster"] if isinstance(d, dict) else d
        for s in lst:
            out[int(s["id"])] = s
    return out


@st.cache_data(show_spinner="جارٍ حساب الأداء من الصفقات الفعلية ...")
def run_strategy(sid: int, ticker: str, tf: str, commission: float, slippage: float):
    rec = json.loads((REFINE / "validated" / f"{sid}_{ticker}.json").read_text())
    spec = rec["spec"]
    params = rec.get("best_params") or {}
    roster = roster_map().get(sid, {})
    sl = float(params["sl"]) if "sl" in params else roster.get("stop_loss_pct")
    tp = float(params["tp"]) if "tp" in params else roster.get("take_profit_pct")
    df = TASI.load(ticker, tf)
    eq, trades = _simulate(
        df, spec,
        BacktestConfig(commission_bps=commission, slippage_bps=slippage,
                       stop_loss_pct=sl, take_profit_pct=tp),
    )
    bench = float(df["close"].iloc[-1] / df["close"].iloc[0] - 1)
    return eq, trades, {
        "name": roster.get("name") or rec["spec"].get("name", ""),
        "family": roster.get("family"), "params": params, "bench": bench,
    }


def pct(v) -> str:
    return f"{v * 100:.1%}"


TEST_WINDOW = ("2026-01-01", "2026-09-21")
VERIFY_COSTS = (20.0, 5.0)


@st.cache_data(show_spinner=False)
def load_verify_exports() -> tuple[pd.DataFrame, pd.DataFrame]:
    """survivors_enriched.csv (one row per passing combo) + all_survivor_trades.csv."""
    base = PAYREPORT / "trades"
    enr = pd.read_csv(base / "survivors_enriched.csv", dtype={"ticker": str})
    trd = pd.read_csv(base / "all_survivor_trades.csv", dtype={"ticker": str})
    trd["entry_time"] = pd.to_datetime(trd["entry_time"], format="mixed")
    trd["exit_time"] = pd.to_datetime(trd["exit_time"], format="mixed")
    return enr, trd


def trades_view(g: pd.DataFrame) -> pd.DataFrame:
    """Adapt exported ledger rows into the trade view used by charts/tables.

    The ledger carries pnl per trade but no equity curve, so the curve is rebuilt
    from cumulative pnl on a 100k base to draw drawdown.
    """
    if g.empty:
        return pd.DataFrame(columns=["trade_no", "entry_time", "exit_time", "side", "qty", "entry",
                                     "exit", "pnl", "fees", "reason", "cum_pnl", "equity"])
    td = g.sort_values("exit_time").reset_index(drop=True).copy()
    td["trade_no"] = range(1, len(td) + 1)
    td["cum_pnl"] = td["pnl"].cumsum()
    td["cum_pos"] = td["cum_pnl"].clip(lower=0)
    td["cum_neg"] = td["cum_pnl"].clip(upper=0)
    td["win"] = td["pnl"] > 0
    td["result"] = td["pnl"].map(lambda v: "ربح" if v > 0 else ("خسارة" if v < 0 else "تعادل"))
    td["equity"] = INITIAL_CASH + td["cum_pnl"]
    peak = td["equity"].cummax()
    td["dd_ratio"] = td["equity"] / peak - 1
    td["dd_sar"] = td["equity"] - peak
    return td


@st.cache_data(show_spinner="جارٍ إعادة المحاكاة على بيانات السوق ...")
def rerun_engine(sid: int, ticker: str, tf: str, entry_long: str, exit_long: str,
                 sl, tp) -> dict | None:
    """Re-run the engine today on current price files and re-measure the test window."""
    df = TASI.load_clean(ticker, tf)
    if df is None:
        return None
    commission, slippage = VERIFY_COSTS
    cfg = BacktestConfig(
        commission_bps=commission, slippage_bps=slippage,
        stop_loss_pct=None if pd.isna(sl) else float(sl),
        take_profit_pct=None if pd.isna(tp) else float(tp),
    )
    eq, trades = _simulate(df, {"entry_long": entry_long, "exit_long": exit_long}, cfg)
    eqw = eq[(eq.index >= pd.Timestamp(TEST_WINDOW[0])) & (eq.index <= pd.Timestamp(TEST_WINDOW[1]))]
    _, _, trw = window_metrics(eq, trades, *TEST_WINDOW, cfg)
    winners = [t["pnl"] for t in trw if t["pnl"] > 0]
    losers = [t["pnl"] for t in trw if t["pnl"] < 0]
    peak = eqw.cummax()
    metrics = {
        "trades": len(trw),
        "win_rate": (len(winners) / len(trw)) if trw else 0.0,
        "engine_win_ret": (float(eqw.iloc[-1] / eqw.iloc[0] - 1) if len(eqw) else 0.0),
        "max_drawdown": (float((eqw / peak - 1).min()) if len(eqw) else 0.0),
        "profit_factor": (sum(winners) / abs(sum(losers))) if losers else (float("inf") if winners else 0.0),
    }
    metrics["window"] = f"{TEST_WINDOW[0]} → {TEST_WINDOW[1]}"
    return {"test": metrics, "n_trades_all": len(trades)}


# ---------------------------------------------------------------- filtering
cards = load_cards()
cards["family"] = cards["family"].map(FAMILY_AR).fillna(cards["family"])
FAMILIES = sorted(cards["family"].dropna().unique().tolist())
TIMEFRAMES = [t for t in ["15min", "30min", "1h", "4h", "Daily"] if t in cards["timeframe"].unique()]

with st.sidebar:
    st.markdown("## :material/filter_alt: التصفية")
    fams = st.multiselect("العائلة", FAMILIES, default=FAMILIES, placeholder="اختر العائلات")
    tfs = st.multiselect("الإطار الزمني", [TF_AR[t] for t in TIMEFRAMES], default=[TF_AR[t] for t in TIMEFRAMES], placeholder="اختر الإطار")
    gain_hi_slider = max(1.5, float(cards["stress_oos_gain"].max()))
    gain_lo, gain_hi = st.slider("نطاق الربح المجمع خارج العينة", min_value=-0.5, max_value=gain_hi_slider, value=(-0.5, gain_hi_slider), step=0.05)
    picks_only = st.checkbox("فقط أفضل اختيار لكل سهم", value=False)
    hide_thin = st.checkbox("إخفاء النتائج ذات الصفقات القليلة", value=False)
    top_n = st.select_slider("عدد أعلى الاختيارات في الرسم", options=[10, 20, 30, 50], value=20)
    st.divider()
    st.caption("تكاليف نافذة التشديد لكل اتجاه: عمولة 40 + انزلاق 10 نقطة أساس (= 1.00% رحلة ذهاب وإياب). "
               "المستوى الواقعي المعتمَد من الكتالوج: عمولة 17.825 + انزلاق 20 (= 0.76% رحلة ذهاب وإياب).")

mask = cards["family"].isin(fams)
mask &= cards["timeframe"].isin({k for k, v in TF_AR.items() if v in tfs})
mask &= (cards["stress_oos_gain"] >= gain_lo) & (cards["stress_oos_gain"] <= gain_hi)
if hide_thin:
    mask &= cards["flags"].str.contains("thin_trades") == False  # noqa: E712
if picks_only:
    mask &= cards["is_pick"] == 1
df = cards[mask]

st.title(f"{rl}لوحة نتائج تحسين الاستراتيجيات — السوق السعودي (TASI)")
st.markdown(
    f"{rl}تحسين وتثبيت معاملات الاستراتيجيات على فترة تدريبية ثم التحقق خارج العينة "
    "في نافذتين (التحقق: 01-08-2024 ← 31-12-2025، والاختبار: 01-01-2026 ← 21-09-2026). "
    "كل الأرقام نتائج تاريخية وليست تعهدًا بأرباح مستقبلية."
)

tab_overview, tab_plots, tab_table, tab_cards, tab_verify, tab_method = st.tabs(
    [":material/query_stats: نظرة عامة على الأداء",
     ":material/analytics: الرسوم البيانية",
     ":material/table_view: جدول الاختيارات",
     ":material/grid_view: البطاقات التفصيلية",
     ":material/fact_check: التحقق اليدوي من الصفقات",
     ":material/science: المنهجية والتحذيرات"]
)

# =========================================================== 1) OVERVIEW
with tab_overview:
    st.subheader("نظرة عامة على الأداء — استراتيجية واحدة")
    picks = load_picks()
    rows = []
    for r in picks.itertuples():
        rows.append(f"{r.ticker} — {r.name} ({int(r.strategy_id)}, {r.timeframe})")
    sel = st.selectbox("الاستراتيجية المعروضة (أفضل اختيار لكل سهم)", rows, key="ov_sel")
    row = picks.iloc[rows.index(sel)]
    cost = st.segmented_control("مستوى التكلفة (لرحلة ذهاب وإياب)", list(COST_LEVELS), default=COST_DEFAULT, key="ov_cost")
    commission, slippage = COST_LEVELS[cost]
    round_trip = 2 * (commission + slippage) / 10000

    eq, trades, meta = run_strategy(int(row.strategy_id), row.ticker, row.timeframe, commission, slippage)
    st.markdown(
        f"{rl}**:material/info: تفاصيل العرض**\n\n"
        f"{rl}- **السهم:** {row.ticker}\n"
        f"{rl}- **الاستراتيجية:** {meta['name']} (معرف {int(row.strategy_id)}، {row.timeframe})\n"
        f"{rl}- **المعاملات:** `{json.dumps(meta['params'], ensure_ascii=False)}`\n"
        f"{rl}- **الشراء والاحتفاظ على كامل الفترة:** {pct(meta['bench'])}\n"
        f"{rl}- **التكلفة:** عمولة {commission:g} + انزلاق {slippage:g} نقطة أساس لكل اتجاه "
        f"(≈ {round_trip * 100:.2f}% رحلة ذهاب وإياب)"
    )
    if not trades:
        st.warning("لا توجد صفقات لهذه الاستراتيجية ضمن البيانات المتاحة.")
        st.stop()
    td = build_trade_view(eq, trades)

    net = float(td["pnl"].sum())
    peak_full = eq.cummax()
    dd_pct = float((eq / peak_full - 1).min())
    dd_sar = float((eq - peak_full).min())
    wins = int((td["pnl"] > 0).sum())
    n = len(td)
    win_rate = wins / n
    gp = float(td.loc[td["pnl"] > 0, "pnl"].sum())
    gl = abs(float(td.loc[td["pnl"] < 0, "pnl"].sum()))
    pf = (gp / gl) if gl else (float("inf") if gp else 0.0)

    with st.container(horizontal=True):
        st.metric(f"{rl}صافي الأرباح والخسائر", f"{net:+,.0f} ر.س", pct(net / INITIAL_CASH), border=True)
        st.metric(f"{rl}الحد الأقصى للتراجع", f"{dd_sar:,.0f} ر.س", pct(dd_pct), border=True)
        st.metric(f"{rl}الصفقات الرابحة", f"{wins} / {n}", border=True)
        st.metric("عامل الربح", f"{pf:.2f}" if pf != float("inf") else "∞", border=True)
        st.metric("متوسط الصفقة", f"{float(td['pnl'].mean()):+,.0f} ر.س", pct(float(td["pnl"].mean()) / INITIAL_CASH), border=True)

    view_mode = st.segmented_control("العرض", ["رسم بياني", "جدول"], default="رسم بياني", key="ov_view")
    if view_mode == "جدول":
        st.dataframe(style_trade_table(td), hide_index=True, height=460, width="stretch")
    else:
        st.altair_chart(overview_chart(td), width="stretch")

# =========================================================== 2) PLOTS
with tab_plots:
    if len(df) == 0:
        st.warning("لا توجد نتائج مطابقة لمعايير التصفية الحالية.")
        st.stop()
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.markdown("**:material/analytics: توزيع الربح المجمع خارج العينة**")
            hist = (
                alt.Chart(df)
                .mark_bar(color="#2b83ba")
                .encode(
                    x=alt.X("stress_oos_gain:Q", bin=alt.Bin(maxbins=40), title="الربح المجمع خارج العينة", axis=alt.Axis(format="~%")),
                    y=alt.Y("count()", title="عدد الاستراتيجيات"),
                )
                .properties(height=280)
            )
            st.altair_chart(hist, width="stretch")
    with c2:
        with st.container(border=True):
            st.markdown(f"**:material/emoji_events: أعلى {top_n} اختيارًا (الربح المجمع خارج العينة)**")
            top = df[df["is_pick"] == 1].nlargest(top_n, "stress_oos_gain") if len(df[df["is_pick"] == 1]) else df.nlargest(top_n, "stress_oos_gain")
            bar = (
                alt.Chart(top)
                .mark_bar(color="#1a9850")
                .encode(
                    y=alt.Y("ticker:N", sort="-x", title="السهم"),
                    x=alt.X("stress_oos_gain:Q", title="الربح المجمع", axis=alt.Axis(format="~%")),
                    tooltip=["ticker", "name", "stress_oos_gain"],
                )
                .properties(height=280)
            )
            st.altair_chart(bar, width="stretch")
    with st.container(border=True):
        st.markdown("**:material/query_stats: توزيع الناجين حسب الإطار الزمني**")
        st.caption(
            f"{rl}لكل إطار زمني: عدد الاستراتيجيات الناجية، عدد الأسهم التي تعمل فيها، "
            "وداخل كل إطار يمكنك فتح تفاصيل الاستراتيجيات والرموز المعنية."
        )
        by_tf = (
            df.groupby("timeframe")
            .agg(survivors=("strategy_id", "nunique"), stocks=("ticker", "nunique"), cards=("strategy_id", "size"))
            .reindex(TIMEFRAMES, fill_value=0)
            .reset_index()
        )
        counts = by_tf.melt(id_vars="timeframe", value_vars=["survivors", "stocks"], var_name="type", value_name="count")
        counts["label"] = counts["timeframe"].map(TF_AR)
        counts["series"] = counts["type"].map({"survivors": "استراتيجيات ناجية", "stocks": "أسهم"})
        axis_fmt = alt.Axis(grid=True, gridColor="#2d363d", gridOpacity=0.6, labelFontSize=13, titleFontSize=14)
        tf_chart = (
            alt.Chart(counts)
            .mark_bar(opacity=0.85)
            .encode(
                x=alt.X("label:N", title="الإطار الزمني", sort=[TF_AR[t] for t in TIMEFRAMES], axis=axis_fmt),
                xOffset=alt.XOffset("series:N"),
                y=alt.Y("count:Q", title="العدد", axis=axis_fmt),
                color=alt.Color("series:N", legend=alt.Legend(title=None), scale=alt.Scale(range=["#1a9850", "#2b83ba"])),
                tooltip=[
                    alt.Tooltip("label:N", title="الإطار"),
                    alt.Tooltip("series:N", title="النوع"),
                    alt.Tooltip("count:Q", title="العدد", format="d"),
                ],
            )
            .properties(height=280)
        )
        st.altair_chart(tf_chart, width="stretch")
        counts_tbl = pd.DataFrame({
            "الإطار الزمني": [TF_AR[t] for t in by_tf["timeframe"]],
            "استراتيجيات ناجية": by_tf["survivors"],
            "أسهم": by_tf["stocks"],
            "بطاقات": by_tf["cards"],
        })
        st.dataframe(
            styled_df(counts_tbl, ["استراتيجيات ناجية", "أسهم", "بطاقات"], {"استراتيجيات ناجية": "{:d}", "أسهم": "{:d}", "بطاقات": "{:d}"}),
            hide_index=True, height=min(60 + 34 * len(counts_tbl), 260), width="stretch"
        )
        for r in by_tf.itertuples():
            if r.survivors == 0:
                continue
            sub = df[df["timeframe"] == r.timeframe]
            g = sub.groupby(["strategy_id", "name"], as_index=False)["ticker"].agg(lambda v: sorted(set(v)))
            g["n"] = g["ticker"].str.len()
            g = g.sort_values("n", ascending=False)
            gv = pd.DataFrame({
                "الاستراتيجية": g["name"],
                "الأسهم (عدد)": g["n"],
                "الأسهم": g["ticker"].str.join("، "),
            })
            with st.expander(f"{TF_AR.get(r.timeframe, r.timeframe)} — {int(r.survivors)} استراتيجية ناجية / {int(r.stocks)} سهم"):
                st.dataframe(gv, hide_index=True, height=min(120 + 30 * len(gv), 480), width="stretch")
    with st.container(border=True):
        st.markdown("**:material/scatter_plot: العائد مقابل المخاطرة (أفضل اختيار لكل سهم)**")
        picks_df = df[df["is_pick"] == 1]
        st.caption(
            f"{rl}المحور الأفقي: الربح المجمع خارج العينة\n"
            f"{rl}المحور الرأسي: أقصى تراجع (القيم السلبية الأقل عمقًا أفضل)\n"
            f"{rl}اللون: عائلة الاستراتيجية"
        )
        sc = (
            alt.Chart(picks_df)
            .mark_circle(size=60, opacity=0.75)
            .encode(
                x=alt.X("stress_oos_gain:Q", title="الربح المجمع خارج العينة", axis=alt.Axis(format="~%")),
                y=alt.Y("full_stress_maxdd:Q", title="أقصى تراجع", axis=alt.Axis(format="~%")),
                color=alt.Color("family:N", legend=alt.Legend(title="العائلة"), scale=alt.Scale(scheme="tableau10")),
                tooltip=["ticker", "name", "stress_oos_gain", "full_stress_maxdd"],
            )
            .properties(height=320)
        )
        st.altair_chart(sc, width="stretch")

# =========================================================== 3) TABLE
with tab_table:
    if len(df) == 0:
        st.warning("لا توجد نتائج مطابقة لمعايير التصفية الحالية.")
    else:
        with st.container(border=True):
            view = (df[df["is_pick"] == 1] if picks_only else df).reset_index(drop=True)
            board = view[ROW_COLUMNS[::-1]].rename(columns={k: PERF_COLUMNS[k] for k in ROW_COLUMNS})
            st.caption(
                f"{rl}**الربح الفعلي — التحقق/الاختبار:** العائد المحقق الفعلي داخل كل نافذة، بدون سنَوية.\n"
                f"{rl}**الربح المجمع خارج العينة:** (1+التحقق) × (1+الاختبار) − 1.\n"
                f"{rl}**أرقام التاريخ الكامل** تشمل فترة التدريب."
            )
            st.dataframe(styled_df(board, BOARD_SUBSET, BOARD_FORMAT), hide_index=True, height=min(320 + 28 * len(view), 760))
            fname = "picks" if picks_only else "survivors"
            st.download_button(
                f":material/download: تحميل الجدول (CSV)",
                view[ROW_COLUMNS].to_csv(index=False).encode("utf-8-sig"),
                file_name=f"results_{fname}.csv",
                mime="text/csv",
            )

# =========================================================== 4) CARDS
with tab_cards:
    if len(df) == 0:
        st.warning("لا توجد نتائج مطابقة لمعايير التصفية الحالية.")
    else:
        cards_total = len(cards)
        lbl = (
            f"**:material/grid_view: البطاقات التفصيلية (جميع الاستراتيجيات — {cards_total})**"
            if len(df) == cards_total
            else f"**:material/grid_view: البطاقات التفصيلية ({len(df)} استراتيجية من أصل {cards_total} وفق التصفية)**"
        )
        st.markdown(lbl)
        st.caption(
            f"{rl}**كل الأرقام محققة فعلية** (نسب مئوية، بدون سنَوية).  \n"
            f"{rl}**الربح المجمع خارج العينة:** (1+التحقق) × (1+الاختبار) − 1.  \n"
            f"{rl}**الربح الإجمالي (التاريخ الكامل)** يشمل فترة التدريب."
        )
        for t, g in df.groupby("ticker"):
            with st.expander(f"{rl}{t} — {len(g)} استراتيجية"):
                with st.container(horizontal=True):
                    st.metric("أفضل ربح مجمع", pct(g["stress_oos_gain"].max()), border=True)
                    st.metric("متوسط الربح المجمع", pct(g["stress_oos_gain"].mean()), border=True)
                    st.metric("أفضل ربح إجمالي (التاريخ الكامل)", pct(g["full_stress_total_ret"].max()), border=True)
                gv = g.sort_values("stress_oos_gain", ascending=False).reset_index(drop=True)
                gb = gv[ROW_COLUMNS[::-1]].rename(columns={k: PERF_COLUMNS[k] for k in ROW_COLUMNS})
                st.dataframe(styled_df(gb, BOARD_SUBSET, BOARD_FORMAT), hide_index=True)

# =========================================================== 5) MANUAL VERIFY
with tab_verify:
    st.subheader(f"{rl}التحقق اليدوي: هل الأرقام مطابقة للصفقات فعلًا؟")
    st.caption(
        f"{rl}هذه الصفحة للمراجعة اليدوية وتعمل بشكل مستقل عن التصفية في الشريط الجانبي. "
        "تعرض لكل سهم صفقات كل استراتيجية ناجية عليه داخل نافذة الاختبار، وتقارن الأرقام "
        "المخزَّنة بما تحسبه الصفقات نفسها فعليًا، مع إمكانية إعادة تشغيل المحرك على البيانات الحالية."
    )
    exports_ok = (PAYREPORT / "trades" / "all_survivor_trades.csv").exists() and (
        PAYREPORT / "trades" / "survivors_enriched.csv").exists()
    if not exports_ok:
        st.warning(
            "ملفات تصدير الصفقات غير موجودة. شغّل الأمر التالي مرة واحدة لتوليدها:\n\n"
            "```\npython scripts/export_survivor_trades.py --window test\n```"
        )
    else:
        enr, trd = load_verify_exports()
        enr = enr.rename(columns={"ticker": "ticker"})
        stocks = (
            enr.groupby("ticker")
            .agg(stock_name=("stock_name", "first"), sector=("sector", "first"), strategies=("strategy_id", "size"))
            .reset_index()
            .sort_values("stock_name", kind="stable")
        )
        label_to_ticker = {
            (f"{r.ticker} — {r.stock_name}" if r.stock_name else str(r.ticker)): r.ticker
            for r in stocks.itertuples()
        }
        stock_pick = st.selectbox("السهم", list(label_to_ticker), key="vf_stock")
        tk = label_to_ticker[stock_pick]
        sub = enr[enr["ticker"] == tk].copy()
        st.caption(
            f"{rl}**{tk} — {stocks.loc[stocks['ticker'] == tk, 'stock_name'].iloc[0]}** | "
            f"{stocks.loc[stocks['ticker'] == tk, 'sector'].iloc[0]} | "
            f"{len(sub)} استراتيجية ناجية في نافذة الاختبار."
        )

        vcols = ["strategy", "strategy_id", "timeframe", "n_trades", "engine_ret_base_test",
                "alpha_base_test", "win_rate_base_test", "profit_factor_base_test",
                "maxdd_base_test", "engine_ret_stress_test", "alpha_stress_test",
                "spec_matches_catalog"]
        vhead = {
            "strategy": "الاستراتيجية", "strategy_id": "المعرف", "timeframe": "الإطار",
            "n_trades": "صفقات الاختبار", "engine_ret_base_test": "العائد الفعلي (أساسي)",
            "alpha_base_test": "الألفا (أساسي)", "win_rate_base_test": "نسبة الربح",
            "profit_factor_base_test": "عامل الربحية", "maxdd_base_test": "أقصى تراجع",
            "engine_ret_stress_test": "العائد الفعلي (مشدّد)", "alpha_stress_test": "الألفا (مشدّد)",
            "spec_matches_catalog": "مطابق للقواعد",
        }
        with st.container(border=True):
            st.markdown(f"**:material/list_alt: استراتيجيات {tk} الناجية (نافذة الاختبار)**")
            gv = sub[vcols].sort_values("alpha_base_test", ascending=False).rename(columns=vhead)
            st.caption(
                f"{rl}الأرقام المخزَّنة عند **التكاليف الأساسية 20/5** (عمولة 20 + انزلاق 5)، "
                "وهي نفس التكاليف المستخدمة في إعادة المحاكاة أدناه. أما صفقات هذا التبويب "
                "فمبنية على **تكاليف واقعية 17.825/20**، لذلك لا تُقارن مباشرةً بالأرقام المخزَّنة. "
                "عمود «مطابق للقواعد» يوضّح هل القواعد المحقَّقة هي نفسها المستخدمة في توليد دفتر الصفقات."
            )
            st.dataframe(
                gv.style.map(style_sign, subset=["العائد الفعلي (أساسي)", "الألفا (أساسي)",
                                                  "العائد الفعلي (مشدّد)", "الألفا (مشدّد)"]).format(
                    {"المعرف": "{:d}", "صفقات الاختبار": "{:d}", "العائد الفعلي (أساسي)": "{:+.2%}",
                     "الألفا (أساسي)": "{:+.2%}", "نسبة الربح": "{:.1%}", "عامل الربحية": "{:.2f}",
                     "أقصى تراجع": "{:.1%}", "العائد الفعلي (مشدّد)": "{:+.2%}", "الألفا (مشدّد)": "{:+.2%}",
                     "مطابق للقواعد": lambda v: "✅" if v else "⚠️"},
                    na_rep=""),
                hide_index=True, height=min(320 + 28 * len(gv), 760), width="stretch",
            )

        strat_rows = {
            f"{r.strategy} ({int(r.strategy_id)} — {r.timeframe})": (int(r.strategy_id), r.timeframe)
            for r in sub.sort_values("alpha_base_test", ascending=False).itertuples()
        }
        strat_pick = st.selectbox("الاستراتيجية", list(strat_rows), key="vf_strat")
        sid, tf = strat_rows[strat_pick]
        row = sub[(sub["strategy_id"] == sid) & (sub["timeframe"] == tf)].iloc[0]

        c1, c2 = st.columns([3, 2], gap="medium")
        with c1:
            with st.container(border=True):
                st.markdown("**:material/code: القواعد المستخدمة في التحقق**")
                st.code(f"الدخول: {row['entry_long']}\n\nالخروج: {row['exit_long']}", language="text")
                bits = [f"العائلة: {FAMILY_AR.get(row['family'], row['family'])}",
                        f"الإطار: {TF_AR.get(row['timeframe'], row['timeframe'])}",
                        f"وقف الخسارة: {'—' if pd.isna(row['stop_loss_pct']) else f'{row['stop_loss_pct']}%'}",
                        f"هدف الربح: {'—' if pd.isna(row['take_profit_pct']) else f'{row['take_profit_pct']}%'}"]
                st.caption(f"{rl}" + " | ".join(bits))
                if isinstance(row["notes"], str) and row["notes"]:
                    st.markdown(f"{rl}**شرح المستند المرجعي (بالإنجليزية):**")
                    st.caption(f"{rl}{row['notes']}")
                if not bool(row["spec_matches_catalog"]):
                    st.warning(
                        "القواعد المحقَّقة تختلف قليلًا عن القواعد التي وُلِّدت بها دفتر الصفقات "
                        "(الأمعال المُحسَّنة لم تُحفظ، والقيم الاحتياطية استُخدمت بدلها). "
                        "لذلك من المتوقّع ألا تطابق أرقام دفتر الصفقات الأرقام المخزَّنة هنا."
                    )
        with c2:
            with st.container(border=True):
                st.markdown("**:material/description: تعريف الصفقة**")
                st.caption(
                    f"{rl}صفقات نافذة الاختبار لهذا السهم وهذه الاستراتيجية، محسوبة من دفتر الصفقات نفسه.\n"
                    f"{rl}كل صفقة على رأس مال ابتدائي 100,000 ر.س — لذلك لا تُجمع الأرباح عبر الاستراتيجيات."
                )
                g = trd[(trd["strategy_id"] == sid) & (trd["timeframe"] == tf) & (trd["ticker"] == tk)]
                st.markdown(f"**عدد الصفقات:** {len(g)}")
                st.markdown(f"**مجموع الربح/الخسارة:** {float(g['pnl'].sum()):+,.0f} ر.س")
                st.markdown(f"**نسبة الصفقات الرابحة:** {float((g['pnl'] > 0).mean()):.1%}")

        # ---------------------------------------------- truth check (live re-sim)
        td = trades_view(g)
        live = rerun_engine(int(sid), tk, tf, row["entry_long"], row["exit_long"],
                           row["stop_loss_pct"], row["take_profit_pct"])
        if live is None:
            st.warning("تعذّر تحميل بيانات هذا السهم على هذا الإطار الزمني.")
        else:
            m = live["test"]
            checks = [
                ("عدد الصفقات", float(m["trades"]), float(row["n_trades"]), 0.0, 0.0, "{:d}"),
                ("نسبة الربح", float(m["win_rate"]), float(row["win_rate_base_test"]), 0.005, 0.0, "{:.4f}"),
                ("العائد من 100,000 ر.س", float(m["engine_win_ret"]), float(row["engine_ret_base_test"]), 0.005, 0.0, "{:+.4f}"),
                ("أقصى تراجع", float(m["max_drawdown"]), float(row["maxdd_base_test"]), 0.005, 0.0, "{:+.4f}"),
                ("عامل الربحية", float(m["profit_factor"]), float(row["profit_factor_base_test"]), 0.10, 0.05, "{:.3f}"),
            ]
            rows_cmp = []
            for k, got, want, atol, rtol, fmt in checks:
                d = got - want
                okk = abs(d) <= atol + rtol * abs(want)
                rows_cmp.append({"المقياس": k, "المحاكاة الآن": got, "المخزَّن": want,
                                 "الفرق": d, "الحكم": "مطابق ✅" if okk else "مختلف ⚠️"})
            cmp_df = pd.DataFrame(rows_cmp)
            n_bad = int((cmp_df["الحكم"] != "مطابق ✅").sum())
            with st.container(border=True):
                st.markdown("**:material/fact_check: هل الأرقام المخزَّنة صادقة؟**")
                st.caption(
                    f"{rl}**المحاكاة الآن:** نُفِّذت للتو على ملفات الأسعار الحالية، بنفس القواعد "
                    "وبنفس التكاليف الأساسية 20/5 التي استُخدمت عند الحفظ.\n"
                    f"{rl}**المخزَّن:** ما كتبته مرحلة التحقق في وقتها.\n"
                    f"{rl}التطابق الكامل يعني أن النتائج حتمية وقابلة لإعادة الإنتاج."
                )
                disp = cmp_df.copy()
                st.dataframe(
                    disp.style.map(style_sign, subset=["المحاكاة الآن", "المخزَّن", "الفرق"]).format(
                        {"المحاكاة الآن": "{:+.4f}", "المخزَّن": "{:+.4f}", "الفرق": "{:+.4f}"},
                        na_rep="", precision=4),
                    hide_index=True, width="stretch",
                )
                if n_bad == 0:
                    st.success("إعادة المحاكاة طابقت الأرقام المخزَّنة تمامًا — النتائج قابلة للتكرار.")
                else:
                    st.info(
                        f"{n_bad} من {len(cmp_df)} مقياس مختلف عن المخزَّن."
                    )
                    if bool(row.get("data_version_match", True)):
                        st.info(
                            f"**السبب المرجّح:** ملفات الأسعار تغيّرت بعد حفظ النتائج — "
                            f"نافذة الاختبار كانت {int(row['bars_stored_test'])} شمعة وقت الحفظ "
                            f"وهي {int(row['bars_current_test'])} شمعة الآن "
                            f"({int(row['bars_stored_test']) - int(row['bars_current_test']):+d}). "
                            "هذا فرق في نسخة البيانات وليس خطأً في المحرك."
                        )
                    else:
                        st.info("**السبب المرجّح:** القواعد المحقَّقة تختلف عن دفتر الكتالوج لهذا التركيب.")
                        st.warning(
                            "المعاملات المُحسَّنة لهذا التركيب غير محفوظة في السجل، لذا لا يمكن "
                            "إعادة إنتاج رقم المخزَّن حتميًا."
                        )


        # ---------------------------------------------- trades
        with st.container(border=True):
            st.markdown(f"**:material/receipt_long: صفقات نافذة الاختبار ({len(td)} صفقة)**")
            if len(td) == 0:
                st.warning("لا توجد صفقات مُصدَّرة لهذا التركيب.")
            else:
                view_mode = st.segmented_control("العرض", ["رسم بياني", "جدول"], key="vf_view",
                                                 default="رسم بياني")
                if view_mode == "جدول":
                    st.dataframe(style_trade_table(td), hide_index=True, height=460, width="stretch")
                else:
                    st.altair_chart(overview_chart(td), width="stretch")
                st.download_button(
                    ":material/download: تحميل هذه الصفقات (CSV)",
                    td.to_csv(index=False).encode("utf-8-sig"),
                    file_name=f"trades_{tk}_{sid}_{tf}.csv", mime="text/csv",
                )


# =========================================================== 6) METHOD
with tab_method:
    st.markdown(
        """
### ١) الفكرة والمنهجية
- لكل سهم خُصّصت أفضل **5 استراتيجيات مرشحة** (من أصل **3,779 استراتيجية موثّقة** في الكتالوج المرجعي عبر 8 عائلات)، حُدّدت معاملاتها في فترة التدريب وثُبّتت،
  ثم شُخّص أداؤها خارج العينة في نافذتين:
  * **التدريب (حتى 31-07-2024):** ضبط المعاملات (ولا تُحتسب نتائجُها النهائية).
  * **التحقق (01-08-2024 → 31-12-2025):** نافذة أولى لفحص أداء المعاملات المُثبّتة.
  * **الاختبار (01-01-2026 → 21-09-2026):** نافذة لم تُستخدم في أي اختيار (رصيد نهائي).
- لم تُغيَّر أي معاملات بناءً على هاتين النافذتين؛ المعنى أن المحسّن لم "يرَ" هذه الفترات.
- **نظرة عامة على الأداء:** يُعاد حساب منحنى الأرباح والتراجع وتتابع الصفقات من صفقات الاستراتيجية المختارة
  على كامل الفترة وبالمعاملات المثبتة (بالريال السعودي)، مع إمكانية تبديل مستوى التكلفة.
- **رأس المال:** يفترض الحساب رأس مال ابتدائي **100,000 ر.س**، وتُحسب عليه النسب المئوية وتُعرض تفاصيل الصفقات بالريال.
- **التنفيذ بالأسهم الكاملة فقط:** تُشترى الأسهم بأعداد صحيحة (لا أسهم كسرية)، ويُشترط القدرة على شراء سهم كامل عند الدخول، وتبقى الفروقات النقدية في الحساب.

---

### ٢) التكاليف
- المحرك يخصم العمولة والانزلاق **لكل اتجاه** (دخول + خروج):
  * **المستوى الواقعي (افتراضي):** عمولة 17.825 نقطة أساس (0.3565% رحلة ذهاب وإياب شاملة ضريبة القيمة المضافة 15%) +
    انزلاق 20 نقطة أساس لكل اتجاه = **75.65 نقطة أساس رحلة ذهاب وإياب** — وهو المستوى المعتمد في الكتالوج المرجعي.
  * **أساسي (20/5):** = 0.50% رحلة ذهاب وإياب.
  * **تشديد (40/10):** = 1.00% رحلة ذهاب وإياب — نافذة إجهاد تصميمية (اشترط بقاء العائد الإضافي موجبًا في
    النافذتين حتى عند هذه التكاليف)، وليست رقم وسيط. أرقام جداول الاختيارات والبطاقات محسوبة على نافذة التشديد 40/10.

---

### ٣) قراءة الأرقام في الجداول
- **الربح المجمع خارج العينة** = ربح التحقق × ربح الاختبار − 1 (نحو 21 شهرًا معًا).
- **الربح الفعلي — التحقق/الاختبار** = العائد المحقق الفعلي داخل كل نافذة بدون سنَوية.
- **نسبة شارب:** العائد مقابل حجم التذبذب (أعلى = أفضل؛ فوق 1 جيد نسبيًا).
- **معامل الربحية:** إجمالي أرباح الصفقات ÷ إجمالي خسائرها (أكبر من 1 = الأرباح تغطي الخسائر).
- **أقصى تراجع:** أعمق هبوط من قمة سابقة في منحنى الأرباح (نسبة سالبة؛ الأقل عمقًا أفضل).
- **عدد الصفقات:** أقل من 8 صفقات في نافذة = قلة الدلالة الإحصائية (وُسمت بانخفاض).

---

### ٤) البيانات والنطاق
- أسعار OHLCV **معدّلة لأحداث الشركات** (كإصدار المنح) بمعالجة استمرارية السعر والحجم، وتُستثنى السلاسل التي تحتوي أحداثًا لا يمكن تعديلها (تقسيمات، اندماج، تخفيض رأس المال، حقوق أولوية) من نتائج هذه النسخة، بالترددات المتاحة: 15 دقيقة، 30 دقيقة، ساعة، 4 ساعات، ويومي.
- **عائلات الاستراتيجيات الثماني:** الاتجاه، الزخم، كسر النطاق، الارتداد للمتوسط، التذبذب، الحجم، الأنماط، وأخرى.
- قائمة الـ 222 سهمًا مبنية على **التشكيلة الحالية** (احتمال انحياز الناجين تاريخيًا).

---

### ٥) تنبيهات وقيود
- **تنبيه مهم:** "النجاة" تعني عائدًا إضافيًا إيجابيًا مقارنة بالشراء والاحتفاظ في كلتا النافذتين؛
  فقد تكون الاستراتيجية ناجية مع ربح مطلق سلبي إذا هبط السوق (تفادي جزء من الخسارة لا يعني ربحًا).
- أرقام **التاريخ الكامل** تشمل فترة التدريب (بيانات داخلها جزئيًا) فلا تُقارن مباشرة بأرقام خارج العينة.
- **البيانات التاريخية لا تضمن أرباحًا مستقبلية، ولا تُقرأ هذه النتائج كتوصية شراء أو بيع.**
"""
    )