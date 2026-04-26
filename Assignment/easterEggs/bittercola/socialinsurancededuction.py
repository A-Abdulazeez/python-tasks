salary = float(input("Enter salary: "))

if salary <= 50000:
    deduction = 0
elif salary <= 150000:
    deduction = salary * 0.05
elif salary <= 500000:
    deduction = salary * 0.075
else:
    deduction = salary * 0.10

print("Social insurance deduction:", deduction)
