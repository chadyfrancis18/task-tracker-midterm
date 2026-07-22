from fastapi.testclient import TestClient
from backend.main import app
from datetime import date, timedelta

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Task Tracker API with Advanced Features"}

def test_create_task_with_tags_and_due_date():
    task_data = {
        "id": 10,
        "title": "Complete Midterm",
        "description": "Due dates and tags feature",
        "completed": False,
        "due_date": str(date.today() + timedelta(days=2)),
        "tags": ["urgent", "backend"]
    }
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Complete Midterm"
    assert "urgent" in response.json()["tags"]

def test_filter_overdue_tasks():
    response = client.get("/tasks?overdue=true")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_task():
    response = client.delete("/tasks/10")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}
