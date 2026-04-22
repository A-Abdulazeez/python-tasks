total_sum = 0

while True:
    user_number = int(input("Enter number: "))

    if user_number == 0:
        break

    total_sum += user_number

print("Total is:", total_sum)
