from dotenv import dotenv_values

env_config = dotenv_values()

OLT_IP = env_config["OLT_IP"]
OLT_USERNAME = env_config["OLT_USERNAME"]
OLT_PASSWORD = env_config["OLT_PASSWORD"]