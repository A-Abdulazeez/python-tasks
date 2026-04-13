number = input("input your five digit number: ")
number = int(number)

first_digit = number // 10000
second_digit = (number % 10000) // 1000
third_digit = (number % 1000) // 100
fourth_digit = (number % 100) // 10
fifth_digit = number % 10

print(first_digit, '  ', second_digit, '  ', third_digit, '  ', fourth_digit, '  ', fifth_digit)
