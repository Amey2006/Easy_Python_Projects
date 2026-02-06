from database import Base,sessionLocal,engine
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__="users"

    id=Column(Integer,unique=True,primary_key=True,index=True)
    username=Column(String,unique=True, index=True)
    password=Column(String)


