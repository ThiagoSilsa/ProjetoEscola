# Menu principal do projeto!


while True:
    print()
    print("-" * 12 + " Menu principal " + "-" * 12)
    print(
        "Escolha a opção desejada:\n1 - Acessar Alunos\n2 - Acessar Turmas\n3 - Menu ADM  \n4 - Sair")
    try:
        opt = int(input(">>"))
        if opt == 1:
            menu_alunos()
        elif opt == 2:
            menu_turmas()
        elif opt == 3:
            menu_principal_adm()
        elif opt == 4:
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida!")
    except:
        print("Algo deu errado!")
