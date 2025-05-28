# Rotas do coordenador

from flask import Blueprint, render_template, request
from models.aluno import Aluno
from models.turma import Turma

# Criando o blueprint:
coord_route = Blueprint('coord', __name__)


# Todas as rotas abaixo criadas irão aparecer após o prefixo mencionado no main.py
@coord_route.route('/', methods=['GET'])
def menu_coord():
    return render_template('menu_coord.html')


# --------------------------------------------
# Alunos

@coord_route.route('/alunos', methods=['GET', 'POST'])
def menu_alunos():
    return render_template('menu_alunos.html')


@coord_route.route('/alunos/listar', methods=['GET'])
def listar_alunos():
    # Solicita a lista de alunos ao backend 
    lista_alunos = Aluno.buscar_todos()
    # Enviando ao fragmento a lista de alunos
    return render_template('partials/aluno/lista_alunos.html', alunos=lista_alunos)

# _________________________________________________________________
@coord_route.route('/alunos/busca-por-turma', methods=['POST'])
def listar_alunos_turma():
    id = request.form.get('id')
    # Chegou o id da turma aqui
    # Buscar do back end a lista de alunos da turma em questão
    resultado = Aluno.buscar_por_turma(id)
    # Recebi lista de alunos
    # Devolvi lista de alunos
    return render_template('partials/aluno/aluno_por_turma.html', alunos = resultado)



@coord_route.route('/alunos/new', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        # Receber dados do formulário e salvar aluno
        nome = request.form.get('nome')
        turma_id = request.form.get('turma_id')
        novo_aluno = Aluno(nome, int(turma_id))
        novo_aluno.salvar()
        return menu_alunos()  
    else:
        # Mostrar o formulário
        return render_template('partials/aluno/form_add_aluno.html')
    

@coord_route.route('/alunos/del', methods=['GET', 'POST'])
def deletar_aluno():
    if request.method == 'POST':
        # Receber dados do formulário e salvar aluno
        aluno_id = int(request.form.get('id'))
        Aluno.excluir(aluno_id)
        return menu_alunos()
    else:
        # Mostrar o formulário
        return render_template('partials/aluno/form_del_aluno.html')




# --------------------------------------------


@coord_route.route('/turmas', methods=['GET'])
def menu_turmas():
    return render_template('menu_turmas.html')


@coord_route.route('/turmas/listar', methods=['GET'])
def listar_turmas():
    lista_turmas = Turma.buscar_todas()
    return render_template('partials/turma/lista_turmas.html', turmas=lista_turmas)

@coord_route.route('/turmas/buscar-turmas', methods=['GET'])
def buscar_turmas():
    # Banda a lista para o select_turmas
    lista_turmas = Turma.buscar_todas()
    return render_template('partials/turma/select_turmas.html', turmas=lista_turmas)


@coord_route.route('/turmas/new', methods=['GET', 'POST'])
def adicionar_turma():
    if request.method == 'POST':
        # Receber dados do formulário e salvar aluno
        nome = request.form.get('nome')
        serie = request.form.get('serie')
        nova_turma = Turma(nome, serie)
        nova_turma.salvar()
        return menu_turmas()  
    else:
        # Mostrar o formulário
        return render_template('partials/turma/form_add_turma.html')


@coord_route.route('/turmas/del', methods=['GET', 'POST'])
def deletar_turma():
    if request.method == 'POST':
        turma_id = int(request.form.get('id'))
        Turma.excluir(turma_id)
        return menu_turmas()
    else:
        # Mostrar o formulário
        return render_template('partials/turma/form_del_turma.html')
