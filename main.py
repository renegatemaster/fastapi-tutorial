from fastapi import FastAPI

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


@app.get("/")
def first_fastapi():
    return {"Output": "My first FastAPI"}


@app.get("/users")
def get_users_query(limit: int = 2):
    user_list = list(users_db.values())
    return user_list[:limit]


@app.get("/users/{username}")
def get_user(username: str):
    return users_db[username]
