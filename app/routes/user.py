# app/routes/user.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.services.user import create_user
from app.core.deps import get_db

router = APIRouter()

@router.post("/users/create")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
