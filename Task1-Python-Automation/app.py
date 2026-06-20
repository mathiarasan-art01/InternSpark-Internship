from flask import Flask, render_template, request, send_file
import os
import zipfile
import tempfile
import uuid
import shutil
from modules import organizer as org

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":

        file = request.files.get("file")

        if not file or file.filename == "":
            return render_template(
                "index.html",
                result={"success": False, "error": "No file uploaded"}
            )

        job_id = str(uuid.uuid4())
        work_dir = tempfile.mkdtemp()

        try:
            # 1. Save ZIP
            zip_path = os.path.join(work_dir, "input.zip")
            file.save(zip_path)

            # 2. Extract ZIP
            extract_dir = os.path.join(work_dir, "extract")
            os.makedirs(extract_dir, exist_ok=True)

            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(extract_dir)

            # 3. Process files
            moved = org.organize_files(extract_dir)
            renamed = org.rename_files(extract_dir, "FILE")
            removed = org.remove_empty_folders(extract_dir)
            duplicates = org.find_duplicates(extract_dir)

            # 4. Create output ZIP
            zip_base_path = os.path.join(OUTPUT_FOLDER, job_id)

            shutil.make_archive(
                zip_base_path,
                "zip",
                extract_dir
            )

            final_zip = zip_base_path + ".zip"
            filename = os.path.basename(final_zip)

            # 5. Result
            result = {
                "success": True,
                "moved": moved,
                "renamed": renamed,
                "removed": removed,
                "duplicates": len(duplicates),
                "download": filename
            }

        except Exception as e:
            result = {
                "success": False,
                "error": str(e)
            }

        finally:
            # cleanup temp folder
            if work_dir and os.path.exists(work_dir):
                shutil.rmtree(work_dir, ignore_errors=True)

    return render_template("index.html", result=result)


@app.route("/download/<filename>")
def download(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)

    if not os.path.exists(path):
        return "File not found", 404

    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)