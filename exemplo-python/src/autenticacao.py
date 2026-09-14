"""Exemplos de VULNERABILIDADES comuns que o SonarQube detecta em Python."""

import hashlib
import sqlite3

# VULNERABILIDADE: credenciais/segredos "hardcoded" direto no código-fonte.
SENHA_ADMIN = "admin123456"
API_KEY = "sk-teste-1234567890abcdef"


def gerar_hash_senha(senha: str) -> str:
    """Gera um hash da senha.

    VULNERABILIDADE: MD5 é um algoritmo de hash criptograficamente
    quebrado e não deve ser usado para senhas (o ideal seria bcrypt,
    scrypt ou argon2).
    """
    return hashlib.md5(senha.encode()).hexdigest()


def buscar_usuario(conexao: sqlite3.Connection, nome_usuario: str):
    """Busca um usuário pelo nome.

    VULNERABILIDADE: a query SQL é montada por concatenação de string
    com entrada do usuário, permitindo SQL Injection
    (ex: nome_usuario = "' OR '1'='1").
    """
    cursor = conexao.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome_usuario + "'"
    cursor.execute(query)
    return cursor.fetchall()
