from flask import Flask
#follow microsoft tutorial to get flask running
#https://code.visualstudio.com/docs/python/tutorial-flask
#python -m flask run

app = Flask(__name__)

# Members API route

@app.route("/")
def home():
    return 'Home'

@app.route("/Genre")
def genre():
    return 'Genre'
    
@app.route("/faq")
def faq():
    return 'faq'

#puts the server into debug state, for development only
if __name__ == "__main__":
    app.run(debug=True)