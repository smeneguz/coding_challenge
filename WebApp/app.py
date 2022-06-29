from http import client
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://MongoDB:27017")
db = client.projectDB
users = db["Users"]