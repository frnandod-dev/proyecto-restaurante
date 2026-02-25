from cliente import Cliente
import pytest

@pytest.fixture 
def cliente():
    return Cliente("Fernando", 20)

def test_cliente_nuevo_lista_vacia(cliente):
    assert len(cliente.ventas) == 0

def test_cliente_guardado_correctamente(cliente):
    assert cliente.nombre == "Fernando"

def test_ventas_igual_0(cliente):
    assert cliente.total_consumido() == 0

def test_edad_invalida():
    with pytest.raises(ValueError):
        Cliente("Fernando", -3)

