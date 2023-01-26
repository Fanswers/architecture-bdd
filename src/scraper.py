import requests
from bs4 import BeautifulSoup
import json


def artists_urls_to_dict():
    """
    Function that create a dictionary of 50 most popular artists on InfoConcert site.

    :return: Dictionary with artist as key and link of all of his concerts as value.
    """
    base_url = "https://www.infoconcert.com/artiste/les-plus-consultes.html"
    artists_urls = {}

    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    artists_names = soup.find_all("div", {"class": "top-line-name"})

    for artist in artists_names:
        artists_urls[artist.a.text] = f"https://www.infoconcert.com{artist.a['href']}"

    return artists_urls


def scrap_artists_concerts():
    """
    Function that will scrap spec of all concerts of all artists.

    :return: Dictionary of all concerts spec of all artists.
    """
    all_concerts = {}
    status = 0

    artists_urls = artists_urls_to_dict()
    for artist in artists_urls:
        page = requests.get(artists_urls[artist])
        soup = BeautifulSoup(page.text, 'html.parser')
        artist_concerts = soup.find_all("div", {"class": "panel panel-default date-line date-line-concert"})
        artist_concerts_dict = {"concerts": {}}

        for concert in artist_concerts:
            day = concert.find("div", {"class": "date"}).time['datetime']
            location = concert.find("div", {"class": "ville-dpt"}).span.text
            salle = concert.find("div", {"class": "salle"}).span.text

            try:
                price = concert.find("div", {"class": "col-xs-5 col-sm-12 price"}).text
            except:
                pass

            final_price = split_price(price)
            artist_concerts_dict["concerts"][day] = {"location": location, "salle": salle, "price": final_price}

        all_concerts[artist] = artist_concerts_dict

        # Scraping status
        status += 1
        print(f"scraping {(status/len(artists_urls))*100}% done")

    return all_concerts


def split_price(str_price):
    """
    Function that will clean price scraped.

    :param str_price: Price of the concert scraped
    :return: Average cleaned price
    """

    list_prices = str_price.split("à")
    list_prices = list(map(lambda x: "".join([ele for ele in x if ele.isdigit()]), list_prices))

    if list_prices[0] == '':
        list_prices = None
    elif len(list_prices) == 2:
        list_prices = (int(list_prices[0]) + int(list_prices[1])) / 2
    else:
        list_prices = int(list_prices[0])

    return list_prices


def save_artists_concerts_json(artists_concerts_dict):
    """
    Save dictionary as Json file

    :param artists_concerts_dict: Dictionary of all concerts of all artists
    """

    with open("./data/artists_concerts.json", "w") as outfile:
        json.dump(artists_concerts_dict, outfile)
