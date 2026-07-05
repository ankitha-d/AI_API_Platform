from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.auth import get_current_user
from app.database.database import get_db
from app.models.api_key import APIKey
from app.models.user import User
from app.utils.api_key import generate_api_key

router = APIRouter()


@router.post("/generate-api-key")
def create_api_key(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    user = db.query(User).filter(User.email == current_user["sub"]).first()

    api_key = APIKey(
        key=generate_api_key(),
        user_id=user.id,
    )

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return {
        "api_key": api_key.key
    }