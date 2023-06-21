from authlib.integrations.flask_client import OAuth
from flask import Blueprint, Flask, flash, redirect, render_template, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
import requests

from app import login_manager, oauth
from app.database import db

from .models import SpotifyTokens, Users

auth_bp = Blueprint("auth", __name__)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def register_oauth(app: Flask, oauth: OAuth):
    oauth.register(
        name="spotify",
        client_id=app.config["SPOTIFY_CLIENT_ID"],
        client_secret=app.config["SPOTIFY_CLIENT_SECRET"],
        access_token_url="https://accounts.spotify.com/api/token",
        access_token_params=None,
        authorize_url="https://accounts.spotify.com/authorize",
        authorize_params=None,
        api_base_url="https://api.spotify.com/v1/",
        client_kwargs={
            "scope": "user-library-read user-read-recently-played user-top-read user-read-currently-playing user-read-email"
        },
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    return Users.query.get(int(user_id))


@auth_bp.route("/spotify/login")
def spotify_login():
    """Redirect user to Spotify OAuth page to login and authorize the app."""
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))
    redirect_uri = url_for("auth.spotify_authorize", _external=True)
    print(redirect_uri)
    return oauth.spotify.authorize_redirect(redirect_uri)


@auth_bp.route("/spotify/authorize")
def spotify_authorize():
    """Get the user's Spotify info and create a new user if they don't exist."""
    token = oauth.spotify.authorize_access_token()  # Get access token
    response = oauth.spotify.get("me")  # Get user info
    try:
        spotify_info = response.json()
    except requests.exceptions.JSONDecodeError:
        logger.error("Failed to decode JSON from response")
        logger.error("Response Content: %s", response.content)
        if b"User not registered in the Developer Dashboard" in response.content:
            flash(
                "Please contact the site administrator to be added to the Developer Dashboard.",
                "danger",
            )
            return redirect(url_for("auth.unauth_home"))
        return "Error processing request", 400
    user = Users.query.filter_by(spotify_id=spotify_info["id"]).first()
    if not user:
        # User doesn't exist, create a new user
        user = Users(
            username=spotify_info["display_name"],
            email=spotify_info["email"],
            spotify_id=spotify_info["id"],
        )
        tokens = SpotifyTokens(
            id=user.id,
            access_token=token["access_token"],
            refresh_token=token["refresh_token"],
        )
        user.spotify_tokens = tokens  # Add relationship
        db.session.add(user)
        db.session.add(tokens)
        db.session.commit()
        flash("Account created!", "success")

    login_user(user)
    return redirect(url_for("auth.home"))


@login_manager.unauthorized_handler
def unauthorized_callback():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for("auth.unauth_home"))


@auth_bp.route("/")
def unauth_home():
    # If user is authenticated, redirect to /home
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))
    else:
        return render_template(
            "unauth_home.html", spotify_auth_url=url_for("auth.spotify_login")
        )


@auth_bp.route("/home")
@login_required
def home():
    return render_template("auth_home.html", user=current_user)


@auth_bp.route("/success")
@login_required
def success():
    return "Yes!"


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.unauth_home"))
