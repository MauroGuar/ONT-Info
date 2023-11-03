# Import necessary modules
from flask_pymongo import PyMongo


class MongoConnection:
    """
    A singleton class for MongoDB connection.
    This pattern is a design principle that ensures a class has only one instance, and provides a global point of access to it.
    """

    __instance = None

    def __new__(cls):
        """
        Create a new instance if one doesn't exist.
        """

        if cls.__instance is None:
            cls.__instance = super(MongoConnection, cls).__new__(cls)
            cls.__instance.init_app()
        return cls.__instance

    def init_app(self):
        """
        Initialize PyMongo instance.
        """

        self.mongo = PyMongo()

    def init_app_with_app(self, app):
        """
        Initialize PyMongo instance with a Flask app.

        Args:
            app: A Flask application instance.
        """

        self.mongo.init_app(app)

    def get_db(self):
        """
        Get the database from the PyMongo instance.

        Returns:
            The database from the PyMongo instance.
        """

        return self.__instance.mongo.db

    def get_queries_collection(self):
        """
        Get the 'queries' collection from the database.

        Returns:
            The 'queries' collection from the database.
        """

        return self.__instance.mongo.db.queries


def init_db(app):
    """
    Initialize the database with a Flask app.

    Args:
        app: A Flask application instance.
    """

    connection = MongoConnection()
    connection.init_app_with_app(app)


