from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user.user import User
from app.schemas.user.user import UserCreate
from app.core.security import hash_password


def create_user(db: Session, user: UserCreate) -> User:
    # Step 1: Check if user already exists (friendly error)
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Step 2: Create user with hashed password
    hashed_pwd = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_pwd)
    db.add(db_user)

    # Step 3: Try commit, catch race condition error from DB
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
