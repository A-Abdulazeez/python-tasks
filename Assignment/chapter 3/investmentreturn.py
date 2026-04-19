principal = 1000
return_rate = 7 / 100


for number_of_years in range(1,31):
    amount = principal * (1 + return_rate) ** number_of_years
    print(f"Amount after {number_of_years} years = {amount}")