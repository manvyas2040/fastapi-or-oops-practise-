from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import Integer,Float,String,column
from sqlalchemy.orm import Session
from database import engine,SessionLocal,Base

app = FastAPI()

class empdb(Base):
    __tablename__ ="emps"
    id = column(Integer,primary_key =True ,index = True)
    employe_name = column(String)
    salary = column(Integer)
    department = column(String)
Base.metadat.create_all(bind =engine)



class Employe(BaseModel):
    id : int
    employe_name : str
    salary : int
    department : str
    class config:
        from_attributes =True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return "welcome to office"



@app.post("/employe")
def add_emp_dit(emp : Employe,db : Session = Depends(get_db)):
    existing = db.query(empdb).filter(empdb.id == emp.id).first()
    if existing:
        return "alrady existing"
    
    new_emp = empdb(

        id = emp.id,
        employe_name = emp.employe_name,
        salary = emp.salary,
        department = emp.department
    )
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"message" :"data succesfully add","data" :new_emp}

@app.get("/employe")
def emp_dit(db :Session = Depends(get_db)):
    emp =db.query(empdb).all()
    return emp



@app.get("/employe/{e_id}")
def   emp_id(e_id : int,db : Session = Depends(get_db)):
    emp = db.query(empdb).filter(empdb.id == e_id).first()
    if not emp:
        return "data not found"
    return emp

@app.put("/employe/{e_id}")
def updet_emp_dit(e_id : int,updet : Employe,db :Session = Depends(get_db)):
    emp = db.query(empdb).filter(empdb.id == e_id).first()
    if not emp:
        return "data not found"
    emp.employe_name = updet.employe_name
    emp.salary = updet.salary
    emp.department = updet.department

    db.commit()
    db.refresh(emp)
    return "data updeted"

@app.delete("/eploye/{e_id}")
def delete_edata(e_id : int,db : Session= Depends(get_db)):
    emp = db.query(empdb).filter(empdb.id== e_id).first()
    if not emp:
        return "data not found"
    db.delete(emp)
    db.commit()
    return "data deleted"