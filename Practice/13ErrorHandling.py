# Error Handling
from fastapi import FastAPI, HTTPException, Path, status
from typing import Annotated

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}/")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="item not found!")
    return {"data": items}


# Add custom header
@app.get("/curtom-header/{item_id}/")
async def get_item_with_custom_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail="item not found!",
            headers={"X-Error": "Their goes an error"}
            )
    return {"data": items[item_id]}


# you could add a custom expection handler

# @app.get("/unicorn/{name}/")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornExpection()
#     return 