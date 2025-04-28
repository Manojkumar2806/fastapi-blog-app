from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, database, schema
from ..repository import blog
from .. import oauth2

router = APIRouter(
    prefix='/blog',
    tags=['Blogs'],
    dependencies=[Depends(oauth2.get_current_user)]
)

get_db = database.get_db

@router.get('/', response_model=List[schema.showBlog], status_code=status.HTTP_200_OK)
def read_all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.BlogSchema, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/{id}', response_model=schema.showBlog, status_code=status.HTTP_200_OK)
def read_one(id: int, db: Session = Depends(get_db)):
    return blog.get_by_id(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.BlogSchema, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)
