from src.databse import MySQLConnection

connection_object = MySQLConnection.connect()

cursor = connection_object.cursor()
class NewAccount():
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    balance = 0
    cursor.execute("INSERT INTO atm (name, account_number, balance) VALUES (%s, %s, %s)", (name, account_number, balance))
    connection_object.commit()