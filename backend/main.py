from datetime import date
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

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
    due_date: Optional[date] = None
    tags: List[str] = Field(default_factory=list)


# Schema for partial task updates (PATCH)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[date] = None
    tags: Optional[List[str]] = None


tasks_db: List[Task] = []


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Task Tracker API with Advanced Features"}


# Get tasks endpoint
@app.get("/tasks", response_model=List[Task])
def get_tasks(
    overdue: Optional[bool] = None, tag: Optional[str] = None
):
    result = tasks_db
    today = date.today()

    if overdue is not None:
        if overdue:
            result = [
                t
                for t in result
                if t.due_date and t.due_date < today and not t.completed
            ]
        else:
            result = [
                t
                for t in result
                if not (t.due_date and t.due_date < today and not t.completed)
            ]

    if tag:
        result = [t for t in result if tag in t.tags]

    return result


# Create task endpoint (POST)
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(
                status_code=400, detail="Task with this ID already exists"
            )
    tasks_db.append(task)
    return task


# Full update task endpoint (PUT)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for idx, t in enumerate(tasks_db):
        if t.id == task_id:
            tasks_db[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


# Partial update task endpoint (PATCH)
@app.patch("/tasks/{task_id}", response_model=Task)
def patch_task(task_id: int, task_update: TaskUpdate):
    for idx, t in enumerate(tasks_db):
        if t.id == task_id:
            stored_task_data = t.dict()
            update_data = task_update.dict(exclude_unset=True)
            updated_fields = {**stored_task_data, **update_data}
            updated_task = Task(**updated_fields)
            tasks_db[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


# Delete task endpoint (DELETE)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for idx, t in enumerate(tasks_db):
        if t.id == task_id:
            tasks_db.pop(idx)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
