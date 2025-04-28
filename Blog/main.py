from fastapi import FastAPI  
from .database import  engine
from . import models

from .routers import  blog, user, authentication

app = FastAPI()


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(bind=engine)







# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create(request: BlogSchema, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog', response_model=List[showBlog], status_code=status.HTTP_200_OK, tags=['Blogs'])
# def read_all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', response_model=showBlog, status_code=status.HTTP_200_OK, tags=['Blogs'])
# def read_one(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=404, detail="Blog not found with id {id}")
#     return blog

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update(id: int, request: BlogSchema, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=404, detail="Blog not found")
#     blog.title = request.title
#     blog.body = request.body
#     db.commit()
#     db.refresh(blog)
#     return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs']  )
# def delete(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=404, detail="Blog not found")
#     db.delete(blog)
#     db.commit()
#     return {"detail": "Blog deleted with id {id}" }

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post('/users', response_model=ShowUser, status_code=status.HTTP_201_CREATED, tags=['Users'])
# def create_user(request: User, db: Session = Depends(get_db)):
#      hashed_password = pwd_context.hash(request.password)
#      new_user = models.User(name=request.name, email=request.email, password=hashed_password)
#      db.add(new_user)
#      db.commit()
#      db.refresh(new_user)
#      return new_user

# @app.get('/users/{id}', response_model=ShowUser, status_code=status.HTTP_200_OK, tags=['Users'])
# def read_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail=f"User not found with id {id}")
#     return user
