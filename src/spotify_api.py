import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date


# Radiohead followers 7735381
def get_token():

    SPOTIPY_CLIENT_ID = "3cf5956ceada437082a9d61dd78b7691"
    SPOTIPY_CLIENT_SECRET = "4e08e1d5e7784738991bc0899ed7b553"

    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

    return spotify


def get_spotify_info(group_list, spotify):
    today = date.today()

    for group in group_list:
        results = spotify.search(q='artist:' + group, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            group_list[group]["spotify_id"], group_list[group]["followers"], group_list[group]["popularity"] = artist["id"], {today.strftime("%d/%m/%Y"): int(artist["followers"]["total"])}, artist["popularity"]

    return group_list


def set_artist_info(group_name):
    spotify = get_token()
    today = date.today()
    results = spotify.search(q='artist:' + group_name, type='artist')
    group_list = {"_id": group_name}
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        group_list["spotify_id"], group_list["followers"], group_list["popularity"] = artist["id"], {today.strftime("%d/%m/%Y"): int(artist["followers"]["total"])}, artist["popularity"]

    return group_list
