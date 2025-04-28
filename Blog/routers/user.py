from fastapi import  APIRouter, HTTPException, status, Depends
from .. import models, schema, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext 

get_db = database.get_db

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/', response_model=schema.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schema.User, db: Session = Depends(get_db)):
     hashed_password = pwd_context.hash(request.password)
     new_user = models.User(name=request.name, email=request.email, password=hashed_password)
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return new_user

@router.get('/{id}', response_model=schema.ShowUser, status_code=status.HTTP_200_OK)
def read_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found with id {id}")
    return user
