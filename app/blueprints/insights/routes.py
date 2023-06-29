# app/blueprints/insights/routes.py
import requests
from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

insights_bp = Blueprint("insights", __name__)

TOP_LIMIT = 10


@insights_bp.route("/insights")
@login_required
def home():
    """Retrieve the user's top tracks from the songswap-insights API"""

    # Get the user's ID from the session
    user_id = current_user.id

    # Send a GET request to the songswap-insights API with the user's ID as an argument
    response = requests.get(
        f"http://127.0.0.1:5001/insights/top/tracks/{user_id}",
        params={"limit": TOP_LIMIT},
    )

    # If the response is not successful, raise an error
    if not response.ok:
        print(response.text)
        print(response.status_code)
        return abort(500)

    # Get the response data as JSON
    data = response.json()

    # Convert data['duration_ms'] to minutes and seconds
    for track in data:
        track[
            "duration_str"
        ] = f"{track['duration_ms'] // 60000}:{(track['duration_ms'] % 60000) // 1000:02}"

    # Render the template with the data
    # return render_template("insights.html", data=data)
    # Return the data as JSON
    return render_template("insights.html", tracks=data)


@insights_bp.route("/insights_global")
@login_required
def home_global():
    """Retrieve total and distinct statistics from songswap-insights API"""

    total_tracks = requests.get(f"http://127.0.0.1:5001/insights/global/total/listens")
    distinct_tracks = requests.get(
        f"http://127.0.0.1:5001/insights/global/distinct/tracks"
    )
    distinct_artists = requests.get(
        f"http://127.0.0.1:5001/insights/global/distinct/primary-artists"
    )
    total_listen_time = requests.get(
        f"http://127.0.0.1:5001/insights/global/total/listen-time",
        params={"as_string": True},
    )

    top_tracks = requests.get(
        "http://127.0.0.1:5001/insights/global/top/tracks", params={"limit": TOP_LIMIT}
    )
    top_artists = requests.get(
        "http://127.0.0.1:5001/insights/global/top/artists", params={"limit": TOP_LIMIT}
    )

    top_tracks_json = top_tracks.json()
    top_artists_json = top_artists.json()
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

    # Send a GET request to the songswap-insights API with the user's ID as an argument
    return render_template(
        "insights_global.html",
        total_tracks=total_tracks.json(),
        distinct_tracks=distinct_tracks.json(),
        distinct_artists=distinct_artists.json(),
        total_listen_time=total_listen_time.content.decode("utf-8").replace('"', ""),
        top_tracks=top_tracks,
        top_artists=top_artists,
    )
