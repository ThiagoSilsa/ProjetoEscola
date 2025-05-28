# Rotas do coordenador

from flask import Flask, Blueprint, render_template

# Criando o blueprint:
home_route = Blueprint('home', __name__)



@home_route.route('/', methods=['GET'])
def home():
    return render_template('index.html')



