from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from ..oauth2 import get_current_user
from .. database import get_db 
from .. import schemas
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/", response_model= schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    return user.create_user(request, db)

@router.get("/", response_model=list[schemas.ShowUser])
def data(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return user.get_all(db)

@router.get("/{id}", response_model=schemas.ShowUser)
def showUser(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):

    return user.get_detail(id, db)
