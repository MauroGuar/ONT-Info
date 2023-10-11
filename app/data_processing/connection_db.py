from pymongo import MongoClient

class DataBase:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://scapitani:santiago2005@cluster0.gds8oe1.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["OLT_Information"]
        self.collection = self.db["client"]

    def save_mongo(self, data):
        self.collection.insert_one(data)

    def get_mongo(self, olt_ip, ont_sn):
        return list(self.collection.find({"olt_ip":olt_ip, "ont_sn":ont_sn}))
