from .base import BaseRepository
from ..models import Track, Artist, Album

class TrackRepository(BaseRepository):
    def add_track(self, title: str, duration: float, album_id: int, artist_id: int) -> Track:
        new_track = Track(title=title, duration=duration, album_id=album_id, artist_id=artist_id)
        self.session.add(new_track)
        self.session.commit()
        return new_track

    def get_all_tracks(self):
        return self.session.query(Track).all()

    def get_track(self, track_id: int) -> Track:
        return self.session.query(Track).filter(Track.id == track_id).first()

    def update_track(self, track_id: int, title: str = None, duration: float = None, artist_id: int = None) -> Track:
        track = self.get_track(track_id)
        if track:
            if title is not None:
                track.title = title
            if duration is not None:
                track.duration = duration
            if artist_id is not None:
                track.artist_id = artist_id
            self.session.commit()
        return track

    def delete_track(self, track_id: int) -> None:
        track = self.get_track(track_id)
        if track:
            self.session.delete(track)
            self.session.commit()
