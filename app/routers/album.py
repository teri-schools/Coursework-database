from flask import Blueprint, current_app as app
from flask import render_template, request, redirect, url_for
from db.models import Album, Artist, Genre, Label

bp = Blueprint("album", __name__)


@bp.route("/")
def catalog():
    albums = app.crud.get_all(Album)
    return render_template("album/list.html", albums=albums)


@bp.route("/album/<int:album_id>")
def detail(album_id):
    album = app.crud.get(Album, id=album_id)
    return render_template("album/info.html", album=album)


@bp.route("/album/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        release_year = request.form["release_year"]
        label_id = request.form["label_id"]
        artist_ids = request.form.getlist("artist_ids")
        genre_ids = request.form.getlist("genre_ids")

        album = Album(title=title, release_year=release_year, label_id=label_id)
        album.artists = [app.crud.get(Artist, id=artist_id) for artist_id in artist_ids]
        album.genres = [app.crud.get(Genre, id=genre_id) for genre_id in genre_ids]

        app.crud.save(album)
        return redirect(url_for("index"))

    labels = app.crud.get_all(Label)
    artists = app.crud.get_all(Artist)
    genres = app.crud.get_all(Genre)
    return render_template(
        "album/create.html", labels=labels, artists=artists, genres=genres
    )


@bp.route("/album/edit/<int:album_id>", methods=["GET", "POST"])
def edit(album_id):
    album = app.crud.get(Album, id=album_id)
    if request.method == "POST":
        album.title = request.form["title"]
        album.release_year = request.form["release_year"]
        album.label_id = request.form["label_id"]
        artist_ids = request.form.getlist("artist_ids")
        genre_ids = request.form.getlist("genre_ids")

        album.artists = [app.crud.get(Artist, id=artist_id) for artist_id in artist_ids]
        album.genres = [app.crud.get(Genre, id=genre_id) for genre_id in genre_ids]

        app.crud.update(album)
        return redirect(url_for("album_detail", album_id=album_id))

    labels = app.crud.get_all(Label)
    artists = app.crud.get_all(Artist)
    genres = app.crud.get_all(Genre)
    return render_template(
        "album/edit.html", album=album, labels=labels, artists=artists, genres=genres
    )


@bp.route("/album/delete/<int:album_id>", methods=["POST"])
def delete(album_id):
    app.crud.delete(Album, id=album_id)
    return redirect(url_for("index"))
