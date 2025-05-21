# Menu de modificação e atualização de turma:
from menus.menu_turmas.funcionalidades_turmas import Turma

def menu_turmas():
    while True:
        print()
        print("-" * 12 + " Menu de Turmas " + "-" * 12)
        print("Escolha a opção desejada:")
        print("1 - Listar turmas")
        print("2 - Adicionar turma")
        print("3 - Excluir turma")
        print("4 - Voltar")
        try:
            opt = int(input(">>"))
            if opt == 1:
                nova_turma = Turma("0", "0")
                nova_turma.listar_turmas()
            elif opt == 2:
                
                nova_turma = Turma("0", "0")
                nova_turma.listar_turmas()
                nome_turma = input('Digite o nome da turma:')
                serie_turma = input('Digite a série da turma:')
                nova_turma = Turma(nome_turma, serie_turma)
                nova_turma.salvar_no_banco()

            elif opt == 3:
                nova_turma = Turma("0", "0")
                nova_turma.listar_turmas()
                nova_turma.excluir_turma()

            elif opt == 4:
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida!")
        except:
            print("Algo deu errado!")
