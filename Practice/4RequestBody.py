from fastapi import FastAPI
from pydantic import BaseModel, Field, AfterValidator
from typing import Optional, Annotated
from enum import Enum

app = FastAPI()


class Role(str, Enum):
    admin = 'admin'
    user = 'manager'
    guest = 'guest' 


class Address(BaseModel):
    city: str
    state: str
    country: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

class User(BaseModel):
    fname: str =  Field(..., min_length=2, max_length=50)
    lastname: str = Field(..., min_length=2, max_length=50)
    age: int =  Field(..., gt=0, lt=140)
    email: str
    isEligible: bool = False
    bio: Optional[str] = None
    address: Address
    role: Role

class UserResponse(BaseModel):
    fname: str
    lastname: str
    age: int
    email: str
    role: Role

class OptionalBody(BaseModel):
    name: str
    description: str | None = None
    price: float
    discount: Optional[float] = None

@app.post("/items/")
def create_item(item: Item):
    return {"data": item}

@app.post("/user/", response_model=UserResponse)
def create_user(user: User):
    return user

@app.post("/optional/body")
def optional_body(item: OptionalBody, limit: Annotated[int | None, Query(gt=0)] = None):
    data = {"item1": [{"name": "simething", "price": 100}, {"name": ""}]}
    return {"data": item}
