import pytest

from PromoçãoProduto import promocao_produto

def test_1():
    assert promocao_produto(500.00, 50.00)

def test_2():
    assert promocao_produto(10500.00, 500.00)

def test_3():
    assert promocao_produto(90.00, 0.80)