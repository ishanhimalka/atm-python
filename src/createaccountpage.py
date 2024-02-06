from src.dbconfig import account_collection
from src.findaccountpage import FindAccountPage
import time
import uuid

class CreateAccountPage:
    def __init__(self):
        self.account_number = str(uuid.uuid4())

    def create_account(self):
        print("Create an Account")

        name = input("Enter your name: ")
        balance = float(input("Enter your initial balance: "))
        pin = input("Enter your PIN: ")

        account_data = {
            "name": name,
            "balance": balance,
            "pin": pin,
            "account_number": self.account_number
        }

        if account_collection.find_one({"account_number": self.account_number}):
            print("Error: Account number already exists. Please try again.")
        else:
            account_collection.insert_one(account_data)
            print(f"Account created successfully. Here is your account number: {self.account_number}")
            time.sleep(15)
            FindAccountPage().find_account()