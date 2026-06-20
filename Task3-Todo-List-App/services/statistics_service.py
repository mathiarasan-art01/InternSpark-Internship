"""Dashboard analytics aggregations."""
from models.task_model import get_db
def summary() -> dict:
    row = get_db().execute(
        "SELECT COUNT(*) AS total,"
        " SUM(CASE WHEN completed=1 THEN 1 ELSE 0 END) AS done"
        " FROM tasks"
    ).fetchone()
    total = row["total"] or 0
    done = row["done"] or 0
    pending = total - done
    pct = round((done / total) * 100) if total else 0
    return {"total": total, "done": done, "pending": pending, "pct": pct}
def by_category() -> list[dict]:
    rows = get_db().execute(
        "SELECT category, COUNT(*) AS n,"
        " SUM(CASE WHEN completed=1 THEN 1 ELSE 0 END) AS done"
        " FROM tasks GROUP BY category ORDER BY n DESC"
    ).fetchall()
    return [dict(r) for r in rows]
def by_priority() -> list[dict]:
    rows = get_db().execute(
        "SELECT priority, COUNT(*) AS n,"
        " SUM(CASE WHEN completed=1 THEN 1 ELSE 0 END) AS done"
        " FROM tasks GROUP BY priority"
    ).fetchall()
    order = {"High": 1, "Medium": 2, "Low": 3}
    return sorted([dict(r) for r in rows], key=lambda x: order.get(x["priority"], 9))
