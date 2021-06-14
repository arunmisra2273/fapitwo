from blog.routers import user
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, hashy, token

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/', status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    usr = db.query(models.User).filter(models.User.email == request.username).first()
    if not usr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Creds')
    if not hashy.Hashy.verify(request.password, usr.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Password')
    access_token = token.create_access_token(
        data={"sub": usr.email})
    return {"access_token": access_token, "token_type": "bearer"}
