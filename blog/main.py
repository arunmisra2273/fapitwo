from fastapi import FastAPI, Depends, Response, status, HTTPException
from fastapi.param_functions import Body
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

import blog

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session=Depends(get_db)):
    newBlog = models.Blog(title=blog.title, body=blog.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The requested resource was not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, blog:schemas.Blog, db: Session = Depends(get_db)):
    bloggy = db.query(models.Blog).filter(models.Blog.id == id)
    if not bloggy.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The requested resource was not found')
    bloggy.update(blog.dict())
    db.commit()
    return 'updated'

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Error': f'Blog with id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return blog
