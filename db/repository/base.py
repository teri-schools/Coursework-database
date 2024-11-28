from ..utils import get_session

class BaseRepository:
    @property
    def session(self):
        return get_session()
