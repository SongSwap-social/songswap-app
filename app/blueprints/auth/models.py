import flask_login

from app.database import db


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    spotify_id = db.Column(db.String(120), unique=True, nullable=False)
    # Define relationships with other models (e.g., posts, groups)

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
