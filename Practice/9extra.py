from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union

app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# class UserInDb(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr 
#     full_name: str | None = None

# def fake_password_hahser(raquired_password: str):
#     return "supersecret" + raquired_password

# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hahser(user_in.password)
#     user_in_db = UserInDb(**user_in.model_dump(), hashed_password=hashed_password)
#     print("user saved!")
#     return user_in_db

# @app.post("/user", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved


# Refactored Code

class UserBaseModel(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(UserBaseModel):
    password: str


class UserOut(UserBaseModel):
    pass

class UserInDb(UserBaseModel):
    hashed_password: str

def fake_password_hahser(raquired_password: str):
    return "supersecret" + raquired_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hahser(user_in.password)
    user_in_db = UserInDb(**user_in.model_dump(), hashed_password=hashed_password)
    print("user saved!")
    return user_in_db

@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


# Union of Example

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

class ItemBase(BaseModel):
    description: str
    type: str

class CarItem(ItemBase):
    type: str = "car"

class PlaneItem(ItemBase):
    type: str = "plane"
    size: int

@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
def read_item(item_id: str):
    return items[item_id]



# return list of modle

user_list = [
    {"username": "user1", "email": "something1@gmail.com", "full_name": "User One"},
    {"username": "user2", "email": "something2@gmail.com", "full_name": "User Two"},
]

class SingleUser(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None

@app.get("/return_list_of_models/")
def return_list_of_models():
    return user_list


# return dict of models

user_list_dist = {
    1: {"username": "user1", "email": "something1@gmail.com", "full_name": "User One"},
    2: {"username": "user2", "email": "something2@gmail.com", "full_name": "User Two"},
}


class SingleUserModel(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None

@app.get("/return_dist_of_models/", response_model=dict[int, SingleUserModel])
def return_list_of_models():
    return user_list_dist