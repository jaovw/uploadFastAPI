from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import Depends, HTTPException, status
from ..database import get_db

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_detail(id, db: Session= Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= F'Post whit id {id} is not avaliable!')
       
    return blog

def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= F'Post whit id {id} is not avaliable!')
    else:   
        db.query(models.Blog).filter(models.Blog.id == id).delete()
        db.commit()
    return 'feito'

