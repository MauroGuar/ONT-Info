The program consists of various sub-divided directories, each one of them take care of their own tasks. All of it starts from run.py, /run.py is the command you should optimally execute in order to get the app up and running.

The rest of the program, is all inside /app/ 
# inside /app/
## /app/config.py
The file config.py contains all the hardcoded data you should put in in order needed for the program to run, like the olt_username which is the ssh username, the olt_password which is the ssh password of that user, etc
config.py is used by many files, mainly main.py
## /app/main.py
The file main.py is called by run.py and contains all the flask routes containing the "classical" main structure, mostly function calls with personalized data, this is arguably the most important part of the code and the "hearth" of it, here you can set the items_to_show to the user, set Debug mode, etc
## /app/data_processing/
The data_processing directory is where most part of the code is, the task/mission of all this code is basically to be the back end of the page, this includes but not limited to:
* Error handling
* ssh operations (entering an ssh session, executing commands, reading the output of commands)
* db data handling
* data parsing
* displaying/showing data

## /app/database/
The database directory basically contains the file connection.py, but
### /app/database/connection.py
The file connection.py is pretty self explanatory, this file defines many functions that would handle connection with the running database
## /app/static/
The static directory contains the front-end stuff used to make the page look nice and properly, this includes css, images, javascript scripts, and some jsons for testing.
## /app/templates/
The templates directory contains all the flask's templates used for the page
### /app/templates/base.html
The file base.html basically is the header of the page, containing the help button, the name of the page and the logo, this is used throughout the page
### /app/templates/index.html
The file index.html is the index, the first page you enter and where users will enter the corresponding data, then users will push the "Buscar" button, that searches the latest entry in the database, if there is none or the entries are too old(24 hours or more), then just send a new request to the olt. Errors should be shown in this page
### /app/templates/results.html
The file results.html is the page users are sent after searching for some data, this is a basic page that formats the retrieved json in a clean and simple way, being easy to read and comprehend, there is also the "Actualizar datos" button that refreshes the data, sending a new request to the olt, then refreshing the page showing the new data

