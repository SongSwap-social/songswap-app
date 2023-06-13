"""Add cascading delete and update to History, ArtistTracks, and Tracks

This revision does two things:
1. Adds cascading delete and update to History, ArtistTracks, and Tracks
2. Adds a foreign key constraint to SpotifyTokens
    The foreign key is renamed with PascalCase to match the table name
    NOTE: Leave `create_foreign_key` as `None` to allow Alembic to generate a PascalCase name

Revision ID: manualrevision1
Revises:
Create Date: 2023-06-13 15:53:02.162055

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "manualrevision1"
down_revision = "36d8ca5b553b"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("SpotifyTokens") as batch_op:
        batch_op.drop_constraint("spotify_tokens_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "Users", ["id"], ["id"], ondelete="CASCADE", onupdate="CASCADE"
        )

    with op.batch_alter_table("History") as batch_op:
        batch_op.drop_constraint("history_user_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "Users", ["user_id"], ["id"], ondelete="CASCADE", onupdate="CASCADE"
        )
        batch_op.drop_constraint("history_track_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "Tracks", ["track_id"], ["id"], ondelete="CASCADE", onupdate="CASCADE"
        )

    with op.batch_alter_table("ArtistTracks") as batch_op:
        batch_op.drop_constraint("artist_tracks_artist_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None,
            "Artists",
            ["artist_id"],
            ["id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
        )
        batch_op.drop_constraint("artist_tracks_track_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "Tracks", ["track_id"], ["id"], ondelete="CASCADE", onupdate="CASCADE"
        )

    with op.batch_alter_table("TrackPopularity") as batch_op:
        batch_op.drop_constraint("track_popularity_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "Tracks", ["id"], ["id"], ondelete="CASCADE", onupdate="CASCADE"
        )

    with op.batch_alter_table("TrackFeatures") as batch_op:
        batch_op.drop_constraint("track_features_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "Tracks", ["id"], ["id"], ondelete="CASCADE", onupdate="CASCADE"
        )


def downgrade():
    # Define how to reverse the changes if needed
    with op.batch_alter_table("SpotifyTokens") as batch_op:
        batch_op.drop_constraint("SpotifyTokens_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key("spotify_tokens_id_fkey", "Users", ["id"], ["id"])

    with op.batch_alter_table("History") as batch_op:
        batch_op.drop_constraint("History_user_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            "history_user_id_fkey", "Users", ["user_id"], ["id"]
        )
        batch_op.drop_constraint("History_track_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            "history_track_id_fkey", "Tracks", ["track_id"], ["id"]
        )

    with op.batch_alter_table("ArtistTracks") as batch_op:
        batch_op.drop_constraint("ArtistTracks_artist_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            "artist_tracks_artist_id_fkey", "Artists", ["artist_id"], ["id"]
        )
        batch_op.drop_constraint("ArtistTracks_track_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            "artist_tracks_track_id_fkey", "Tracks", ["track_id"], ["id"]
        )

    with op.batch_alter_table("TrackPopularity") as batch_op:
        batch_op.drop_constraint("TrackPopularity_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(
            "track_popularity_id_fkey", "Tracks", ["id"], ["id"]
        )

    with op.batch_alter_table("TrackFeatures") as batch_op:
        batch_op.drop_constraint("TrackFeatures_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key("track_features_id_fkey", "Tracks", ["id"], ["id"])
