hourly_wage = float(input("Enter hourly wage: "))
hours_worked = float(input("Enter hours worked: "))

if hours_worked <= 40:
    total_earnings = hourly_wage * hours_worked
else:
    total_earnings = hourly_wage * 40 + (hours_worked - 40) * hourly_wage * 1.5

print("Total earnings is", total_earnings)
