import flask
from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__, static_folder='./my-app/')
CORS(app)

movie_file = '../../python-back-end/shows/HuluShows.txt'
NAME = 0
PRICE = 1
URL = 2

titles = {}
with open(movie_file) as f:
    lines = [line.strip() for line in f]
    for line in lines:
        data = [m.strip() for m in line.split('{')]
        movie = {
           'name': data[NAME],
           'price': data[PRICE],
           'url': data[URL],
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


@app.route('/home')
def home():
    return 'home'

@app.route('/genres')
def genres():
    return 'genres'

@app.route('/faq')
def faq():
    return 'faq'


#puts the server into debug state, for development only
if __name__ == "__main__":
    app.run(debug=True)