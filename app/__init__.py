# app/__init__.py
from authlib.integrations.flask_client import OAuth
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from app.database import db

migrate = Migrate()
login_manager = LoginManager()
oauth = OAuth()


def create_app(config_object="config"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)

    from app.blueprints.auth import auth_bp, register_oauth
    from app.blueprints.insights import insights_bp
    from app.blueprints.health import health_bp
    from app.blueprints.history import history_bp

    register_oauth(app, oauth)

    app.register_blueprint(auth_bp)
    app.register_blueprint(insights_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(history_bp)

    return app
