from cliente import Cliente
import pytest

def test_cliente_nuevo_lista_vacia():
    cliente = Cliente("Fernando", 20)
    assert len(cliente.ventas) == 0

def test_cliente_guardado_correctamente():
    cliente = Cliente("Fernando", 20)
    assert cliente.nombre == "Fernando"

def test_ventas_igual_0():
    cliente = Cliente("Fernando", 29)
    assert cliente.total_consumido() == 0

def test_edad_invalida():
    with pytest.raises(ValueError):
        Cliente("Fernando", -3)

