from fastapi import FastAPI

app = FastAPI(title="Task Manager API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def home():
    return {"message": "Task Manager API"}
