import json
from account import Account


class Bank:
    def __init__(self):
        self.accounts = {}
        

    def create_account(self, account_no, customer_name, pin):

        if account_no in self.accounts:
            return False

        account = Account(account_no, customer_name, pin)

        self.accounts[account_no] = account


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

            return True

        return False

   