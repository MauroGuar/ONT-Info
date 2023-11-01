# Import necessary modules
from os import environ
from dotenv import find_dotenv, load_dotenv

# Find and load the .env file in the project directory
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

# Retrieve environment variables from the loaded .env file

# OLT_USERNAME: This variable stores the username for the OLT device connection via ssh, which is read from the environment.
OLT_USERNAME = environ["OLT_USERNAME"]

# OLT_PASSWORD: This variable stores the password for connecting to the OLT device via ssh, which is read from the environment.
OLT_PASSWORD = environ["OLT_PASSWORD"]

# MONGO_URI: This variable stores the MongoDB connection URI, used to connect to the MongoDB database. It is read from the environment.
MONGO_URI = environ["MONGO_URI"]

# FLASK_SESSION_SECRET_KEY: This variable stores the secret key for the flask session, which is read from the environment.
FLASK_SESSION_SECRET_KEY = environ["FLASK_SESSION_SECRET_KEY"]
