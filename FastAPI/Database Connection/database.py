from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DB_URL="sqlite:///./test.db"

engine=create_engine(
    DB_URL,
    connect_args={"check_same_thread":False}
)


sessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base=declarative_base()
