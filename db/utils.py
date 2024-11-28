from contextlib import contextmanager
from .models import Artist, Album, Track, Genre, AlbumGenreAssociation
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import DATABASE_URL
from flask import g


def get_engine(url=DATABASE_URL):
    return create_engine(url)


def get_sessionmaker(engine=None, autoflush: bool = True):
    if engine is None:
        engine = get_engine()
    return sessionmaker(engine, autoflush=autoflush)

def get_session():
    key_Session = "_Session"
    Session = getattr(g, key_Session, None)
    if not Session:
        Session = get_sessionmaker()
        setattr(g, key_Session, Session)
    return Session()

    