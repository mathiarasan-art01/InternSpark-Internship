"""Business-logic layer for tasks. Thin wrapper around the model today,
but a good seam to add notifications, audit logs, etc."""
from models import task_model
def add(data: dict) -> int:
    return task_model.create_task(data)
def update(task_id: int, data: dict) -> None:
    task_model.update_task(task_id, data)
def remove(task_id: int) -> None:
    task_model.delete_task(task_id)