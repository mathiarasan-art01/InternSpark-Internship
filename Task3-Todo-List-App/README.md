# 🪺 TaskNest — Smart Task & Notes Manager (Flask Web Application)

## 📌 Overview

TaskNest is a modern productivity web application built using **Flask, SQLite, and Bootstrap 5**.
It is designed to help users efficiently manage daily tasks, organize personal notes, track productivity progress, and generate professional reports.

TaskNest combines a clean **glassmorphic UI design** with practical productivity tools, making task management simple, elegant, and highly efficient.

---

## 📌 Features

### ✅ Task Management

* Create, edit, update, and delete tasks
* Mark tasks as completed or pending
* Assign categories and priorities
* Set due dates
* Filter and search tasks instantly

---

### 📝 Sticky Notes

* Create colorful quick notes
* Organize ideas and reminders
* Delete notes when no longer needed

---

### 📊 Analytics Dashboard

* View productivity statistics
* Track completed vs pending tasks
* Category-wise task breakdown
* Priority-based insights

---

### 📄 PDF Report Export

* Generate downloadable productivity reports
* Includes task summary and statistics
* Lists all current tasks in a professional PDF format

---

### 🎨 Modern UI

* Responsive design
* Glassmorphism-inspired interface
* Dark / Light theme support
* Smooth animations and transitions

---

## 🛠️ Technologies Used

### Backend

* Python 3
* Flask

### Database

* SQLite3

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Libraries

* ReportLab (PDF generation)
* Jinja2 Templates

---

## 📂 Project Structure

```text
TaskNest/
│
├── app.py
├── config.py
├── requirements.txt
│
├── database/
│   └── tasknest.db
│
├── models/
│   └── task_model.py
│
├── routes/
│   ├── task_routes.py
│   ├── api_routes.py
│   └── auth_routes.py
│
├── services/
│   ├── task_service.py
│   ├── statistics_service.py
│   └── export_service.py
│
├── utils/
│   └── validators.py
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── dashboard.css
│   │   └── animations.css
│   │
│   └── js/
│       ├── app.js
│       ├── dashboard.js
│       ├── export.js
│       └── filters.js
│
└── templates/
    ├── layouts/
    ├── pages/
    └── errors/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tasknest.git
cd tasknest
```

---

### 2. Create Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📸 Key Modules

### 📊 Dashboard

* Task list
* Notes overview
* Statistics summary
* Filters and controls

---

### 📈 Analytics

* Completion rate tracking
* Task distribution insights
* Productivity analysis

---

### 📄 PDF Export

Generates a professional report containing:

* Total tasks
* Completed tasks
* Pending tasks
* Progress percentage
* Full task list

---

## 🎯 Learning Outcomes

This project demonstrates:

* Flask Application Structure
* Blueprint Architecture
* SQLite Database Operations
* CRUD Functionality
* Form Validation
* PDF Generation using ReportLab
* Responsive UI Design
* Dark/Light Theme Implementation
* Service-Based Project Design

---

## 🚀 Future Enhancements

* User Authentication System
* Task Reminders
* Calendar View
* Drag-and-Drop Task Management
* Email Notifications
* Cloud Database Integration
* AI Productivity Suggestions
* REST API Expansion

---

## 👨‍💻 Internship Project

**Task 3 – Advanced To-Do List Web Application**

Developed as part of a Python Internship Program to demonstrate:

* Python Development
* Flask Framework
* Database Management
* Frontend Integration
* Software Architecture

---

## 📜 License

This project is created for **educational and internship purposes**.

---

## 💙 Final Note

Built with **Flask, SQLite, Bootstrap & Python**

> TaskNest — Organize Tasks. Track Progress. Stay Productive. 🪺✨

---

