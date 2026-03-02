from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer,primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    