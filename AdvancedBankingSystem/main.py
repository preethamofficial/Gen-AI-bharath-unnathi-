from models.bank_account import BankingError
from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount
from utils.file_handler import load_accounts, save_accounts
from utils.logger import get_logger
from utils.validators import require_non_empty, require_pin

deposit_log = get_logger("deposits", "deposits.log")
withdrawal_log = get_logger("withdrawals", "withdrawals.log")
error_log = get_logger("errors", "errors.log")


def create_account(accounts):
    name = require_non_empty(input("Holder name: "), "Holder name")
    pin = require_pin(input("4-digit PIN: "))
    password = require_non_empty(input("Password: "), "Password")
    kind = input("Type [savings/current]: ").strip().lower() or "savings"
    cls = CurrentAccount if kind == "current" else SavingsAccount
    account = cls(name, pin, password)
    accounts[account.account_number] = account
    print(f"Created {account.account_type} account: {account.account_number}")


def find(accounts):
    number = input("Account number: ").strip()
    account = accounts.get(number)
    if not account:
        raise BankingError("Account not found")
    if not account.verify_password(input("Password: ")):
        raise BankingError("Invalid password")
    return account


def dashboard():
    accounts = load_accounts()
    while True:
        print("\n1.Create 2.Deposit 3.Withdraw 4.Transfer 5.Transactions 6.AI Analysis 7.Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                create_account(accounts)
            elif choice == "2":
                account = find(accounts)
                amount = float(input("Amount: "))
                category = input("Category: ") or "income"
                account.deposit(amount, category)
                deposit_log.info("%s deposited %.2f", account.account_number, amount)
            elif choice == "3":
                account = find(accounts)
                amount = float(input("Amount: "))
                category = input("Category: ") or "cash"
                account.withdraw(amount, category)
                withdrawal_log.info("%s withdrew %.2f", account.account_number, amount)
            elif choice == "4":
                source = find(accounts)
                target = accounts[input("Target account: ").strip()]
                source.transfer_money(target, float(input("Amount: ")), input("PIN: "))
            elif choice == "5":
                print(find(accounts).mini_statement(10))
            elif choice == "6":
                print(find(accounts).analyze_spending_pattern())
            elif choice == "7":
                save_accounts(accounts)
                break
            save_accounts(accounts)
        except Exception as exc:
            error_log.exception("Operation failed")
            print(f"Error: {exc}")


if __name__ == "__main__":
    dashboard()
