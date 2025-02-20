from fastapi import FastAPI
from typing import List

app = FastAPI()

items = {}

@app.post("/items/{item_id}")
def create_item(item_id: int, name: str):
    items[item_id] = name
    return {"message": "Item created", "item": {item_id: name}}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item": items.get(item_id, "Item not found")}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    if item_id in items:
        items[item_id] = name
        return {"message": "Item updated", "item": {item_id: name}}
    return {"message": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return {"message": "Item not found"}


@app.get("/search/")
def search_items(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
