"""Exemplos de BUGS comuns que o SonarQube detecta em Python."""


def calcular_media(notas=[]):
    """Calcula a média de uma lista de notas.

    BUG: o valor padrão do parâmetro é uma lista mutável. Como listas
    são criadas apenas uma vez (na definição da função), ela é
    compartilhada entre todas as chamadas que não passam 'notas'
    explicitamente, acumulando dados de execuções anteriores.
    """
    notas.append(10)
    return sum(notas) / len(notas)


def dividir(a, b):
    """Divide 'a' por 'b'.

    BUG: não trata o caso b == 0, o que gera ZeroDivisionError em
    tempo de execução em vez de um erro tratado.
    """
    return a / b


def esta_vazio(valor):
    """Verifica se um valor é None (uso correto de 'is')."""
    return valor is None


def comparar_status(status):
    """Compara o status atual com o texto 'ativo'.

    BUG: usa 'is' para comparar strings em vez de '=='. Isso depende
    de um detalhe de implementação do interpretador (string interning)
    e pode dar resultado errado de forma inconsistente.
    """
    return status is "ativo"
