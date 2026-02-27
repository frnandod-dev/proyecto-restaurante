from fastapi import FastAPI

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
    return clientes