from fastapi import FastAPI,Depends,HTTPException, Request, Form
from pydantic import BaseModel
from sqlalchemy.orm import Session
from userDB import SessionLocal,engine,Base
import uuid
from sqlalchemy import Column,Integer,String

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app =FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Usercreate(BaseModel):
    username : str
    password : str

class Userlogin(BaseModel):
    username : str
    password : str

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username =Column(String,unique=True)
    password = Column(String)

class Sessiontoken(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    username =Column(String)
    token = Column(String,unique = True)

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/signup_page")
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/login_page")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/signup")
def signup(user : Usercreate,db :Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.username == user.username).first()
        if existing_user :
            raise HTTPException(status_code=400,detail="user  already exists")
        new_user = User(username = user.username,password = user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message" : "signup sucessfully","user": user.username}
    except Exception as e :
        print(e)

@app.post("/login")
def login(user : Userlogin, db: Session = Depends(get_db)):
  try:
        existing = db.query(User).filter(User.username == user.username ).first()
        if not existing:
            raise HTTPException(status_code=404,detail="data not found")
        if existing.password != user.password:
            raise HTTPException(status_code=401,detail="incorrect password")
        
        token = str(uuid.uuid4())
        session = Sessiontoken(username = user.username,token = token)
        db.add(session)
        db.commit()
        return {"message":"login successful","token":token}
  except Exception as e:
    print(e)


@app.post("/logout")
def logout(token :str,db : Session = Depends(get_db)):
    try:

        session = db.query(Sessiontoken).filter(Sessiontoken.token == token).first()
        if not session:
            raise HTTPException(status_code=400,detail="invalid token")
        db.delete(session)
        db.commit()
        return {"message" : "logout sucessful"}
    except Exception as e:
      print(e)


@app.get("/profile")
def profile(token : str,db : Session = Depends(get_db)):
    try :
        session = db.query(Sessiontoken).filter(Sessiontoken.token ==token ).first()
        if not session:
            raise HTTPException(status_code=401,detail="invalid or token expired")
        
        return {"  user":session.username,"message":"profile access granted"}
    except Exception as e:
     print(e)

@app.post("/signup_user")
def signup_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            return templates.TemplateResponse("error.html", {"request": request, "message": "User already exists"})

        new_user = User(username=username, password=password)
        db.add(new_user)
        db.commit()

        return templates.TemplateResponse("login.html", {"request": request})
    except Exception as e:
     print(e)

@app.post("/login_user")
def login_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user = db.query(User).filter(User.username == username).first()

        if not user:
            return templates.TemplateResponse("error.html", {"request": request, "message": "User not found"})

        if user.password != password:
            return templates.TemplateResponse("error.html", {"request": request, "message": "Incorrect password"})

        token = str(uuid.uuid4())
        session = Sessiontoken(username=username, token=token)
        db.add(session)
        db.commit()

        return templates.TemplateResponse(
            "profile.html",
            {"request": request, "username": username, "token": token}
        )
    except Exception as e:
        print(e)