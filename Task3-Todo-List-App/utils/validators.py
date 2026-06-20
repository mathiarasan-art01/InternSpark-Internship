"""Lightweight form validators."""
from .constants import PRIORITIES, CATEGORIES, MAX_TITLE_LEN, MAX_DESC_LEN
def validate_task_form(form) -> list[str]:
    errors: list[str] = []
    title = (form.get("title") or "").strip()
    if not title:
        errors.append("Title is required.")
    elif len(title) > MAX_TITLE_LEN:
        errors.append(f"Title must be ≤ {MAX_TITLE_LEN} characters.")
    if len((form.get("description") or "")) > MAX_DESC_LEN:
        errors.append(f"Description must be ≤ {MAX_DESC_LEN} characters.")
    priority = form.get("priority") or "Medium"
    if priority not in PRIORITIES:
        errors.append("Invalid priority.")
    category = form.get("category") or "General"
    if category not in CATEGORIES:
        errors.append("Invalid category.")
    return errors
