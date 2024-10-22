from contextlib import contextmanager
from .models import Artist, Album, Track, Genre, AlbumGenreAssociation
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import DATABASE_URL


def get_engine(url=DATABASE_URL):
    return create_engine(url)


def get_sessionmaker(engine=None, autoflush: bool = True):
    if engine is None:
        engine = get_engine()
    return sessionmaker(engine, autoflush=autoflush)


class Crud:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()

    def get(self, model, **kwargs):
        return self.session.query(model).filter_by(**kwargs).first()

    def get_all(self, model, **kwargs):
        return self.session.query(model).filter_by(**kwargs).all()

    def create(self, model, **kwargs):
        obj = model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj

    def save(self, *objs):
        self.session.add_all(objs)
        self.session.commit()

    def update(self, model, filters: dict[str], values: dict[str]):
        self.session.query(model).filter_by(**filters).update(values)
        self.session.commit()

    def delete(self, model, **kwargs):
        self.session.query(model).filter_by(**kwargs).delete()
        self.session.commit()
