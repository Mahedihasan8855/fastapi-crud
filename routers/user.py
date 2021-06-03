from fastapi import APIRouter, Depends, status, Response, HTTPException
import hashing
from hashing import Hash
import schemas
import database
import models
import oauth2
from oauth2 import get_current_user
from repository import user
from sqlalchemy.orm import Session
from typing import List
from database import get_db
router = APIRouter(prefix="/user", tags=['User'])

get_db = database.get_db


@ router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@ router.get('/', response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return user.get_all(db)


@ router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id, response: Response, db: Session = Depends(get_db)):
    return user.get_one(id, db)
