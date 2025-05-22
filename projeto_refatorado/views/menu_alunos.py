
# Implementar um while que será o menu alunos
def menu_alunos():
    while True:
        print()
        print("-" * 12 + " Menu de Alunos " + "-" * 12)
        print("Escolha a opção desejada:")
        print("1 - Listar alunos")
        print("2 - Adicionar aluno")
        print("3 - Excluir aluno")
        print("4 - Atualizar turma do aluno")
        print("5 - Voltar")

        opt = int(input(">>"))
        if opt == 1:
            from controllers.alunos_controller import listar_alunos
            listar_alunos()
        elif opt == 2:
            # Só importa quando for realmente utilizar, é bom pois esse while vai ficar repetindo
            from controllers.alunos_controller import cadastrar_aluno
            cadastrar_aluno()
        elif opt == 3:
            # É importante listar os alunos antes de excluir
            from controllers.alunos_controller import listar_alunos
            listar_alunos()
            from controllers.alunos_controller import excluir_aluno
            excluir_aluno()
        elif opt == 4:
            # Alunos disponíveis
            from controllers.alunos_controller import listar_alunos
            listar_alunos()
            # Turmas disponíveis
            from controllers.turmas_controller import listar_turmas
            listar_turmas()
            from controllers.alunos_controller import alterar_turma
            alterar_turma()
        elif opt == 5:
            print("Voltando ao menu principal!")
            break
        else:
            print("Opção inválida!")


def mostrar_lista_alunos(lista_de_alunos):
    if not lista_de_alunos:
        print("Nenhum aluno cadastrado!")
        return
    else:
        print("Lista de Alunos:")
        for aluno in lista_de_alunos:
            print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Turma ID: {aluno[2]}')
