first_value = float(input("Enter first value: "))
second_value = float(input("Enter second value: "))

if first_value > second_value:
    larger_value = first_value
    smaller_value = second_value
else:
    larger_value = second_value
    smaller_value = first_value

value_sum = first_value + second_value
value_difference = first_value - second_value
value_product = first_value * second_value

print("Larger value:", larger_value)
print("Smaller value:", smaller_value)
print("Sum:", value_sum)
print("Difference:", value_difference)
print("Product:", value_product)

if second_value == 0:
    print("Quotient: Cannot divide by zero")
else:
    quotient = first_value / second_value
    print("Quotient:", quotient)
