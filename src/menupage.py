from src.dbconfig import account_collection

class MenuPage:
    def __init__(self, account):
        self.account = account

    def show_menu(self):
        print(f"Welcome, {self.account['name']}!")

        while True:
            print("\nMenu:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw_money()
            elif choice == "3":
                self.deposit_money()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def check_balance(self):
        print(f"Your current balance: ${self.account['balance']}")

    def withdraw_money(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.account['balance']:
            print("Insufficient funds. Cannot withdraw.")
        else:
            self.account['balance'] -= amount
            print(f"Withdrawal successful. Remaining balance: ${self.account['balance']}")

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: "))
        self.account['balance'] += amount
        print(f"Deposit successful. New balance: ${self.account['balance']}")

    