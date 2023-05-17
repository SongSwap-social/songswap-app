# app/blueprints/auth/providers.py
from abc import ABC, abstractmethod

import spotipy
from flask import Flask, current_app
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


class MusicAuthProvider(ABC):
    @abstractmethod
    def get_authorize_url(self):
        pass

    @abstractmethod
    def get_access_token(self, code):
        pass

    @abstractmethod
    def me(self):
        pass


class SpotifyAuthProvider(MusicAuthProvider):
    def __init__(self):
        self._spotify: Spotify = None

    @property
    def spotify(self):
        if self._spotify is None:
            self._spotify = self.create_spotify_client(current_app)
        return self._spotify

    def create_spotify_client(self, app: Flask) -> Spotify:
        """Create a Spotify client using the SpotifyOAuth flow."""
        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=app.config["SPOTIFY_CLIENT_ID"],
                client_secret=app.config["SPOTIFY_CLIENT_SECRET"],
                redirect_uri=app.config["SPOTIFY_REDIRECT_URI"],
                scope="user-read-email",
            )
        )

    def get_authorize_url(self):
        return self.spotify.auth_manager.get_authorize_url()

    def get_access_token(self, code: str, check_cache: bool = True):
        return self.spotify.auth_manager.get_access_token(code, check_cache=check_cache)

    def get_cached_tokens(self):
        return self.spotify.auth_manager.get_cached_token()

    def me(self):
        return self.spotify.me()
