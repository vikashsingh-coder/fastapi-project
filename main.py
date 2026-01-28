from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

class Items(BaseModel):
    name: str
    price: int
    description: str | None
    tax: int
    
class ItemResponse(BaseModel):
    name: str

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
    elif user_role.value == ModelRole.manager.value:
        return {"access_role": user_role, "message": "have partial access" }
    else:
        return {"access_role": user_role, "message": "Read only accesss" }


# if tax applied used give price by including tax
@app.post("/items", tags=["Items"], description="Used to create new items")
def createItem(items: Items):
    item_dict = items.model_dump()
    if items.tax:
        price_with_tax = (items.price/100)* (100 + items.tax)
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Update item details
@app.put("/items/{itemId}", tags=["Items"])
def updateItems(itemId, items: Items):
    return {
        "itemId": itemId,
        "body": items 
    }

# query parameter list with multiple values eg: http://localhost:8000/read-items/?q=blog&q=vikash
@app.get("/read-items/")
def read_items(q: Annotated[ list[str] | None, Query(min_length=1) ] = ["foo", "bar"] ):
    query_items = {"q": q}
    return query_items


# example of query parameter with additional metadata
# http://localhost:8000/additonal-metadata/?item-query=fixedquery
@app.get("/additonal-metadata/")
async def additonal_metadata(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string title",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results