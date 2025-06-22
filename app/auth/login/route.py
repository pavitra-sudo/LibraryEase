from fastapi import APIRouter,Depends,HTTPException,status
from app.auth.login import schema
from app.core.deps import get_db
from sqlalchemy.orm import Session
from app.models import user as user_model
from app.core.security import verify_password
from app.auth.token.token import create_access_token


router = APIRouter(tags=['Authentication'])

@router.post('/login')
async def login(request:schema.Login,db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.email == request.username).first()
    if not user:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Username')
    if not verify_password(request.password,user.password):
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Password')

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token" :access_token, "token_type":"bearer"}
