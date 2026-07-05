from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usage import Usage


DAILY_LIMIT = 100


def check_rate_limit(user_id: int, db: Session):
    total_requests = (
        db.query(Usage)
        .filter(Usage.user_id == user_id)
        .count()
    )

    if total_requests >= DAILY_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Daily request limit reached"
        )