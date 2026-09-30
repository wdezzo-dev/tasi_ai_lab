# TASI AI Lab — Strategy Dashboard

Arabic (RTL) Streamlit dashboard for exploring validated trading-strategy picks across the
222-stock Saudi (Tadawul) universe.

## Run
```bash
pip install -r requirements.txt
streamlit run results/strategy_refine_v1/dashboard_ar/app.py
```

## Deployed entry point
`results/strategy_refine_v1/dashboard_ar/app.py`

- Tab 1 نظرة عامة — best pick per stock, equity/drawdown/trade charts from actual trades
- Tab 2 الرسوم البيانية — chart builder
- Tab 3 جدول الاختيارات — filterable results table
- Tab 4 البطاقات التفصيلية — detailed metric cards per stock
- Tab 5 المنهجية والتحذيرات — methodology, costs, and caveats

## Notes
- Timeframes: 15min, 30min, 1h, 4h, Daily. The repository ships the OHLCV files used by the
  current pick list (one file per picked ticker x timeframe) to keep the repo small.
- Prices are pre-adjusted for corporate actions (bonus shares, splits, rights, mergers) as of
  the 2026-09-30 run; `data/_exclusions.json` (`mode: preadjusted`) lists the (ticker, timeframe)
  pairs whose event history could not be resolved — those pairs are excluded from the analysis.
- Execution is whole-share only (fractional buys are not allowed); commissions 20 bps / slippage
  5 bps in the base case, 40/10 under stress.
- Historical backtests are not guarantees of future profitability. Not financial advice.