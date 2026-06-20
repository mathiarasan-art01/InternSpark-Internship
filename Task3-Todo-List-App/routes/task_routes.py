from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    send_file
)

from services.export_service import export_pdf as generate_pdf
from models import task_model
from services import task_service, statistics_service
from utils.validators import validate_task_form

task_bp = Blueprint("tasks", __name__)


# =====================================================
# DASHBOARD
# =====================================================
@task_bp.route("/")
def dashboard():
    status = request.args.get("status", "all")
    category = request.args.get("category", "all")
    query = (request.args.get("q") or "").strip()

    tasks = task_model.list_tasks(status, category, query)
    notes = task_model.list_notes()
    stats = statistics_service.summary()

    return render_template(
        "pages/dashboard.html",
        tasks=tasks,
        notes=notes,
        stats=stats,
        categories=current_app.config["CATEGORIES"],
        priorities=current_app.config["PRIORITIES"],
        filters={"status": status, "category": category, "q": query},
    )


# =====================================================
# ADD TASK
# =====================================================
@task_bp.route("/tasks/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        errors = validate_task_form(request.form)

        if errors:
            for e in errors:
                flash(e, "warning")
            return redirect(url_for("tasks.add_task"))

        task_service.add(request.form.to_dict())
        flash("Task added successfully ✨", "success")
        return redirect(url_for("tasks.dashboard"))

    return render_template(
        "pages/add_task.html",
        categories=current_app.config["CATEGORIES"],
        priorities=current_app.config["PRIORITIES"],
    )


# =====================================================
# EDIT TASK
# =====================================================
@task_bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = task_model.get_task(task_id)

    if not task:
        return render_template("errors/404.html"), 404

    if request.method == "POST":
        errors = validate_task_form(request.form)

        if errors:
            for e in errors:
                flash(e, "warning")
            return redirect(url_for("tasks.edit_task", task_id=task_id))

        task_model.update_task(task_id, request.form.to_dict())
        flash("Task updated ✨", "success")

        return redirect(url_for("tasks.dashboard"))

    return render_template(
        "pages/edit_task.html",
        task=task,
        categories=current_app.config["CATEGORIES"],
        priorities=current_app.config["PRIORITIES"],
    )


# =====================================================
# TOGGLE TASK
# =====================================================
@task_bp.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    task_model.toggle_task(task_id)
    return redirect(request.referrer or url_for("tasks.dashboard"))


# =====================================================
# DELETE TASK
# =====================================================
@task_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task_model.delete_task(task_id)
    flash("Task deleted", "info")
    return redirect(request.referrer or url_for("tasks.dashboard"))


# =====================================================
# COMPLETED TASKS
# =====================================================
@task_bp.route("/tasks/completed")
def completed_tasks():
    tasks = task_model.list_tasks(status="completed")
    return render_template("pages/completed_tasks.html", tasks=tasks)


# =====================================================
# ANALYTICS
# =====================================================
@task_bp.route("/analytics")
def analytics():
    return render_template(
        "pages/analytics.html",
        stats=statistics_service.summary(),
        by_category=statistics_service.by_category(),
        by_priority=statistics_service.by_priority(),
    )


# =====================================================
# NOTES
# =====================================================
@task_bp.route("/notes/new", methods=["POST"])
def create_note():
    content = (request.form.get("content") or "").strip()
    color = request.form.get("color") or "mint"

    if not content:
        flash("Empty note not saved", "warning")
        return redirect(url_for("tasks.dashboard") + "#notes")

    task_model.create_note(content, color)
    return redirect(url_for("tasks.dashboard") + "#notes")


@task_bp.route("/notes/<int:note_id>/delete", methods=["POST"])
def delete_note(note_id):
    task_model.delete_note(note_id)
    return redirect(url_for("tasks.dashboard") + "#notes")


# =====================================================
# PDF EXPORT
# =====================================================
@task_bp.route("/export/pdf")
def export_pdf_route():

    pdf_path = generate_pdf()

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name="tasknest-report.pdf"
    )