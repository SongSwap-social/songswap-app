# app/blueprints/auth/routes.py
from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import login_manager
from app.database import db

from .forms import RegistrationForm
from .models import User
from .providers import SpotifyAuthProvider

auth_bp = Blueprint("auth", __name__)


@login_manager.unauthorized_handler
def unauthorized_callback():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for("auth.unauth_home"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route("/callback")
def spotify_callback():
    code = request.args.get("code")

    auth_provider = SpotifyAuthProvider()
    auth_provider.get_access_token(code, check_cache=False)
    me = auth_provider.me()

    spotify_id = me["id"]
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user:
        # User exists, log them in and redirect to authorized home page
        login_user(user)
        return redirect(url_for("auth.home"))
    else:
        # User does not exist, redirect to registration form
        # Store the tokens in the session
        session["spotify_id"] = spotify_id
        cached_tokens = auth_provider.get_cached_tokens()
        session["access_token"] = cached_tokens["access_token"]
        session["refresh_token"] = cached_tokens["refresh_token"]
        session["expires_at"] = cached_tokens["expires_at"]

        return redirect(url_for("auth.register"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # If user is authenticated, redirect to /home
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            spotify_id=session["spotify_id"],
            access_token=session["access_token"],
            refresh_token=session["refresh_token"],
            expires_at=session["expires_at"],
        )
        db.session.add(user)
        db.session.commit()

        # Remove the stored variables from the session
        session.pop("spotify_id", None)
        session.pop("access_token", None)
        session.pop("refresh_token", None)
        session.pop("expires_at", None)

        return redirect(url_for("auth.home"))

    return render_template("register.html", form=form)


@auth_bp.route("/")
def unauth_home():
    # If user is authenticated, redirect to /home
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))
    else:
        auth_provider = SpotifyAuthProvider()
        auth_url = auth_provider.get_authorize_url()
        return render_template("unauth_home.html", auth_url=auth_url)


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
