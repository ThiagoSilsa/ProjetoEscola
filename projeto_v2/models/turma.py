from db.database import get_connection


class Turma():
    def __init__(self, nome: str, serie: str) -> None:
        self.__nome = nome
        self.__serie = serie

    def salvar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO turmas (nome, serie)
                VALUES (?,?)
            """, (self.__nome, self.__serie),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_todas():

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
                    SELECT * FROM turmas
                """
        )
        resultado = cursor.fetchall()
        conn.close()
        return resultado


    @staticmethod
    def excluir(turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM turmas WHERE id = ?", (turma_id,))
        conn.commit()
        conn.close()
    
    # Método para verificar se a turma existe!

    @staticmethod
    def existe(turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM turmas WHERE id = ?",(turma_id,)
            )
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None
