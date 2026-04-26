weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

body_mass_index = weight / (height * height)
print("BMI:", body_mass_index)

if body_mass_index < 18.5:
    print("Underweight")
elif body_mass_index <= 24.9:
    print("Normal")
elif body_mass_index <= 29.9:
    print("Overweight")
else:
    print("Obese")
