from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from api_resource import HelloWorldExample

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
    application = Api(app)
    CORS(app)
    application.add_resource(HelloWorldExample,"/")
    app.run()