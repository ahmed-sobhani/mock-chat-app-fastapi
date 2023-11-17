from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
import uuid

class RoleEnum(str, Enum):
    humam="human"
    ai="ai"


class MessageBase(BaseModel):
    content: str
    role: RoleEnum 

class MessageCreate(MessageBase):
    pass 

class Message(MessageBase):
    id: int
    created_at: datetime
    updated_at: datetime
    interaction_id: int

    class Config:
        orm_mode = True