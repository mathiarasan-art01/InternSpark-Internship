# 📂 Smart File Organizer (Cloud Version - ZIP Automation)

## Overview

Smart File Organizer is a Flask-based Python automation project designed to simplify file management by processing uploaded ZIP files and automatically organizing their contents into categorized folders.

The system performs full automation including file categorization, bulk renaming, duplicate detection, empty folder cleanup, and downloadable output generation.

Unlike traditional desktop tools, this version is **fully cloud-compatible (Render deployment ready)** and does not require access to local system folders.

This project demonstrates real-world concepts of **automation, backend development, file handling, and cloud deployment.**

---

## 🚀 Features

### 📦 ZIP File Upload System

Users upload a ZIP file containing multiple files for processing.

---

### 📁 Automatic File Organization

Files are sorted based on file extensions into structured folders:

* Images → `.jpg`, `.jpeg`, `.png`, `.gif`
* Documents → `.pdf`, `.docx`, `.txt`
* Audio → `.mp3`, `.wav`
* Videos → `.mp4`, `.avi`
* Code → `.py`, `.js`, `.cpp`

---

### 🔄 Bulk File Renaming

Files are renamed automatically using a custom prefix.

Example:

Before:

```
image1.jpg
```

After:

```
FILE_image1.jpg
```

---

### 🧹 Empty Folder Cleanup

Automatically removes unnecessary empty directories after processing.

---

### 🔍 Duplicate File Detection

Uses **hashing (MD5 algorithm)** to identify duplicate files efficiently.

---

### 📊 Automatic Report Generation

Generates a summary including:

* Files moved
* Files renamed
* Empty folders removed
* Duplicate files detected

---

### ⬇️ Downloadable Output ZIP

After processing, the system generates a **new organized ZIP file** that users can download.

---

### ☁️ Cloud Safe Processing

Uses temporary workspace (`tempfile`) ensuring:

* No server storage overload
* No access to user local system
* Safe isolated execution

---

## 🧰 Technologies Used

* Python 3.x
* Flask
* OS Module
* Shutil
* Hashlib
* Zipfile
* Tempfile
* UUID
* HTML5
* CSS3
* Gunicorn (Deployment)
* Render Cloud Hosting

---

## 📁 Project Structure

```
Task1-Python-Automation/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── modules/
│   └── organizer.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── uploads/        (temporary use)
├── outputs/        (generated ZIP files)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd Task1-Python-Automation
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

## 🧪 How It Works

1. User uploads ZIP file
2. System extracts files into temporary folder
3. Files are categorized automatically
4. Duplicate files are detected
5. Empty folders are removed
6. Files are renamed (optional logic)
7. Organized ZIP is generated
8. User downloads final output

---

## 📤 Sample Output

```
Files Moved            : 25
Files Renamed          : 25
Empty Folders Removed  : 3
Duplicates Found       : 2
Output File Generated  : organized.zip
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Flask web development
* File upload handling
* ZIP file processing
* File automation logic
* Cloud deployment concepts
* Temporary file management
* Backend workflow design

---

## 🚀 Future Improvements

* Drag & drop upload UI
* Real-time progress bar
* Advanced file analytics dashboard
* PDF report generation
* Cloud storage integration (Google Drive / S3)
* User authentication system

---

## 👨‍💻 Author

**Madhiyarasu D D**
Internship Project — Task 1: Python Automation (Cloud Version)

---

## 📜 License

This project is created for **educational and internship submission purposes**.

