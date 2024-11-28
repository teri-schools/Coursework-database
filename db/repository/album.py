from .base import BaseRepository
from ..models import Album, Artist, Genre

class AlbumRepository(BaseRepository):
    def add_album(self, title: str, release_year: int, label_id: int, artist_ids: list, genre_ids: list) -> Album:
        new_album = Album(title=title, release_year=release_year, label_id=label_id)
        new_album.artists = [self.session.query(Artist).get(artist_id) for artist_id in artist_ids]
        new_album.genres = [self.session.query(Genre).get(genre_id) for genre_id in genre_ids]
        self.session.add(new_album)
        self.session.commit()
        return new_album
    
    def get_all_album(self):
        return self.session.query(Album).all()

    def get_album(self, album_id: int) -> Album:
        return self.session.query(Album).filter(Album.id == album_id).first()

    def update_album(self, album_id: int, title: str = None, release_year: int = None, label_id: int = None, artist_ids: list = None, genre_ids: list = None) -> Album:
        album = self.get_album(album_id)
        if album:
            if title is not None:
                album.title = title
            if release_year is not None:
                album.release_year = release_year
            if label_id is not None:
                album.label_id = label_id
            if artist_ids is not None:
                album.artists = [self.session.query(Artist).get(artist_id) for artist_id in artist_ids]
            if genre_ids is not None:
                album.genres = [self.session.query(Genre).get(genre_id) for genre_id in genre_ids]
            self.session.commit()
        return album

    def delete_album(self, album_id: int) -> None:
        album = self.get_album(album_id)
        if album:
            self.session.delete(album)
            self.session.commit()
