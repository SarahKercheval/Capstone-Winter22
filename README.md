# Find That Show
Capstone project for CS481 Winter Quarter 2022

The focus of the project is providing an efficient search of television shows and movies across a range of all current streaming services via web scraping.

More specifications and details can be found in the Find That Show Final Document pdf.

Installation:

-Download source code zipped from the GitHub: SarahKercheval/Capstone-Winter22
-Unzip the file
-Install Node.js/npm (if not already installed)
-Install python (if not already installed)
-Ensure the latest versions of npm and python are installed, elsewise errors may appear.
    There may be issues with installing npm if there is not enough disk space available.
    The front-end may compile with errors if the react version is not updated.
    
**On Mac OS:**

To begin running the server: Open a terminal and go into the main directory and run “pip3 install flask”, then “pip3 install flask-cors”. From here, run “cd flask-server/app” to go into the main flask server directory. Run the command “export FLASK_APP=server.py” to set your environment, then run “python3 -m flask run” to start the server.

To begin running the frontend: Open another terminal, go into the my-app directory and run “npm install”. If another application is running on localHost:3000 it will ask if you want to run it on a different port. Answer yes. After npm installs, run the command “npm run start”. This will open a tab on your browser on the localhost.

If you need to exit either the server or the react UI, “control-c” will exit out of them.

**On Windows OS:**

To begin running the server: Open a powershell terminal and go into the main directory. Run “pip3 install flask” then “pip3 install flask-cors”. From here, run “cd flask-server/app” to go into the main flask server directory. Run the command “ $env:FLASK_APP=”server.py” ” to set your environment, then run “python -m flask run” to start the server. The server will start on 127.0.0.1:5000, in order to see the search results the URL will need to be 127.0.0.1:5000/search-result/movieTitle, where movieTitle is the searched title you want.

To begin running the frontend: Open a powershell terminal and go to the main directory. From here run “cd my-app” then run “npm install”. This installation will likely take a couple minutes. After npm has installed, run “cd my-app” which is the main react directory. Inside here run “npm run start”. This will start the development page on a web browser.

If you need to exit either the server or the react UI, “control-c” will exit out of them.

**Bugs**

Depending on the environment and browser, CORS issues may prevent the front-end from displaying correctly.
The filters are automatically set to paramount, this is an issue with the flask integration that is still unknown.
