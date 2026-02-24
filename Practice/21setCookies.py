
# Method 1: Using Response Parameter (Recommended)

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(
        key="username",
        value="vikash",
        max_age=3600,        # 1 hour
        httponly=True,       # Prevent JS access
        secure=False         # True in production (HTTPS)
    )
    return {"message": "Cookie set successfully"}

'''
What happens?

FastAPI sends a Set-Cookie header.

Browser stores the cookie.

On next request, browser automatically sends it back.
'''

# Method 2: Using JSONResponse - want full control

@app.get("/set-cookie")
def set_cookie():
    response = JSONResponse(content={"message": "Cookie set"})
    response.set_cookie(key="token", value="abc123")
    return response

'''
| Parameter  | Meaning                             |
| ---------- | ----------------------------------- |
| `key`      | Cookie name                         |
| `value`    | Cookie value                        |
| `max_age`  | Time in seconds                     |
| `expires`  | Expiry date                         |
| `httponly` | Blocks JavaScript access (security) |
| `secure`   | Only sent over HTTPS                |
| `samesite` | Controls cross-site behavior        |

example:

response.set_cookie(
    key="access_token",
    value="jwt_token_here",
    httponly=True,
    secure=True,
    samesite="Strict"
)
'''

# ❌ How to Delete Cookie

@app.get("/delete-cookie")
def delete_cookie(response: Response):
    response.delete_cookie("username")
    return {"message": "Cookie deleted"}