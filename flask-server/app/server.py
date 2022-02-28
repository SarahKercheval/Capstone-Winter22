
import flask
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='./my-app/build')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/home')
def home(home):
    return 'Hello, world'


#puts the server into debug state, for development only
if __name__ == "__main__":
    app.run(debug=True)