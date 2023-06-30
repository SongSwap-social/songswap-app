# app/blueprints/insights/routes.py
import requests
from flask import Blueprint, render_template
from flask_login import current_user, login_required

from .helpers import _get, get_top_tracks

insights_bp = Blueprint("insights", __name__)


@insights_bp.route("/insights")
@login_required
def home():
    """Retrieve the user's top tracks from the songswap-insights API"""

    # Get the user's ID from the session
    user_id = current_user.id

    # Get the response data as JSON
    data = get_top_tracks(user_id)

    # Convert data['duration_ms'] to minutes and seconds
    for track in data:
        track[
            "duration_str"
        ] = f"{track['duration_ms'] // 60000}:{(track['duration_ms'] % 60000) // 1000:02}"

    # Render the template with the data
    return render_template("insights.html", tracks=data)


@insights_bp.route("/insights_global")
@login_required
def home_global():
    """Retrieve total and distinct statistics from songswap-insights API"""

    total_tracks_json = _get("/insights/global/total/listens", as_json=True)
    distinct_tracks_json = _get("/insights/global/distinct/tracks", as_json=True)
    distinct_artists_json = _get(
        "/insights/global/distinct/primary-artists", as_json=True
    )
    total_listen_time = _get(
        "/insights/global/total/listen-time",
        params={"as_string": True},
    )

    top_tracks_json = _get(
        "/insights/global/top/tracks",
        params={"limit": 10},
        as_json=True,
    )
    top_artists_json = _get(
        "/insights/global/top/artists",
        params={"limit": 10},
        as_json=True,
    )

    track_names = [track["track_name"] for track in top_tracks_json]
    artist_names = [track["artist_name"] for track in top_tracks_json]
    track_counts = [track["count"] for track in top_tracks_json]

    top_tracks = [
        {"track_name": track_name, "artist_name": artist_name, "count": count}
        for track_name, artist_name, count in zip(
            track_names, artist_names, track_counts
        )
    ]
    top_artists = [
        {"artist_name": artist["artist_name"], "count": artist["count"]}
        for artist in top_artists_json
    ]

    return render_template(
        "insights_global.html",
        total_tracks=total_tracks_json,
        distinct_tracks=distinct_tracks_json,
        distinct_artists=distinct_artists_json,
        total_listen_time=total_listen_time.content.decode("utf-8").replace('"', ""),
        top_tracks=top_tracks,
        top_artists=top_artists,
    )
