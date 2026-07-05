from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class Usage(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    requests = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())