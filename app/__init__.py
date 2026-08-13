import os

from flask import Flask
from config import Config

import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.config.from_object(Config)

from app import routes, forms