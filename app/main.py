from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .models import get_db, UserCreate, UserOut, PostCreate, PostOut
from .crud import create_user, create_post, get_users, get_posts, update_user_email, update_post_content, delete_post, delete_user
from .schemas import UserCreate, User, Post, PostCreate

app = FastAPI()

# Роут для создания пользователя
@app.post("/users/")
def create_user_view(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db=db, user=user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Роут для создания поста
@app.post("/posts/", response_model=PostOut)
def create_post_view(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db=db, title=post.title, content=post.content, user_id=post.user_id)

# Роут для получения всех пользователей
@app.get("/users/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

# Роут для получения всех постов
@app.get("/posts/", response_model=list[PostOut])
def read_posts(db: Session = Depends(get_db)):
    return get_posts(db)

# Роут для обновления email пользователя
@app.put("/users/{user_id}/email/", response_model=UserOut)
def update_user_email_view(user_id: int, new_email: str, db: Session = Depends(get_db)):
    return update_user_email(db=db, user_id=user_id, new_email=new_email)

# Роут для обновления контента поста
@app.put("/posts/{post_id}/content/", response_model=PostOut)
def update_post_content_view(post_id: int, new_content: str, db: Session = Depends(get_db)):
    return update_post_content(db=db, post_id=post_id, new_content=new_content)

# Роут для удаления поста
@app.delete("/posts/{post_id}/")
def delete_post_view(post_id: int, db: Session = Depends(get_db)):
    delete_post(db=db, post_id=post_id)
    return {"message": "Post deleted"}

# Роут для удаления пользователя и их постов
@app.delete("/users/{user_id}/")
def delete_user_view(user_id: int, db: Session = Depends(get_db)):
    delete_user(db=db, user_id=user_id)
    return {"message": "User and their posts deleted"}
