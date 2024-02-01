import mysql.connector
from mysql.connector import Error

class MySQLConnection:
    def connect():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Miluv@2023",
                database="atm"
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Error as e:
            print(e)

