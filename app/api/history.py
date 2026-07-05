from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.auth import get_current_user
from app.models.user import User
from app.models.chat import Chat

router = APIRouter()


@router.get("/history")
def history(current_user=Depends(get_current_user),
            db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.email == current_user["sub"]
    ).first()

    chats = db.query(Chat).filter(
        Chat.user_id == user.id
    ).all()

    return chats