import spotipy
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from spotipy.oauth2 import SpotifyOAuth


app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=app.config["SPOTIFY_CLIENT_ID"],
        client_secret=app.config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=app.config["SPOTIFY_REDIRECT_URI"],
        scope="user-read-email",
    )
)

from app import routes, models
