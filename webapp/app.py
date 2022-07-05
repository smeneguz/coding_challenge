from distutils.log import debug
from http import client
from flask import Flask
from flask_restful import Api, Resource

from resource import Test, Register, RetrieveImg, Load

app = Flask(__name__)
api = Api(app)

api.add_resource(Test, '/test')
api.add_resource(Register, '/register')
api.add_resource(RetrieveImg, '/retrieve')
api.add_resource(Load, '/load')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)