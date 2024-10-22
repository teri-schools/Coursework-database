from flask import Blueprint, current_app as app
from flask import render_template, request, redirect, url_for
from db.models import Artist, Track, Album

bp = Blueprint("track", __name__)


@bp.route("/album/<int:album_id>/new_track", methods=["GET", "POST"])
def create(album_id):
    album = app.crud.get(Album, id=album_id)
    if request.method == "POST":
        title = request.form["title"]
        duration = float(request.form["duration"])
        artist_id = int(request.form["artist_id"])

        track = Track(title=title, duration=duration, album=album, artist_id=artist_id)
        app.crud.save(track)
        return redirect(url_for("album_detail", album_id=album_id))

    artists = app.crud.get_all(Artist)
    return render_template("track/create.html", album_id=album_id, artists=artists)


@bp.route("/track/edit/<int:track_id>", methods=["GET", "POST"])
def edit(track_id):
    track = app.crud.get(Track, id=track_id)
    if request.method == "POST":
        update_values = dict(
            title=request.form["title"],
            duration=float(request.form["duration"]),
            artist_id=int(request.form["artist_id"]),
        )
        app.crud.update(Track, dict(id=track_id), update_values)
        return redirect(url_for("album_detail", album_id=track.album_id))

    artists = app.crud.get_all(Artist)
    return render_template("track/edit.html", track=track, artists=artists)


@bp.route("/track/delete/<int:track_id>", methods=["POST"])
def delete(track_id):
    track = app.crud.get(Track, id=track_id)
    album_id = track.album_id
    app.crud.delete(Track, id=track_id)
    return redirect(url_for("album_detail", album_id=album_id))


@bp.route("/tracks")
def catalog():
    tracks = app.crud.get_all(Track)
    return render_template("track/list.html", tracks=tracks)
