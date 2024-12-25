from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel  # Для работы с Pydantic моделями

# Базовый класс для всех моделей
Base = declarative_base()

# Модель для таблицы Users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    posts = relationship("Post", back_populates="user")


# Модель для таблицы Posts
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="posts")


# Подключение к базе данных
DATABASE_URL = "postgresql+psycopg2://lab9:lab9@localhost/lab9"  

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Создаёт таблицы в базе данных, если они не существуют

# Сессия для работы с базой
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Получение сессии для взаимодействия с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic модели для валидации данных

# Модель для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True  # Эта опция позволяет Pydantic модели работать с SQLAlchemy моделями


# Модель для отображения пользователя
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Эта опция позволяет Pydantic модели работать с SQLAlchemy моделями


# Модель для создания поста
class PostCreate(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True  # Эта опция позволяет Pydantic модели работать с SQLAlchemy моделями


# Модель для отображения поста
class PostOut(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True  # Эта опция позволяет Py
