import random
import sys
from src.databse import MySQLConnection
from src.newaccount import NewAccount

connection_object = MySQLConnection.connect()
cursor = connection_object.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS atm (name VARCHAR(255), account_number VARCHAR(255), balance INT(10))")

existing_account = input("Have an account?(y/n):")
if existing_account == "y":
     print("adf")
elif existing_account == "n":
    NewAccount()
else:
    print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")

