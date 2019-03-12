from flask import Flask
from flask_restful import Resource, Api, reqparse

application = Flask(__name__)
api = Api(application)

class HelloWorld(Resource):

    def get(self):
        return {'rate': 55}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')  
        args = parser.parse_args()
        return {"found" : args['rate']}

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    application.run()