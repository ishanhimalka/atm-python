from src.databse import MySQLConnection
from src.newaccount import NewAccount

connection_object = MySQLConnection.connect()
cursor = connection_object.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS atm (name VARCHAR(255), account_number VARCHAR(255), balance INT(10))")
class ATM:
    existing_account = input("Have an account?(y/n):")
    if existing_account == "y":
        account = input("Enter your Account Number: ")
        cursor.execute("SELECT * FROM atm WHERE account_number = %s", (account,))
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            print("Invalid Account Number!")
    elif existing_account == "n":
        NewAccount()
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")

 