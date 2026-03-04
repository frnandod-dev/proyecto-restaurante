from sqlalchemy import create_engine
from models.models import Base 
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///restaurante.db")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


