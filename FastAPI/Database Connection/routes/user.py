from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
from .user import User
from .user import LoginRequest, UserResponse
from database import get_db
# from .security import hash_password, verify_password
router=APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router.get("/")
def show_table(db=Depends(get_db)):
   return db.query(User).all()