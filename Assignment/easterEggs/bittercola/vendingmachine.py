print("1 = Water ₦100")
print("2 = Juice ₦200")
print("3 = Soda ₦150")
print("4 = Snack ₦300")

product_code = int(input("Enter product code: "))
amount_tendered = int(input("Enter amount tendered: "))

price = 0
product_name = ""

if product_code == 1:
    product_name = "Water"
    price = 100
elif product_code == 2:
    product_name = "Juice"
    price = 200
elif product_code == 3:
    product_name = "Soda"
    price = 150
elif product_code == 4:
    product_name = "Snack"
    price = 300

if price == 0:
    print("Invalid product code")
elif amount_tendered >= price:
    change = amount_tendered - price
    print("Product:", product_name)
    print("Change: ₦", change)
else:
    shortage = price - amount_tendered
    print("Insufficient amount. Add ₦", shortage)
