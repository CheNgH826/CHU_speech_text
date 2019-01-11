from pymongo import MongoClient
from pprint import pprint

# Connect with MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')

pprint(list(mongo_client.log.user_answers.find({}).limit(5)))