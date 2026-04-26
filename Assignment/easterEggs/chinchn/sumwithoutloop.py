number = int(input("Enter a positive number: "))

if number > 0:
    total_sum = number * (number + 1) // 2
    print("Sum is", total_sum)
else:
    print("Invalid number")
