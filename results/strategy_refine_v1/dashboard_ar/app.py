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
    style_trade_table,
)
from src.backtest import BacktestConfig, _simulate  # noqa: E402
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
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"],
    [data-testid="stMetricDelta"] { direction: rtl; text-align: right; }
    [data-testid="stWidgetLabel"] { direction: rtl; text-align: right; }
    [data-testid="stHeader"] { direction: rtl; text-align: right; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] { direction: rtl; text-align: right; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] { direction: rtl; text-align: right; }
    [data-testid="stTabs"] { direction: rtl; }
    [data-testid="stExpander"] { direction: rtl; text-align: right; }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] { direction: rtl; }
    [data-testid="stVegaLiteChart"] { direction: ltr !important; overflow: hidden; }
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
    return f"{v * 100:.1f}%"


# ---------------------------------------------------------------- filtering
cards = load_cards()
FAMILIES = sorted(cards["family"].dropna().unique().tolist())
TIMEFRAMES = [t for t in ["15min", "30min", "1h", "4h", "Daily"] if t in cards["timeframe"].unique()]

with st.sidebar:
    st.markdown("## :material/filter_alt: التصفية")
    fams = st.multiselect("العائلة", [FAMILY_AR[f] for f in FAMILIES], default=[FAMILY_AR[f] for f in FAMILIES], placeholder="اختر العائلات")
    tfs = st.multiselect("الإطار الزمني", [TF_AR[t] for t in TIMEFRAMES], default=[TF_AR[t] for t in TIMEFRAMES], placeholder="اختر الإطار")
    gain_lo, gain_hi = st.slider("نطاق الربح المجمع خارج العينة", min_value=-0.5, max_value=1.5, value=(-0.5, 1.5), step=0.05)
    picks_only = st.checkbox("فقط أفضل اختيار لكل سهم", value=False)
    hide_thin = st.checkbox("إخفاء النتائج ذات الصفقات القليلة", value=False)
    top_n = st.select_slider("عدد أعلى الاختيارات في الرسم", options=[10, 20, 30, 50], value=20)
    st.divider()
    st.caption("تكاليف نافذة التشديد لكل اتجاه: عمولة 40 + انزلاق 10 نقطة أساس (= 1.00% رحلة ذهاب وإياب). "
               "المستوى الواقعي المعتمَد من الكتالوج: عمولة 17.825 + انزلاق 20 (= 0.76% رحلة ذهاب وإياب).")

mask = cards["family"].isin({k for k, v in FAMILY_AR.items() if v in fams})
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
    "في نافذتين (التحقق: 01-08-2024 → 31-12-2025، والاختبار: 01-01-2026 → 21-09-2026). "
    "كل الأرقام نتائج تاريخية وليست تعهدًا بأرباح مستقبلية."
)

tab_overview, tab_plots, tab_table, tab_cards, tab_method = st.tabs(
    [":material/query_stats: نظرة عامة على الأداء",
     ":material/analytics: الرسوم البيانية",
     ":material/table_view: جدول الاختيارات",
     ":material/grid_view: البطاقات التفصيلية",
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
    st.caption(
        f"{rl}السهم: {row.ticker} — الاستراتيجية: {meta['name']} (معرف {int(row.strategy_id)}, {row.timeframe}) "
        f"| المعاملات: `{json.dumps(meta['params'], ensure_ascii=False)}` | "
        f"الشراء والاحتفاظ على كامل الفترة: {pct(meta['bench'])} | التكلفة: عمولة {commission:g} + انزلاق {slippage:g} نقطة أساس لكل اتجاه (≈ {round_trip * 100:.2f}% رحلة ذهاب وإياب)"
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
        st.metric(f"{rl}الحد الأقصى للتراجع", f"{dd_sar:,.0f} ر.س", pct(dd_pct), delta_color="inverse", border=True)
        st.metric(f"{rl}الصفقات الرابحة", f"{wins} / {n}", pct(win_rate), border=True)
        st.metric("عامل الربح", f"{pf:.2f}" if pf != float("inf") else "∞", border=True)
        st.metric("متوسط الصفقة", f"{float(td['pnl'].mean()):+,.0f} ر.س", border=True)

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
        st.markdown("**:material/scatter_plot: العائد مقابل المخاطرة (أفضل اختيار لكل سهم)**")
        picks_df = df[df["is_pick"] == 1]
        st.caption("المحور الأفقي: الربح المجمع خارج العينة — المحور الرأسي: أقصى تراجع (قيمة سلبية أقل). اللون: عائلة الاستراتيجية.")
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
                f"{rl}الربح الفعلي — التحقق/الاختبار = العائد المحقق الفعلي داخل النافذة بدون سنَوية. "
                "الربح المجمع خارج العينة = (1+التحقق) × (1+الاختبار) − 1. "
                "أرقام التاريخ الكامل تشمل فترة التدريب."
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
        st.markdown(f"**:material/grid_view: البطاقات التفصيلية (جميع الاستراتيجيات — {len(df)})**")
        st.caption(
            f"{rl}كل الأرقام محققة فعلية (نسب مئوية، بدون سنَوية): "
            "الربح المجمع خارج العينة = (1+التحقق) × (1+الاختبار) − 1. "
            "الربح الإجمالي يشمل فترة التدريب."
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

# =========================================================== 5) METHOD
with tab_method:
    st.markdown(
        """
### ١) الفكرة والمنهجية
- لكل سهم خُصّصت أفضل **5 استراتيجيات مرشحة** (من أصل 2,935 عبر 8 عائلات)، حُدّدت معاملاتها في فترة التدريب وثُبّتت،
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