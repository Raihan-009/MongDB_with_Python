import pymongo
import random
from pymongo.mongo_client import MongoClient

cluster = MongoClient('mongodb+srv://admin:admin@cluster0.dcnym1g.mongodb.net/?retryWrites=true&w=majority')

db = cluster['videoInfo']

collection = db['videoInfo']

info = {"Videos": [
      {
        "category": "react",
        "video": [
          {
            "_id" : 1,
            "URL": "1234",
            "ID": "abcd",
            "KEYWORD": "Instalaltion"
          },
          {
            "_id" : 2,
            "URL": "12345",
            "ID": "efgh",
            "KEYWORD": "Documentaion"
          },
          {
            "_id" : 3,
            "URL": "12346",
            "ID": "ijkl",
            "KEYWORD": "Dependecies"
          }
        ]
      }
]}

collection.insert_one(info)