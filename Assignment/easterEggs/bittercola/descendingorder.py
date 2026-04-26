first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))
third_number = int(input("Enter third integer: "))

if first_number < second_number:
    temporary_number = first_number
    first_number = second_number
    second_number = temporary_number

elif first_number < third_number:
    temporary_number = first_number
    first_number = third_number
    third_number = temporary_number

elif second_number < third_number:
    temporary_number = second_number
    second_number = third_number
    third_number = temporary_number

print(first_number, second_number, third_number)
