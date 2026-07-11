from bank import Bank
from menu import displaychoice, displayaccountchoice


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
                    bank.deposit(account, amount)

                elif account_choice == 2:

                    amount = float(input("Enter amount to withdraw: "))
                    bank.withdraw(account, amount)

                elif account_choice == 3:

                    to_account_no = input("Enter receiver account number: ")

                    if to_account_no not in bank.accounts:
                        print("Account does not exist!")
                        continue

                    to_account = bank.accounts[to_account_no]

                    amount = float(input("Enter amount to transfer: "))

                    bank.transfer(account, to_account, amount)

                elif account_choice == 4:

                    account.print_balance()

                elif account_choice == 5:

                    account.print_history()

                elif account_choice == 6:

                    confirm = input(
                        "Are you sure you want to delete your account? (yes/no): "
                    )

                    if confirm.lower() == "yes":

                        if bank.delete_account(account.account_no):
                            print("Account deleted successfully!")
                            break

                    else:
                        print("Deletion cancelled.")

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
        print("Invalid choice!")