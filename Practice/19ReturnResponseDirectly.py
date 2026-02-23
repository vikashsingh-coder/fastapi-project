
# Return a Response Directly

from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


# I keep seeing different ways people return data from endpoints. 
# Some use response_model, some return JSONResponse directly... what's the difference?

app = FastAPI()

# FastAPI automatically converts it to JSON using jsonable_encoder and wraps it in a JSONResponse. You do nothing extra
# When a customer orders food, the chef (FastAPI) takes your raw ingredients (your data — a dict, list, or Pydantic model),
# cooks it properly, plates it nicely, and serves it.

@app.get("/item")
def get_item():
    # return "anything I can send"
    # return {"name": "Apple", "price": 1.5}
    return [{"name": "Apple", "price": 1.5}, {"name": "Banana", "price": 2.5}]


# what about response_model? Why would I use that?

# now imagine you have a strict recipe card (the Pydantic model). The chef follows it precisely. 
# Every dish that leaves the kitchen is guaranteed to have the right ingredients, 
# in the right format, cooked the right way. No surprises for the customer.

class Item(BaseModel):
    name: str
    price: float

@app.get("/item-with-model", response_model=Item)  # ← The "recipe card"
def get_item():
    return {"name": "Apple", "price": 1.5, }

# validates AND formats the output
# Pydantic v2 does this serialization in Rust under the hood, so it's much faster than the default approach.
# auto-generates API documentation


# What if I return a JSONResponse or Response object directly?
# you're the chef and the waiter. You plate the food yourself, carry it yourself, and serve it yourself. 
# Total control — but also total responsibility.

@app.get("/item-jsonResponse")
def get_item():
    item = Item(name="Apple", price=1.5, somemore=154.25)
    return JSONResponse(content=jsonable_encoder(item))

@app.get("/item-xml")
def get_item_xml():
    xml_content = "<item><name>Apple</name><price>1.5</price></item>"
    return Response(content=xml_content, media_type="application/xml")




