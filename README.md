# FlyRank CRUD API

A simple CRUD API built with FastAPI for the FlyRank AI Backend Engineering Internship assignment.

## Features

- GET /
- GET /health
- GET /tasks
- GET /tasks/{task_id}
- POST /tasks
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## Run Locally

```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

pip install fastapi uvicorn

uvicorn main:app --reload
```

Visit:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
