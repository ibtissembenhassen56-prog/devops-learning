from fastapi import FastAPI

app = FastAPI(title="Task Manager API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def home():
    return {"message": "Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {"id": 1, "title": "Apprendre GitHub Actions"},
            {"id": 2, "title": "Créer une API avec FastAPI"}
        ]
    }
