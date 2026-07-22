from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Task Tracker API", version="1.0")

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

fake_db: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Tracker API"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return fake_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    fake_db.append(task)
    return task
