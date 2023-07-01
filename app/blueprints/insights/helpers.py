"""
Helper functions for the insights blueprint.

This module contains helper functions for the insights blueprint. These functions
are used to retrieve data from the songswap-insights API and format it for the
insights pages.

Functions
---------
get_top_tracks(limit)
    Retrieve the top tracks from the songswap-insights API.
get_top_artists(limit)
    Retrieve the top artists from the songswap-insights API.
get_top_genres(limit)
    Retrieve the top genres from the songswap-insights API.
"""

from typing import Any, Dict, Optional

import requests
from flask import abort

from config import INSIGHTS_API_URL

TOP_LIMIT = 10


def _get(
    endpoint: str, params: Optional[Dict[str, Any]] = None, as_json: bool = False
) -> Dict[str, Any]:
    """
    Send a GET request to the songswap-insights API.

    Args:
        endpoint (str): The URL to send the request to.
        params (Optional[Dict[str, Any]]): The parameters to send with the request.
        as_json (bool): Whether to return the response as JSON or not.

    Returns:
        The response from the songswap-insights API.

    Raises:
        Exception: If the response is not successful.
    """
    # Format the URL
    url = f"{INSIGHTS_API_URL}{endpoint}"

    # Send a GET request to the songswap-insights API with the user's ID as an argument
    response = requests.get(url, params=params)

    # If the response is not successful, raise an error
    if not response.ok:
        print(response.text)
        print(response.status_code)
        return abort(500)

    # If as_json is True, return the response as JSON
    if as_json:
        return response.json()
    return response


def get_top_tracks(user_id: int, limit: int = TOP_LIMIT):
    """
    Retrieve the top tracks from the songswap-insights API.

    Args:
        user_id (int): The ID of the user to retrieve the top tracks for.
        limit (int, optional): The number of tracks to retrieve. Defaults to 10.

    Returns:
        list: The top tracks.
    """
    response = _get(
        f"/insights/top/tracks/{user_id}", params={"limit": limit}, as_json=True
    )
    return response


def get_top_artists(user_id: int, limit: int = TOP_LIMIT):
    """
    Retrieve the top artists from the songswap-insights API.

    Args:
        user_id (int): The ID of the user to retrieve the top artists for.
        limit (int, optional): The number of artists to retrieve. Defaults to 10.

    Returns:
        list: The top artists.
    """
    response = _get(
        f"/insights/top/primary-artists/{user_id}",
        params={"limit": limit},
        as_json=True,
    )
    return response
