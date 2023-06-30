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

IS_LOCAL = environ.get("IS_LOCAL", False)
# If IS_LOCAL, set the URL to localhost
# Otherwise, set the URL to the Docker container name
INSIGHTS_API_URL = (
    "http://localhost:5001" if IS_LOCAL else "http://songswap-insights:5001"
)

if DEBUG:
    print(f"{IS_LOCAL=},{INSIGHTS_API_URL=}")
