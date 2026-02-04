from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/users")
def get_users(limit: int = 10, page_no: int = 1):
    return { "page_no": page_no, "limit": limit}

@app.get("/read_items")
async def read_items():
    return {"data": "final data"}

# get endpoints with query parameters
@app.get("/blogs")
def read_blogs(limit: int | None = None, page: int = 1, published: bool = True ):
    if limit is not None:
        return {"data": f"here we have a list of {limit}, page number {page}, are published: {published} "}
    return {"data": "here we have all the blogs"}


# here both are same, we can use either one of them
@app.get("/testAnnotated")
def test_annotated(q: str | None = Query(default=None, min_length=3, max_length=20)):
# def test_annotated(q: Annotated[str | None, Query(min_length=3, max_length=20)] = None):
    newdata = {"data": "test annotated"}
    if q:
        newdata.update({"q": q}) 
    return newdata

# here we are using multiple parameters in Annotated
@app.get("/mutipleAnnotated")
def multiple_annotated(q: Annotated[str | None, Query(min_length=3,max_length=30, title="Query title", description="this is the little description", pattern="^fragment$", deprecated=True, alias="query-multi")] = None):
    newdata = {"data": "multiple annotated"}
    if q:
        newdata.update({"q": q})
    return newdata

# this query parameter will not be shown in the docs
@app.get("/hidden-query")
def hidden_query(sercret_query: Annotated[str | None, Query(include_in_schema=False)] = None):
    data = {"name": "hidden query endpoint"}
    if sercret_query:
        data.update({"secret_query": sercret_query})
    return {"data": data}
