from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
@app.get("/")
def home():
    return {"message": "CRUD app is running!"}
    

# Step 1: Create a Model
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None

# Step 2: Fake database (list)
products_db: List[Product] = []

# CREATE (POST)
@app.post("/products", response_model=Product)      
def create_product(product: Product):
    for p in products_db:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    products_db.append(product)
    return product

# READ ALL (GET)
@app.get("/products", response_model=List[Product])
def get_all_products():
    return products_db

# READ ONE (GET)
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# UPDATE (PUT)
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated: Product):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            products_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Product not found")

# DELETE (DELETE)
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            products_db.pop(index)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
