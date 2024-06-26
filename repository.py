from fastapi import HTTPException
from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskAdd, STask, STaskID


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def return_one(cls, task_id_model: int):
        async with new_session() as session:
            query = select(TaskOrm).where(TaskOrm.id == task_id_model)
            result = await session.execute(query)
            task_models = result.scalars().one_or_none()
            return task_models

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models

    @classmethod
    async def delete_one(cls, task_id_model: STaskID):
        async with new_session() as session:
            task = await session.get(TaskOrm, task_id_model.task_id)
            print(task)
            if task is None:
                raise HTTPException(status_code=404, detail="Task not found")
            await session.delete(task)
            await session.commit()
            return {"ok": True}
