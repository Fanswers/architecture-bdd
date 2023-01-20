import pymongo
import json


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    client = pymongo.MongoClient("mongodb+srv://Admin:Admin@architecture-bdd.hgcnpfm.mongodb.net/?retryWrites=true&w=majority")
    return client


def split_json(json_dict):

    documents = []
    for key in json_dict:
        temporary_dict = json_dict[key]
        temporary_dict["_id"] = key
        documents.append(temporary_dict)
    return documents


def insert_json(client):
    db = client['MusicProj']
    collection = db["Artists"]

    with open('../data/artists_concerts.json') as file:
        file_data = json.load(file)
    documents = split_json(file_data)
    print(documents)
    collection.insert_many(documents)
