"""Misc helper functions."""
from datetime import datetime
def parse_date(value: str | None):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace(" ", "T"))
    except Exception:
        return None
def safe_int(value, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default