from pydantic import BaseModel
from datetime import datetime
from app.message.schemas import Message
import uuid

class InteractionBase(BaseModel):
    title: str

class InteractionCreate(InteractionBase):
    pass

class Interaction(InteractionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    messages: list[Message] = []

    class Config:
        orm_mode = True