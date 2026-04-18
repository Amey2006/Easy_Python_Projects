# # from fastapi import FastAPI

# # app=FastAPI()

# # @app.get("/")
# # def hello():
# #     return {"message": "Hello World"}

# # @app.get("/status")
# # def status():
# #     return {
# #         "server":"running",
# #         "system":"active"
# #     }
# # from pydantic import BaseModel

# # class User(BaseModel):
# #     name: str
# #     age: int
# #     email: str

# # @app.post("/create-user")
# # def create_user(user: User):
# #     return {
# #         "message": "User created",
# #         "user": user
# #     }
# # @app.get("/search/")
# # def showProduct(product:str,price:int):
# #     return {
# #         "Product":product,
# #         "Price":price
# #     }
# # class Client(BaseModel):
# #     name:str
# #     password:str
# #     age:int

# # @app.post("/register/")
# # def register(client:Client):
# #     return{
# #         "message":"User created",
# #         "Name":client.name,
# #         "Age":client.age

# #     }
# # from fastapi import HTTPException

# # @app.get("/users/{id}")
# # def get_user(id: int):
# #     if id != 1:
# #         raise HTTPException(
# #             status_code=404,
# #             detail="User not found"
# #         )
# #     return {"id": 1, "name": "Amey"}


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base, Session
# from passlib.context import CryptContext
# from jose import jwt
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# from datetime import datetime, timedelta

# # -------------------- CONFIG --------------------
# DATABASE_URL = "sqlite:///./test.db"
# SECRET_KEY = "mysecretkey"
# ALGORITHM = "HS256"

# # -------------------- DB SETUP --------------------
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

# # -------------------- MODEL --------------------
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True)
#     password = Column(String)

# Base.metadata.create_all(bind=engine)

# # -------------------- APP --------------------
# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # -------------------- PASSWORD HASH --------------------
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str):
#     return pwd_context.hash(password)

# def verify_password(plain, hashed):
#     return pwd_context.verify(plain, hashed)

# # -------------------- JWT TOKEN --------------------
# def create_token(username: str):
#     data = {
#         "sub": username,
#         "exp": datetime.utcnow() + timedelta(minutes=30)
#     }
#     return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("sub")
#         return username
#     except:
#         raise HTTPException(status_code=401, detail="Invalid Token")

# # -------------------- ROUTES --------------------

# # Signup
# @app.post("/signup")
# def signup(username: str, password: str, db: Session = Depends(get_db)):
#     hashed_pwd = hash_password(password)

#     user = User(username=username, password=hashed_pwd)
#     db.add(user)
#     db.commit()

#     return {"msg": "User created"}

# # Login
# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == form_data.username).first()

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     if not verify_password(form_data.password, user.password):
#         raise HTTPException(status_code=401, detail="Wrong password")

#     token = create_token(user.username)

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }

# # Protected Route
# @app.get("/dashboard")
# def dashboard(user: str = Depends(get_current_user)):
#     return {"msg": f"Welcome {user}"}
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ------------------ CONFIG ------------------
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE_URL = "sqlite:///./users.db"

# ------------------ DB SETUP ------------------
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

# ------------------ APP ------------------
app = FastAPI()

# ------------------ SECURITY ------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ------------------ AUTH ------------------
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ------------------ ROUTES ------------------

# ✅ Register
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=username,
        password=hash_password(password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

# ✅ Login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# ✅ Protected Route
@app.get("/hello")
def hello_user(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, you are authenticated 🎉"}