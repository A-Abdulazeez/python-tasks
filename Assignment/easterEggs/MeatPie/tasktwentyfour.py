first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("Before swapping")
print("First number is", first_number)
print("Second number is", second_number)

temporary_number = first_number
first_number = second_number
second_number = temporary_number

print("First number is", first_number)
print("Second number is", second_number)
