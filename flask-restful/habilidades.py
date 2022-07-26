from flask import request
from flask_restful import Resource
import json

lista_habilidades = [
    {
        "id":0,
        "habilidade": "Python",
    },
    {
        "id":1,
        "habilidade": "Flask",
    },
    {
        "id":2,
        "habilidade": "Java",
    }
]

#Altera e deleta uma habilidade pelo ID.
class Habilidades(Resource):
    def get(self, id):
        try: 
            response = lista_habilidades[id]
        except IndexError:
            mensagem = f'Habilidade de ID {id} não existe.'
            response = {
                'status': 'erro',
                'mensagem': mensagem
            }
        except Exception:
            mensagem = 'Erro desconhecido. Procuro o ADM da API.'
            response = {
                'status': 'erro',
                'mensagem': mensagem
            }
        return response

    def put(self, id):
        dados = json.loads(request.data)
        texto = dados['habilidade']
        lista_habilidades[id]['habilidade'] = texto
        return lista_habilidades[id]
    
    def delete(self, id):
        lista_habilidades.pop(id)
        return {
            'status':'sucesso',
            'mensagem':'Registro Excluido'
        }

#Lista todas as habilidade e permite registrar uma nova habilidade
class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados[id] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]
