import pytest

from desconto_produto import desconto_produto

def test_1():
    novo_valor, desconto = desconto_produto(100)
    assert novo_valor == 91.00
    assert desconto == 9.00

def test_2():
    novo_valor, desconto = desconto_produto(1500)
    assert novo_valor == 1365.00
    assert desconto == 135.00

def test_3():
    novo_valor, desconto = desconto_produto(60000)
    assert novo_valor == 54600.00
    assert desconto == 5400.00