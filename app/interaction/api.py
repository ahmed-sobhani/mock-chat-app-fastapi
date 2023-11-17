from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from .schemas import Interaction, InteractionCreate
from . import service as interaction_service

router = APIRouter()

@router.post("/interactions/", 
             response_model=Interaction, 
             description="Create a new interaction")
def create_interaction(interaction: InteractionCreate, db: Session = Depends(get_db)):
    return interaction_service.create(db, interaction)

@router.get("/interactions/", 
            response_model=list[Interaction], 
            description="Get all interactions")
def get_all_interactions(db: Session = Depends(get_db)):
    return interaction_service.getAll(db)