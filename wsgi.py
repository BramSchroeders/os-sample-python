from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import psycopg2

application = Flask(__name__)
CORS(application)
api = Api(application)

parser = reqparse.RequestParser()
parser.add_argument("task",type=list,location="json")

class HelloWorld(Resource):

    def get(self):
        return [{'id': 32, 'name' : 'Josh'}, {'id' : 42, 'name' : 'Also Josh'}]
    
    def post(self):
        args = parser.parse_args()
        task = {'task' : args["task"]}
        return task, 200

'''
class HelloWorld2(Resource):

    def get(self):
        try:
            conn = psycopg2.connect(host="postgresql://postgresql:5432/",dbname="sampledb", user="user0MQ", password="KQoVIps3xkOSLQ7t")
            cur = conn.cursor()
            cur.execute('SELECT * from heroes')
            ver = cur.fetchone()
            cur.close()
            conn.close()
            return ver
        except Exception as e:
            return {"msg" : str(e)}
    
    def post(self):
        args = parser.parse_args()
        task = {'task' : args["task"]}
        return task, 200
'''
api.add_resource(HelloWorld, '/')
#api.add_resource(HelloWorld2, '/help/')

if __name__ == "__main__":
    application.run()