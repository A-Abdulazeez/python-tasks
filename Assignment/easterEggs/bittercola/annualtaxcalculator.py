monthly_salary = float(input("Enter monthly salary: "))

annual_salary = monthly_salary * 12

if annual_salary <= 300000:
    annual_tax = annual_salary * 0.10
elif annual_salary <= 600000:
    annual_tax = annual_salary * 0.15
else:
    annual_tax = annual_salary * 0.25

print("Annual tax owed:", annual_tax)
