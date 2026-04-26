import random

first_number = random.randint(0, 9)
second_number = random.randint(0, 9)

if first_number > second_number:
    difference = first_number - second_number
else:
    difference = second_number - first_number

print("Positive difference:", difference)
