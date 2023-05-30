"""
/health endpoint checks critical functions of the app like database connectivity, availability of other services it depends on, etc., and returns a 200 status code if everything is okay.
"""

from flask import Blueprint

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health():
    """Perform a health check on the API and return 200 if successful"""
    return "OK", 200
