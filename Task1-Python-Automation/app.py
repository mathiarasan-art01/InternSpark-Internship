from flask import Flask, render_template, request
import modules.organizer as org
import threading
import webbrowser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        folder = request.form["folder"]
        prefix = request.form.get("prefix", "FILE")

        try:
            backup_file = org.create_backup(folder)
            moved = org.organize_files(folder)
            renamed = org.rename_files(folder, prefix)
            removed = org.remove_empty_folders(folder)
            duplicates = org.find_duplicates(folder)

            report = org.generate_report(
                moved, renamed, removed, duplicates
            )

            result = {
                "backup": backup_file,
                "moved": moved,
                "renamed": renamed,
                "removed": removed,
                "duplicates": len(duplicates),
                "report": report,
                "success": True
            }

        except Exception as e:
            result = {
                "success": False,
                "error": str(e)
            }

    return render_template("index.html", result=result)


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=False)