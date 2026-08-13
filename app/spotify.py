from flask import session
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheHandler
import os

class SessionCacheHandler(CacheHandler):
    def __init__(self, session_obj):
        self.session_obj = session_obj

    def get_cached_token(self):
        return self.session_obj.get("spotify_token")

    def save_token_to_cache(self, token_info):
        self.session_obj["spotify_token"] = token_info

    def remove_cached_token(self):
        self.session_obj.pop("spotify_token", None)

def make_oauth():
    return SpotifyOAuth(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
        scope="playlist-read-private playlist-read-collaborative",
        cache_handler=SessionCacheHandler(session)
    )