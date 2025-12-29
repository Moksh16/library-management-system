from fastapi import FastAPI, Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from . import models

models.Base.metadata.create_all(bind=engine)



app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='moksh', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connection established")
        break
    except Exception as error:
        print("Connection to server failed")
        print("error,",error)
        time.sleep(2)

class Post(BaseModel):
    name: str
    author: str
    rating: Optional[int] = None
    year_published: int

my_post = [{"name": "Fountainhead", "rating":5, "published":True,"id":1},{"name": "Intelligent Investor", "rating":5,"published": True,"id":2}]

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

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return {"data": posts} 



@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post,db: Session = Depends(get_db)):
    # cursor.execute("""insert into books (name,author,rating,year_published) values (%s,%s,%s,%s) returning *""",(post.name,post.author,post.rating,post.year_published))
    # new_post = cursor.fetchone()
    # conn.commit()

    new_post = models.Post(name =post.name, author=post.author, rating = post.rating, year_published=post.year_published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}



@app.get("/case/su")
def get_latest():
    post = my_post[-1]
    return {"latest post": post}
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("""select * from books where id=%s""",str(id))
    post =cursor.fetchone()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} was not found"}
    return {"post detail": post}

@app.delete('/posts/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    cursor.execute("""delete from books where id=%s returning *""",str(id))
    deleted_post = cursor.fetchone()
    if deleted_post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id:int, post:Post):
    cursor.execute("""update books set name=%s,author=%s,rating=%s,year_published=%s where id =%s returning *""",(post.name,post.author,post.rating,post.year_published,str(id)))
    new_post = cursor.fetchone()
    conn.commit()
    if new_post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return {"data": new_post}