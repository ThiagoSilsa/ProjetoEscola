from db.database import get_connection


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
    def excluir(aluno_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
        conn.commit()
        conn.close()
    
    @staticmethod
    # Buscando todos os alunos no banco de dados
    def buscar_todos():
        conn = get_connection()
        cursor = conn.cursor()
        # Irá receber os alunos em forma de lista
        cursor.execute("SELECT * FROM alunos")
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    
    @staticmethod
    def buscar_por_turma(turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        # Irá receber os alunos em forma de lista
        cursor.execute("SELECT * FROM alunos WHERE turma_id = ?", (turma_id,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado


    @staticmethod
    # Verificando a existencia do aluno
    def existe(aluno_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM alunos WHERE id = ?",(aluno_id,)
            )
        resultado = cursor.fetchone()
        conn.close()
        # is not none converte o resultado em valor booleano
        # caso o resultado for none (não existe) retornará False
        # Se existir retornará True
        return resultado is not None
    
    @staticmethod
    def alterar_turma(aluno_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE alunos SET turma_id = ? WHERE id = ?",(turma_id, aluno_id)
            )
        conn.commit()
        conn.close()
    