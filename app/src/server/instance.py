from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, title='Delivery API', description="Uma API simples para lidar com um sistema CRUD")
    
    def run(self,):
        self.app.run(
            port=5000,
            host="0.0.0.0"
        )

server = Server()