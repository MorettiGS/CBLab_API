from flask import Flask, request
from flask_restplus import Api, Resource
from src.server.instance import server
import json, datetime

app, api = server.app, server.api

file=open("pedidos.json", "r")
pedidos = json.load(file)
file.close()

def next_id():
    found, pos = search(pedidos["nextId"])
    while found:
        pedidos["nextId"]+=1
        found, pos = search(pedidos["nextId"])

def search(id):  
    for dict in pedidos["pedidos"]:
        if dict is not None:
            if dict['id'] == id:
                return True, pedidos["pedidos"].index(dict)
    return False, False

def dumpBD():
    file=open("pedidos.json", "w")
    json.dump(pedidos, file)
    file.close()

@api.route('/')
class consultarBD(Resource):
    def get(self, ):
        return pedidos

@api.route('/criar')
class criarPedido(Resource):
    def post(self, ):
        response = {
            "id": pedidos["nextId"],
            "cliente": request.args.get('cliente'),
            "produto": request.args.get('produto'),
            "valor": round(float(request.args.get('valor')),2),
            "entregue": False,
            "timestamp": datetime.datetime.now().isoformat()[:-3] + "Z"
        }

        pedidos["pedidos"].append(response)

        next_id()
        dumpBD()

        return response, 200



        