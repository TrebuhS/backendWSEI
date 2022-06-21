import os

from sqlalchemy import (MetaData, create_engine)

from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = os.getenv('DATABASE_URI')

# engine = create_engine(DATABASE_URI)
# metadata = MetaData()
# database = Database(DATABASE_URI)
# Base = declarative_base()
engine = create_engine(
    DATABASE_URI,
    connect_args={},
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    print(DATABASE_URI)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    print(engine.url)
    Base.metadata.create_all(bind=engine)
