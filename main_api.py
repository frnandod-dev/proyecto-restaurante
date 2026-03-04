from fastapi import FastAPI
from models.database import SessionLocal
from models.models import Cliente
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al restaurante"}



@app.get("/clientes")
def obtener_clientes():
    db = SessionLocal()
    clientes_todos = db.query(Cliente).all()
    db.close()
    return clientes_todos

@app.get(("/clientes/{id}"))
def obtener_cliente(id: int):
    db = SessionLocal()
    buscar_id = db.query(Cliente).filter(Cliente.id == id).first()
    db.close()
    if not buscar_id:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return buscar_id


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