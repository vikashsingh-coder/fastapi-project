# I’m building a frontend app on localhost:8080, and my backend is on localhost:8000 — 
# but my browser blocks the requests. What’s going on?

from fastapi import FastAPI

# you’ve hit CORS — Cross-Origin Resource Sharing. 

# Your frontend is a delivery driver, and your backend is a restaurant
# If the driver shows up in a different car (different port/protocol), 
# the restaurant won’t let them in unless they’re on the approved list.

# How do I fix it in FastAPI?

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",  # assume port no 80
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # allow_methods=['POST'],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


# So CORS is just the bouncer checking IDs before letting the delivery driver in.

# You could also use from starlette.middleware.cors import CORSMiddleware


# Can I just use ["*"] for everything?
# Only if you’re not using credentials: cookies or auth tokens. If you are, you must list origins explicitly

