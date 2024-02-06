from pymongo import MongoClient

host = "localhost"
port = 27017
database = "atm"
username = "root"
password = "7yAH4tv5L0UywvNu"

client = MongoClient(host, port)
db = client[database]
account_collection = db["account"]
