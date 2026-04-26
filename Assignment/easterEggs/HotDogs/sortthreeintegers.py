first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))
third_number = int(input("Enter third integer: "))

if first_number < second_number:
    first_number, second_number = second_number, first_number

if first_number < third_number:
    first_number, third_number = third_number, first_number

if second_number < third_number:
    second_number, third_number = third_number, second_number

print(first_number, second_number, third_number)
