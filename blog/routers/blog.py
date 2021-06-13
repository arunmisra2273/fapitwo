from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

@router.get('/', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(database.get_db)):
    return blog.all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK)
def show(id, db: Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)
