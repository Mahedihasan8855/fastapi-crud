
from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi import APIRouter, Depends, status, Response, HTTPException,File, UploadFile
import schemas
import database
import models
import oauth2
import shutil,os
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from repository import blog
from oauth2 import get_current_user
router = APIRouter(prefix="/blog", tags=['Blog'])

get_db = database.get_db




@ router.post( '/upload_file/',status_code=status.HTTP_201_CREATED)
def upload_file(title:str,file:UploadFile=File(...),db: Session = Depends(get_db)):
    dir ='media/service_course/audio/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open("media/service_course/audio/"+file.filename,"wb") as image:
        shutil.copyfileobj(file.file,image)
    url=str("media/service_course/audio/"+file.filename)
    new_blog = models.Blog(title=title,body=url, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
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
