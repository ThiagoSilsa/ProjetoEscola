from models.adm import Tabela
from views.menu_adm import mostrar_lista_tabelas

def listar_tabelas():
    # Acessar o back e recebe tabelas
    resultado = Tabela.buscar_todas()

    # Envia para o front
    mostrar_lista_tabelas(resultado)


def add_tabela_alunos():
    nome_tabela =  "alunos"
    if Tabela.existe_tabela(nome_tabela):
        print('Tabela já existe!')
    else:
        # Existe tabela alunos?
        Tabela.criar_tabela_alunos()
        print('Tabela criada com sucesso!')

def add_tabela_turmas():
    nome_tabela = "turmas"
    if Tabela.existe_tabela(nome_tabela):
        print('Tabela já existe!')
    else:
        # Existe tabela alunos?
        Tabela.criar_tabela_turmas()
        print('Tabela criada com sucesso!')


def excluir_tabela_alunos():
    nome_tabela =   "alunos"
    if not Tabela.existe_tabela(nome_tabela):
        print('Tabela não existe!')
    else:
        Tabela.excluir("alunos")
        print('Tabela excluida com sucesso!')


def excluir_tabela_turmas():
    nome_tabela = "turmas"
    if not Tabela.existe_tabela(nome_tabela):
        print('Tabela não existe!')
    else:
        Tabela.excluir("turmas")
        print('Tabela excluida com sucesso!')
    