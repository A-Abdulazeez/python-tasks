water_amount = float(input("Enter the amount of water in kilograms: "))
initial_temperature = float(input("Enter the initial temperature: "))
final_temperature = float(input("Enter the final temperature: "))

energy = water_amount * (final_temperature - initial_temperature) * 4184

print("The energy needed is", energy)
