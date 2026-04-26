price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount_amount = price * discount_percentage / 100
final_price = price - discount_amount

print("Final price:", final_price)
