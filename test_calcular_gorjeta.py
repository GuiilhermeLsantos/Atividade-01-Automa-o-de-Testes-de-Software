import pytest

from calcular_gorjeta import calcular_gorjeta

def test_1():
    valor_total_conta, valor_gorjeta = calcular_gorjeta(75.00)
    assert valor_total_conta == 82.50
    assert valor_gorjeta == 7.5

def test_2():
    valor_total_conta, valor_gorjeta = calcular_gorjeta(125)
    assert valor_total_conta == 137.50
    assert valor_gorjeta == 12.5

def test_3():
    assert calcular_gorjeta(350.87) == pytest.approx((385.96, 35.09), abs= 0.01) 