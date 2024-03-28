from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes(): # (GET) Exibe todos os clientes cadastrados
    todos_clientes = Cliente.select()
    return render_template('lista_clientes.html', usuarios = todos_clientes)

@cliente_route.route('/<int:id_cliente>') # (GET) Exibe o cliente com base no id 
def ver_cliente(id_cliente):
    usuario_obtido = Cliente.get_by_id(id_cliente)
    return render_template('cliente.html', usuario = usuario_obtido)


@cliente_route.route('/new') # (GET) Vai exibir o formulario de cadastro de clientes 
def form_cadastro_cliente():
    return render_template('cadastro_cliente.html')

@cliente_route.route('/', methods=["POST"]) # (POST) Vai receber os dados do formulario de clientes e vai validar e armazenar no database
def cadastro_cliente():
    try:
        data = request.json
        novo_cliente = Cliente.create(name = data['username'], email = data['email'])
        return render_template('item_cliente.html', usuario=novo_cliente)
    except:
        return render_template('item_cliente.html', email_existente = True)

@cliente_route.route('/edit/<int:id_cliente>') # (GET) Exibe o formulario para editar o cliente
def form_update_cliente(id_cliente):
    cliente = Cliente.get_by_id(id_cliente)
    return render_template('cadastro_cliente.html', cliente=cliente)

@cliente_route.route('/<int:id_cliente>', methods=['PUT']) # (PUT) Atualiza os dados de um cliente ja existente
def update_cliente(id_cliente):
    data = request.json
    cliente_editado = Cliente.get_by_id(id_cliente)
    cliente_editado.name = data['username']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', usuario=cliente_editado)

@cliente_route.route('/<int:id_cliente>', methods=['DELETE']) # (DELETE) Deleta um cliente
def deletar_cliente(id_cliente):
    Cliente.delete_by_id(id_cliente)
    return 'Usuário Deletado'

 

