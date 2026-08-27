from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    title="Task Tracker API with Advanced Features", version="2.0.0"
)

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

tasks_db: List[Task] = [
    Task(
        id=1,
        title="Sample Task",
        description="Initial task for testing",
        completed=False,
    )
]

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Tracker API with Advanced Features"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(
                status_code=400, detail="Task with this ID already exists"
            )
    tasks_db.append(task)
    return task

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

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, t in enumerate(tasks_db):
        if t.id == task_id:
            tasks_db.pop(i)
            return {"message": f"Task {task_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
