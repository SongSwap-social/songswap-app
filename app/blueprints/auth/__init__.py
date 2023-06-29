# auth/__init__.py
from . import routes, models, forms

auth_bp = routes.auth_bp
register_oauth = routes.register_oauth
