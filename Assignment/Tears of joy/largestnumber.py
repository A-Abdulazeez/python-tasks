largest_number = None

while True:
    user_input = input("Enter youe number: ")

    if user_input == "done":
        break

    number = int(user_input)

    if largest_number is None or number > largest_number:
        largest_number = number

print("Largest is:", largest_number)
