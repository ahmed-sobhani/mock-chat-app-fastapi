from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Message(Base):
    __tablename__ = "messages"

    content = Column(String)
    role = Column(String)
    interaction_id = Column(Integer, ForeignKey("interactions.id"))

    interaction = relationship("Interaction", back_populates="messages")