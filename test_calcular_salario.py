import pytest

from calcular_salario import calcular_salario

def test_1():
    assert calcular_salario(6.25, 160, 1.3) == 987.00

def test_2():
    assert calcular_salario(20.5, 240, 1.7) == 4836.36

def test_3():
    assert calcular_salario(13.9, 200, 6.48) == pytest.approx(13.9, 200, 6.48) == 2599.86