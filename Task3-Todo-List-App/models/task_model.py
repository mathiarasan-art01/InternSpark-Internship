import os
import sqlite3
from flask import current_app, g
def get_db() -> sqlite3.Connection:
    if "db" not in g:
        conn = sqlite3.connect(current_app.config["DATABASE_PATH"])
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        g.db = conn
    return g.db
def close_db(_exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
def init_db() -> None:
    os.makedirs(current_app.config["DATABASE_DIR"], exist_ok=True)
    schema_path = current_app.config["SCHEMA_PATH"]
    conn = sqlite3.connect(current_app.config["DATABASE_PATH"])
    with open(schema_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
# --- Task queries -----------------------------------------------------------
def list_tasks(status: str = "all", category: str = "all", query: str = "") -> list[sqlite3.Row]:
    sql = "SELECT * FROM tasks WHERE 1=1"
    params: list = []
    if status == "active":
        sql += " AND completed = 0"
    elif status == "completed":
        sql += " AND completed = 1"
    if category and category != "all":
        sql += " AND category = ?"
        params.append(category)
    if query:
        sql += " AND (title LIKE ? OR description LIKE ?)"
        like = f"%{query}%"
        params.extend([like, like])
    sql += (
        " ORDER BY completed ASC,"
        " CASE priority WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END,"
        " datetime(created_at) DESC"
    )
    return get_db().execute(sql, params).fetchall()
def get_task(task_id: int) -> sqlite3.Row | None:
    return get_db().execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
def create_task(data: dict) -> int:
    db = get_db()
    cur = db.execute(
        "INSERT INTO tasks (title, description, category, priority, due_date) "
        "VALUES (?, ?, ?, ?, ?)",
        (
            data.get("title", "").strip(),
            (data.get("description") or "").strip(),
            data.get("category") or "General",
            data.get("priority") or "Medium",
            data.get("due_date") or None,
        ),
    )
    db.commit()
    return cur.lastrowid
def update_task(task_id: int, data: dict) -> None:
    db = get_db()
    db.execute(
        "UPDATE tasks SET title=?, description=?, category=?, priority=?, due_date=?,"
        " updated_at=CURRENT_TIMESTAMP WHERE id=?",
        (
            data.get("title", "").strip(),
            (data.get("description") or "").strip(),
            data.get("category") or "General",
            data.get("priority") or "Medium",
            data.get("due_date") or None,
            task_id,
        ),
    )
    db.commit()
def toggle_task(task_id: int) -> None:
    db = get_db()
    row = db.execute("SELECT completed FROM tasks WHERE id=?", (task_id,)).fetchone()
    if row:
        db.execute(
            "UPDATE tasks SET completed=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
            (0 if row["completed"] else 1, task_id),
        )
        db.commit()
def delete_task(task_id: int) -> None:
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    db.commit()
# --- Note queries -----------------------------------------------------------
def list_notes() -> list[sqlite3.Row]:
    return get_db().execute(
        "SELECT * FROM notes ORDER BY datetime(created_at) DESC"
    ).fetchall()
def create_note(content: str, color: str = "mint") -> int:
    db = get_db()
    cur = db.execute("INSERT INTO notes (content, color) VALUES (?, ?)", (content, color))
    db.commit()
    return cur.lastrowid
def delete_note(note_id: int) -> None:
    db = get_db()
    db.execute("DELETE FROM notes WHERE id=?", (note_id,))
    db.commit()
