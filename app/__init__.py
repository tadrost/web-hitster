import os

from flask import Flask
from config import Config

import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.config.from_object(Config)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=os.environ["SPOTIFY_SCOPE"], 
                                               client_id=os.environ["SPOTIFY_CLIENT_ID"], 
                                               client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
                                               redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"]))

from app import routes, forms