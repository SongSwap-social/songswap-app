from app.database import db


class History(db.Model):
    __tablename__ = "History"

    user_id = db.Column(
        db.Integer, db.ForeignKey("Users.id"), nullable=False, primary_key=True
    )
    played_at = db.Column(db.DateTime, nullable=False, primary_key=True)
    track_id = db.Column(db.String(24), db.ForeignKey("Tracks.id"), nullable=False)

    def __repr__(self):
        return f"History('{self.user_id}', '{self.played_at}', '{self.track_id}')"


class Artists(db.Model):
    __tablename__ = "Artists"

    id = db.Column(db.String(24), primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Artist('{self.name}')"


class Tracks(db.Model):
    __tablename__ = "Tracks"

    id = db.Column(db.String(24), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    duration_ms = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Track('{self.name}')"


class ArtistTracks(db.Model):
    __tablename__ = "ArtistTracks"

    track_id = db.Column(db.String(24), db.ForeignKey("Tracks.id"), primary_key=True)
    artist_id = db.Column(db.String(24), db.ForeignKey("Artists.id"), primary_key=True)
    is_primary = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return (
            f"ArtistTracks('{self.track_id}', '{self.artist_id}', '{self.is_primary}')"
        )


class TrackPopularity(db.Model):
    __tablename__ = "TrackPopularity"

    id = db.Column(db.String(24), db.ForeignKey("Tracks.id"), primary_key=True)
    date = db.Column(db.DateTime, nullable=False, primary_key=True)
    popularity = db.Column(db.Integer, nullable=False)


class TrackFeatures(db.Model):
    # https://developer.spotify.com/documentation/web-api/reference/get-audio-features
    __tablename__ = "TrackFeatures"

    id = db.Column(db.String(24), db.ForeignKey("Tracks.id"), primary_key=True)
    acousticness = db.Column(db.Float, nullable=False)
    danceability = db.Column(db.Float, nullable=False)
    energy = db.Column(db.Float, nullable=False)
    instrumentalness = db.Column(db.Float, nullable=False)
    key = db.Column(db.Integer, nullable=False)
    liveness = db.Column(db.Float, nullable=False)
    loudness = db.Column(db.Float, nullable=False)
    mode = db.Column(db.Integer, nullable=False)
    speechiness = db.Column(db.Float, nullable=False)
    tempo = db.Column(db.Float, nullable=False)
    time_signature = db.Column(db.Integer, nullable=False)
    valence = db.Column(db.Float, nullable=False)
