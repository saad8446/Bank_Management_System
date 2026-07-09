import json

class Account:
    def __init__(self,account_no,customer_name,pin):
        self.account_no=account_no
        self.customer_name=customer_name
        self.pin=pin
        self.balance=0
        self.transactions=[]

    def deposit(self,amount):
        if(amount<=0):
            print("Invalid amount")
            return
        self.balance+=amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount or insufficient balance")

    def transfer(self,amount,to_account):
        if amount>0 and amount<self.balance:
            self.balance-=amount
            to_account.balance+=amount

            print(f"Transferred: {amount} to {to_account.account_no}. New balance: {self.balance}")
            to_account.transactions.append(f"Received:{amount} from {self.account_no}")
            self.transactions.append(f"Transferred: {amount} to {to_account.account_no}")
        else:
            print("Invalid amount or insufficient balance")

    def print_balance(self):
        print(f"Current balance: {self.balance}")

    def print_history(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)




class Bank:
    def __init__(self):
        self.accounts={}


    def create_account(self,account_no,customer_name,pin):
        if account_no in self.accounts:
            return False
        else:
            account=Account(account_no,customer_name,pin)
            self.accounts[account_no]=account
            return True 
        
    def login(self,account_no,pin):
        if account_no in self.accounts:
            account=self.accounts[account_no]
            if account.pin==pin:
                return account
            else:
                return None
        else:
            return None
        
    def delete_account(self,account_no):
        if account_no in self.accounts:
            del self.accounts[account_no]
            return True
        else:
            return False
        
    
        


def displaychoice():
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    return int(input("Enter your choice: "))


def displayaccountchoice():
    print("\n===== ACCOUNT MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Balance")
    print("5. History")
    print("6. Delete Account")
    print("7. Logout")
    return int(input("Enter your choice: "))


bank = Bank()

while True:
    choice = displaychoice()

    if choice == 1:
        account_no = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        pin = input("Enter PIN: ")

        if bank.create_account(account_no, customer_name, pin):
            print("Account created successfully!")
        else:
            print("Account already exists!")

    elif choice == 2:
        account_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        account = bank.login(account_no, pin)

        if account:
            print("Login Successful!")

            while True:
                account_choice = displayaccountchoice()

                if account_choice == 1:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif account_choice == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif account_choice == 3:
                    to_account_no = input("Enter account number to transfer to: ")
                    if to_account_no in bank.accounts:
                        to_account = bank.accounts[to_account_no]
                        amount = float(input("Enter amount to transfer: "))
                    else:
                        print("Account does not exist!")
                        continue
                    account.transfer(amount, to_account)

                elif account_choice == 4:
                    account.print_balance()

                elif account_choice == 5:
                    account.print_history()

                elif account_choice==6:
                    confirm = input("Are you sure you want to delete your account? (yes/no): ")
                    if confirm.lower() == "yes":
                        if bank.delete_account(account.account_no):
                            print("Account deleted successfully!")
                            break
                        else:
                            print("Error deleting account!")
                    else:
                        print("Account deletion canceled.")
                    

                elif account_choice == 7:
                    print("Logged out successfully!")
                    break

                else:
                    print("Invalid choice!")

        else:
            print("Invalid account number or PIN!")

    elif choice == 3:
        print("Thank you for using our Bank Management System.")
        break

    else:
        print("Invalid choice! Please try again.")

    


