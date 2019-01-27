# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:16:32 2019

@author: brams
"""

from flask_restful import Resource

major = 0
minor = 0
patch = 1

class HelloWorldExample(Resource):
    
    def get(self):
        return {"message":"Hello World!"}
    
    @staticmethod
    def get_path():
        return "/api/v"+major+"-"+minor+"-"+patch+"/hello"