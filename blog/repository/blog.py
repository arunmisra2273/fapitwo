from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas

def all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return blog

def create(blog: schemas.Blog, db: Session):
    newBlog = models.Blog(title=blog.title, body=blog.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

def update(id: int, blog: schemas.Blog, db: Session):
    bloggy = db.query(models.Blog).filter(models.Blog.id == id)
    if not bloggy.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The requested resource was not found')
    bloggy.update(blog.dict())
    db.commit()
    return 'updated'

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The requested resource was not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'
