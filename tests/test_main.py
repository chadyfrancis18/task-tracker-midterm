from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Task Tracker API"}

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    response = client.post("/tasks", json={"id": 1, "title": "Test Task", "completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_dummy_extra():
    assert 1 + 1 == 2
