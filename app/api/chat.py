from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.chat import Chat
from app.models.user import User
from app.auth.auth import get_current_user
from app.services.gemini_service import ask_gemini
from app.models.usage import Usage
from app.middleware.rate_limit import check_rate_limit
router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    user = db.query(User).filter(User.email == current_user["sub"]).first()
    usage = Usage(user_id=user.id)
    db.add(usage)
    check_rate_limit(user.id, db)

    answer = ask_gemini(request.prompt)

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