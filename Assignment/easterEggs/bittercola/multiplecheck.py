first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if second_number != 0 and first_number % second_number == 0:
    print(first_number, "is a multiple of", second_number)
else:
    print(first_number, "is not a multiple of", second_number)
