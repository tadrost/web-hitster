from flask import Flask, render_template, url_for, redirect, request
from app import app
from app.forms import EmptyForm
from random import randint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SCOPE = "user-read-currently-playing"
CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= CLIENT_ID,
                                               client_secret= CLIENT_SECRET,
                                               redirect_uri= REDIRECT_URI,
                                               scope=SCOPE))
@app.route('/')
def index():
    current_song = sp.currently_playing()
    if current_song is not None:
        current_song = current_song["item"]["name"]

    form = EmptyForm()
    return render_template('index.html', current_song=current_song, form=form)

# @app.route('/test')
# def test():
#     return f"""
# id: {CLIENT_ID}
# secret: {CLIENT_SECRET}
# redirect_uri: {REDIRECT_URI}"""