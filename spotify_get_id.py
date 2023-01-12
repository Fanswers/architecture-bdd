import spotipy
import sys

from collections import defaultdict

import requests
from spotipy.oauth2 import SpotifyClientCredentials


# Radiohead followers 7731689

def get_token():

    # Remplacez {client_id} et {client_secret} par votre propre ID de client et secret de client
    client_id = "3cf5956ceada437082a9d61dd78b7691"
    client_secret = "4e08e1d5e7784738991bc0899ed7b553"

    # Demande un jeton d'accès
    response = requests.post("https://accounts.spotify.com/api/token", {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    })

    ## Récupère le jeton d'accès de la réponse
    #access_token = response.json()["access_token"]
    ## Envoie une requête à l'API en utilisant le jeton d'accès
    #response = requests.get("https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers={
    #    "Authorization": f"Bearer {access_token}"
    #})

    ## Affiche le résultat de la requête
    #print(response.json())
    return response


def get_spotify_id(group_list):
    dict_group = defaultdict(defaultdict)
    for group in group_list:
        SPOTIPY_CLIENT_ID = "3cf5956ceada437082a9d61dd78b7691"
        SPOTIPY_CLIENT_SECRET = "4e08e1d5e7784738991bc0899ed7b553"

        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
        results = spotify.search(q='artist:' + group, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            dict_group[artist['name']]["id"], dict_group[artist['name']]["followers"], dict_group[artist['name']]["popularity"] = artist["id"], int(artist["followers"]["total"]), artist["popularity"]
    print(dict_group)
    return dict_group


group_list = ["Radiohead", "FEU! CHATTERTON"]

get_spotify_id(group_list)
get_token()