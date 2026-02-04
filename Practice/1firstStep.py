from fastapi import FastAPI, Query, Path
app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "Hello, World!"}