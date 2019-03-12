from flask import Flask
from flask_restful import Resource, Api, reqparse
import datetime

application = Flask(__name__)
api = Api(application)

parser = reqparse.RequestParser()
parser.add_argument("task",location="json")

class HelloWorld(Resource):

    def get(self):
        return {'rate': 32}
    
    def post(self):
        args = parser.parse_args()
        task = {'task' : args["task"]}
        return task, 200#, {'Last-Modified': datetime.now(), 'Cache-Control' : 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0', 'Pragma': 'no-cache','Expires':'-1'}

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    application.run()