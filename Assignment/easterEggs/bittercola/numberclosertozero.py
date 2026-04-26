first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number < second_number:
    print(first_number, "is closer to zero")
elif second_number < first_number:
    print(second_number, "is closer to zero")
else:
    print("Both are equally close to zero")
