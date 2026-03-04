import pytest
from core.venta import Venta 

@pytest.fixture 
def venta1():
    return Venta("hamburguesa", 390, 56, 446)

def test_total(venta1):
    assert venta1.total == venta1.subtotal + venta1.iva