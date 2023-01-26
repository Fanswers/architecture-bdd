from flask import Flask
from flask_restful import Resource, Api, reqparse
from database.send_to_database import get_database
from bson.json_util import dumps
import json

app = Flask(__name__)
api = Api(app)

# Allow us to get json argument from method
post_args = reqparse.RequestParser()
post_args.add_argument("_id", type=str)
post_args.add_argument("new_id", type=str)
post_args.add_argument("concerts", type=dict)
post_args.add_argument("spotify_id", type=str)
post_args.add_argument("followers", type=dict)
post_args.add_argument("popularity", type=int)


def get_collection():
    client = get_database()
    db = client['MusicProj']
    collection = db["Artists"]

    return collection

# All artists
class Artists(Resource):
    def get(self):
        collection = get_collection()

        cursor = collection.find()
        list_cur = list(cursor)

        return list_cur

    # Create One
    def post(self):
        args = post_args.parse_args()
        collection = get_collection()

        collection.insert_one({"_id": args['_id']})

    # Update One
    def put(self):
        args = post_args.parse_args()
        collection = get_collection()

        actual_values = collection.find_one({"_id": args["_id"]}, {"_id": 1, "spotify_id": 1, "popularity": 1})
        if args["new_id"] == "":
            args["new_id"] = actual_values["_id"]
        if args["spotify_id"] == "":
            args["spotify_id"] = actual_values["spotify_id"]
        if args["popularity"] == 0:
            args["popularity"] = actual_values["popularity"]

        collection.update_one({"_id": args['_id']}, {"$set": {"_id": args["_id"], "spotify_id": args["spotify_id"], "popularity": args["popularity"]}})

    # Delete One
    def delete(self):
        args = post_args.parse_args()
        collection = get_collection()

        collection.delete_one({"_id": args['_id']})


# Artist by name
class Artist(Resource):
    def get(self, artist_name):
        collection = get_collection()

        cursor = collection.find({"_id": artist_name})
        list_cur = list(cursor)

        return list_cur


# Artist concerts
class ArtistConcerts(Resource):
    def get(self, artist_name):
        collection = get_collection()

        cursor = collection.find({"_id": artist_name})
        concerts = cursor[0]["concerts"]

        return concerts


# Artist concert
class ArtistConcert(Resource):
    def get(self, artist_name, concert_date):
        collection = get_collection()

        cursor = collection.find({"_id": artist_name})
        concert = cursor[0]["concerts"][concert_date]

        return concert

    # Create One
    def post(self, artist_name, concert_date):
        args = post_args.parse_args()
        collection = get_collection()

        collection.update_one({"_id": artist_name}, {"$set": {f"concerts.{concert_date}": args["concerts"][concert_date]}})


api.add_resource(Artists, '/')
api.add_resource(Artist, '/<artist_name>')
api.add_resource(ArtistConcerts, '/<artist_name>/concerts')
api.add_resource(ArtistConcert, '/<artist_name>/concerts/<concert_date>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)