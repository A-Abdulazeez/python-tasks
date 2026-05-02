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
            if user_email(user_email) and strong_password(user_password):
                print("Registration successful")
            else:
                print("Registration failed")
                
        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if user_email(user_email) and strong_password(user_password):
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
            print("Your balance is ", total_transactions)
                
          
