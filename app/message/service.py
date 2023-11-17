from sqlalchemy.orm import Session
from .model import Message as MessageModel
from .schemas import MessageCreate
from gpt4free import you
import uuid

"""Create New Row for Model"""
def create(db: Session, message: MessageCreate, interaction_id: int):
    db_obj = MessageModel(content=message.content, role= message.role, interaction_id= interaction_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

"""Get One Row By ID"""
def getById(db: Session, id: int):
    return db.query(MessageModel).filter(MessageModel.id == id).first()

"""Get All Rows"""
def getAll(db: Session):
    return db.query(MessageModel).all()

"""Get All Rows By Filter Specific Column"""
def getAllFilterBy(db: Session, _key: any, _value: any):
    return db.query(MessageModel).filter(getattr(MessageModel, _key) == _value).all()

"""Get Response from GPT4Free"""
def getgptReponse(message: str):
    # simple request
    response = you.Completion.create(prompt=message)

    return response.text