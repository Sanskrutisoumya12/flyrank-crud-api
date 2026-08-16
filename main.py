from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

from database import create_db_and_tables, engine
from models import Task


app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks",
    version="1.0"
)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()



    
# In-memory task list


@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks")
def get_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        return tasks
    


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)

        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return task

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)

        return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    with Session(engine) as session:
        task = session.get(Task, task_id)

        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        task.title = updated_task.title
        task.completed = updated_task.completed

        session.add(task)
        session.commit()
        session.refresh(task)

        return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)

        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        session.delete(task)
        session.commit()

        return {
            "message": "Task deleted successfully"
        }