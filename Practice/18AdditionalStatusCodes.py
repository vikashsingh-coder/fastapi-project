# FastAPI will return the responses using a JSONResponse

# Additional Status Codes
# you can do that by returning a Response directly, like a JSONResponse, and set the additional status code directly
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from typing import Annotated


app = FastAPI()

# Dummy Disc
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
def upsert_item(
    item_id: str,
    name: Annotated[str | None, Body()] = None,
    size: Annotated[int | None, Body()] = None,
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=items)

# It won't be serialized with a model, etc.
# Make sure it has the data you want it to have, and that the values are valid JSON 
