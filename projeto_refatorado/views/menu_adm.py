# Nesse Menu eu posso adicionar ou excluir tabelas!


def menu_adm():
    while True:
        print()
        print("-" * 12 + " Menu ADM " + "-" * 12)
        print("1 - Listar tabelas")
        print("2 - Adicionar tabela alunos")
        print("3 - Adicionar tabela turmas")
        print("4 - Excluir tabela alunos")
        print("5 - Excluir tabela turmas")
        print("0 - Voltar")

        opt = int(input(">>"))
        if opt == 1:
            from controllers.adm_controller import listar_tabelas
            listar_tabelas()
        elif opt == 2:
            from controllers.adm_controller import add_tabela_alunos
            add_tabela_alunos()
        elif opt == 3:
            from controllers.adm_controller import add_tabela_turmas
            add_tabela_turmas()
        elif opt == 4:
            from controllers.adm_controller import excluir_tabela_alunos
            excluir_tabela_alunos()
        elif opt == 5:
            from controllers.adm_controller import excluir_tabela_turmas
            excluir_tabela_turmas()
        elif opt == 0:
            print("Finalizando o menu ADM...")
            break
        else:
            print("Opção inválida!")


def mostrar_lista_tabelas(lista_tabelas):
    # Se a lista está vazia:
    if lista_tabelas == []:
        print('Não existem tabelas!')
    else:
        for i, tabela in enumerate(lista_tabelas):
            print(f'ID : {i} | Nome : {tabela[0]}')