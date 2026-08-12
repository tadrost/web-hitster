from flask import Flask, render_template, url_for, redirect, request
from app import app, spotify
from app.forms import EmptyForm
from random import randint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

@app.route('/')
def index():
    current_song = None
    if current_song is not None:
        current_song = current_song["item"]["name"]

    form = EmptyForm()
    return render_template('index.html', current_song=current_song, form=form)

@app.route('/test')
def test():
    currently_playing = spotify.currently_playing()
    if currently_playing:
        song = currently_playing["item"]["name"]
        album = currently_playing["item"]["album"]["name"]
    else: song = album = None
    return render_template('test.html', song=song, album=album) 