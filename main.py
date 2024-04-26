from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# def get_home():
#     task = Task(name="My task", description="my desk")
#     return {"data": task}
