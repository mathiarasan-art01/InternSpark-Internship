from datetime import datetime
from flask import Blueprint, jsonify, request, send_file
from models import task_model
from services import export_service, statistics_service
api_bp = Blueprint("api", __name__)
@api_bp.route("/tasks", methods=["GET"])
def list_tasks():
    rows = task_model.list_tasks(
        status=request.args.get("status", "all"),
        category=request.args.get("category", "all"),
        query=request.args.get("q", ""),
    )
    return jsonify([dict(r) for r in rows])
@api_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    row = task_model.get_task(task_id)
    if not row:
        return jsonify({"error": "not found"}), 404
    return jsonify(dict(row))
@api_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    if not (data.get("title") or "").strip():
        return jsonify({"error": "title is required"}), 400
    new_id = task_model.create_task(data)
    return jsonify(dict(task_model.get_task(new_id))), 201
@api_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if not task_model.get_task(task_id):
        return jsonify({"error": "not found"}), 404
    data = request.get_json(silent=True) or {}
    task_model.update_task(task_id, data)
    return jsonify(dict(task_model.get_task(task_id)))
@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task_model.delete_task(task_id)
    return jsonify({"deleted": task_id})
@api_bp.route("/stats")
def stats():
    s = statistics_service.summary()
    s["generated_at"] = datetime.utcnow().isoformat() + "Z"
    return jsonify(s)
@api_bp.route("/export/json")
def export_json():
    path = export_service.export_json()
    return send_file(path, as_attachment=True, download_name="tasknest-export.json")
@api_bp.route("/export/csv")
def export_csv():
    path = export_service.export_csv()
    return send_file(path, as_attachment=True, download_name="tasknest-tasks.csv")