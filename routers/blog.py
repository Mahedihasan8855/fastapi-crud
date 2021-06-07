
from fastapi import APIRouter, Depends, status, Response, HTTPException

import schemas
import database
import models
import oauth2
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from repository import blog
from oauth2 import get_current_user
router = APIRouter(prefix="/blog", tags=['Blog'])

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.Blog)
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.get_one(id, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int,  request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)
