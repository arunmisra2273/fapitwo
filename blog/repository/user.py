from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, hashy


def all(db: Session):
    users = db.query(models.User).all()
    return users


def show(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} is not available')
    return user


def create(user: schemas.User, db: Session):
    newUser = models.User(name=user.name, email=user.email, password=hashy.Hashy.bashy(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
