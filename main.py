# from fastapi import FastAPI, Query, Body
# from enum import Enum
# from pydantic import BaseModel
# from typing import Annotated
# from datetime import datetime, time, timedelta
# from uuid import UUID

# class Items(BaseModel):
#     name: str
#     price: int
#     description: str | None
#     tax: int
    
# class ItemResponse(BaseModel):
#     name: str

# class ModelRole(str, Enum):
#     admin = "admin"
#     manager = "manager"
#     user = "user"

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}


# @app.get("/user/:user_id")
# def get_user(user_id: int):
#     return {"data": user_id }


# @app.get("/users")
# def get_users(limit: int = 10, page_no: int = 1):
#     return { "page_no": page_no, "limit": limit}

# @app.get("/read_items")
# async def read_items():
#     return {"data": "final data"}


# @app.get("/access/{user_role}")
# def getRole(user_role: ModelRole):
#     if user_role is ModelRole.admin:
#         return {"access_role": user_role, "message": "have all access" }
#     elif user_role.value == ModelRole.manager.value:
#         return {"access_role": user_role, "message": "have partial access" }
#     else:
#         return {"access_role": user_role, "message": "Read only accesss" }


# # if tax applied used give price by including tax
# @app.post("/items", tags=["Items"], description="Used to create new items")
# def createItem(items: Items):
#     item_dict = items.model_dump()
#     if items.tax:
#         price_with_tax = (items.price/100)* (100 + items.tax)
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# # Update item details
# @app.put("/items/{itemId}", tags=["Items"])
# def updateItems(itemId, items: Items):
#     return {
#         "itemId": itemId,
#         "body": items 
#     }

# # query parameter list with multiple values eg: http://localhost:8000/read-items/?q=blog&q=vikash
# @app.get("/read-items/")
# def read_items(q: Annotated[ list[str] | None, Query(min_length=1) ] = ["foo", "bar"] ):
#     query_items = {"q": q}
#     return query_items


# # example of query parameter with additional metadata
# # http://localhost:8000/additonal-metadata/?item-query=fixedquery
# @app.get("/additonal-metadata/")
# async def additonal_metadata(
#     q: Annotated[
#         str | None,
#         Query(
#             alias="item-query",
#             title="Query string title",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^fixedquery$",
#             deprecated=True,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # example of handling datetime, time, timedelta in request body 78aea7e5-97c3-4e77-92ea-d40d6a3a4439
# @app.post("/process-datetime/{id}")
# def process_datetime(
#     id: UUID,
#     start_datetime: Annotated[datetime, Body()],
#     end_datetime: Annotated[datetime, Body()],
#     process_after: Annotated[timedelta, Body()],
#     repeat_at: Annotated[time, Body()]
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "id": id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration
#     }

# # cookies parameter example
# @app.get("/read-cookies/")
# def read_cookies():
#     return {"message": "Reading cookies"}

from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class HeadersModel(BaseModel):
    user_agent: str | None = None
    

# read headers example
@app.get("/read-headers/", )
async def read_headers(user_agent: Annotated[str | None, Header(title="Pass Header", description="User are able to send header values")] = None):
    return {"user_agent": user_agent}


@app.get("/convert_underscores-disable-headers/")
async def read_headers(strange_header: Annotated[str | None, Header(convert_underscores=False)] = None):
    return {"strange_header": strange_header}

# Duplicate headers
@app.get("/duplicate-headers/")
def read_duplicate_headers(X_Token: Annotated[list[str]| None, Header()] = None):
    return {"X_token": X_Token}