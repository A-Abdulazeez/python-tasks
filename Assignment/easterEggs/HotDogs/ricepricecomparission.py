weight_one = float(input("Enter weight for package 1: "))
price_one = float(input("Enter price for package 1: "))
weight_one = float(input("Enter weight for package 2: "))
price_one = float(input("Enter price for package 2: "))

price_per_weight_one = price_one / weight_one
price_per_weight_two = price_two / weight_two

if price_per_weight_one < price_per_weight_two:
    print("Package 1 has the better price")
elif price_per_weight_two < price_per_weight_one:
    print("Package 2 has the better price")
else:
    print("Both packages have the same price")
