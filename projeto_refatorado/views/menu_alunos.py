
# Implementar um while que será o menu alunos
def menu_alunos():
    while True:
        print()
        print("-" * 12 + " Menu de Alunos " + "-" * 12)
        print("Escolha a opção desejada:")
        print("1 - Listar alunos")
        print("2 - Adicionar aluno")
        print("3 - Excluir aluno")
        print("4 - Voltar")
        try:
            opt = int(input(">>"))
            if opt == 1:
                aluno = Alunos("0", 0)
                aluno.listar_alunos()
            elif opt == 2:
                nome = input('Digite o nome do aluno:')
                nova_turma = Turma("0", "0")
                nova_turma.listar_turmas()
                turma = int(input('Digite o id da turma do aluno:'))
                novo_aluno = Alunos(nome, turma)
                novo_aluno.salvar_no_banco()

            elif opt == 3:
                aluno = Alunos("0", 0)
                aluno.listar_alunos()
                aluno.excluir_aluno()
            elif opt == 4:
                print("Finalizando programa...")
                break
            else:
                print("Opção inválida!")
        except:
            print("Algo deu errado!")
