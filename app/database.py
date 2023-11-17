import uuid
from datetime import datetime
from sqlalchemy import create_engine, DateTime, Column, Integer
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base, as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

DATABASE_URL= "sqlite:///./mockChat.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base: DeclarativeMeta = declarative_base()


@as_declarative()
class Base:
    id = Column(Integer, autoincrement=True, primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate= datetime.now())
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()    


def init_db():
    """ Initiate Databas"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """ Get Database """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()