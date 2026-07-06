from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.auth import get_current_user
from app.database.database import get_db
from app.models.user import User

router = APIRouter()


@router.get("/profile")
def profile(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == current_user["sub"]
    ).first()

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "joined": user.created_at
    }