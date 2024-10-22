from faker import Faker
from sqlalchemy.orm.session import Session

from db.models import Album, Artist, Country, Genre, Label, Track

fake = Faker()


def create_fake_data(session: Session, num_records=10):
    countries = [Country(name=fake.country()) for _ in range(num_records)]
    session.add_all(countries)
    session.commit()

    genres = [Genre(name=fake.name()) for _ in range(num_records)]
    session.add_all(genres)
    session.commit()

    labels = [
        Label(name=fake.company(), country=fake.random_element(countries))
        for _ in range(num_records)
    ]
    session.add_all(labels)
    session.commit()

    artists = [
        Artist(name=fake.name(), country=fake.random_element(countries))
        for _ in range(num_records)
    ]
    session.add_all(artists)
    session.commit()

    albums = []
    for _ in range(num_records):
        album = Album(
            title=fake.sentence(nb_words=3),
            release_year=fake.year(),
            label=fake.random_element(labels),
        )
        album.artists.extend(
            fake.random_elements(artists, unique=True, length=fake.random_int(1, 3))
        )
        album.genres.extend(
            fake.random_elements(genres, unique=True, length=fake.random_int(1, 3))
        )
        albums.append(album)
    session.add_all(albums)
    session.commit()

    tracks = []
    for album in albums:
        for _ in range(fake.random_int(8, 15)):
            track = Track(
                title=fake.sentence(nb_words=4),
                duration=fake.pyfloat(
                    left_digits=2, right_digits=2, min_value=1.5, max_value=6.5
                ),
                album=album,
                artist=fake.random_element(album.artists),
            )
            tracks.append(track)
    session.add_all(tracks)
    session.commit()


if __name__ == "__main__":
    from db.crud import get_sessionmaker

    sessionmaker = get_sessionmaker(autoflush=False)

    session = sessionmaker()
    create_fake_data(session, num_records=10)
    session.close()
