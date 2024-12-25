from sqlalchemy.orm import Session
from .models import User, Post
from .schemas import UserCreate, PostCreate

# Функция для создания нового пользователя
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Функция для создания нового поста
def create_post(db: Session, post: PostCreate):
    db_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Функция для получения всех пользователей
def get_users(db: Session):
    return db.query(User).all()

# Функция для получения всех постов
def get_posts(db: Session):
    return db.query(Post).join(User).all()

# Функция для получения постов пользователя
def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

# Функция для обновления email пользователя
def update_user_email(db: Session, user_id: int, new_email: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)
    return db_user

# Функция для обновления content поста
def update_post_content(db: Session, post_id: int, new_content: str):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db_post.content = new_content
        db.commit()
        db.refresh(db_post)
    return db_post

# Функция для удаления поста
def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()

# Функция для удаления пользователя
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()

