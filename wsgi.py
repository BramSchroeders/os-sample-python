from flask_restful import Resource, Api
from flask import Flask
application = Flask(__name__)
api = Api(application)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

if __name__ == "__main__":
    application.run()