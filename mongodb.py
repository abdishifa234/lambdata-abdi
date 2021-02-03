

DB_url ="mongodb+srv://abdi:<password>@cluster0.djakb.mongodb.net/<dbname>?retryWrites=true&w=majority"
clent=pymongo.MongoClient(DB_url)


import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("abdi", default="OOPS")
DB_PASSWORD = os.getenv("Mare0191#", default="OOPS")
CLUSTER_NAME = os.getenv("cluster0.djakb", default="OOPS")

connection_uri = f"mongodb+srv://abdi:<password>@cluster0.djakb.mongodb.net/<dbname>?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))