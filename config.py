from os import environ, path
from dotenv import load_dotenv

# load up .env variables if the file exists
if path.exists(".env"):
    load_dotenv(".env")

DEBUG = environ.get("DEBUG")
SECRET_KEY = environ.get("SECRET_KEY")
SPOTIFY_CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = environ.get("SPOTIFY_REDIRECT_URI")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
