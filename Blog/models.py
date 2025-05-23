from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import  relationship
from .database import Base  

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=False)
    password = Column(String, index=False)

    blogs = relationship("Blog", back_populates="creator")