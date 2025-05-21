import sqlite3

class Alunos():
    def __init__(self, nome: str, turma: int):
        self.__nome = nome
        self.__turma = turma

    def salvar_no_banco(self):
        conexao = sqlite3.connect("zerodois_banco.db")
        cursor = conexao.cursor()

        try:
            cursor.execute(
            """
                INSERT INTO alunos (nome, turma_id)
                VALUES (?,?)

            """,(self.__nome, self.__turma),
                )
            conexao.commit()
            print(f'Aluno {self.__nome} cadastrado com sucesso na turma {self.__turma}')
        except:
            print('Erro ao cadastrar aluno!')
        finally:
            conexao.close()

    def excluir_aluno(self):
        # Verificar se aluno existe:
        try:
            id_exclusao = int(input('Qual id do aluno a ser excluido?'))
            conexao = sqlite3.connect('zerodois_banco.db')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM alunos WHERE id = ?",(id_exclusao,))

            exclusao = cursor.fetchone()
            if exclusao:
                cursor.execute("DELETE FROM alunos WHERE id = ?", (id_exclusao,))
                conexao.commit()
                print('Aluno excluido com sucesso!')
            else:
                print('Aluno inexistente!')
        except:
            print('Algo deu errado!')
        finally:
            conexao.close()

    def atualizar_turma(self):
        print(f'Atualizando a turma do aluno{self.__nome}')

    def listar_alunos(self):
        conexao = sqlite3.connect('zerodois_banco.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        # Irá receber as tabelas em forma de lista
        tabela_alunos = cursor.fetchall()
        if tabela_alunos:
            for aluno in tabela_alunos:
                print(f'id : {aluno[0]} | Nome: {aluno[1]} | turma_id: {aluno[2]}')
        else:
            print('Não existem Alunos!')


