from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class TaskCreate(BaseModel):
    title: str

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str
    completed: bool


@app.get("/")
def root():
    return {"message": "API is running!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = Task (
        id= len(tasks) +1,
        title= task.title
    )
    tasks.append(new_task)
    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            task.title = task_update.title
            task.completed = task_update.completed
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
