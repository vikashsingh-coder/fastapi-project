# Metadata and docs
from fastapi import FastAPI

# description = """
# ChimichangApp API helps you do awesome stuff. 🚀


# You can **read items**.

# ## Users

# You will be able to:

# * **Create users** (_not implemented_).
# * **Read users** (_not implemented_).
# """


# app = FastAPI(
#     title="ChimichangApp",
#     description=description,
#     summary="Deadpool's favorite app. Nuff said.",
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact={
#         "name": "Deadpoolio the Amazing",
#         "url": "http://x-force.example.com/contact/",
#         "email": "dp@x-force.example.com",
#     },
#     license_info={
#         "name": "Apache 2.0",
#         "identifier": "Apache-2.0",
#     },
# )

# @app.get("/")
# def home():
#     return {"mess": "wow such a message"}

# By using this openapi_tags we can decide the order of tags in swagger UI.

tags_metadata = [
    {
        "name": "users",
        "description":  "Operation with users. This **login** is also here"
    },
    {
        "name": "items",
        "description": "Manage items. so _fancy_ they have their own docs",
        # this is used if we want to create an external link, allow user to click on link.
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


app = FastAPI(openapi_tags=tags_metadata)

# OpenAPI URL default was http://localhost:8000/openapi.json after this change http://localhost:8000/api/v1/openapi.json  
app = FastAPI(openapi_url="/api/v1/openapi.json")

# Docs URLs default http://localhost:8000/docs#/ after this http://localhost:8000/documents#/
# ReDoc URLs default http://localhost:8000/redoc after this http://localhost:8000/redocuments
app = FastAPI(docs_url="/documents", redoc_url="/redocuments")

# default http://localhost:8000/redoc after this will not avaliable
# app  = FastAPI(redoc_url=None)


@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]

@app.get("/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
