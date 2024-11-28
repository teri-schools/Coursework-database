from .base import BaseRepository
from ..models import Genre

class GenreRepository(BaseRepository):
    def add_genre(self, name: str) -> Genre:
        new_genre = Genre(name=name)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_genre(self, genre_id: int) -> Genre:
        return self.session.query(Genre).filter(Genre.id == genre_id).first()

    def update_genre(self, genre_id: int, name: str) -> Genre:
        genre = self.session.query(Genre).get(genre_id)
        if genre:
            genre.name = name
            self.session.commit()
        return genre

    def delete_genre(self, genre_id: int):
        genre = self.session.query(Genre).get(genre_id)
        if genre:
            self.session.delete(genre)
            self.session.commit()
