exchange_rate = float(input("Enter the exchange rate from dollars to RMB: "))
code = int(input("Enter 0 to convert dollars to RMB or 1 to convert RMB to dollars: "))

if code == 0:
    dollars = float(input("Enter the dollar amount: "))
    rmb = dollars * exchange_rate
    print(dollars, "dollars is", rmb, "RMB")
elif code == 1:
    rmb = float(input("Enter the RMB amount: "))
    dollars = rmb / exchange_rate
    print(rmb, "RMB is", dollars, "dollars")
else:
    print("Incorrect input")
