number = int(input("Enter a 5-digit number: "))

if number >= 10000 and number <= 99999:
    first_digit = number // 10000
    last_digit = number % 10
    digit_sum = first_digit + last_digit
    print("Sum of first and last digit:", digit_sum)
else:
    print("Invalid input. Enter a 5-digit integer.")
