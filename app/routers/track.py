from flask import Blueprint, current_app as app
from flask import render_template, request, redirect, url_for
from db.models import Artist, Track, Album
from db.repository import TrackRepository, ArtistRepository

bp = Blueprint("track", __name__)
track_repo = TrackRepository()
artist_repo = ArtistRepository()


@bp.route("/album/<int:album_id>/new_track", methods=["GET", "POST"])
def create(album_id):
    if request.method == "POST":
        title = request.form["title"]
        duration = float(request.form["duration"])
        artist_id = int(request.form["artist_id"])
        track_repo.add_track(title=title, duration=duration, album_id=album_id, artist_id=artist_id)
        return redirect(url_for("album.detail", album_id=album_id))

    artists = artist_repo.get_all_artists()
    return render_template("track/create.html", album_id=album_id, artists=artists)


@bp.route("/track/edit/<int:track_id>", methods=["GET", "POST"])
def edit(track_id):
    track = track_repo.get_track(track_id)
    if request.method == "POST":
        update_values = dict(
            title=request.form["title"],
            duration=float(request.form["duration"]),
            artist_id=int(request.form["artist_id"]),
        )
        track_repo.update_track(track_id, **update_values)
        return redirect(url_for("album.detail", album_id=track.album_id))

    artists = artist_repo.get_all_artists(Artist)
    return render_template("track/edit.html", track=track, artists=artists)


@bp.route("/track/delete/<int:track_id>", methods=["POST"])
def delete(track_id):
    track_repo.delete_track(track_id)
    return redirect(url_for("album.detail", album_id=track.album_id))


@bp.route("/tracks")
def catalog():
    tracks = track_repo.get_all_tracks()
    return render_template("track/list.html", tracks=tracks)
