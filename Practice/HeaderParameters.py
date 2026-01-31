from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class HeadersModel(BaseModel):
    user_agent: str | None = None
    

class MultiHeadersModel(BaseModel):
    # model_config = {"extra": "forbid"}  # to forbid extra headers
    model_config = {"extra": "allow"} # to allow extra headers

    host: str
    save_date: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
    
# read headers example
@app.get("/read-headers/", tags=["Headers"])
async def read_headers(user_agent: Annotated[str | None, Header(title="Pass Header", description="User are able to send header values")] = None):
    return {"user_agent": user_agent}


@app.get("/convert_underscores-disable-headers/", tags=["Headers"])
async def read_headers(strange_header: Annotated[str | None, Header(convert_underscores=False)] = None):
    return {"strange_header": strange_header}

# Duplicate headers
@app.get("/duplicate-headers/", tags=["Headers"])
def read_duplicate_headers(X_Token: Annotated[list[str]| None, Header()] = None):
    return {"X_token": X_Token}

# multiple headers using pydantic model
@app.get("/multiple-headers/", tags=["Headers"])
def read_multiple_headers(headers: Annotated[MultiHeadersModel, Header()] ):
    return {"headers": headers}