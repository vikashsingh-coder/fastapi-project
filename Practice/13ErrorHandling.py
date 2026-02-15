# Error Handling
from fastapi import FastAPI, HTTPException, Path, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from typing import Annotated
from starlette.exceptions import HTTPException as StarletteHTTPException

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

class UnicornExpection(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornExpection)
async def unicorn_exception_handler(request: Request, exc: UnicornExpection):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/unicorn/{name}/")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornExpection(name=name)
    return {"unicorn_name": name}


# override default http exception handler by using StarletteHTTPException return string response instead of json
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# override default validation error with your own by using RequestValidationError return string response instead of json
# exc.errors() → list of all validation problems
# error['loc'] → where the error happened (path, query, body, etc.)
# error['msg'] → human-readable error message
@app.exception_handler(RequestValidationError)
async def validation_expection_handler(request: Request, exc: RequestValidationError):
    message = "Validation error from RequestValidationError handler"
    for error in exc.errors():
        message += f"\n{error['loc'][1]}: {error['msg']}"
    return PlainTextResponse(message, status_code=400)


@app.get("/items-validate/{item_id}/")
async def read_items_validate(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}