from flask import Blueprint, render_template, request, redirect, url_for
from db.repository import GenreRepository

bp = Blueprint("genre", __name__)
genre_repo = GenreRepository()

@bp.route("/genres")
def catalog():
    genres = genre_repo.get_all_genres()
    return render_template("genre/list.html", genres=genres)

@bp.route("/genre/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        genre_repo.add_genre(name=name)
        return redirect(url_for("genre.catalog"))

    return render_template("genre/create.html")

@bp.route("/genre/edit/<int:genre_id>", methods=["GET", "POST"])
def edit(genre_id):
    genre = genre_repo.get(genre_id)
    if request.method == "POST":
        genre_repo.update_genre(genre_id, request.form["name"])
        return redirect(url_for("genre.catalog"))
    return render_template("genre/edit.html", genre=genre)

@bp.route("/genre/delete/<int:genre_id>", methods=["POST"])
def delete(genre_id):
    genre_repo.delete_genre(genre_id)
    return redirect(url_for("genre.catalog"))

# Add other routes for edit and delete as needed
