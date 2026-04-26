first_number = int(input("Enter first positive integer: "))
second_number = int(input("Enter second positive integer: "))

if first_number > 0 and second_number > 0 and second_number % first_number == 0:
    print(first_number, "is a factor of", second_number)
else:
    print(first_number, "is not a factor of", second_number)
