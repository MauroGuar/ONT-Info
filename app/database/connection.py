from flask_pymongo import PyMongo


class MongoConnection:
    # Singleton pattern: ensures only one instance of MongoConnection is created

    __instance = None

    def __new__(cls):
        # Creates a new instance if it doesn't exist, otherwise returns the existing instance

        if cls.__instance is None:
            cls.__instance = super(MongoConnection, cls).__new__(cls)
            cls.__instance.init_app()
        return cls.__instance

    def init_app(self):
        # Initializes the PyMongo instance

        self.mongo = PyMongo()

    def init_app_with_app(self, app):
        # Initializes the PyMongo instance with a Flask app

        self.mongo.init_app(app)

    def get_db(self):
        # Returns the MongoDB database object

        return self.__instance.mongo.db

    def get_queries_collection(self):
        # Returns the 'queries' collection from the MongoDB database

        return self.__instance.mongo.db.queries


def init_db(app):
    # Initializes the MongoDB connection with the Flask app

    connection = (
        MongoConnection()
    )  # Create an instance of MongoConnection (singleton pattern)
    connection.init_app_with_app(
        app
    )  # Initialize the PyMongo instance with the Flask app
