from cliente import Cliente
from venta import Venta

def test_cliente_nuevo_lista_vacia():
    cliente = Cliente("Fernando", 20)
    assert len(cliente.ventas) == 0

def test_cliente_guardado_correctamente():
    cliente = Cliente("Fernando", 20)
    assert cliente.nombre == "Fernando"

def test_ventas_igual_0():
    cliente = Cliente("Fernando", 29)
    assert cliente.total_consumido() == 0

def test_agregar_venta():
    cliente = Cliente("Fernando", 29)
    venta = Venta("Hamburguesa",200, 16, 216)
    cliente.agregar_venta(venta)
    assert len(cliente.ventas) > 0
