user_number = int(input("Enter number: "))

factorial_result = 1
current_value = 1

while current_value <= user_number:
    factorial_result *= current_value
    current_value += 1

print("Factorial is:", factorial_result)
