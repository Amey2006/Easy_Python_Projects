from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
class USER(BaseModel):
    name:str
    age:int

app=FastAPI()

@app.get("/product/{id}")
def show_id(id:int):
    if id not in [101,678,443,212]:
        raise HTTPException(status_code=404 ,detail="Product is not in list")
    return {"msg":"Prouct Found"}

@app.get("/items/")
def items(phone :str = "Vivo Y20 ",price :int = 70000):
    return{
        "Mobile" : phone,
        "Price"  :price
    }

@app.post("/create_user/")
def create_user(user:USER):
    return{
        "message": "User created",
        "user": user
    }

@app.post("/login")
def verify(email:str,password):
    if email!="amey123@gmail.com" or password!=123:
        raise HTTPException(status_code=401, detail="wrong user")
    return {"msg":"Hello Amey"}