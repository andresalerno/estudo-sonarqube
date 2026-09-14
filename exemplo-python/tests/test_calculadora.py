"""Testes propositalmente PARCIAIS: cobrem só 'dividir' e 'esta_vazio',
deixando 'calcular_media' e 'comparar_status' sem cobertura para que o
SonarQube mostre a diferença no percentual de Coverage."""

from src.calculadora import dividir, esta_vazio


def test_dividir():
    assert dividir(10, 2) == 5


def test_esta_vazio_com_none():
    assert esta_vazio(None) is True


def test_esta_vazio_com_valor():
    assert esta_vazio("teste") is False
