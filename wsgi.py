from flask_restful import Resource, Api
from flask import Flask
from pymongo import MongoClient

application = Flask(__name__)
api = Api(application)


class HelloWorld(Resource):
    def get(self):
        
        try:
            client = MongoClient('mongodb://172.30.197.160:27017/', username="database-user", password="database-password")
            db = client.test_database
            collection = db.test_collection
            result = {"result" : list(collection.find())}
            return result
        except Exception as e:
            return {"msg":e.message}
        
        #return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

if __name__ == "__main__":
    client = MongoClient('mongodb://172.30.197.160:27017/', username="database-user", password="database-password")
    db = client.test_database
    collection = db.test_collection
    collection.insert_one({"message":"initial message"})
    client.close()
    application.run()