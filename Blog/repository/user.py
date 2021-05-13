from .. import models, schemas
from ..database import get_db
from ..hashing import Hash
from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session


def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name= request.name, email = request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def get_detail(id: int, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= F'User with id {id} is not avaliable!')
    return users
