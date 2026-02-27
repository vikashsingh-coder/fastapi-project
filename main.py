from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()


# Handle Redirect
@app.get("/items/")
def get_items():
    return {"name": "football", "price": 120}
    return "I want to return some text"



# Handle htmlResponse
@app.get("/get-html/") 
def get_items() :
    content = '''
<body>
    <h1>Heading 1</h1>
    <p>this is our paragraph</p>
</body>
'''
    return HTMLResponse(content)

# Handle XML Reponse
@app.get("/get-xml/") 
def get_items() :
    content = "<item><name>Apple</name><price>1.5</price></item>"
    return Response(content=content, media_type="application/xml")

def fake_vidio_streaming():
    for i in range(10):
        yield f"some fake video bites {i} "

# Streaming
@app.get("/streaming-file")
async def main():
    return StreamingResponse(fake_vidio_streaming())

