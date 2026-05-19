from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


class BankingError(ValueError):
    pass


@dataclass
class BankAccount:
    holder_name: str
    pin: str
    password: str
    balance: float = 0.0
    account_number: str = field(default_factory=lambda: str(uuid4()))
    transaction_history: list[dict[str, Any]] = field(default_factory=list)
    account_type: str = "base"

    def __post_init__(self) -> None:
        if self.balance < 0:
            raise BankingError("Opening balance cannot be negative")
        self.balance = round(float(self.balance), 2)

    def verify_pin(self, pin: str) -> bool:
        return self.pin == pin

    def verify_password(self, password: str) -> bool:
        return self.password == password

    def deposit(self, amount: float, category: str = "income") -> None:
        amount = self._positive(amount)
        self.balance = round(self.balance + amount, 2)
        self._record("deposit", amount, category)

    def withdraw(self, amount: float, category: str = "cash") -> None:
        amount = self._positive(amount)
        if amount > self.balance:
            raise BankingError("Insufficient balance")
        self.balance = round(self.balance - amount, 2)
        self._record("withdrawal", amount, category)

    def transfer_money(self, target: "BankAccount", amount: float, pin: str) -> None:
        if not self.verify_pin(pin):
            raise BankingError("Invalid PIN")
        self.withdraw(amount, "transfer")
        target.deposit(amount, "transfer")
        self._record("transfer_out", amount, f"to:{target.account_number}")
        target._record("transfer_in", amount, f"from:{self.account_number}")

    def monthly_interest(self) -> float:
        return 0.0

    def mini_statement(self, limit: int = 5) -> list[dict[str, Any]]:
        return self.transaction_history[-limit:]

    def analyze_spending_pattern(self) -> dict[str, Any]:
        withdrawals = [t for t in self.transaction_history if t["type"] in {"withdrawal", "transfer_out"}]
        by_category: dict[str, float] = {}
        for item in withdrawals:
            by_category[item["category"]] = by_category.get(item["category"], 0.0) + float(item["amount"])
        highest = max(by_category, key=by_category.get) if by_category else "none"
        fraud_flags = [t for t in withdrawals if t["amount"] > max(10000, self.balance * 0.6)]
        return {
            "highest_spending_category": highest,
            "category_totals": by_category,
            "savings_tip": self._tip(highest),
            "fraud_alerts": fraud_flags,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "holder_name": self.holder_name,
            "pin": self.pin,
            "password": self.password,
            "balance": self.balance,
            "account_number": self.account_number,
            "transaction_history": self.transaction_history,
            "account_type": self.account_type,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BankAccount":
        return cls(**data)

    def _record(self, tx_type: str, amount: float, category: str) -> None:
        self.transaction_history.append({
            "type": tx_type,
            "amount": round(float(amount), 2),
            "category": category,
            "time": datetime.now().isoformat(timespec="seconds"),
            "balance_after": self.balance,
        })

    @staticmethod
    def _positive(amount: float) -> float:
        amount = float(amount)
        if amount <= 0:
            raise BankingError("Amount must be positive")
        return amount

    @staticmethod
    def _tip(category: str) -> str:
        tips = {
            "food": "Meal planning can reduce recurring food spends.",
            "shopping": "Try a 24-hour pause before non-essential purchases.",
            "transfer": "Review recurring transfers and automate savings first.",
            "cash": "Track cash usage weekly to avoid invisible spending.",
        }
        return tips.get(category, "Save at least 20% of every deposit before spending.")
