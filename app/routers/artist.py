from flask import render_template, request, redirect, url_for
from db.models import Artist, Country
from flask import Blueprint, current_app as app
from flask import render_template, request, redirect, url_for

bp = Blueprint("artist", __name__)


@bp.route("/artists")
def catalog():
    artists = app.crud.get_all(Artist)
    return render_template("artist/list.html", artists=artists)


@bp.route("/artist/<int:artist_id>")
def detail(artist_id):
    artist = app.crud.get(Artist, id=artist_id)
    return render_template("artist/info.html", artist=artist)


@bp.route("/artist/edit/<int:artist_id>", methods=["GET", "POST"])
def edit(artist_id):
    if request.method == "POST":
        app.crud.update(
            Artist, name=request.form["name"], country_id=request.form["country_id"]
        )
        return redirect(url_for("artist_detail", artist_id=artist_id))

    artist = app.crud.get(Artist, id=artist_id)
    countries = app.crud.get_all(Country)
    return render_template("artist/edit.html", artist=artist, countries=countries)


@bp.route("/artist/delete/<int:artist_id>", methods=["POST"])
def delete(artist_id):
    app.crud.delete(Artist, id=artist_id)
    return redirect(url_for("artist_list"))


@bp.route("/artist/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        country_id = request.form.get("country_id")

        artist = Artist(name=name, country_id=country_id)
        app.crud.save(artist)
        return redirect(url_for("artist_list"))

    countries = app.crud.get_all(Country)
    return render_template("artist/create.html", countries=countries)
