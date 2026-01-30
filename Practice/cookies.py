from typing import Annotated
from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()

class CookiesModal(BaseModel):
    ads_id: str | None = None
    auth_key: str | None = None
    identifier: int | None = None

# cookies parameter example
@app.get("/read-cookies/")
async def read_cookies( 
    ads_id: Annotated[str | None, Cookie()] = None, 
    auth_key: Annotated[str | None, Cookie()] = None
    ):
    return {"ads_id": ads_id, "auth_key": auth_key}

# handle multiple cookies at once
@app.get("/read-multiple-cookies/")
async def read_multiple_cookies(
    cookies: Annotated[CookiesModal, Cookie()]
):
    return cookies
    
