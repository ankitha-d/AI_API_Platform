from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.chat import Chat
from app.models.user import User
from app.models.usage import Usage
from app.auth.auth import get_current_user
from app.middleware.rate_limit import check_rate_limit
from app.services.gemini_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        user = db.query(User).filter(
            User.email == current_user["sub"]
        ).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Rate limit check
        check_rate_limit(user.id, db)

        # Record usage
        usage = Usage(user_id=user.id)
        db.add(usage)

        # Call Gemini
        answer = ask_gemini(request.prompt)

        # Save chat
        chat = Chat(
            user_id=user.id,
            prompt=request.prompt,
            response=answer,
        )

        db.add(chat)
        db.commit()

        return {
            "response": answer
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )