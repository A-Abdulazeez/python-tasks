package_weight = float(input("Enter package weight: "))

if package_weight > 0 and package_weight <= 2:
    print("Shipping cost is $2.5")
elif package_weight > 2 and package_weight <= 4:
    print("Shipping cost is $4.5")
elif package_weight > 4 and package_weight <= 10:
    print("Shipping cost is $7.5")
elif package_weight > 10 and package_weight <= 20:
    print("Shipping cost is $10.5")
elif package_weight > 20:
    print("The package cannot be shipped")
else:
    print("Invalid weight")
