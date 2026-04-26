number = int(input("Enter an integer: "))

print("Is", number, "divisible by 4 and 5?", number % 4 == 0 and number % 5 == 0)
print("Is", number, "divisible by 4 or 5?", number % 4 == 0 or number % 5 == 0)
print("Is", number, "divisible by 4 or 5 but not both?", (number % 4 == 0 or number % 5 == 0) and not (number % 4 == 0 and number % 5 == 0))
