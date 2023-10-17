from os import environ
from dotenv import find_dotenv, load_dotenv

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

OLT_USERNAME = environ["OLT_USERNAME"]
OLT_PASSWORD = environ["OLT_PASSWORD"]

MONGO_URI = environ["MONGO_URI"]

OLT_IP_ENV = environ["OLT_IP"]
ONT_SN_ENV = environ["ONT_SN"]
