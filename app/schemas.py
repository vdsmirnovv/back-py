from pydantic import BaseModel
from typing import List, Optional

# Модель для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        
# Модель для создания поста
class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True  # Это необходимо для правильной работы с SQLAlchemy моделями

# Модель для отображения информации о пользователе (по желанию)
class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Это необходимо для правильной работы с SQLAlchemy моделями

# Модель для отображения информации о посте (по желанию)
class Post(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True  # Это необходимо для правильной работы с SQLAlchemy моделями
