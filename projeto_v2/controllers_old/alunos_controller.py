# Aqui ele faz solicitações ao models e envia para o view
# Pode existir inputs e print aqui

from models.aluno import Aluno
from models.turma import Turma
from views.menu_alunos import mostrar_lista_alunos
from controllers.turmas_controller import listar_turmas


def cadastrar_aluno():
    nome = input('Nome do aluno:')
    listar_turmas()
    turma_id = int(input('Id da turma:'))

    # Se não existir turma:
    # Se Turma.existe == False
    if not Turma.existe(turma_id):
        print('Erro: Turma não encontrada.')
        return

    else:
        aluno = Aluno(nome, turma_id)
        aluno.salvar()
        print(f'Aluno {nome} cadastrado com sucesso!')


def listar_alunos():
    # Solicita lista oa backend
    lista_alunos = Aluno.buscar_todos()
    # devolve lista
    return lista_alunos


def excluir_aluno():
    aluno_id = int(input("ID do aluno a ser excluido"))

    # Se o aluno não existe:
    # Verificar se o aluno existe
    if not Aluno.existe(aluno_id):
        print('Erro: Aluno não encontrada.')
        return
    else:
        Aluno.excluir(aluno_id)
        print(f'Aluno com id {aluno_id} excluido com sucesso!')

def alterar_turma():
    # Qual aluno_id
    aluno_id = int(input("ID do aluno: "))
    # Qual a nova turma?
    turma_id = int(input('Id da turma:'))

    if not Turma.existe(turma_id):
        print('Erro: Turma não encontrada.')
        return

    else:
        Aluno.alterar_turma(aluno_id, turma_id)
        print('Turma alterada com sucesso!')
