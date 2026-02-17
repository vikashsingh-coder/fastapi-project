from fastapi import FastAPI

@app.get("/")
def home():
    return {"data": "success"}