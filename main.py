from fastapi import FastAPI, Depends

from app.database.database import Base, engine

from app.models.user import User
from app.models.chat import Chat
from app.models.api_key import APIKey

from app.api.users import router as user_router
from app.api.chat import router as chat_router
from app.api.api_keys import router as api_key_router

from app.auth.auth import get_current_user
from app.models.usage import Usage
from app.api.dashboard import router as dashboard_router
from app.api.history import router as history_router
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI API Platform")

app.include_router(user_router)
app.include_router(chat_router)
app.include_router(api_key_router)
app.include_router(dashboard_router)
app.include_router(history_router)

@app.get("/")
def home():
    return {"message": "AI API Platform Running 🚀"}


@app.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "email": current_user
    }