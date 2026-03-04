from core.cliente import Cliente
from core.cliente_frecuente import ClienteFrecuente

def registrar_cliente(lista_clientes):
    """
    Registra un nuevo cliente solicitando sus datos por consola.
    
    Pide al usuario que ingrese nombre y edad, crea un objeto Cliente
    con esos datos y lo agrega a la lista proporcionada.

    Args:
        lista_clientes(list): Lista de objetos Cliente
    """
    nombre = input("Nombre: ")
    edad = int(input("edad: "))
    cliente = Cliente(nombre, edad)
    lista_clientes.append(cliente)
    print(f"Cliente {nombre} registrado")

def buscar_cliente(lista_clientes, nombre):
    """
    Busca un cliente por nombre en la lista.
    
    Recorre la lista de clientes comparando nombres hasta encontrar
    una coincidencia. La búsqueda es sensible a mayúsculas/minúsculas.
    
    Args:
        lista_clientes (list): Lista de objetos Cliente
        nombre (str): Nombre del cliente a buscar
    
    Returns:
        Cliente: Objeto Cliente si se encuentra
        None: Si no existe ningún cliente con ese nombre
    """
    for cliente in lista_clientes:
        if cliente.nombre == nombre:
            return cliente
    return None

def listar_clientes(lista_clientes):
    """
    Muestra en consola la información de todos los clientes.
    
    Imprime los datos de cada cliente usando su método mostrar_info().
    Si la lista está vacía, muestra un mensaje indicándolo.
    
    Args:
        lista_clientes (list): Lista de objetos Cliente a mostrar
    """
    if not lista_clientes:
        print("No hay clientes registrados")
        return
    for cliente in lista_clientes:
        cliente.mostrar_info()
        print("-" * 25)

