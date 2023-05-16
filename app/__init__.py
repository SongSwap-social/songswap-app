# app/__init__.py
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate

from app.database import db

migrate = Migrate()
login_manager = LoginManager()


def create_app(config_object="config"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.blueprints.auth import auth_bp

    app.register_blueprint(auth_bp)

    return app
