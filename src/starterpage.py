from src.createaccountpage import CreateAccountPage
from src.findaccountpage import FindAccountPage

class StartPage:
    def __init__(self):
        print("Welcome to the ATM Application!")
        self.choice = input("Do you have an account? (yes/no): ").lower()

    def start(self):
        if self.choice == "yes":
            FindAccountPage().find_account()
        elif self.choice == "no":
            CreateAccountPage().create_account()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            self.start()

if __name__ == "__main__":
    StartPage().start()