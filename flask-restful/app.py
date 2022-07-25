from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Edigar',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Goncalves',
        'habilidades': ['Python', 'Django']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try: 
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
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

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Desenvolvedor, '/dev/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)