from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from api_resource import HelloWorldExample

application = Flask(__name__)

if __name__ == "__main__":
    application.run()
    api = Api(application)
    CORS(application)
    api.add_resource(HelloWorldExample,"/")
    application.run()