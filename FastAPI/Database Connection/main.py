from fastapi import Depends,FastAPI,HTTPException
from model import User
from database import sessionLocal,engine,Base
from sqlalchemy.orm import Session
from schema import LoginRequest,userResponse
from typing import List
from security import hash_password,verify_it
Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(data:LoginRequest,db:Session=Depends(get_db)):

    user=User(
        username=data.username,
        password=hash_password(data.password)

    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "ID ":user.id,
        "Username":user.username
    }

@app.post("/login")
def login(un:str,pw:str,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.username==un).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    elif not verify_it(pw,user.password):
        raise HTTPException(
            status_code=401,
            detail="Unauthorised access"
        )
    else:
        return{
           "msg":"Login Succesful"
        }
    
from routes.user import router as user_router

app.include_router(user_router)