from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, backref, declarative_base, relationship


class Base(DeclarativeBase):
    metadata = MetaData()


# Association Table for Album and Artist (Many-to-Many relationship)
AlbumArtistAssociation = Table(
    "album_artist_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("artist_id", Integer, ForeignKey("artists.id"), primary_key=True),
)

AlbumGenreAssociation = Table(
    "album_genre_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    country_id = Column(
        Integer, ForeignKey("countries.id")
    )  # Normalized country reference

    albums = relationship(
        "Album", secondary=AlbumArtistAssociation, back_populates="artists"
    )
    tracks = relationship("Track", back_populates="artist")
    country = relationship(
        "Country", back_populates="artists"
    )  # Relationship to Country

    def __repr__(self):
        return f"<Artist(id={self.id}, name={self.name})>"


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    release_year = Column(Integer)
    label_id = Column(Integer, ForeignKey("labels.id"))

    label = relationship("Label", back_populates="albums")
    artists = relationship(
        "Artist", secondary=AlbumArtistAssociation, back_populates="albums"
    )
    genres = relationship(
        "Genre", secondary=AlbumGenreAssociation, back_populates="albums"
    )
    tracks = relationship("Track", back_populates="album")

    def __repr__(self):
        return f"<Album(id={self.id}, title={self.title}, release_year={self.release_year})>"


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    duration = Column(Float)  # Duration in minutes
    album_id = Column(Integer, ForeignKey("albums.id"))
    artist_id = Column(Integer, ForeignKey("artists.id"))

    album = relationship("Album", back_populates="tracks")
    artist = relationship("Artist", back_populates="tracks")

    def __repr__(self):
        return f"<Track(id={self.id}, title={self.title}, duration={self.duration})>"


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    albums = relationship(
        "Album", secondary=AlbumGenreAssociation, back_populates="genres"
    )

    def __repr__(self):
        return f"<Genre(id={self.id}, name={self.name})>"


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    country_id = Column(
        Integer, ForeignKey("countries.id")
    )  # Normalized country reference

    albums = relationship("Album", back_populates="label")
    country = relationship(
        "Country", back_populates="labels"
    )  # Relationship to Country

    def __repr__(self):
        return f"<Label(id={self.id}, name={self.name})>"


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    artists = relationship("Artist", back_populates="country")
    labels = relationship("Label", back_populates="country")

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"
