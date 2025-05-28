
## Db - Escola
# Tabela Alunos
    - id, nome, turma
        - Add aluno; ok
        - Listar alunos; ok
        - Excluir aluno; ok
# Tabela Turma (Sala)
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


## Conceitos utilizados
- Solid (S) = Apenas uma funcionalidade por método ou classe;
- Solid (O) = Aberto a expansão, fechado a modificação;
- Solid (L) = Filho usa tudo que o pai oferece;
- Herança;
- Agregação;
- Composição.


# primeiro: CRUD
- CREATE
- READ
- UPDATE
- DELETE

## Primeiras Melhorias:
    - Reorganização das pastas; ok
    - Implementação de métodos estáticos ou função externa; ok
    - Refatoração de try/except;
    - Singular para classes e plural para tabelas; ok
    - Nomes mais assertivos; ok
    - Docstrings;
    - Padronizar com Black; ok
    - Corrigir com try/except os menus

# Ordem:
    1 - Flask
    2 - PeeWee

    
# Aplicação de Flask para o front end
    # Rotas:
        - Home ('/') (GET) - Página principal!
        

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
            - Add aluno, turma, professor....
        - Menu Aluno:
            - Já é aluno?
            - Acessar suas aulas

