from flask import Flask
from app.routers import album_bp, artist_bp, track_bp, genre_bp, label_bp

app = Flask(__name__)

app.register_blueprint(album_bp)
app.register_blueprint(artist_bp)
app.register_blueprint(track_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(label_bp)

app.add_url_rule("/", endpoint="index")


if __name__ == "__main__":
    app.run(debug=True)
