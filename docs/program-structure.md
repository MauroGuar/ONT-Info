# Program Structure

The program consists of various sub-divided directories, each one of them take care of their own tasks. All of it starts from run.py, /run.py is the command you should optimally execute in order to get the app up and running.

The rest of the program is inside /app/

## inside /app/

### /app/config.py

The config.py file contains all the hardcoded data you should put in in order needed for the program to run, like the olt_username which is the ssh username, the olt_password which is the ssh password of that user, etc
config.py is used by many files, mainly main.py

### /app/main.py

The main.py file is called by run.py and contains all the flask routes containing the "classical" main structure, mostly function calls with personalized data, this is arguably the most important part of the code and the "hearth" of it, here you can set the items_to_show to the user, set Debug mode, etc

### /app/data_processing/

The data_processing directory is where most part of the code is, the task/mission of all this code is basically 
to be the back end of the page, this includes but not limited to:

* Error handling
* ssh operations (entering an ssh session, executing commands, reading the output of commands)
* db data handling
* data parsing
* displaying/showing data

#### /app/data_processing/db_handler/

The db_handler directory contains all the back-end logic used to comunicate with the database and also handle the queries

##### /app/data_processing/db_handler/query_history.py

The query_history.py file uses the functions and class provided by connection.py, this contains all the logic that are related to the buttons to make a db proper query.

#### /app/data_processing/error_handler/

The error_handler directory contains the error and validation functions

##### /app/data_processing/error_handler/errors.py

The errors.py file contains the error class and error function that is used throughout the program

##### /app/data_processing/error_handler/user_input

The user_input.py file verifies the data introduced by the user and verifies its correct, also applying some conversion handling because of human input mistakes

#### /app/data_processing/ssh_prompt_handler/

The ssh_prompt_handler directory handles the ssh connection, commanding, reading, parsing(also validating user input) and debugmode, all of this while having exhaustively handling the errors of each part.

* creates and manages the initial part of the ssh connection to the olt
* mimics the human behaviour, writing commands and expecting patterns/strings before taking actions
* read and parses the console output using regex

##### /app/data_processing/ssh_prompt_handler/dictionary_converter.py

The dictionary_converter.py file retrieves ONT information and optical information dictionaries for a given OLT IP and ONT serial number, also handling debugmode

##### /app/data_processing/ssh_prompt_handler/ont_prompt.py

The ont_prompt.py file execute the commands and expects patterns/strings before taking actions, all of this already inside of the ssh session using pexpect, then return what it reads in the terminal

##### /app/data_processing/ssh_prompt_handler/prompt_analysis.py

The prompt_analysis.py file process the raw data given by ont_prompt using regex, storing the data key and value inside a dictionary

##### /app/data_processing/ssh_prompt_handler/session_spawn.py

The session_spawn.py file starts a connection with the olt, until the point the olt gives a prompt

#### /app/data_processing/ont_info.py

The ont_info.py file defines the main back-end functions that handle the database queries with the front end:

* formats the time from utc to gmt-3
* filters which data to show and how to show it
* handles the refresh of queries and the logic behind it(if its older than 24 hours create a new one, etc)


### /app/database/

The database directory basically contains the file connection.py, but here should be all the required code to handle connections with the database.

#### /app/database/connection.py

The file connection.py is pretty self explanatory, this file defines many functions that would handle connection with the running database

### /app/static/

The static directory contains the front-end stuff used to make the page look nice and properly, this includes css, images, javascript scripts, and some jsons for testing.

### /app/templates/

The templates directory contains all the flask's templates used for the page

#### /app/templates/base.html

The file base.html basically is the header of the page, containing the help button, the name of the page and the logo, this is used throughout the page

#### /app/templates/index.html

The file index.html is the index, the first page you enter and where users will enter the corresponding data, then users will push the "Buscar" button, that searches the latest entry in the database, if there is none or the entries are too old(24 hours or more), then just send a new request to the olt. Errors should be shown in this page

#### /app/templates/results.html

The file results.html is the page users are sent after searching for some data, this is a basic page that formats the retrieved json in a clean and simple way, being easy to read and comprehend, there is also the "Actualizar datos" button that refreshes the data, sending a new request to the olt, then refreshing the page showing the new data
