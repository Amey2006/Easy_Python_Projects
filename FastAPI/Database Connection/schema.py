from pydantic import EmailStr,BaseModel

class LoginRequest(BaseModel):
    username:EmailStr
    password:str

class userResponse(BaseModel):
    id:int
    username:str

    class Config:
        from_attributes =True
