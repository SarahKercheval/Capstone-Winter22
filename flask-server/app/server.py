#!/usr/bin/env python3

"""
Server Backend for flask project.
@author: Sarah Kercheval
"""

import os
import pathlib
from enum import IntEnum
import sys
import json
import flask
from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_folder='./my-app/')
CORS(app)


SHOWS_FOLDER = pathlib.Path(__file__).absolute().parent.parent.parent.joinpath(
                                                    'python-back-end', 'shows')

SHOW_FILENAMES = ['HuluShows.txt',
                  'NetflixShows.txt',
                  'ParamountMovies.txt',
                  'ParamountShows.txt']
SHOW_FILES = [SHOWS_FOLDER.joinpath(f) for f in SHOW_FILENAMES]


class DataFields(IntEnum):
    """List of data fields and their corresponding index."""
    NAME = 0
    PRICE = 1
    LINK = 2
    RATING = 3
    GENRE = 4
    PROVIDER = 5


def get_if(array, index):
    """Convenience function for accessing elements that may not
       be present in an array."""
    return array[index] if index < len(array) else None


def load_titles():
    """Loads all movie titles from the list of all shows."""
    out = {}
    count = 0
    for file_name in SHOW_FILES:
        with open(file_name, encoding='utf-8') as file:
            for line in [l.strip() for l in file]:
                data = [m.strip() for m in line.split('{')]
                name = str(file_name).split('/')[-1]
                try:
                    movie = {
                        'name': data[DataFields.NAME],
                        'price': data[DataFields.PRICE],
                        'link': get_if(data, DataFields.LINK),
                        'rating': get_if(data, DataFields.RATING),
                        'genre': get_if(data, DataFields.GENRE)
                    }
                    if count == 0:
                        movie['provider'] = 'Hulu'
                    if count == 1:
                        movie['provider'] = 'Netflix'
                    else: #name == 'ParamountMovies.txt' or name == 'ParamountShows.txt':
                        movie['provider'] = 'Paramount'
                    movie[str(file_name)] = name
                         
                except IndexError:
                    print("received index error for data = ", data)
                    sys.exit(-1)
                out[movie['name'].strip().lower()] = movie
        count += 1
    return out


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def serve(path):
    """Serves the default path."""
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)

    return send_from_directory(app.static_folder, 'index.html')


titles = load_titles()



@app.route('/search-result/<movieTitle>', methods=['GET', 'POST'])
def search(movieTitle):
    """Given a |movieTitle|, searches for it in the list of all movies."""
    ret = []
    requestTitle = movieTitle.lower().strip()
    for title in titles.keys():
        if requestTitle in title:
            ret.append(titles[title])
            # return titles[requestTitle]
    return json.dumps(ret)


# puts the server into debug state
if __name__ == "__main__":
    app.run(debug=True)
