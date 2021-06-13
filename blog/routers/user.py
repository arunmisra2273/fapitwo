from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.get('/', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(database.get_db)):
    return user.all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def show(id, db: Session = Depends(database.get_db)):
    return user.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)
