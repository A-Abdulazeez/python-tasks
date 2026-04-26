bank_balance = float(input("Enter bank balance: "))
annual_interest_rate = float(input("Enter annual interest rate: "))

rate = annual_interest_rate / 100
balance_after_one_year = bank_balance * ((1 + rate) ** 1)
balance_after_two_years = bank_balance * ((1 + rate) ** 2)
balance_after_three_years = bank_balance * ((1 + rate) ** 3)

print("Balance after 1 year:", balance_after_one_year)
print("Balance after 2 years:", balance_after_two_years)
print("Balance after 3 years:", balance_after_three_years)
