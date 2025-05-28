from db.database import get_connection


class Tabela():
    @staticmethod
    # Buscando todas as tabelas no banco de dados
    def buscar_todas():
        conn = get_connection()
        cursor = conn.cursor()
        # Irá receber as tabelas em forma de lista
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    

    @staticmethod
    def existe_tabela(nome_tabela : str):
        conn = get_connection()
        cursor = conn.cursor()
        # Irá receber as tabelas em forma de lista
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' and NAME = ?;",(nome_tabela,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None
    
    @staticmethod
    def criar_tabela_alunos():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS alunos
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                turma_id INTEGER NOT NULL,
                FOREIGN KEY (turma_id) REFERENCES turmas(id)
                )""")
        conn.commit()
        conn.close()

    @staticmethod
    def criar_tabela_turmas():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS turmas
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                serie TEXT NOT NULL
                )""")
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(nome_tabela : str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela} ",)
        conn.commit()
        conn.close()