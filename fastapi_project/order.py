from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Integer,Float,String,Column
from sqlalchemy.orm import Session
from database import engine,SessionLocal,Base

app = FastAPI()
class orderdb(Base):
    __tablename__ ="orders"
    id = Column(Integer,primary_key=True,index=True)
    customer_name = Column(String)
    order_item = Column(String)
    total_price = Column(Integer)
Base.metadata.create_all(bind=engine)

class Order(BaseModel):
    id : int
    customer_name : str
    order_item : str    
    total_price : int
    class config:
        from_attributes = True
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def home():
    return"order detiels"


@app.post("/order")
def   add_oder_dit(order : Order,db: Session= Depends(get_db)):
    existing =db.query(orderdb).filter(orderdb.id == order.id ).first()
    if existing:
        raise HTTPException(status_code=400,detail="alredy exists")
    
    new_order = orderdb(
       id = order.id,
       customer_name =order.customer_name,
       order_item = order.order_item,
       total_price= order.total_price
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message" : "data add succesfuly", "data":new_order}

     

@app.get("/order")
def get_all_dit(db : Session =Depends(get_db)):
    order =db.query(orderdb).all()
    return order

@app.get("/order/{o_id}")
def order_id(o_id : int,db : Session = Depends(get_db)):
    order = db.query(orderdb).filter(orderdb.id == o_id).first()
    if not order:
        raise HTTPException(status_code=404,detail="data not found")
    return order
    
@app.put("/order/{o_id}")
def updete_oder_dit(o_id : int,updete :Order,db : Session = Depends(get_db)):
    order = db.query(orderdb).filter(orderdb.id == o_id).first()
    if not order:
         raise HTTPException(status_code=404,detail="data not found")
    
    order.customer_name = updete.customer_name
    order.order_item = updete.order_item
    order.total_price = updete.total_price

    db.commit()
    db.refresh(order)
    return "data updeted"


@app.delete("/order/{o_id}")
def delet_order(o_id : int,db : Session =Depends(get_db)):
    order = db.query(orderdb).filter(orderdb.id == o_id).first()
    if not order :
         raise HTTPException(status_code=404,detail="data not found")
    db.delete(order)
    db.commit()
    return " data deleted...."

