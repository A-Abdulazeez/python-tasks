number = int(input("Enter a three-digit integer: "))

if number < 0:
    number = -number

first_digit = number // 100
last_digit = number % 10

if first_digit == last_digit:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
