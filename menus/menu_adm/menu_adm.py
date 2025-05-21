# Nesse Menu eu posso adicionar ou excluir tabelas!

from menus.menu_adm.funcionalidades_adm import adicionar_tabela,excluir_tabelas,listar_tabelas

def sistema_de_senha(login: str, senha: str) -> bool:
    if login == "adm123" and senha == 2305:
        return True
    else:
        return False
    # conexão a partir de senha!



def menu_principal_adm():
    cone = False
    while True:
        print()
        print("-" * 12 + " Menu ADM " + "-" * 12)
        try:
            if cone == True:
                pass
            else :
                login = input('Login:')
                senha = int(input('Senha:'))
                if sistema_de_senha(login, senha):
                    print('Acesso autorizado!')
                    cone = True
                else:
                    print('Acesso Negado!')
                    print("Voltando ao menu principal")
                    break

            print(
                "Administrador, escolha a opção desejada:\n1 - Listar tabelas existentes\n2 - Adicionar tabela\n3 - Excluir tabelas \n4 - Sair do menu ADM")
            opt = int(input(">>"))
            if opt == 1:
                listar_tabelas()
            elif opt == 2:
                adicionar_tabela()
            elif opt == 3:
                excluir_tabelas()
            elif opt == 4:
                print("Finalizando o menu ADM...")
                break
            else:
                print("Opção inválida!")
        except:
            print("Algo deu errado!")
