"""Create new Image, Popularity, Genre, Follower tables; Add cascade delete/update

Revision ID: 86cecbe1fd2b
Revises: manualrevision1
Create Date: 2023-06-26 19:49:05.481572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86cecbe1fd2b'
down_revision = 'manualrevision1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ArtistFollowers',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('followers', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['Artists.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    op.create_table('ArtistGenres',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('genre', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['Artists.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'genre')
    )
    op.create_table('ArtistImages',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=240), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['Artists.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'height', 'width')
    )
    op.create_table('ArtistPopularity',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('popularity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['Artists.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    op.create_table('TrackImages',
    sa.Column('id', sa.String(length=24), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=240), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['Tracks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'height', 'width')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TrackImages')
    op.drop_table('ArtistPopularity')
    op.drop_table('ArtistImages')
    op.drop_table('ArtistGenres')
    op.drop_table('ArtistFollowers')
    # ### end Alembic commands ###
