from fastapi import FastAPI
from enum import Enum


class ModelRole(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/user/:user_id")
def get_user(user_id: int):
    return {"data": user_id }


@app.get("/users")
def get_users(limit: int = 10, page_no: int = 1):
    return { "page_no": page_no, "limit": limit}

@app.get("/read_items")
async def read_items():
    return {"data": "final data"}


@app.get("/access/{user_role}")
def getRole(user_role: ModelRole):
    if user_role is ModelRole.admin:
        return {"access_role": user_role, "message": "have all access" }
    elif user_role.value == : ModelRole.manager.value
        return {"access_role": user_role, "message": "have partial access" }
    else:
        return {"access_role": user_role, "message": "Read only accesss" }


