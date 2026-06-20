-- TaskNest database schema
CREATE TABLE IF NOT EXISTS tasks (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT    NOT NULL,
    description  TEXT    DEFAULT '',
    category     TEXT    DEFAULT 'General',
    priority     TEXT    DEFAULT 'Medium',
    due_date     TEXT,
    completed    INTEGER DEFAULT 0,
    created_at   TEXT    DEFAULT CURRENT_TIMESTAMP,
    updated_at   TEXT    DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS notes (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    content    TEXT    NOT NULL,
    color      TEXT    DEFAULT 'mint',
    created_at TEXT    DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_tasks_completed ON tasks(completed);
CREATE INDEX IF NOT EXISTS idx_tasks_category  ON tasks(category);
