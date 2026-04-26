principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100
compound_interest = principal * ((1 + rate / 100) ** time) - principal

print("Simple interest is", simple_interest)
print("Compound interest is", compound_interest)
