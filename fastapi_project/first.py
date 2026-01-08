from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

@app.get("/")
def home():
    return {"message": "FastAPI working!"}

@app.post("/item")
def create_item(item: Item):
    return item.model_dump()
