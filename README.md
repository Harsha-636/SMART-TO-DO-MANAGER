# ✅ Smart To-Do Manager

> A full-stack task management web app built with Python & Flask. Create, update, delete and track tasks with priorities, categories, status tracking and persistent JSON storage.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

- ➕ Add tasks with title, description, priority, category and due date
- ✅ Mark tasks complete / in-progress / pending
- ✏️ Edit any task via modal dialog
- 🗑️ Delete tasks with confirmation
- 📊 Live stats dashboard (total, completed, pending, high priority)
- 📈 Progress bar showing completion rate
- 🔍 Filter by status and priority
- 💾 Persistent JSON file storage
- 🚀 Deployed live on Render

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, REST API (CRUD)
- **Frontend:** Vanilla JS, HTML5, CSS3
- **Storage:** JSON File (Collections Framework equivalent)
- **Deploy:** Render (free tier), Gunicorn

---

## 🚀 Quick Start

```bash
git clone https://github.com/Harsha-636/smart-todo-manager.git
cd smart-todo-manager
pip install -r requirements.txt
python app.py
```

Open [http://localhost:5000](http://localhost:5000)

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Get all tasks (filter by status/priority) |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/<id>` | Update task |
| DELETE | `/api/tasks/<id>` | Delete task |
| GET | `/api/stats` | Get task statistics |

---

## 👨‍💻 Author

**Sai Harsha Vardhan Reddy Avula**
B.Tech CSE @ KMCE Hyderabad (2027)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/harsha-avula)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/Harsha-636)
