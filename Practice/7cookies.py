"""Cookie examples for the FastAPI project.

Cookies are small text files stored in your browser by a website you visit.

This module shows how to read individual cookies and multiple cookies
via a Pydantic model. The routes are examples and can be mounted
into the main application for testing and learning.

"""

from typing import Annotated
from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()

class CookiesModal(BaseModel):
    ads_id: str | None = None
    auth_key: str | None = None
    identifier: int | None = None


# cookies parameter example
@app.get("/read-cookies/")
async def read_cookies(
    ads_id: Annotated[str | None, Cookie()] = None,
    auth_key: Annotated[str | None, Cookie()] = None,
):
    return {"ads_id": ads_id, "auth_key": auth_key}


# handle multiple cookies at once
@app.get("/read-multiple-cookies/")
async def read_multiple_cookies(
    cookies: Annotated[CookiesModal, Cookie()]
):
    return cookies
 
    
"""
Why Are Cookies Used?

Authentication
Keeps you logged in after signing in.

User Preferences
Remembers language, theme (dark/light mode), etc.

Session Management
Tracks your session while browsing.

Analytics & Tracking
Helps website owners understand user behavior.

Shopping Cart
Stores selected items before checkout.

"""

"""
Types of Cookies
1️⃣ Session Cookies

Temporary

Deleted when you close the browser

2️⃣ Persistent Cookies

Stored for a specific time

Remain even after closing the browser

3️⃣ Secure Cookies

Sent only over HTTPS

4️⃣ HttpOnly Cookies

Cannot be accessed by JavaScript

Helps prevent XSS attacks

"""