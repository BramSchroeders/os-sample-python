from flask import Flask
from flask_restful import Resource, Api, reqparse

application = Flask(__name__)
api = Api(application)

parser = reqparse.RequestParser()
parser.add_argument('task', location='form')

class HelloWorld(Resource):

    def get(self):
        return {'rate': 32}
    
    def post(self):
        args = parser.parse_args()
        task = {'task': args['task']}
        return task

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    application.run()