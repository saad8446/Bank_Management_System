class Account:
    def __init__(self, account_no, customer_name, pin):
        self.account_no = account_no
        self.customer_name = customer_name
        self.pin = pin
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False

        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited: {amount}. New balance: {self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Invalid amount or insufficient balance")
            return False

        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")
        print(f"Withdrawn: {amount}. New balance: {self.balance}")
        return True

    def transfer(self, amount, to_account):
        if amount <= 0 or amount > self.balance:
            print("Invalid amount or insufficient balance")
            return False

        self.balance -= amount
        to_account.balance += amount

        self.transactions.append(
            f"Transferred {amount} to {to_account.account_no}"
        )

        to_account.transactions.append(
            f"Received {amount} from {self.account_no}"
        )

        print(f"Transferred {amount} successfully.")
        return True

    def print_balance(self):
        print(f"Current Balance: {self.balance}")

    def print_history(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\nTransaction History")
        for transaction in self.transactions:
            print(transaction)