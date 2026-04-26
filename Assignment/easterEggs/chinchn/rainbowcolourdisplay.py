import random

colour_number = random.randint(1, 7)

if colour_number == 1:
    colour_name = "Violet"
elif colour_number == 2:
    colour_name = "Indigo"
elif colour_number == 3:
    colour_name = "Blue"
elif colour_number == 4:
    colour_name = "Green"
elif colour_number == 5:
    colour_name = "Yellow"
elif colour_number == 6:
    colour_name = "Orange"
else:
    colour_name = "Red"

print("Number:", colour_number)
print("Colour:", colour_name)
