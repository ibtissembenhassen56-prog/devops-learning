from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == {
        "tasks": [
            {"id": 1, "title": "Apprendre GitHub Actions"},
            {"id": 2, "title": "Créer une API avec FastAPI"}
        ]
    }
