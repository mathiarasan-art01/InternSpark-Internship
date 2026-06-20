# 📂 Smart File Organizer**

## Overview

Smart File Organizer is a Python-based automation tool designed to simplify file management tasks. The application automatically organizes files into categorized folders, creates backups, detects duplicate files, performs bulk renaming, removes empty folders, and generates detailed reports. A simple Flask web interface allows users to manage their files without using command-line operations.

This project demonstrates practical use of Python automation, file handling, exception management, logging, and web development concepts.

---

## Features

### 📁 Automatic File Organization

Files are automatically sorted into folders based on their file extensions.

Example:

* Images → `.jpg`, `.png`, `.jpeg`
* Documents → `.pdf`, `.docx`, `.txt`
* Audio → `.mp3`, `.wav`
* Videos → `.mp4`, `.avi`
* Programs → `.py`, `.java`, `.cpp`

---

### 🔄 Bulk File Renaming

Rename files automatically using a custom prefix provided by the user.

Example:

Before:
image1.jpg

After:
College_image1.jpg

---

### 🗂️ Automatic Backup Creation

Before any operation begins, the application creates a ZIP backup of the selected folder to prevent accidental data loss.

---

### 🧹 Empty Folder Cleanup

Detects and removes empty folders that are no longer needed.

---

### 🔍 Duplicate File Detection

Identifies duplicate files using file hashing techniques and reports them to the user.

---

### 📊 Report Generation

Creates a detailed report containing:

* Files moved
* Files renamed
* Empty folders removed
* Duplicate files found
* Execution timestamp

---

### 📝 Logging System

All operations are recorded in a log file for monitoring and debugging purposes.

---

## Technologies Used

* Python 3.x
* Flask
* OS Module
* Shutil Module
* Hashlib
* ZipFile
* Logging
* HTML5
* CSS3

---

## Project Structure

```text
Task1-Python-Automation/
│
├── app.py
├── requirements.txt
├── organizer.log
├── report.txt
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
└── backups/
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Task1-Python-Automation
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How to Use

1. Launch the application.
2. Enter the folder path you want to organize.
3. Enter a rename prefix.
4. Click **Start Automation**.
5. The system will:

   * Create a backup
   * Organize files
   * Rename files
   * Remove empty folders
   * Detect duplicates
   * Generate a report
6. View the results directly on the dashboard.

---

## Sample Output

```text
Backup Created : backup_20260618.zip

Files Moved : 25

Files Renamed : 25

Empty Folders Removed : 3

Duplicates Found : 2

Report Generated Successfully
```

---

## Learning Outcomes

This project helped in understanding:

* Python Automation
* File Management
* Flask Web Development
* Logging and Reporting
* Exception Handling
* Data Organization Techniques
* Real-World Automation Workflows

---

## Future Enhancements

* Drag-and-drop folder selection
* PDF report generation
* Interactive dashboard analytics
* File size statistics
* Custom category management
* Cloud backup integration

---

## Author

**Madhiyarasu D D**

Task 1 : Python Automation - Internship Project

---

## License

This project is developed for educational and internship evaluation purposes.
