from fastapi import FastAPI, Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from . import schemas,utils
from . import models
from .routers import post,users,auth
models.Base.metadata.create_all(bind=engine)



app = FastAPI()



#     try:
#         conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='moksh', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connection established")
#         break
#     except Exception as error:
#         print("Connection to server failed")
#         print("error,",error)
#         time.sleep(2)


my_post = [{"name": "Fountainhead", "rating":5, "published":True,"id":1},{"name": "Intelligent Investor", "rating":5,"published": True,"id":2}]

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_post):
        if p["id"] ==id:
            return i
@app.get("/")
def root():
    return {"Hello": "Make America powerful Again"}



@app.get("/case/su")
def get_latest():
    post = my_post[-1]
    return {"latest post": post}