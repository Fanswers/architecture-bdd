import spotipy
import sys

from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = "3cf5956ceada437082a9d61dd78b7691"
SPOTIPY_CLIENT_SECRET = "4e08e1d5e7784738991bc0899ed7b553"

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET ))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist)

