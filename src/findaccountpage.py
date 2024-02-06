from src.dbconfig import account_collection
from src.menupage import MenuPage

class FindAccountPage:
    def find_account(self):
        print("Find an Account")

        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        account = account_collection.find_one({"account_number": account_number, "pin": pin})

        if not account:
            print("Incorrect PIN. Please try again.")
            self.find_account()
        else:
            print("Login successful!")
            menu = MenuPage(account)
            menu.show_menu()