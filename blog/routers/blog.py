from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)


@router.get('/', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get('/{id}', status_code=status.HTTP_200_OK)
def show(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Error': f'Blog with id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available')
    return blog


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(database.get_db)):
    newBlog = models.Blog(title=blog.title, body=blog.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, blog: schemas.Blog, db: Session = Depends(database.get_db)):
    bloggy = db.query(models.Blog).filter(models.Blog.id == id)
    if not bloggy.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='The requested resource was not found')
    bloggy.update(blog.dict())
    db.commit()
    return 'updated'


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='The requested resource was not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'
