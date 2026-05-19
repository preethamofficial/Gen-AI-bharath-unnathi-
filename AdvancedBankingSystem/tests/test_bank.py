import pytest

from models.bank_account import BankingError
from models.savings_account import SavingsAccount


def test_account_creation():
    account = SavingsAccount("Asha", "1234", "secret", 500)
    assert account.balance == 500
    assert account.account_number


def test_negative_deposit():
    account = SavingsAccount("Asha", "1234", "secret")
    with pytest.raises(BankingError):
        account.deposit(-10)


def test_invalid_withdrawal():
    account = SavingsAccount("Asha", "1234", "secret", 100)
    with pytest.raises(BankingError):
        account.withdraw(200)


def test_transfer_failure_wrong_pin():
    a = SavingsAccount("Asha", "1234", "secret", 100)
    b = SavingsAccount("Ravi", "9999", "secret", 0)
    with pytest.raises(BankingError):
        a.transfer_money(b, 50, "0000")
