# Capstone-Winter22
Capstone project for CS481 Winter 2022

Project is a webpage to search streaming websites for specific movies or tv shows. 

Need to install pip and selenium and download chromedriver

make "Webdrivers" folder on C drive and place chromedriver in the folder

"C:\Webdrivers\chromedriver"

In order to run the flask server for development, move to the flask-server folder in terminal and run three commands: 
'source venv/bin/activate' 
on windows: 'venv\Scripts\activate' 

(This tells the system that you want to use the server, after this point you should be working inside the flask virtual environment. Install modules and python things within the server!! Otherwise the install will likely happen globablly and the server will not necessarily be using the same python interpreter.)

'export FLASK_APP=server.py' 
on windows powershell: '$env:FLASK_APP="server.py"'

(This one tells the flask app which folder to use)


'python -m flask run'  (Run the flask app)

Your flask server should now be running on http://127.0.0.1:5000/

If you encounter the bug "No import module named flask", run the command 'pip3 install flask' inside of the venv
If the bug "error: could not import server" occurs, ensure you are in the correct directory while running commands
