from datetime import date
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

users_db = {
    "gleb": {
        "username": "renegatemaster",
        "date_joined": "2023-11-09",
        "location": "Almaty",
        "age": 24,
    },
    "ivan": {
        "username": "an17on",
        "date_joined": "2023-11-09",
        "location": "Saint-Petersburg",
        "age": 24,
    },
    "anett": {
        "username": "itsnotanett",
        "date_joined": "2023-11-09",
        "location": "Moscow",
        "age": 24,
    },
}


class User(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    date_joined: date
    location: Optional[str] = None
    age: int = Field(None, gt=5, lt=130)


@app.get("/")
def first_fastapi():
    return {"Output": "My first FastAPI"}


@app.get("/users")
def get_users_query(limit: int = 20):
    user_list = list(users_db.values())
    return user_list[:limit]


@app.get("/users/{username}")
def get_user(username: str):
    return users_db[username]


@app.post("/users")
def create_user(user: User):
    username = user.username
    users_db[username] = user.model_dump()
    return {"message": f"Successfully created user: {username}"}
