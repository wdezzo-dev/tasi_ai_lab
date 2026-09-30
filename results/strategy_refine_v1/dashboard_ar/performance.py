import json
from typing import Any

import altair as alt
import pandas as pd
import streamlit as st

TEAL = "#14B8A6"
GREEN = "#22C55E"
RED = "#EF4444"
ORANGE = "#F59E0B"
INITIAL_CASH = 100_000.0


def build_trade_view(eq: pd.Series, trades: list[dict]) -> pd.DataFrame:
    td = pd.DataFrame(trades)
    if td.empty:
        return pd.DataFrame()
    td["exit_time"] = pd.to_datetime(td["exit_time"])
    td = td.sort_values("exit_time").reset_index(drop=True)
    td["trade_no"] = range(1, len(td) + 1)
    td["cum_pnl"] = td["pnl"].cumsum()
    td["cum_pos"] = td["cum_pnl"].clip(lower=0)
    td["cum_neg"] = td["cum_pnl"].clip(upper=0)
    td["win"] = td["pnl"] > 0
    td["result"] = td["pnl"].map(lambda v: "ربح" if v > 0 else ("خسارة" if v < 0 else "تعادل"))
    peak = eq.cummax()
    anchor = pd.DataFrame(
        {"equity": eq.values, "dd_ratio": (eq / peak - 1).values, "dd_sar": (eq - peak).values},
        index=eq.index,
    )
    return td.join(anchor, on="exit_time")


def overview_chart(td: pd.DataFrame) -> alt.VConcatChart:
    def mk_sel(name: str) -> alt.SelectionParameter:
        return alt.selection_point(
            encodings=["x"], nearest=True, on="mouseover", clear="mouseout", empty=False, name=name
        )

    nearest_main = mk_sel("cr_main")
    nearest_dd = mk_sel("cr_dd")
    nearest_bars = mk_sel("cr_bars")
    tt = [
        alt.Tooltip("exit_time:T", title="تاريخ الخروج"),
        alt.Tooltip("trade_no:Q", title="رقم الصفقة"),
        alt.Tooltip("pnl:Q", title="أرباح/خسارة (ر.س)", format=",.0f"),
        alt.Tooltip("cum_pnl:Q", title="الربح التراكمي (ر.س)", format=",.0f"),
        alt.Tooltip("result:N", title="النتيجة"),
        alt.Tooltip("qty:Q", title="الكمية", format=",.2f"),
        alt.Tooltip("reason:N", title="سبب الإغلاق"),
        alt.Tooltip("equity:Q", title="قيمة الحساب (ر.س)", format=",.0f"),
        alt.Tooltip("dd_ratio:Q", title="التراجع المرتبط", format="~%"),
    ]
    pad = pd.Timedelta(days=6)
    x_pad = alt.Scale(
        domain=[td["exit_time"].min() - pad, td["exit_time"].max() + pad],
        nice=False,
    )
    base = alt.Chart(td).encode(
        x=alt.X("exit_time:T", title="تاريخ خروج الصفقات", scale=x_pad),
        tooltip=tt,
    )

    def crosshair(sel: alt.SelectionParameter) -> alt.Chart:
        return alt.Chart(td).transform_filter(sel).mark_rule(
            color="#899499", strokeDash=[3, 3], strokeWidth=1
        ).encode(x="exit_time:T")

    base = alt.Chart(td).encode(
        x=alt.X("exit_time:T", title="تاريخ خروج الصفقات"),
        tooltip=tt,
    )

    y_axis = alt.Axis(
        format=",.0f", title="الربح التراكمي (ر.س)", titleColor=TEAL,
        grid=True, gridColor="#2d363d", gridOpacity=0.6, labelFontSize=13, titleFontSize=14,
    )

    equity = (
        base.mark_area(color=RED, opacity=0.18).encode(y=alt.Y("cum_neg:Q", axis=y_axis, stack=None))
        + base.mark_area(color=TEAL, opacity=0.18).encode(y=alt.Y("cum_pos:Q", axis=y_axis, stack=None))
        + base.mark_line(color=TEAL, strokeWidth=3, opacity=1).encode(y=alt.Y("cum_pnl:Q", axis=y_axis))
        + base.mark_circle(size=55).encode(
            y=alt.Y("cum_pnl:Q", axis=y_axis),
            color=alt.condition(alt.datum.pnl > 0, alt.value(GREEN), alt.value(RED)),
        )
    )
    main = (
        alt.layer(equity, crosshair(nearest_main))
        .add_params(nearest_main)
        .properties(title=alt.Title("\u200fالأداء التراكمي مع نتائج الصفقات (أخضر رابح / أحمر خاسر)", anchor="end", fontSize=15), height=300)
    )

    dd_chart = (
        alt.Chart(td)
        .mark_area(color=ORANGE, opacity=0.40, line={"color": ORANGE, "strokeWidth": 1.2})
        .encode(
            x=alt.X("exit_time:T", title=None, scale=x_pad),
            y=alt.Y("dd_ratio:Q", title="التراجع (%)", axis=alt.Axis(format="%", titleColor=ORANGE, grid=True, gridColor="#2d363d", gridOpacity=0.6, labelFontSize=12, titleFontSize=12)),
            tooltip=[alt.Tooltip("exit_time:T", title="تاريخ الخروج"),
                     alt.Tooltip("dd_ratio:Q", title="التراجع", format="~%"),
                     alt.Tooltip("dd_sar:Q", title="التراجع (ر.س)", format=",.0f")],
        )
        .add_params(nearest_dd)
    )
    dd_strip = alt.layer(dd_chart, crosshair(nearest_dd)).properties(title=alt.Title("\u200fالتراجع", anchor="end", fontSize=13), height=70)

    bar_axis = alt.Axis(
        format=",.0f", title="نتيجة الصفقة (ر.س)",
        grid=True, gridColor="#2d363d", gridOpacity=0.6, labelFontSize=12, titleFontSize=12,
    )
    zero_rule = (
        alt.Chart(pd.DataFrame({"z": [0.0]}))
        .mark_rule(color="#7f8c8d", strokeDash=[4, 4])
        .encode(y=alt.Y("z:Q", axis=bar_axis))
    )
    bars = (
        alt.Chart(td)
        .mark_bar(opacity=0.85, size=2.5)
        .encode(
            x=alt.X("exit_time:T", title="تاريخ خروج الصفقات", scale=x_pad),
            y=alt.Y("pnl:Q", axis=bar_axis),
            color=alt.condition(alt.datum.pnl > 0, alt.value(GREEN), alt.value(RED)),
            tooltip=tt,
        )
        .add_params(nearest_bars)
    )
    strip = alt.layer(bars, zero_rule, crosshair(nearest_bars)).properties(
        title=alt.Title("\u200fنتائج الصفقات الفردية (أخضر رابح / أحمر خاسر)", anchor="end", fontSize=14), height=90
    )

    return alt.vconcat(main, dd_strip, strip, spacing=6).resolve_scale(x="shared")


