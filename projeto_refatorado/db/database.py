# Função de estabelecer conexão com o banco de dados

import sqlite3

def get_connection():
    return sqlite3.connect("zerodois_banco.db")