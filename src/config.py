from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass(frozen=True)
class Settings:
    root: Path
    data_dir: Path
    companies_csv: Path
    reference_catalog: Path
    reference_raw: Path
    results_dir: Path

    @classmethod
    def from_env(cls, root: str | None = None) -> "Settings":
        r = Path(root or os.getenv("TASI_LAB_ROOT", Path.cwd())).expanduser().resolve()
        return cls(
            root=r,
            data_dir=Path(os.getenv("TASI_DATA_DIR", r / "data")),
            companies_csv=Path(os.getenv("TASI_COMPANIES_CSV", r / "companies.csv")),
            reference_catalog=Path(os.getenv("TASI_REFERENCE_CATALOG", r / "reference_catalog.sqlite")),
            reference_raw=Path(os.getenv("TASI_REFERENCE_RAW", r / "reference_raw")),
            results_dir=Path(os.getenv("TASI_RESULTS_DIR", r / "results")),
        )
