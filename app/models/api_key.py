from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(128), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")