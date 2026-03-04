import os
import json
from cliente import Cliente
from cliente_frecuente import ClienteFrecuente
from venta import Venta

def guardar_clientes(clientes, ruta="datos/clientes.json"):
    """
    Guarda la lista de clientes en un archivo JSON.
    
    Serializa todos los clientes (normales y frecuentes) convirtiéndolos
    a diccionarios y guardándolos en formato JSON con codificación UTF-8.
    
    Args:
        clientes (list): Lista de objetos Cliente y/o ClienteFrecuente
        ruta (str): Ruta del archivo JSON. Por defecto: "datos/clientes.json"
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(
            [c.to_dict() for c in clientes],
            archivo,
            indent=4,
            ensure_ascii=False
        )

def cargar_clientes(ruta="datos/clientes.json"):
    """
    Carga la lista de clientes desde un archivo JSON.
    
    Lee el archivo JSON y reconstruye los objetos Cliente y
    ClienteFrecuente con sus ventas. Si el archivo no existe,
    retorna una lista vacía.
    
    Args:
        ruta (str): Ruta del archivo JSON. Por defecto: "datos/clientes.json"
    
    Returns:
        list: Lista de objetos Cliente y/o ClienteFrecuente.
              Lista vacía si el archivo no existe.
    """
    clientes = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        for cliente_dict in data:
            if cliente_dict["tipo"] == "frecuente":
                cliente = ClienteFrecuente(
                    cliente_dict["nombre"], cliente_dict["edad"], cliente_dict["descuento"]
                )
                cliente.puntos = cliente_dict["puntos"]
            else:
                cliente = Cliente(
                    cliente_dict["nombre"], cliente_dict["edad"]
                )

            for venta_dict in cliente_dict["ventas"]:
                venta = Venta(
                    venta_dict["producto"],
                    venta_dict["subtotal"],
                    venta_dict["iva"],
                    venta_dict["total"]
                )
                cliente.agregar_venta(venta)

            clientes.append(cliente)

    except FileNotFoundError:
        pass

    return clientes
