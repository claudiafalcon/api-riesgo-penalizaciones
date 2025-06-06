from pymongo import MongoClient

def get_mongo_client():
    uri = "mongodb+srv://usuario:contraseña@cluster.mongodb.net/"
    return MongoClient(uri)
