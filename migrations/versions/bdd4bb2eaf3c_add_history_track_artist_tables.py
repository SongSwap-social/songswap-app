"""Add History, Track, Artist tables

Revision ID: bdd4bb2eaf3c
Revises: e381845baba9
Create Date: 2023-06-12 16:05:29.211087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdd4bb2eaf3c'
down_revision = 'e381845baba9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tracks',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('duration_ms', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artist_tracks',
    sa.Column('track_id', sa.String(length=24), nullable=False),
    sa.Column('artist_id', sa.String(length=24), nullable=False),
    sa.Column('is_primary', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('track_id', 'artist_id')
    )
    op.create_table('history',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('played_at', sa.DateTime(), nullable=False),
    sa.Column('track_id', sa.String(length=24), nullable=False),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('played_at')
    )
    op.create_table('track_features',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('acousticness', sa.Float(), nullable=False),
    sa.Column('danceability', sa.Float(), nullable=False),
    sa.Column('energy', sa.Float(), nullable=False),
    sa.Column('instrumentalness', sa.Float(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=False),
    sa.Column('liveness', sa.Float(), nullable=False),
    sa.Column('loudness', sa.Float(), nullable=False),
    sa.Column('mode', sa.Integer(), nullable=False),
    sa.Column('speechiness', sa.Float(), nullable=False),
    sa.Column('tempo', sa.Float(), nullable=False),
    sa.Column('time_signature', sa.Integer(), nullable=False),
    sa.Column('valence', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('track_popularity',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('popularity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('track_popularity')
    op.drop_table('track_features')
    op.drop_table('history')
    op.drop_table('artist_tracks')
    op.drop_table('tracks')
    op.drop_table('artists')
    # ### end Alembic commands ###
