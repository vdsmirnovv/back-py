from fastapi import FastAPI, Query, Form, Header, Cookie, Response
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# 1. Базовый маршрут
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 2. Обработка параметров
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/search")
def search(query: Optional[str] = Query(None)):
    return {"message": f"You searched for: {query}"}

# 3. Отправка различных типов данных
@app.get("/json")
def get_json():
    return {"name": "Vadim", "age": 21, "hobbies": ["coding", "reading", "traveling"]}

@app.get("/file")
def get_file():
    file_path = "example.txt"
    with open(file_path, "w") as file:
        file.write("This is an example file.")
    return FileResponse(file_path, media_type="text/plain", filename="example.txt")

@app.get("/redirect")
def redirect_to_root():
    return RedirectResponse(url="/")

# 4. Работа с заголовками и куками
@app.get("/headers")
def get_headers(headers: dict = Header(...)):
    return {"headers": headers}

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="username", value="your_name")
    return {"message": "Cookie set successfully"}

@app.get("/get-cookie")
def get_cookie(username: Optional[str] = Cookie(None)):
    return {"username": username}

# 5. Обработка данных запроса
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"message": f"Welcome, {username}!"}

@app.post("/register")
def register(user: dict = Form(...)):
    return {"message": f"User {user['username']} registered successfully!"}

# 6. Работа с классами
class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

users = [
    User(id=1, username="john_doe", email="john@example.com", password="12345"),
    User(id=2, username="jane_doe", email="jane@example.com", password="67890"),
]

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}
