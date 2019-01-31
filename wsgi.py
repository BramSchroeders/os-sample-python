from flask_restful import Resource, Api
from flask import Flask
from pymongo import MongoClient
import os

application = Flask(__name__)
api = Api(application)


class HelloWorld(Resource):

    def get(self):
        client = MongoClient('mongodb://userF1A:XoPYB07S8CG8D8KV@mongodb/sampledb')
        #client.close()
        dbs = client.sampledb
        collection = dbs.test_collection
        out = {"stuff": list(collection.find())}
        client.close()
        return out
        #return {'hello': 'world'}
        
class PutIn(Resource):
    
    def get(self):
        client = MongoClient('mongodb://userF1A:XoPYB07S8CG8D8KV@mongodb/sampledb')
        #client.close()
        names = client.database_names()
        client.close()
        return {"message": list(names)}

api.add_resource(HelloWorld, '/hello')
api.add_resource(PutIn, '/putt')


if __name__ == "__main__":
    client = MongoClient('mongodb://userF1A:XoPYB07S8CG8D8KV@mongodb/sampledb')
    #client.close()
    dbs = client.sampledb
    collection = dbs.test_collection
    out = collection.insert_one({"hup":"hup"})
    client.close()
    application.run()
        