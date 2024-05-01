from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends

from database import create_tables, delete_tables
from router import router as tasks_router
from schemas import STaskAdd


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

tasks = []


