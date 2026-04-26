first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))

if first_number > 0 and second_number > 0:
    print("Sum:", first_number + second_number)
elif first_number < 0 and second_number < 0:
    print("Product:", first_number * second_number)
else:
    if first_number > second_number:
        larger_number = first_number
        smaller_number = second_number
    else:
        larger_number = second_number
        smaller_number = first_number
    print("Difference:", larger_number - smaller_number)
