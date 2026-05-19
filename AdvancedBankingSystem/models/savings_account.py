from .bank_account import BankAccount


class SavingsAccount(BankAccount):
    account_type = "savings"

    def __init__(self, *args, **kwargs):
        kwargs["account_type"] = "savings"
        super().__init__(*args, **kwargs)

    def monthly_interest(self) -> float:
        interest = round(self.balance * 0.035 / 12, 2)
        if interest:
            self.deposit(interest, "interest")
        return interest
