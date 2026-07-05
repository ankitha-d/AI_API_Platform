from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.auth.auth import get_current_user
from app.models.user import User
from app.models.usage import Usage

router = APIRouter()


@router.get("/dashboard")
def dashboard(current_user=Depends(get_current_user), db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == current_user["sub"]).first()

    total_requests = (
        db.query(func.count(Usage.id))
        .filter(Usage.user_id == user.id)
        .scalar()
    )

    return {
        "user": user.username,
        "total_requests": total_requests
    }