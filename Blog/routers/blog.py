from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix = "/data",
    tags = ['Blog']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def new (request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.create_blog(request, db)

@router.get("/", response_model=List[schemas.ShowBlog])
def data(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.get_all(db) 

@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):

    return blog.get_detail(id, db)
    
# ERRO #
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= F'Post with id {id} not found')
    blog.update(request)
    db.commit()
    return 'updated'

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):

   return blog.delete_blog(id,db) 



