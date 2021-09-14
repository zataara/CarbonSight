## A collection of functions used with the Spotipy library
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import client_id, client_secret

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



