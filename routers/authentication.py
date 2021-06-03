from fastapi.param_functions import Depends
from pydantic.networks import HttpUrl
from sqlalchemy.orm.session import Session
from routers import user
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import schemas
import database
import models
import hashing
import jwt_token
from hashing import Hash
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])
get_db = database.get_db


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalied Credentials with this username : {request.username}")
    if Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Pasword Please Provide Correct Password")
    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
