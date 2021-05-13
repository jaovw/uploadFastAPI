from os import stat
from fastapi.param_functions import Depends
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models
from ..JWTtoken import create_access_token
from ..hashing import Hash
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=['Auth'])

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=F'Invalid Credentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=F'Incorrect Password!')
    #GENERATE A JWT TOKEN AND RETURN#
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    