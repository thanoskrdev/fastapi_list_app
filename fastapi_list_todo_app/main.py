from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str 
    is_done: bool = False


items =[]



@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items" , response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")



@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated.id = item_id
            items[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted = items.pop(index)
            return {"deleted": deleted}
    raise HTTPException(status_code=404, detail="Item not found")
