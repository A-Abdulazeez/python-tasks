sub_total =int(input("Enter your sub total: "))
gratuity_rate =float (input("Enter your gratuity rate: "))

gratuity = (12/100) * sub_total
total = sub_total + gratuity

print("Your Gratuity is ",gratuity,"And your total amount is ",total)
