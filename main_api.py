from fastapi import FastAPI
from database import SessionLocal
from models import Cliente

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al restaurante"}

clientes = [
    {"nombre": "Fernando", "edad": 20},
    {"nombre": "Diana", "edad": 23}
]

@app.get("/clientes")
def obtener_clientes():
    db = SessionLocal()
    clientes_todos = db.query(Cliente).all()
    db.close()
    return clientes_todos

from pydantic import BaseModel

class ClienteSchema(BaseModel):
    nombre: str
    edad: int

@app.post("/cliente")
def crear_cliente(cliente: ClienteSchema):
    db = SessionLocal()
    nuevo_cliente = Cliente(nombre=cliente.nombre, edad=cliente.edad)
    db.add(nuevo_cliente)
    db.commit()
    db.close()
    return nuevo_cliente