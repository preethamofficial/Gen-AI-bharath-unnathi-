class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Balance: {self.balance}")


def main():
    print("=== Smart Bank Management System ===")

    name = input("Enter Account Holder Name: ")
    acc_no = input("Enter Account Number: ")
    initial_balance = float(input("Enter Initial Balance: "))

    account = BankAccount(name, acc_no, initial_balance)

    while True:
        print("\n===== MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == 3:
            account.check_balance()

        elif choice == 4:
            account.display_details()

        elif choice == 5:
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()