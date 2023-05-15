from flask import render_template, redirect, url_for, request, session
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from app import app, db, sp
from app.models import User
from app.forms import RegistrationForm

login_manager = LoginManager(app)
login_manager.login_view = "/home"


@login_manager.unauthorized_handler
def unauthorized_callback():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for("unauth_home"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/callback")
def spotify_callback():
    code = request.args.get("code")
    sp.auth_manager.get_access_token(code, check_cache=False)
    me = sp.me()

    spotify_id = me["id"]
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user:
        # User exists, log them in and redirect to authorized home page
        login_user(user)
        return redirect(url_for("home"))
    else:
        # User does not exist, redirect to registration form
        # Store the tokens in the session
        session["spotify_id"] = spotify_id
        session["access_token"] = sp.auth_manager.get_cached_token()["access_token"]
        session["refresh_token"] = sp.auth_manager.get_cached_token()["refresh_token"]
        session["expires_at"] = sp.auth_manager.get_cached_token()["expires_at"]

        return redirect(url_for("register"))


@app.route("/register", methods=["GET", "POST"])
def register():
    # If user is authenticated, redirect to /home
    if current_user.is_authenticated:
        return redirect(url_for("home"))

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

        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.route("/")
def unauth_home():
    # If user is authenticated, redirect to /home
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    else:
        auth_url = sp.auth_manager.get_authorize_url()
        return render_template("unauth_home.html", auth_url=auth_url)


@app.route("/home")
@login_required
def home():
    return render_template("auth_home.html", user=current_user)


@app.route("/success")
@login_required
def success():
    return "Yes!"


@app.route("/groups")
@login_required
def groups():
    pass


@app.route("/insights")
@login_required
def insights():
    pass


@app.route("/notifications")
@login_required
def notifications():
    pass


@app.route("/profile")
@login_required
def profile():
    pass


@app.route("/settings")
@login_required
def settings():
    pass


@app.route("/account")
@login_required
def account():
    pass


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("unauth_home"))
