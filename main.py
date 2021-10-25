from fastapi import FastAPI
from sqlalchemy.sql.functions import user
import models
import database
from database import engine
from routers import authentication, blog, user


app = FastAPI()


models.Base.metadata.create_all(engine)

get_db = database.get_db
app.include_router(authentication.router)
app.include_router(blog.router)
