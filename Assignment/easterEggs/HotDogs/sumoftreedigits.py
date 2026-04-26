number = int(input("Enter an integer between 0 and 1000: "))

first_digit = number % 10
remaining_number = number // 10

second_digit = remaining_number % 10
remaining_number = remaining_number // 10

third_digit = remaining_number % 10

sum_of_digits = first_digit + second_digit + third_digit

print("The sum of the digits is", sum_of_digits)
