from models.turma import Turma
from views.menu_turmas import mostrar_lista_turmas


def listar_turmas():
    # Receber lista
    lista_de_turmas = Turma.buscar_turmas()
    # Mandar lista pro front
    mostrar_lista_turmas(lista_de_turmas)


def cadastrar_turma():
    # nome, série
    # Acessar banco de dados
    nome = input('Nome da turma:')
    serie = input('Série da turma:')

    turma = Turma(nome, serie)
    turma.salvar()
    print('Turma cadastrada com sucesso!')


def excluir_turma():
    # Qual id?
    turma_id = int(input('ID da turma a ser excluida'))
    # Verificar se a turma existe
    if not Turma.existe(turma_id):
        # Se turma não existe, não tem oq excluir
        print('Turma inexistente!')
        return
    else:
        Turma.excluir(turma_id)
        print(f'A turma com id : {turma_id} foi excluida com sucesso!')
    # Se turma existe: Exclui
