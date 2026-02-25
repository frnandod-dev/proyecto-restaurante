import pytest
from cliente_frecuente import ClienteFrecuente

@pytest.fixture
def cliente_frecuente():
    return ClienteFrecuente("Diana", 23, .20)

def test_cliente_frecuente_nuevo_lista_vacia(cliente_frecuente):
    assert len(cliente_frecuente.ventas) == 0

def test_cliente_frecuente_guardado_correctamente(cliente_frecuente):
    assert cliente_frecuente.nombre == "Diana"

def test_ventas_igual_0_cliente_frecuente(cliente_frecuente):
    assert cliente_frecuente.total_consumido() == 0

def test_edad_invalida_cliente_frecuente():
    with pytest.raises(ValueError):
        ClienteFrecuente("Fernando", -3, .20)

def test_descuento_invalido():
    with pytest.raises(ValueError):
        ClienteFrecuente("Diana", 23, 1.2)

def test_descuento_negativo():
    with pytest.raises(ValueError):
        ClienteFrecuente("Diana", 23, -.5)