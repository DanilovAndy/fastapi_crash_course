from typing import Optional

from pydantic import BaseModel


class STaskId(BaseModel):
    id: int


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int
