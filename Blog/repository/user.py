from fastapi import  APIRouter, HTTPException, status, Depends
from .. import models, schema, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext 


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create(request: schema.User, db: Session):
    hashed_password = pwd_context.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found with id {id}")
    return user