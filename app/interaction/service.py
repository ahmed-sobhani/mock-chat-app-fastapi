from fastapi import HTTPException
from sqlalchemy.orm import Session
from .model import Interaction as InteractionModel
from .schemas import InteractionCreate, Interaction

"""Create New Row for Model"""
def create(db: Session, interaction: InteractionCreate):
    db_obj = InteractionModel(title=interaction.title)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

"""Get One Row By ID"""
def getById(db: Session, id: int):
    return db.query(InteractionModel).filter(InteractionModel.id == id).first()

"""Get All Rows"""
def getAll(db: Session):
    return db.query(InteractionModel).all()

"""Get All Rows By Filter Specific Column"""
def getAllFilterBy(db: Session, _key: any, _value: any):
    return db.query(InteractionModel).filter(getattr(InteractionModel, _key) == _value).all()

"""Validate Interaction"""
def validate_interaction_id(interaction_id: int, db: Session) -> Interaction:
    interaction = getById(db, interaction_id)
    if interaction is None:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return interaction