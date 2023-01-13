from scraper import scrap_artists_concerts, save_artists_concerts_json

if __name__ == "__main__":
    artists_concerts_dict = scrap_artists_concerts()
    save_artists_concerts_json(artists_concerts_dict)
