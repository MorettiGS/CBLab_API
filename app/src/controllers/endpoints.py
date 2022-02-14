from flask import Flask, request
from flask_restx import Api, Resource
from src.server.instance import server
import json, datetime

app, api = server.app, server.api

file=open("./app/pedidos.json", "r", encoding="utf-8")
pedidos = json.load(file)
file.close()

def next_id():
    found, pos = searchId(pedidos["nextId"])
    while found:
        pedidos["nextId"]+=1
        found, pos = searchId(pedidos["nextId"])

def searchId(id):  
    for dict in pedidos["pedidos"]:
        if dict is not None:
            if dict['id'] == id:
                return True, pedidos["pedidos"].index(dict)
    return False, False

def searchStr(str,value):
    qnt=0
    for dict in pedidos["pedidos"]:
        if dict is not None and str in dict.keys():
            if dict[str].lower() == value.lower() and dict['entregue'] == True:
                qnt+=1
    return qnt

def dumpDB():
    with open('./app/pedidos.json', 'w', encoding='utf8') as file:
        json.dump(pedidos, file, ensure_ascii=False, indent=4)
    file.close()

def boolean(i):
    if pedidos["pedidos"][i]['entregue'].lower() == "true":
        pedidos["pedidos"][i]['entregue'] = True
    else:
        pedidos["pedidos"][i]['entregue'] = False

@api.route('/geral', methods=['GET'])
class consultarBD(Resource):
    def get(self, ):
        return pedidos

@api.route('/criar', methods=['POST'])
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
        dumpDB()

        return response, 200

@api.route('/atualizar', methods=['PUT'])
class atualizarPedido(Resource):
    def put(self, ):
        found, pos = searchId(int(request.args['id']))
        if found == False:
            raise Exception("Id do pedido não pode ser encontrado")
        else:
            pedidos["pedidos"][pos]['cliente'] = request.args.get('cliente')
            pedidos["pedidos"][pos]['produto'] = request.args.get('produto')
            pedidos["pedidos"][pos]['valor'] = round(float(request.args.get('valor')),2)
            pedidos["pedidos"][pos]['entregue'] = request.args.get('entregue')
            boolean(pos)
            response = pedidos["pedidos"][pos]
            dumpDB()
            return response, 200
    
@api.route('/statusEntrega', methods=['PUT'])
class atualizarEntrega(Resource):
    def put(self, ):
        found, pos = searchId(int(request.args['id']))
        if found == False:
            raise Exception("Id do pedido não pode ser encontrado")
        else:
            pedidos["pedidos"][pos]['entregue'] = request.args.get('entregue')
            boolean(pos)
            response = pedidos["pedidos"][pos]
            dumpDB()
            return response, 200

@api.route('/excluir', methods=['DELETE'])
class excluirPedido(Resource):
    def delete(self, ):
        found, pos = searchId(int(request.args['id']))
        if found == False:
            raise Exception("Id do pedido não pode ser encontrado")
        else:
            del pedidos["pedidos"][pos]
            dumpDB()
            return "Pedido excluído com sucesso", 200

@api.route('/consultar', methods=['GET'])
class consultarPedido(Resource):
    def get(self, ):
        found, pos = searchId(int(request.args['id']))
        if found == False:
            raise Exception("Id do pedido não pode ser encontrado")
        else:
            response = pedidos["pedidos"][pos]
            return response, 200

@api.route('/totalCliente', methods=['GET'])
class consultarTotalCliente(Resource):
    def get(self, ):
        qnt=searchStr("cliente", request.args.get("cliente"))
        return qnt, 200

@api.route('/totalProduto', methods=['GET'])
class consultarTotalProduto(Resource):
    def get(self, ):
        qnt=searchStr("produto", request.args.get("produto"))
        return qnt, 200

@api.route('/ordemProduto', methods=['GET'])
class consultarOrdemProduto(Resource):
    def get(self, ):
        dictVendidos, response={},{}
        for dict in pedidos["pedidos"]:
            if dict is not None and "produto" in dict.keys():
                if dict["produto"] not in dictVendidos.keys():
                    if searchStr("produto", dict["produto"]) != 0:
                        dictVendidos[dict["produto"]] = searchStr("produto", dict["produto"])
        for dict in sorted(dictVendidos, key=dictVendidos.get, reverse=True):
            response[dict] = dictVendidos[dict]
        return response, 200
        