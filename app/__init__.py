from flask import Flask
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config.from_object('config')

oauth = OAuth(app)

from app import views
