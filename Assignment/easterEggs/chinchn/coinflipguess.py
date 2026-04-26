import random

coin_result = random.randint(0, 1)
user_guess = int(input("Enter 0 for head or 1 for tail: "))

if coin_result == 0:
    result_name = "Head"
else:
    result_name = "Tail"

print("Coin result:", result_name)

if user_guess == coin_result:
    print("Correct guess")
else:
    print("Wrong guess")
