# Função de estabelecer conexão com o banco de dados

import sqlite3


def get_connection():
    return sqlite3.connect("projeto_refatorado/db/zerodois_banco.db")
