from flask import redirect, request, url_for, session
from app import app, oauth

spotify = oauth.remote_app(
    "spotify",
    consumer_key=app.config["SPOTIFY_CLIENT_ID"],
    consumer_secret=app.config["SPOTIFY_CLIENT_SECRET"],
    request_token_params={"scope": "user-read-private user-read-email"},
    base_url="https://api.spotify.com/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.spotify.com/api/token",
    authorize_url="https://accounts.spotify.com/authorize",
)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    callback = app.config["SPOTIFY_REDIRECT_URI"]
    return spotify.authorize(callback=callback)


@app.route("/login/authorized")
def authorized():
    resp = spotify.authorized_response()
    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error_reason"],
            request.args["error_description"],
        )
    session["spotify_token"] = (resp["access_token"], "")
    me = spotify.get("me")
    return "Logged in as id=%s name=%s email=%s" % (
        me.data["id"],
        me.data["display_name"],
        me.data["email"],
    )


@spotify.tokengetter
def get_spotify_oauth_token():
    return session.get("spotify_token")
