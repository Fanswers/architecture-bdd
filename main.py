from src.scraper import scrap_artists_concerts, save_artists_concerts_json
from src.spotify_api import get_token, get_spotify_info
from database.send_to_database import get_database, update_database

# 13/01/2023 3749329
if __name__ == "__main__":
    # Scrap concert site
    print("scraping starting")
    artists_concerts_dict = scrap_artists_concerts()
    print("scraping done")

    # Get spotify api token then get spotify data of each group
    spotify_auth = get_token()
    artists_concerts_dict = get_spotify_info(artists_concerts_dict, spotify_auth)

    # Write our dict in a json
    save_artists_concerts_json(artists_concerts_dict)

    # Create a connexion to our database and send the json file
    client = get_database()
    print("connected to database")

    # Init database
    # insert_json(client)

    # Update database
    update_database(client)
    print("database updated")
