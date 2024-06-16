from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=["Taskmanager"]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.get("/{task_id}")
async def get_one_task_by_id(task_id: int) -> STask | None:
    result = await TaskRepository.return_one(task_id)
    return result


@router.delete("")
async def delete_task(task_id: Annotated[STaskID, Depends()]):
    result = await TaskRepository.delete_one(task_id)
    return result
