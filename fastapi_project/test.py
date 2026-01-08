from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id :int
    name : str
    price : float
    description : str
    quantity : int

@app.get("/")
def greet():
    return "welcome to bigning... "

products = [Product(id=1,name="tv",price=25000,quantity=3)]

@app.get("/products")
def get_all_product():
    return products

@app.get("/product{id}")
def get_product_id(id:int):
    for product in products:
        if product.id == id:
            return product
        
    return "product not found"


@app.post("/product")
def add_product(product : Product):
    products.append(product)
    return product

@app.put("/product/{id}")    
def update_product(id:int,product:Product):
   for i in range(len(products)):
       if products[i].id== id:
           products[i] = product
           return "product add successfully"
       
   return "no product found"   
@app.delete("/product")
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
    return "product not found"
