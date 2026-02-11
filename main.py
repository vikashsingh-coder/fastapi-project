# Middlewares
# A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it

import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

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

# CORS (Cross-Origin Resource Sharing) 
# When you're building a MERN-style frontend + FastAPI backend, you need CORS.
# Required when frontend and backend run on different ports
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specify allowed origins (e.g., frontend)
    allow_credentials=True,  # Allow cookies and credentials (must not use '*' with this)
    allow_methods=["*"],     # Allow all HTTP methods (e.g., GET, POST, PUT, DELETE)
    allow_headers=["*"],     # Allow all headers (e.g., Content-Type, Authorization)
)

# Rate Limiting (Production Use Case)



@app.get("/unprotected")
async def unprotected_route():
    return {"message": "This is an unprotected route"}

@app.get("/protected")
async def protected_route():
    return {"message": "This is a protected route"}
