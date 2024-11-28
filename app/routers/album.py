from flask import Blueprint, current_app as app
from flask import render_template, request, redirect, url_for
from db.models import Album, Artist, Genre, Label
from db.repository import AlbumRepository

bp = Blueprint("album", __name__)
album_repo = AlbumRepository()


@bp.route("/")
def catalog():
    albums = album_repo.get_all_album()
    return render_template("album/list.html", albums=albums)


@bp.route("/album/<int:album_id>")
def detail(album_id):
    album = album_repo.get_album(album_id)
    return render_template("album/info.html", album=album)


@bp.route("/album/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        release_year = request.form["release_year"]
        label_id = request.form["label_id"]
        artist_ids = request.form.getlist("artist_ids")
        genre_ids = request.form.getlist("genre_ids")

        album = album_repo.add_album(title=title, release_year=release_year, label_id=label_id, artist_ids=artist_ids, genre_ids=genre_ids)
        return redirect(url_for("index"))

    labels = app.crud.get_all(Label)
    artists = app.crud.get_all(Artist)
    genres = app.crud.get_all(Genre)
    return render_template(
        "album/create.html", labels=labels, artists=artists, genres=genres
    )


@bp.route("/album/edit/<int:album_id>", methods=["GET", "POST"])
def edit(album_id):
    album = album_repo.get_album(album_id)
    if request.method == "POST":
        album.title = request.form["title"]
        album.release_year = request.form["release_year"]
        album.label_id = request.form["label_id"]
        artist_ids = request.form.getlist("artist_ids")
        genre_ids = request.form.getlist("genre_ids")

        album_repo.update_album(album_id, title=album.title, release_year=album.release_year, label_id=album.label_id, artist_ids=artist_ids, genre_ids=genre_ids)
        return redirect(url_for("album.detail", album_id=album_id))

    labels = app.crud.get_all(Label)
    artists = app.crud.get_all(Artist)
    genres = app.crud.get_all(Genre)
    return render_template(
        "album/edit.html", album=album, labels=labels, artists=artists, genres=genres
    )


@bp.route("/album/delete/<int:album_id>", methods=["POST"])
def delete(album_id):
    album_repo.delete_album(album_id)
    return redirect(url_for("index"))
