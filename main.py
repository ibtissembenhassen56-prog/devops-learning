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
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title
    }

    tasks.append(new_task)

    return {
        "message": "Tâche créée",
        "task": new_task
    }
    tasks_response = client.get("/tasks")

    assert tasks_response.json()["tasks"][-1] == {
        "id": 3,
        "title": "Apprendre Docker"
    }
