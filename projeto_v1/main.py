# Menu principal do projeto!

while True:
    print()
    print("-" * 12 + " Menu principal " + "-" * 12)
    print(
        "Escolha a opção desejada:\n1 - Acessar Alunos\n2 - Acessar Turmas\n3 - Menu ADM  \n0 - Sair")

    opt = int(input(">>"))
    if opt == 1:
        from views.menu_alunos import menu_alunos
        menu_alunos()
    elif opt == 2:
        from views.menu_turmas import menu_turmas
        menu_turmas()
    elif opt == 3:
        from views.menu_adm import menu_adm
        menu_adm()
    elif opt == 0:
        print("Finalizando programa...")
        break
    else:
        print("Opção inválida!")
