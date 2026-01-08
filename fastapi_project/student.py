from fastapi import FastAPI,Depends,HTTPException,Header
from pydantic import BaseModel
from typing import List

from sqlalchemy import Integer,Float,String,Column
from sqlalchemy.orm import Session
from database import engine,SessionLocal,Base


app = FastAPI()

            

class Studentdb(Base):  
    __tablename__ ="student"
    id = Column(Integer,primary_key =True,index=True )
    name = Column(String)
    std  = Column(Integer)
    markes = Column(Float)

Base.metadata.create_all(bind=engine)

class Student(BaseModel):
    id : int
    name : str
    std  : int
    markes : float
    class Config:
        from_attributes =True

def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@app.get("/")
def home():
    return {"message":"welcome to SCHOOL.."}


@app.post("/student")
def add_student_data(student :Student,db : Session=Depends(get_db)):
    try:

        existing= db.query(Studentdb).filter(Studentdb.id == student.id).first() 
        if existing:
            raise HTTPException(status_code=400,detail="student already exists")
        new_student = Studentdb(
            id=student.id,
            name=student.name,
            std=student.std,
            markes=student.markes
            )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"message":"data add successfully","data": new_student}
    except Exception as e :
        return {"error" :str(e)}
        

@app.get("/student")

def get_all_Sdata(db :Session = Depends(get_db),str = Header("*")):
    try:

       student = db.query(Studentdb).all()
       return {"student" : student}
    except Exception as e:
     return {"error" :str(e)}

@app.get("/student/{s_id}")
def student_id(s_id:int,db : Session =Depends(get_db)):
    try:

        student = db.query(Studentdb).filter(Studentdb.id == s_id).first()
        if not student :
            raise HTTPException(status_code=404,detail="data not found")
        return student
    except Exception as e:
        return {"error" :str(e)}

@app.put("/studnet/{s_id}")
def updete_Sdata(s_id:int,updete : Student,db : Session = Depends(get_db)):
    try:

        studen = db.query(Studentdb).filter(Studentdb.id == s_id).first()
        if not studen:
            raise HTTPException(status_code=404,detail="data not found")
        
        studen.name = updete.name
        studen.std = updete.std
        studen.markes = updete.markes

        db.commit()
        db.refresh(studen)
        return {"message":"data updete"}
    except Exception as e:
       return {"error" :str(e)}

@app.delete("/student/{s_id}")
def delete_sdata(s_id : int,db :Session = Depends(get_db)):
    try:

        student = db.query(Studentdb).filter(Studentdb.id == s_id).first()
        if not student:
            raise HTTPException(status_code=404,detail="data not found")
        db.delete(student)
        db.commit()

        return {"message":"data deleted"}
    except Exception as e:
        return {"error" :str(e)}





# Form /File 
# RequestBody
# Header
# Query


