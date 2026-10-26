from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="Task Manager API")

tasks = [
    {"id": 1, "title": "Apprendre GitHub Actions"},
    {"id": 2, "title": "Créer une API avec FastAPI"}
]
@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def home():
    return {"message": "Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}
class Task(BaseModel):
    title: str
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: Task):
    return {
        "message": "Tâche créée",
        "task": {
            "id": 3,
            "title": task.title
        }
    }
