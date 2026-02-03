
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class FormData(BaseModel):
    fname: str
    lname: str
    email: str
    bio: str | None = None

@app.post("/submit-form/", status_code=201)
def submit_form( from_Data: Annotated[FormData, Form()]):
    return {"form_data": from_Data}

# here I need to return an html form for login
@app.get("/login/", response_class=HTMLResponse)
def Login():
    html_content = """
    <html>
        <head>
            <title>Login Form</title>
        </head>
        <body>
            <h2>Login</h2>
            <form action="/submit-form" method="post">
                <label for="fname">fname:</label><br>
                <input type="text" id="fname" name="fname"><br><br>
                <label for="lname">lname:</label><br>
                <input type="pasword" id="lname" name="lname"><br><br>
                 <label for="email">email:</label><br>
                <input type="text" id="email" name="email"><br><br>
                <button type="submit" >Submit</button>
            </form>
        </body>
    </html>"""
    return HTMLResponse(content=html_content)