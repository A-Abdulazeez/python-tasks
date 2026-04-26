first_number = int(input("Enter m: "))
second_number = int(input("Enter n: "))

if second_number == 0:
    print("Error: n cannot be zero")
else:
    result = first_number / second_number
    print("Result is", result)
