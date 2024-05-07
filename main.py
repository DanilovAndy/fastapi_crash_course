from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from database import create_tables, delete_tables, new_session, TaskOrm
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


# @app.delete("/task/{task_id}")
# async def delete_task(
# ):
#     async with new_session() as session:
#         task = await session.get(TaskOrm, task_id)
#         if task is None:
#             raise HTTPException(status_code=404, detail="Task not found")
#         await session.delete(task)
#         await session.commit()
#
#         return {"ok": True}
