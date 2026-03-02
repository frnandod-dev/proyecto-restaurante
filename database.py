from sqlalchemy import create_engine
from modelo import Base 

engine = create_engine("sqlite:///restaurante.db")

Base.metadata.create_all(engine)


