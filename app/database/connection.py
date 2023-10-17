from flask_pymongo import PyMongo


class MongoConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MongoConnection, cls).__new__(cls)
            cls.__instance.init_app()
        return cls.__instance

    def init_app(self):
        self.mongo = PyMongo()

    def init_app_with_app(self, app):
        self.mongo.init_app(app)

    def get_db(self):
        return self.__instance.mongo.db

    def get_queries_collection(self):
        return self.__instance.mongo.db.queries


def init_db(app):
    connection = MongoConnection()
    connection.init_app_with_app(app)
