from fastapi import FastAPI
# we need to import StaticFiles from fastapi
from fastapi.staticfiles import StaticFiles

# description = """
# ChimichangApp API helps you do awesome stuff. 🚀


app = FastAPI(
    title= "StaticFileServe",
    description= "Here we learn how to fix static file in fastapi",
    summary="Static file handling",
)

# used to set the public path. You can direclty access anything in this file without any permission
# http://localhost:8000/static/image1.png
# Import StaticFiles. "Mount" a StaticFiles() instance in a specific path.
app.mount("/static", StaticFiles(directory="static"), name="static")

#"Mounting" means adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths.
 
@app.get("/")
def home():
    return {"data": "success"}