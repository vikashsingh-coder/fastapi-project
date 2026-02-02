from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Crud operation with status code

items_db = {
    "item1": {"name": "Apple", "quantity": 10},
    "item2": {"name": "Banana", "quantity": 20},
    "item3": {"name": "Orange", "quantity": 15},
}

class Item(BaseModel):
    name: str
    quantity: int


@app.get("/items", response_model=list[Item], status_code=200)
def read_items():
    return [ Item(**items) for items in items_db.values()]

@app.post("/items/new", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    item_id = f"item{len(items_db) + 1}"
    items_db[item_id] = item.model_dump() 
    return item

@app.put("/items/{item_id}", response_model=Item, responses={404: {"description": "Item not found"}}, status_code=status.HTTP_200_OK)
def update_item(item_id: str, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.model_dump()
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: str):
    if item_id in items_db:
        del items_db[item_id]
        return 