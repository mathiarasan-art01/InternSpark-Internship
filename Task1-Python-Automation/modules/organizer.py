import os
import shutil
import hashlib
import zipfile
import logging
from datetime import datetime

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup(folder):
    backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"

    with zipfile.ZipFile(backup_name, 'w', zipfile.ZIP_DEFLATED) as backup:
        for root, _, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)
                backup.write(path)

    logging.info(f"Backup created {backup_name}")
    return backup_name


def organize_files(folder):

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".avi"],
        "Code": [".py", ".java", ".cpp"]
    }

    moved = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = os.path.splitext(file)[1].lower()

            for cat, exts in categories.items():
                if ext in exts:
                    target = os.path.join(folder, cat)
                    os.makedirs(target, exist_ok=True)
                    shutil.move(path, os.path.join(target, file))
                    moved += 1
                    break

    return moved


def rename_files(folder, prefix):
    count = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            new_name = f"{prefix}_{file}"
            os.rename(path, os.path.join(folder, new_name))
            count += 1

    return count


def remove_empty_folders(folder):
    removed = 0

    for root, dirs, _ in os.walk(folder, topdown=False):
        for d in dirs:
            p = os.path.join(root, d)
            if not os.listdir(p):
                os.rmdir(p)
                removed += 1

    return removed


def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            try:
                with open(path, "rb") as f:
                    h = hashlib.md5(f.read()).hexdigest()

                if h in hashes:
                    duplicates.append(path)
                else:
                    hashes[h] = path
            except:
                pass

    return duplicates


def generate_report(moved, renamed, removed, duplicates):
    report = f"""
SMART FILE ORGANIZER REPORT

Moved: {moved}
Renamed: {renamed}
Empty folders removed: {removed}
Duplicates: {len(duplicates)}

Time: {datetime.now()}
"""

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    return report