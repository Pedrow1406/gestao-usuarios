from flask import Blueprint, render_template, request
from database.clientes import CLIENTES
cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes(): # (GET) Exibe todos os clientes cadastrados
    return render_template('lista_clientes.html', usuarios=CLIENTES)

@cliente_route.route('/<int:id_cliente>') # (GET) Exibe o cliente com base no id 
def ver_cliente(id_cliente):
    return render_template('cliente.html')


@cliente_route.route('/new') # (GET) Vai exibir o formulario de cadastro de clientes 
def form_cadastro_cliente():
    return render_template('cadastro_cliente.html')

@cliente_route.route('/', methods=["POST"]) # (POST) Vai receber os dados do formulario de clientes e vai validar e armazenar no database
def cadastro_cliente():
    data = request.json
    novo_usuario = {"id":CLIENTES[-1]['id'] + 1, "nome":data['username'],"email": data['email']}
    CLIENTES.append(novo_usuario)
    print(request.json)
    return render_template('item_cliente.html', usuario=novo_usuario)

@cliente_route.route('/edit') # (GET) Exibe o formulario para editar o cliente
def form_update_cliente():
    return render_template('edit_cliente.html')

@cliente_route.route('/<int:id_cliente>', methods=['PUT']) # (PUT) Atualiza os dados de um cliente ja existente
def update_cliente(id_cliente):
    return 'Atualiza os dados de um cliente ja existente'

@cliente_route.route('/<int:id_cliente>', methods=['DELETE']) # (DELETE) Deleta um cliente
def deletar_cliente(id_cliente):
    global CLIENTES
    CLIENTES = [cliente for cliente in CLIENTES if cliente['id'] != id_cliente]
    return 'Usuário Deletado'



 

