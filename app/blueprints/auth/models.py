import flask_login

from app.database import db


class Users(db.Model, flask_login.UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    spotify_id = db.Column(db.String(120), unique=True, nullable=False)
    spotify_tokens = db.relationship(  # Create a relationship between Users and SpotifyTokens
        "SpotifyTokens",
        backref="users",  # Create a back reference so we can access the Users from SpotifyTokens
        lazy=True,  # Don't load tokens unless requested
        uselist=False,  # Only one SpotifyTokens per user
        cascade="all, delete",  # Delete SpotifyTokens when a user is deleted
    )
    history = db.relationship("History", backref="user", lazy=True)

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
        return f"Users('{self.username}', '{self.email}', '{self.spotify_id}')"


class SpotifyTokens(db.Model):
    __tablename__ = "spotify_tokens"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    access_token = db.Column(db.String(256), unique=True, nullable=False)
    refresh_token = db.Column(db.String(256), unique=True, nullable=False)
