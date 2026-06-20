import os
import shutil
import hashlib


def organize_files(folder):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".avi"],
        "Code": [".py", ".js", ".cpp"]
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
            if os.path.exists(p) and not os.listdir(p):
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