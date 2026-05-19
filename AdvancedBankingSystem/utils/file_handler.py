from __future__ import annotations

import json
from pathlib import Path

from models.bank_account import BankAccount
from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount


ACCOUNT_TYPES = {"savings": SavingsAccount, "current": CurrentAccount, "base": BankAccount}


def load_accounts(path: str = "data/accounts.json") -> dict[str, BankAccount]:
    file_path = Path(path)
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("{}", encoding="utf-8")
    raw = json.loads(file_path.read_text(encoding="utf-8") or "{}")
    accounts = {}
    for number, data in raw.items():
        cls = ACCOUNT_TYPES.get(data.get("account_type", "base"), BankAccount)
        accounts[number] = cls.from_dict(data) if cls is BankAccount else cls(**data)
    return accounts


def save_accounts(accounts: dict[str, BankAccount], path: str = "data/accounts.json") -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {number: account.to_dict() for number, account in accounts.items()}
    file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
