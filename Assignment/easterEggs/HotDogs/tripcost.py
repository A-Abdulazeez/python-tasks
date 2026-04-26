distance = float(input("Enter the distance to drive: "))
fuel_efficiency = float(input("Enter miles per gallon: "))
price_per_gallon = float(input("Enter price per gallon: "))

cost = (distance / fuel_efficiency) * price_per_gallon

print("The cost of the trip is", cost)
