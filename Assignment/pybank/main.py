from pybank import *

message = """1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """

while True:
    user_input = input(message)

    match user_input:
        case "1":
            email = input("Enter email: ")
            password = input("Enter password: ")

            if user_email(email) and strong_password(password):
                print("Registration successful")
            else:
                print("Registration failed")

        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")

            if user_email(email) and strong_password(password):
                print("Login successful")
            else:
                print("Login failed")

        case "3":
            transactions = []
            amount = float(input("Enter amount or 0 to stop: "))

            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter amount or 0 to stop: "))

            total_transactions = calculate_balance(transactions)
            print("Your balance is", total_transactions)

        case "4":
            balance = float(input("Enter balance: "))
            rate = float(input("Enter rate: "))
            years = int(input("Enter number of years: "))

            interest = apply_interest(balance, rate, years)
            print("Your interest is", interest)

        case "5":
            transactions = []

            transaction_type = input("Enter transaction type credit/debit or 0 to stop: ")

            while transaction_type != "0":
                amount = float(input("Enter amount: "))
                transactions.append([transaction_type, amount])
                transaction_type = input("Enter transaction type credit/debit or 0 to stop: ")

            transaction_summary = get_transaction_summary(transactions)
            print("Transaction summary is", transaction_summary)

        case "6":
            break

        case _:
            print("Invalid option")
