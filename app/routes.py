from flask import render_template, url_for, redirect, request, session
from app import app, spotify
from app.forms import EmptyForm
import spotipy

@app.route('/test')
def test(): #FOR TESTING PURPOSES! 
    return f"""TESTING PAGE""" 

@app.route('/')
def index():
    current_song = None
    if current_song is not None:
        current_song = current_song["item"]["name"]

    form = EmptyForm()
    return render_template('index.html', current_song=current_song, form=form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/spotify_login')
def spotify_login():
    auth_manager = spotify.make_oauth()
    return redirect(auth_manager.get_authorize_url())

@app.route('/callback')
def spotify_callback():
    auth_manager = spotify.make_oauth()
    code = request.args.get("code")

    if not code:
        return "Spotify login failed", 400

    token_info = auth_manager.get_access_token(code=code)
    session["spotify_token"] = token_info

    return redirect(url_for("playlists"))

@app.route('/playlists')
def playlists():
    token = session.get("spotify_token")
    if not token:
        return redirect(url_for("login"))

    sp = spotipy.Spotify(auth=token["access_token"])
    playlists = sp.current_user_playlists()

    playlist_names = []
    if playlists is not None:
        for playlist in playlists["items"]:
            playlist_names.append(playlist["name"])
    
    return render_template('playlists.html', playlists=playlist_names)