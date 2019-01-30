from flask_restful import Resource, Api
from flask import Flask
from pymongo import MongoClient
import os

application = Flask(__name__)
api = Api(application)


class HelloWorld(Resource):

    def get(self):
        client = MongoClient('mongodb://user78M:iYNNx53CdEGAIu1I@mongodb/sampledb')
        #client.close()
        dbs = client.sampledb
        collection = dbs.test_collection
        out = collection.find_one()
        client.close()
        return out
        #return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

if __name__ == "__main__":
    client = MongoClient('mongodb://user78M:iYNNx53CdEGAIu1I@mongodb/sampledb')
    #client.close()
    dbs = client.sampledb
    collection = dbs.test_collection
    out = collection.insert_one({"hup":"hup"})
    client.close()
    application.run(debug=True)
        