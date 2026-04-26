import random

lottery_number = random.randint(0, 99)
user_number = int(input("Enter a two-digit number: "))

lottery_tens = lottery_number // 10
lottery_units = lottery_number % 10
user_tens = user_number // 10
user_units = user_number % 10

print("Lottery number:", lottery_number)

if user_number == lottery_number:
    print("Exact match. You win $10000")
elif user_tens == lottery_units and user_units == lottery_tens:
    print("All digits match. You win $3000")
elif user_tens == lottery_tens or user_tens == lottery_units or user_units == lottery_tens or user_units == lottery_units:
    print("One digit matches. You win $1000")
else:
    print("No match")
