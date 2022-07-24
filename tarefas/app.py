from crypt import methods
from distutils.log import debug
from urllib import response
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Edigar',
        'tarefa': 'Desenvolver o método GET',
        'status': 'andamento'
    },
    {
        'id': 1,
        'responsavel': 'Israel',
        'tarefa': 'Desenvolver o método PUT',
        'status': 'pendente'
    }
]

#Consultar uma tarefa pelo ID, alterar e deletar.
@app.route('/tar/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try: 
            response = tarefas[id]
            return jsonify(response)
        except IndexError:
            mensagem = f'Tarefa de ID {id} não existe.'
            response = {
                'status': 'erro',
                'mensagem': mensagem
            }
            return jsonify(response)
        except Exception:
            mensagem = 'Erro desconhecido. Procuro o ADM da API.'
            response = {
                'status': 'erro',
                'mensagem': mensagem
            }
            return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        texto = dados['status']
        tarefas[id]['status'] = texto
        response = tarefas[id]
        return jsonify(response)
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({
            'status':'sucesso',
            'mensagem':'Registro Excluido'
        })

@app.route('/tar', methods=['GET', 'POST'])
def listar_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
if __name__ == '__main__':
    app.run(debug=True)