def style_sign(v, tint: bool = False) -> str:
    if pd.isna(v):
        return ""
    if v > 0:
        base = f"color: {GREEN}; font-weight: 600;"
        return base + " background-color: rgba(34,197,94,0.12);" if tint else base
    if v < 0:
        base = f"color: {RED}; font-weight: 600;"
        return base + " background-color: rgba(239,68,68,0.12);" if tint else base
    return "color: #9ca3af;"


def trade_detail_table(td: pd.DataFrame) -> pd.DataFrame:
    cols = ["trade_no", "exit_time", "side", "qty", "entry", "exit", "pnl", "fees", "reason", "cum_pnl", "equity"]
    out = td[cols[::-1]].copy()
    return out.rename(columns={
        "trade_no": "رقم", "exit_time": "تاريخ الخروج", "side": "الجانب", "qty": "الكمية",
        "entry": "دخول", "exit": "خروج", "pnl": "الربح/الخسارة", "fees": "الرسوم",
        "reason": "سبب الإغلاق", "cum_pnl": "التراكمي", "equity": "رصيد الحساب",
    })


TRADE_FORMAT = {
    "تاريخ الخروج": lambda v: v.strftime("%d-%m-%Y"),
    "الكمية": "{:,.2f}", "دخول": "{:,.2f}", "خروج": "{:,.2f}",
    "الربح/الخسارة": "{:+,.2f}", "الرسوم": "{:,.2f}",
    "التراكمي": "{:+,.2f}", "رصيد الحساب": "{:,.2f}",
}


def style_trade_table(td: pd.DataFrame):
    t = trade_detail_table(td)
    return t.style.map(style_sign, subset=["الربح/الخسارة", "التراكمي"]).format(TRADE_FORMAT, na_rep="")


def styled_df(df: pd.DataFrame, subset, fmt: dict, tint: bool = False):
    return df.style.map(style_sign, subset=subset).format(fmt, na_rep="")


TRADE_COL_DEF: dict[str, Any] = {
    "رقم": st.column_config.NumberColumn("رقم", format="%d"),
    "تاريخ الخروج": st.column_config.DatetimeColumn("تاريخ الخروج"),
    "الجانب": st.column_config.TextColumn("الجانب"),
    "الكمية": st.column_config.NumberColumn("الكمية", format="%.2f"),
    "دخول": st.column_config.NumberColumn("دخول", format="%.2f"),
    "خروج": st.column_config.NumberColumn("خروج", format="%.2f"),
    "الربح/الخسارة": st.column_config.NumberColumn("الربح/الخسارة (ر.س)", format="%+.2f"),
    "الرسوم": st.column_config.NumberColumn("الرسوم", format="%.2f"),
    "سبب الإغلاق": st.column_config.TextColumn("سبب الإغلاق"),
    "التراكمي": st.column_config.NumberColumn("التراكمي (ر.س)", format="%+.2f"),
    "رصيد الحساب": st.column_config.NumberColumn("رصيد الحساب (ر.س)", format="%.2f"),
}