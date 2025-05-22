from db.database import get_connection
import sqlite3

class Aluno():
    def __init__(self, nome: str, turma: int):
        self.__nome = nome
        self.__turma = turma

    def salvar(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
                INSERT INTO alunos (nome, turma_id)
                VALUES (?,?)

            """,(self.__nome, self.__turma),
                )
        conn.commit()
        conn.close()
    # Método estático pois pode ser acessado mesmo sem informar parâmetros como nome e turma_id
    @staticmethod
    def excluir_aluno(id_exclusao):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_exclusao,))
        conn.commit()
        conn.close()
    
    @staticmethod
    def listar_alunos():
        conn = get_connection()
        cursor = conn.cursor()
        # Irá receber os alunos em forma de lista
        cursor.execute("SELECT * FROM alunos")
        resultado = cursor.fetchall()
        conn.close()
        return resultado


