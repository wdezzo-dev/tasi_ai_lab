# Roster completion and validation report

- Complete roster files: **375/375** (`batch_001` through `batch_375`).
- Total roster entries: **3,750**.
- Missing batches filled: **143** batches / **1,430** entries (starting at batch 181, using the existing pool selections).
- Batches 181–375: **195/195** complete.
- Pool-selected IDs in batches 181–375: **1,950**, all unique, and each roster matches its pool IDs exactly and in order.
- DSL validation: **3,750/3,750** entry/exit expressions evaluated successfully against a synthetic OHLCV frame.
- Existing legacy duplicate IDs preserved: `7, 38, 55, 58, 91, 104, 115` (each appears twice).
- One pre-existing malformed DSL expression in `batch_006_roster.json` (ID 38) was corrected from `bb_mid(close,20,2)` to the valid `bb_mid(close,20)` signature while retaining the intended logic.
- Real TASI `validate_roster.py` validation was **not run**, because the archive intentionally excludes the OHLCV data directory required by that validator. The DSL/static checks therefore confirm structural correctness, not market-data correctness.
- Existing pool files were preserved; no new reference IDs were sampled.
