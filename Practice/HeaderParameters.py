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