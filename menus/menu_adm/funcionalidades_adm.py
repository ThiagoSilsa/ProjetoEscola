import sqlite3

def listar_tabelas():
    lista_tabelas = []
    conexao = sqlite3.connect('zerodois_banco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # Irá receber as tabelas em forma de lista
    tabelas = cursor.fetchall()
    if tabelas == []:
        print('Não existem tabelas!')
    else:
        print('Tabelas Existentes:')
        for i, tabela in enumerate(tabelas):
            print(f'Índice {i} | Tabela: {tabela[0]}')
            tabela = {
                "id" : i,
                "nome" : tabela[0]
            }
            lista_tabelas.append(tabela)

    # Irá listar o nome de todas as tabelas

    conexao.close()
    return lista_tabelas

def criar_tabela_turmas():
    conexao = sqlite3.connect('zerodois_banco.db')
    cursor = conexao.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS turmas
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            serie TEXT NOT NULL
            )

            """
    )
    conexao.commit()
    conexao.close()

def criar_tabela_alunos():
    conexao = sqlite3.connect('zerodois_banco.db')
    cursor = conexao.cursor()

    # O id da turma depende se a turma com o id existe!
    cursor.execute(
        """
                CREATE TABLE IF NOT EXISTS alunos
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                turma_id INTEGER NOT NULL,
                FOREIGN KEY (turma_id) REFERENCES turmas(id)
                )
            """
    )

    conexao.commit()
    conexao.close()

def adicionar_tabela():
    while True:
        try:
            opt = int(input(
                'Qual tabela deseja adicionar?\n1 - Tabela alunos\n2 - Tabela Turmas\n3 - Voltar'))
            if opt == 1:
                criar_tabela_alunos()
                print('Tabela alunos criada com sucesso!')
                break
            elif opt == 2:
                criar_tabela_turmas()
                print('Tabela turmas criada com sucesso!')
                break
            elif opt == 3:
                print('Voltando ao menu adm...')
                break
            else:
                print('Opção inválida!')
        except:
            print("Tabela já existente")

def excluir_tabelas():
    while True:
        lista_tabelas =  listar_tabelas()
        try:
            print()
            id_remover = int(input(
                'Qual o índice da tabela que deseja excluir?'))
            for tabela in (lista_tabelas):
                if tabela["id"] == id_remover:
                    conexao = sqlite3.connect('zerodois_banco.db')
                    cursor = conexao.cursor()
                    cursor.execute(f"DROP TABLE IF EXISTS {tabela['nome']}")
                    conexao.commit()
                    conexao.close()
                    print(f'Tabela {tabela["nome"]} excluida com sucesso')
                    return
            print('Tabela com esse ID não foi encontrado')

        except:
            print("Algo deu errado!")


