from .bank_account import BankAccount, BankingError


class CurrentAccount(BankAccount):
    account_type = "current"

    def __init__(self, *args, overdraft_limit: float = 25000.0, **kwargs):
        kwargs["account_type"] = "current"
        super().__init__(*args, **kwargs)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float, category: str = "business") -> None:
        amount = self._positive(amount)
        if self.balance - amount < -self.overdraft_limit:
            raise BankingError("Overdraft limit exceeded")
        self.balance = round(self.balance - amount, 2)
        self._record("withdrawal", amount, category)

    def to_dict(self):
        data = super().to_dict()
        data["overdraft_limit"] = self.overdraft_limit
        return data
