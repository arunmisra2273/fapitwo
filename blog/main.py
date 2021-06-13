from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blog'])
# def create(blog: schemas.Blog, db: Session=Depends(get_db)):
#     newBlog = models.Blog(title=blog.title, body=blog.body)
#     db.add(newBlog)
#     db.commit()
#     db.refresh(newBlog)
#     return newBlog


# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The requested resource was not found')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'Deleted'


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
# def update(id, blog:schemas.Blog, db: Session = Depends(get_db)):
#     bloggy = db.query(models.Blog).filter(models.Blog.id == id)
#     if not bloggy.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The requested resource was not found')
#     bloggy.update(blog.dict())
#     db.commit()
#     return 'updated'


# @app.get('/blog', status_code=status.HTTP_200_OK, tags=['Blog'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['Blog'])
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'Error': f'Blog with id {id} is not available'}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
#     return blog

#########################################################################################################################


# @app.post('/user', status_code=status.HTTP_201_CREATED, tags=['User'])
# def createUser(user: schemas.User, db: Session = Depends(get_db)):
#     newUser = models.User(name=user.name, email=user.email, password=hashy.Hashy.bashy(user.password))
#     db.add(newUser)
#     db.commit()
#     db.refresh(newUser)
#     return newUser


# @app.get('/user', status_code=status.HTTP_200_OK, tags=['User'])
# def all(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users


# @app.get('/user/{id}', status_code=status.HTTP_200_OK, tags=['User'])
# def show(id, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'user with id {id} is not available')
#     return user
