from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    title = Column(String, index=True)

    messages = relationship("Message", back_populates="interaction")
