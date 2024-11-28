from .base import BaseRepository
from ..models import Artist

class ArtistRepository(BaseRepository):
    def add_artist(self, name: str, country_id: int) -> Artist:
        new_artist = Artist(name=name, country_id=country_id)
        self.session.add(new_artist)
        self.session.commit()
        return new_artist

    def get_artist(self, artist_id: int) -> Artist:
        return self.session.query(Artist).filter(Artist.id == artist_id).first()

    def get_all_artists(self):
        return self.session.query(Artist).all()

    def update_artist(self, artist_id: int, name: str = None, country_id: int = None) -> Artist:
        artist = self.get_artist(artist_id)
        if artist:
            if name is not None:
                artist.name = name
            if country_id is not None:
                artist.country_id = country_id
            self.session.commit()
        return artist

    def delete_artist(self, artist_id: int) -> None:
        artist = self.get_artist(artist_id)
        if artist:
            self.session.delete(artist)
            self.session.commit()
