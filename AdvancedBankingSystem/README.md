# Advanced AI Banking System

A Python CLI banking application that supports account creation, deposits, withdrawals, transfers, transaction history, spending analysis, and persistent JSON storage.

## Features

- Create savings and current bank accounts
- Secure account access with password authentication
- Deposit and withdraw funds with transaction logging
- Internal account transfers with PIN validation
- View recent transaction history
- Analyze spending patterns for AI-driven insights
- Save account data to `data/accounts.json`
- Persistent logging for deposits, withdrawals, and errors

## Requirements

- Python 3.14 or newer
- `pytest` for running tests
- `matplotlib` (required by the project dependencies)

## Setup

From the `AdvancedBankingSystem` folder:

```powershell
py -3 -m pip install -r requirements.txt
```

If your environment provides `python`, you can also use:

```powershell
python -m pip install -r requirements.txt
```

## How it works

1. The CLI starts in `main.py` and loads all saved accounts from `data/accounts.json`.
2. `main.py` shows a menu with options to create accounts, deposit, withdraw, transfer, view transactions, analyze spending, and exit.
3. Account classes in `models/` manage account behavior and maintain transaction history.
4. `utils/` handles JSON persistence, log file creation, and validation rules.
5. Every deposit or withdrawal is logged and stored as a transaction record.
6. Transfers verify the source PIN and move funds between accounts.
7. AI analysis inspects spending categories and returns savings tips and alerts.
8. On exit, the program saves any changes back to `data/accounts.json`.

## Run

Start the CLI from the project folder:

```powershell
py -3 main.py
```

Then follow the prompts:

- `1` to create a new account
- `2` to deposit funds
- `3` to withdraw funds
- `4` to transfer money between accounts
- `5` to view recent transactions
- `6` to analyze spending patterns
- `7` to exit and save data

## Test

Run the automated tests from the project folder:

```powershell
py -3 -m pytest
```

## Project Structure

- `main.py` - main command-line interface and workflow
- `models/` - account classes, including `BankAccount`, `CurrentAccount`, and `SavingsAccount`
- `utils/` - persistence, logging, and validation helpers
- `data/accounts.json` - stored account data
- `tests/` - test suite for banking operations

## Notes

- Account data is persisted automatically after each operation.
- Logs are written to `deposits.log`, `withdrawals.log`, and `errors.log` in the project folder.
- Use `py -3` on Windows if `python` is not available on PATH.
