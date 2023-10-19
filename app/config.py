# Import necessary modules
from os import environ
from dotenv import find_dotenv, load_dotenv

# Find and load the .env file in the project directory
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

# Retrieve environment variables from the loaded .env file

# OLT_USERNAME: This variable stores the username for the OLT device, which is read from the environment.
OLT_USERNAME = environ["OLT_USERNAME"]

# OLT_PASSWORD: This variable stores the password for the OLT device, which is read from the environment.
OLT_PASSWORD = environ["OLT_PASSWORD"]

# MONGO_URI: This variable stores the MongoDB connection URI, typically used to connect to a MongoDB database. It is read from the environment.
MONGO_URI = environ["MONGO_URI"]

# OLT_IP_ENV: This variable stores the OLT (Optical Line Terminal) IP address, which is read from the environment.
OLT_IP_ENV = environ["OLT_IP"]

# ONT_SN_ENV: This variable stores the ONT (Optical Network Terminal) serial number, which is read from the environment.
ONT_SN_ENV = environ["ONT_SN"]
