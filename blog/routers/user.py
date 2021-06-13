from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, hashy

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.get('/', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.get('/{id}', status_code=status.HTTP_200_OK)
def show(id, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with id {id} is not available')
    return user


@router.post('/', status_code=status.HTTP_201_CREATED)
def createUser(user: schemas.User, db: Session = Depends(database.get_db)):
    newUser = models.User(name=user.name, email=user.email,
                          password=hashy.Hashy.bashy(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
