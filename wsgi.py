from flask_restful import Resource, Api
from flask import Flask
from pymongo import MongoClient
import os

application = Flask(__name__)
api = Api(application)


class HelloWorld(Resource):

    def get(self):
        #client = MongoClient(os.environ['OPENSHIFT_NOSQL_DB_URL'])
        #client.close()
        '''
        dbs = client.db
        collection = dbs.test_collection
        out = collection.find_one()
        client.close()
        '''
        x = os.environ['MONGO_URL']
        return {'hello': 'world'}
        #return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

if __name__ == "__main__":
    application.run(debug=True)
        