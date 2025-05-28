
## Db - Escola
# Tabela Alunos ok
    - id, nome, turma
        - Add aluno; ok
        - Listar alunos; ok
        - Excluir aluno; ok
# Tabela Turma (Sala) ok
    - id, nome ("912"), serie(ano)
        - Add turma; ok
        - Mostrar turmas; ok
        - Excluir turmas; ok

# Tabela Professores
    - id, nome, disciplina, "turmas que dá aula"


## Menu ADM: OK
- Listar tabelas; ok
- Selecionar tabela; ok
- Excluir tabelas; ok


## Conceitos utilizados ok
- Solid (S) = Apenas uma funcionalidade por método ou classe;
- Solid (O) = Aberto a expansão, fechado a modificação;
- Solid (L) = Filho usa tudo que o pai oferece;
- Herança;
- Agregação;
- Composição.


# primeiro: CRUD ok
- CREATE
- READ
- UPDATE
- DELETE

# Primeiras Melhorias: ok
    - Reorganização das pastas; ok
    - Implementação de métodos estáticos ou função externa; ok
    - Singular para classes e plural para tabelas; ok
    - Nomes mais assertivos; ok
    - Padronizar com Black; ok




# Segundas melhorias:
    - Relacionamento aluno turma:
        - Conseguir um select por turma ok
        - Buscar aluno por turma ok
    - Edição de alunos/turmas
        - alterar turma do aluno 
    - Validação dos formulários
        - exibir mensagens de erro em html
        - verificar se a turma existe
    - Feedback
        - Turma deletada, turma excluinda, aluno adicionado...
    - Organização de código
    - interface
    - Autenticação


# Ordem:
    1 - Flask
    2 - PeeWee

    
# Aplicação de Flask para o front end
    # Rotas:
        - Home ('/') (GET) - Página principal!
        - Administrador (/coord) - (GET) - Entra no Menu coord
        - Administrador (/coord/aluno) - (GET) - Menu coord aluno
            - Escolher entre:
            - Menu aluno
            - Menu turmas
        - Administrador (/coord/aluno/new) - (POST) - Adicionar aluno
        - Administrador (/coord/aluno/new) - (GET) - Mostrar lista de alunos
        - Administrador (/coord/aluno/delete) - (DELETE) - Adicionar aluno

        - Administrador (/coord/turmas) - (GET) - Menu coord aluno
            - Escolher entre:
            - Menu aluno
            - Menu turmas
        - Administrador (/coord/turmas/new) - (POST) - Adicionar turma
        - Administrador (/coord/turmas/new) - (GET) - Mostrar lista de turmas
        - Administrador (/coord/turmas/delete) - (DELETE) - Adicionar turma

        

# Front-End
    Páginas:
        - Home: 
            - Redes sociais;
            - Sobre a escola;
            - Portal do aluno;
            - Portal adm;
            - Unidades;
            - Informações importantes embaixo.
        - Menu adm
            - Menu aluno
        - Menu Aluno:
            - Já é aluno?
            - Acessar suas aulas


    

