import flask
from flask import Flask, send_from_directory, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__, static_folder='./my-app/')
CORS(app)

movie_file = '../../python-back-end/shows/HuluShows.txt'
NAME = 0
PRICE = 1
LINK = 2
RATING = 3
GENRE = 4

titles = {}
with open(movie_file) as f:
    lines = [line.strip() for line in f]
    for line in lines:
        data = [m.strip() for m in line.split('{')]
        movie = {
           'name': data[NAME],
           'price': data[PRICE],
           'link': data[LINK],
           'rating': data[RATING],
           'genre': data[GENRE]
        }
        titles[movie['name']] = movie


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/search-result/<movieTitle>', methods=['GET', 'POST'])
def search(movieTitle):
    if movieTitle in titles:
        return titles[movieTitle]
    else:
        flask.abort(404)


#puts the server into debug state, for development only
if __name__ == "__main__":
    app.run(debug=True)