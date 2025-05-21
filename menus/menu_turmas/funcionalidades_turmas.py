import sqlite3


class Turma():
    def __init__(self, nome: str, serie: str) -> None:
        self.__nome = nome
        self.__serie = serie

    def listar_turmas(self):

        conexao = sqlite3.connect("zerodois_banco.db")
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """
                    SELECT * FROM turmas
                """
            )
            turmas = cursor.fetchall()

            conexao.close()
            # Verificando se existem turmas
            if turmas:
                for turma in turmas:
                    print(
                        f'Id: {turma[0]} | Nome: {turma[1]} | Série: {turma[2]} ')
            else:
                print('Não existem Turmas!')
        except:
            print('Erro ao apresentar Turmas!')
        finally:
            conexao.close()

    def salvar_no_banco(self):
        conexao = sqlite3.connect("zerodois_banco.db")
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """
                    INSERT INTO turmas (nome, serie)
                    VALUES (?,?)
                """, (self.__nome, self.__serie),
            )
            conexao.commit()
            conexao.close()
            print(
                f'Turma {self.__nome} da série {self.__serie} cadastrada com sucesso!')
        except:
            print('Erro ao cadastrar Turma!')
        finally:
            conexao.close()

    def excluir_turma(self):
        try:
            id_exclusao = int(input('Qual o id da turma a ser excluida?'))
            conexao = sqlite3.connect("zerodois_banco.db")
            cursor = conexao.cursor()
            # Verificando se a turma existe:
            cursor.execute(
                """
                        SELECT * FROM turmas WHERE id = ?
                    """, (id_exclusao,))
            # Irá preencher lista se existir turma com o id
            turma = cursor.fetchone()

            if turma:
                print(f'Excluindo turma {turma[1]}')
                cursor.execute(""" DELETE FROM turmas WHERE id = ?
                            """, (id_exclusao,))
                conexao.commit()
                print('Turma excluida com sucesso!')
            else:
                print('Turma não encontrada')
        except:
            print('Algo deu errado!')
        finally:
            conexao.close()
