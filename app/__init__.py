from flask import Flask
from db.crud import Crud
from app.routers import album_bp, artist_bp, track_bp

app = Flask(__name__)
app.crud = Crud()

app.register_blueprint(album_bp)
app.register_blueprint(artist_bp)
app.register_blueprint(track_bp)

app.add_url_rule('/', endpoint='index')


if __name__ == "__main__":
    app.run(debug=True)
