import json
from account import Account


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def save_accounts(self):
        data = {}

        for account_no, account in self.accounts.items():
            data[account_no] = {
                "customer_name": account.customer_name,
                "pin": account.pin,
                "balance": account.balance,
                "transactions": account.transactions
            }

        with open("accounts.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_accounts(self):
        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)

            self.accounts = {}

            for account_no, info in data.items():

                account = Account(
                    account_no,
                    info["customer_name"],
                    info["pin"]
            )

                account.balance = info["balance"]
                account.transactions = info["transactions"]

                self.accounts[account_no] = account

        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

    def create_account(self, account_no, customer_name, pin):

        if account_no in self.accounts:
            return False

        account = Account(account_no, customer_name, pin)

        self.accounts[account_no] = account

        self.save_accounts()

        return True

    def login(self, account_no, pin):

        if account_no not in self.accounts:
            return None

        account = self.accounts[account_no]

        if account.pin == pin:
            return account

        return None

    def delete_account(self, account_no):

        if account_no in self.accounts:
            del self.accounts[account_no]

            self.save_accounts()

            return True

        return False

    def deposit(self, account, amount):

        if account.deposit(amount):
            self.save_accounts()

    def withdraw(self, account, amount):

        if account.withdraw(amount):
            self.save_accounts()

    def transfer(self, from_account, to_account, amount):

        if from_account.transfer(amount, to_account):
            self.save_accounts()