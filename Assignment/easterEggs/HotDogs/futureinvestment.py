investment_amount = float(input("Enter investment amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
number_of_years = int(input("Enter number of years: "))

monthly_interest_rate = annual_interest_rate / 1200

future_investment_value = investment_amount * ((1 + monthly_interest_rate) ** (number_of_years * 12))

print("Future investment value is", future_investment_value)
