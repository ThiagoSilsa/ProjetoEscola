# Menu de modificação e atualização de turma:

def menu_turmas():
    while True:
        print()
        print("-" * 12 + " Menu de Turmas " + "-" * 12)
        print("Escolha a opção desejada:")
        print("1 - Listar turmas")
        print("2 - Adicionar turma")
        print("3 - Excluir turma")
        print("0 - Voltar")

        opt = int(input(">>"))
        if opt == 1:
            from controllers.turmas_controller import listar_turmas
            listar_turmas()
        elif opt == 2:
            from controllers.turmas_controller import cadastrar_turma
            cadastrar_turma()
        elif opt == 3:
            from controllers.turmas_controller import listar_turmas
            listar_turmas()
            from controllers.turmas_controller import excluir_turma
            excluir_turma()
        elif opt == 0:
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida!")

# exibir turmas


def mostrar_lista_turmas(lista_de_turmas):
    if not lista_de_turmas:
        print("Nenhuma turma cadastrado!")
        return
    else:
        print("Lista de Turmas")
        for turma in lista_de_turmas:
            print(f'ID: {turma[0]} | Nome: {turma[1]} | Turma ID: {turma[2]}')
