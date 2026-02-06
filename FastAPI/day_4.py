from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
app=FastAPI()

DBURL="sqlite:///./test.db"

engine=create_engine(
    DBURL,
    connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

