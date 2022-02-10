from flask import Flask, request
from flask_restplus import Api, Resource
from src.server.instance import server

app, api = server.app, server.api

