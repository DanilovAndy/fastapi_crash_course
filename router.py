from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from database import new_session, TaskOrm
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


@router.delete("")
async def delete_task(task_id: Annotated[STaskID, Depends()]):
    async with new_session() as session:
        task_dict = task_id.model_dump()
        print(task_dict)
        task = await session.get(TaskOrm, task_dict['task_id']) #FIXME

        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        await session.delete(task)
        await session.commit()

        return {"ok": True}

# @router.delete("")
# async def delete_task(
#         task: Annotated[STaskID, Depends()]
# ):
#
#
#     return {"ok": True}
