from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Any

class StrategyCatalog:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)

    def _conn(self):
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        return con

    def search(self, query: str, limit: int = 10, family: str | None = None) -> list[dict[str, Any]]:
        con = self._conn()
        try:
            q = query.strip()
            if family:
                sql = """
                SELECT s.* FROM strategies_fts f JOIN strategies s ON s.rowid=f.rowid
                WHERE strategies_fts MATCH ? AND s.family=? LIMIT ?
                """
                rows = con.execute(sql, (q, family, int(limit))).fetchall()
            else:
                rows = con.execute("""
                    SELECT s.* FROM strategies_fts f JOIN strategies s ON s.rowid=f.rowid
                    WHERE strategies_fts MATCH ? LIMIT ?
                """, (q, int(limit))).fetchall()
            return [dict(r) for r in rows]
        finally:
            con.close()

    def get(self, slug: str | None = None, strategy_id: int | None = None) -> dict[str, Any] | None:
        con = self._conn()
        try:
            if slug:
                r = con.execute("SELECT * FROM strategies WHERE slug=? LIMIT 1", (slug,)).fetchone()
            else:
                r = con.execute("SELECT * FROM strategies WHERE id=? ORDER BY rowid LIMIT 1", (strategy_id,)).fetchone()
            return dict(r) if r else None
        finally:
            con.close()

    def stats(self) -> dict[str, Any]:
        con = self._conn()
        try:
            total = con.execute("SELECT COUNT(*) FROM strategies").fetchone()[0]
            families = dict(con.execute("SELECT family, COUNT(*) FROM strategies GROUP BY family" ).fetchall())
            return {"total": total, "families": families}
        finally:
            con.close()
