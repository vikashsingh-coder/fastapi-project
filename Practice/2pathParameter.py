import random
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import AfterValidator


app = FastAPI()

@app.get("/posts")
def read_posts():
    return {"data": [{"title" : "first post title", "content": "first post content"}, {"title" : "second post title", "content": "second post content"}]}

@app.get("/posts/{post_id}")
def read_post(post_id: int):
    return {"data": f"details of the post with id {post_id}"}

@app.get("/user/:user_id")
def get_user(user_id: int):
    return {"data": user_id }

# get multiple path parameters
@app.get("/blogs/{blogID}/comments/{commentId}")
def read_blogs_comments(blogID: int, commentId: int, limit: int | None = None):
    if limit is not None:
        return {"data": f"we are reading of blog {blogID}, and have comments {commentId} with limit {limit}"}
    return {"data": f"we are reading of blog {blogID}, and have comments {commentId}"}

# endpoint for custom validation
def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError("invalid id format")

@app.get("/custom-validation")
def custom_validation(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    data = {
        "isbn-12345": {"title": "some book", "author": "some author"},
        "imdb-54321": {"title": "some movie", "director": "some director"}
    }
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items())) 
    return {"id": id, "item": item}

# path and number validation
@app.get("/path-and-number-validation/{item_id}")
def path_and_number_validation(item_id: Annotated[int | None, Path(ge=1, le=100, title="item_id should be grater then 1 and then less then 101")], q: Annotated[str | None, Query(min_length=3, max_length=20, alias="query")] = None):
    data = {"item_id": item_id,}
    if q:
        data.update({"q": q})
    return {"data": data}
