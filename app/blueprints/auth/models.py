import flask_login

from app.database import db


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    spotify_id = db.Column(db.String(120), unique=True, nullable=False)
    spotify_tokens = db.relationship(  # Create a relationship between User and SpotifyTokens
        "SpotifyTokens",
        backref="user",  # Create a back reference so we can access the User from SpotifyTokens
        lazy=True,  # Don't load tokens unless requested
        uselist=False,  # Only one SpotifyTokens per user
    )

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.spotify_id}')"


class SpotifyTokens(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    spotify_id = db.Column(db.String(120), unique=True, nullable=False)
    access_token = db.Column(db.String(120), unique=True, nullable=False)
    refresh_token = db.Column(db.String(120), unique=True, nullable=False)
