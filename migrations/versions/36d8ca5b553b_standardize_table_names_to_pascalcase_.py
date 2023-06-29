"""Standardize table names to PascalCase from snake_case

Revision ID: 36d8ca5b553b
Revises: bdd4bb2eaf3c
Create Date: 2023-06-13 12:31:50.855006

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "36d8ca5b553b"
down_revision = "bdd4bb2eaf3c"
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("tracks", "Tracks")
    op.rename_table("artist_tracks", "ArtistTracks")
    op.rename_table("history", "History")
    op.rename_table("users", "Users")
    op.rename_table("artists", "Artists")
    op.rename_table("track_popularity", "TrackPopularity")
    op.rename_table("spotify_tokens", "SpotifyTokens")
    op.rename_table("track_features", "TrackFeatures")


def downgrade():
    op.rename_table("Tracks", "tracks")
    op.rename_table("ArtistTracks", "artist_tracks")
    op.rename_table("History", "history")
    op.rename_table("Users", "users")
    op.rename_table("Artists", "artists")
    op.rename_table("TrackPopularity", "track_popularity")
    op.rename_table("SpotifyTokens", "spotify_tokens")
    op.rename_table("TrackFeatures", "track_features")
