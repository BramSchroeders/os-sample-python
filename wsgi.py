from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from api_resource import HelloWorldExample

application = Flask(__name__)

if __name__ == "__main__":
    api = Api(application)
    CORS(application)
    application.add_resource(HelloWorldExample,"/hello")
    application.run()