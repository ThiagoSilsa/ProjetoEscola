# Aplicando Flask ao projeto!
from flask import Flask

# Importar as rotas:
from controller.home_route import home_route
from controller.coordenador_route import coord_route


# Iniciar flask:
app = Flask(__name__)

# Registrar as rotas:
app.register_blueprint(home_route)
app.register_blueprint(coord_route, url_prefix = '/coord')

# Garantir execução apenas quando o arquivo for executado diretamente!
if __name__ == '__main__':
    app.run(debug=True)