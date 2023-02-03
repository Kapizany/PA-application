from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorldClass(Resource):
    def get(self):
        return {'hello': 'world'}

