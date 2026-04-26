number = int(input("Enter a three-digit number: "))

hundreds_digit = number // 100
tens_digit = (number // 10) % 10
units_digit = number % 10

digit_sum = hundreds_digit + tens_digit + units_digit

print("Sum of digits is", digit_sum)
