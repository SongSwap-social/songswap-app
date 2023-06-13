from flask import Blueprint
from flask_login import login_required

history_bp = Blueprint("history", __name__)


@history_bp.route("/history")
@login_required
def history():
    """Show the user's listening history"""
    return "History"
