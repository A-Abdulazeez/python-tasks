principal = int(input("Enter your principal amount: "))
rate = int(input("Enter your rate in %: "))
percentage_rate = rate/100
time = int(input("Enter your time(years): "))

simple_interest =(principal * percentage_rate * time)
total_amount = principal + simple_interest

print("The simple interest is ",simple_interest,"and the total amount is",total_amount)
