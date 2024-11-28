from flask import render_template, request, redirect, url_for
from db.models import Artist, Country
from flask import Blueprint, current_app as app
from db.repository.artist import ArtistRepository

bp = Blueprint("artist", __name__)
artist_repo = ArtistRepository()


@bp.route("/artists")
def catalog():
    artists = artist_repo.get_all_artists()
    return render_template("artist/list.html", artists=artists)


@bp.route("/artist/<int:artist_id>")
def detail(artist_id):
    artist = artist_repo.get_artist(artist_id)
    return render_template("artist/info.html", artist=artist)


@bp.route("/artist/edit/<int:artist_id>", methods=["GET", "POST"])
def edit(artist_id):
    if request.method == "POST":
        artist_repo.update_artist(
            artist_id, name=request.form["name"], country_id=request.form["country_id"]
        )
        return redirect(url_for("artist.detail", artist_id=artist_id))

    artist = artist_repo.get_artist(artist_id)
    countries = app.crud.get_all(Country)
    return render_template("artist/edit.html", artist=artist, countries=countries)


@bp.route("/artist/delete/<int:artist_id>", methods=["POST"])
def delete(artist_id):
    artist_repo.delete_artist(artist_id)
    return redirect(url_for("artist.catalog"))


@bp.route("/artist/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        country_id = request.form.get("country_id")
        artist_repo.add_artist(name=name, country_id=country_id)
        return redirect(url_for("artist.catalog"))

    countries = app.crud.get_all(Country)
    return render_template("artist/create.html", countries=countries)
