from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

app = FastAPI(title="Task Tracker API with Features", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[date] = None  # ميزة تواريخ الاستحقاق
    tags: List[str] = Field(default_factory=list)  # ميزة التصنيفات

tasks_db: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Tracker API with Advanced Features"}

@app.get("/tasks", response_model=List<Task>)
def get_tasks(overdue: Optional[bool] = None, tag: Optional[str] = None):
    result = tasks_db
    today = date.today()
    
    if overdue is not None:
        if overdue:
            result = [t for t in result if t.due_date and t.due_date < today and not t.completed]
        else:
            result = [t for t in result if not (t.due_date and t.due_date < today and not t.completed)]
            
    if tag:
        result = [t for t in result if tag in t.tags]
        
    return result

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks_db.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for idx, t in enumerate(tasks_db):
        if t.id == task_id:
            tasks_db[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for idx, t in enumerate(tasks_db):
        if t.id == task_id:
            tasks_db.pop(idx)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
