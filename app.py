from flask import Flask, jsonify, request
from flask_cors import CORS
import json, os, uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    status = request.args.get("status")
    priority = request.args.get("priority")
    if status and status != "all":
        tasks = [t for t in tasks if t["status"] == status]
    if priority and priority != "all":
        tasks = [t for t in tasks if t["priority"] == priority]
    return jsonify({"tasks": tasks, "total": len(tasks)})

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks = load_tasks()
    task = {
        "id": str(uuid.uuid4())[:8],
        "title": data.get("title", "").strip(),
        "description": data.get("description", "").strip(),
        "priority": data.get("priority", "medium"),
        "status": "pending",
        "created_at": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "due_date": data.get("due_date", ""),
        "category": data.get("category", "General"),
    }
    if not task["title"]:
        return jsonify({"error": "Title required"}), 400
    tasks.append(task)
    save_tasks(tasks)
    return jsonify({"task": task, "message": "Task added!"}), 201

@app.route("/api/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t.update({k: v for k, v in data.items() if k != "id"})
            save_tasks(tasks)
            return jsonify({"task": t, "message": "Task updated!"})
    return jsonify({"error": "Task not found"}), 404

@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Task deleted!"})

@app.route("/api/stats", methods=["GET"])
def get_stats():
    tasks = load_tasks()
    total = len(tasks)
    completed = len([t for t in tasks if t["status"] == "completed"])
    pending = len([t for t in tasks if t["status"] == "pending"])
    in_progress = len([t for t in tasks if t["status"] == "in-progress"])
    high = len([t for t in tasks if t["priority"] == "high"])
    return jsonify({
        "total": total,
        "completed": completed,
        "pending": pending,
        "in_progress": in_progress,
        "high_priority": high,
        "completion_rate": round((completed / total * 100) if total else 0, 1)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
