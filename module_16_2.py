from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated

# Создаем экземпляр приложения FastAPI

app = FastAPI()

# Определение базового маршрута

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/{username}/{age}")
async def username(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):

    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/admin")
async def admin():
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=1, description='Enter User ID', example='3')]):
    return {f"Вы вошли как пользователь № {user_id}"}

