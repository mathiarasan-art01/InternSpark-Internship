import os
from datetime import datetime

from flask import current_app
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
)

from models import task_model
from services.statistics_service import summary


# ==========================================
# Export PDF Report
# ==========================================
def export_pdf() -> str:

    report_dir = os.path.join(
        current_app.config["EXPORT_DIR"],
        "reports"
    )

    os.makedirs(report_dir, exist_ok=True)

    # ==========================================
    # File Name
    # ==========================================
    filename = (
        f"tasknest-report-"
        f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.pdf"
    )

    pdf_path = os.path.join(report_dir, filename)

    # ==========================================
    # PDF Setup
    # ==========================================
    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    content = []

    # ==========================================
    # Title
    # ==========================================
    content.append(
        Paragraph("TaskNest Productivity Report", styles["Title"])
    )

    content.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %b %Y %I:%M %p')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    # ==========================================
    # Statistics Section
    # ==========================================
    stats = summary()

    content.append(Paragraph("Task Summary", styles["Heading2"]))
    content.append(Paragraph(f"Total Tasks: {stats.get('total', 0)}", styles["Normal"]))
    content.append(Paragraph(f"Completed Tasks: {stats.get('done', 0)}", styles["Normal"]))
    content.append(Paragraph(f"Pending Tasks: {stats.get('pending', 0)}", styles["Normal"]))
    content.append(Paragraph(f"Completion Rate: {stats.get('pct', 0)}%", styles["Normal"]))

    content.append(Spacer(1, 20))

    # ==========================================
    # Task List Section
    # ==========================================
    content.append(Paragraph("Task Details", styles["Heading2"]))

    tasks = task_model.list_tasks()

    if not tasks:
        content.append(Paragraph("No tasks available.", styles["Normal"]))
    else:
        for task in tasks:

            # ✅ FIX: sqlite3.Row → dictionary-style access
            title = task["title"] or "Untitled"
            description = task["description"] or "-"
            category = task["category"] or "-"
            priority = task["priority"] or "-"
            due_date = task["due_date"] or "Not Set"

            status = "Completed" if task["completed"] else "Pending"

            task_html = f"""
            <b>{title}</b><br/>
            Description: {description}<br/>
            Category: {category}<br/>
            Priority: {priority}<br/>
            Due Date: {due_date}<br/>
            Status: {status}
            """

            content.append(Paragraph(task_html, styles["Normal"]))
            content.append(Spacer(1, 10))

        content.append(PageBreak())

    # ==========================================
    # Build PDF
    # ==========================================
    doc.build(content)

    return pdf_path