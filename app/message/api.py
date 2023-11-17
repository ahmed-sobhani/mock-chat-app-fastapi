from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from .schemas import Message, MessageCreate, RoleEnum
from . import service as message_service
from app.interaction import service as interacion_service

router = APIRouter()

@router.post("/interaction/{interaction_id}/messages", 
             response_model=list[Message], 
             description="Add new message to interaction")
def create_message(interaction_id: int,message: MessageCreate,db: Session = Depends(get_db)):

    """Check Interaction existance"""
    interacion_service.validate_interaction_id(interaction_id, db)

    try:
        """Add Message to interaction"""
        message.role = RoleEnum.humam
        created_message = message_service.create(db, message, interaction_id)

        """Add Response from GPT4Free"""
        ai_resp_text = message_service.getgptReponse(message.content)
        ai_message = MessageCreate(content=ai_resp_text, role=RoleEnum.ai)
        ai_message = message_service.create(db, ai_message, interaction_id)
    
        return [created_message,ai_message]
    except:
        raise HTTPException(status_code=500, detail="Internal server error on adding new message")
         

@router.get("/interaction/{interaction_id}/messages", 
            response_model=list[Message], 
            description="Get interaction messages")
def get_interaction_messages(interaction_id: int, db: Session = Depends(get_db)):
    return message_service.getAllFilterBy(db, "interaction_id", interaction_id)
