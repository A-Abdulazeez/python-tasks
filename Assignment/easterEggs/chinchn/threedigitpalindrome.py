number = int(input("Enter a three-digit number: "))

hundreds_digit = number // 100
units_digit = number % 10

if hundreds_digit == units_digit:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
