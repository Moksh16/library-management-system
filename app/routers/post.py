from fastapi import FastAPI, Response,status,HTTPException, Depends, APIRouter
from .. import utils,schemas,models, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import SessionLocal, get_db
from typing import List, Optional


router = APIRouter(
    prefix="/posts",
    tags = ['Posts']
)


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user), limit:int = 10, skip:int=0,
              search: Optional[str]= ""):
    print(limit)
    posts = db.query(models.Post).filter(models.Post.name.contains(search)).limit(limit).offset(skip).all()
    results=db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Votes.post_id==models.Post.id, isouter=True).group_by(models.Post.id).all()
    print(results)
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""insert into books (name,author,rating,year_published) values (%s,%s,%s,%s) returning *""",(post.name,post.author,post.rating,post.year_published))
    # new_post = cursor.fetchone()
    # conn.commit()
    print(current_user.email)
    new_post = models.Post(owner_id = current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
@router.get("/{id}")
def get_post(id: int, response: Response,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""select * from books where id=%s""",str(id))
    # post =cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} was not found"}
    return {"post detail": post}



@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""delete from books where id=%s returning *""",str(id))
    # deleted_post = cursor.fetchone()

    deleted_post = db.query(models.Post).filter(models.Post.id ==id)
    if deleted_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    
    deleted_post.delete(synchronize_session = False)
    # conn.commit()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=schemas.Post)
def update_post(id:int, post:schemas.PostCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""update books set name=%s,author=%s,rating=%s,year_published=%s where id =%s returning *""",(post.name,post.author,post.rating,post.year_published,str(id)))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = db.query(models.Post).filter(models.Post.id == id)
    if new_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    new_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return new_post.first()


