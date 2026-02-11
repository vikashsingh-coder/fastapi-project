# Middlewares
# A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it

import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


app = FastAPI()

# This middleware adds a custom header "X-Process-Time" to the response, which indicates the time taken to process. 
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# This middleware logs the incoming request method and URL, and also logs the time taken to process 
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()

    print(f"Incoming request: {request.method} {request.url}")
    
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    print(f"Completed request in {process_time: 4f} seconds with status code {response.status_code}")

    return response

# if protected route and token in the Authorization header. 
# If not, it will return a 401 Unauthorized response. 
# Otherwise, it will allow the request to proceed
@app.middleware("http")
async def authenticate_requrest(request: Request, call_next):
    if request.url.path.startswith("/protected"):
        token = request.headers.get("Authorization")
        if token != "mysecrettoken:":
            return JSONResponse(
                status_code=401,
                content={"message": "Unauthorized"}
            )
    response = await call_next(request)
    return response

@app.get("/unprotected")
async def unprotected_route():
    return {"message": "This is an unprotected route"}

@app.get("/protected")
async def protected_route():
    return {"message": "This is a protected route"}
