''' collect the total purchase spent from the user
if total amount spent is betweeen 1000 and 10000' 5 percent discount should be applied
convert the percentage to decimal and multiply by the total amount spent 
then repeat the same for 10% and 20% discount '''







total_purchases = int(input("Enter total amount spent: "))

if (total_purchases >= 1000 and total_purchases <= 10000):
	percentage_discount = (5/100) * total_purchases
	discount_amount = percentage_discount - total_purchases
	print("The Percentage discount ", percentage_discount)

elif (total_purchases > 10000 and total_purchases <= 50000):
	percentage_discount = (10/100) * total_purchases
	discount_amount = percentage_discount - total_purchases
	print("The Percentage discount ", percentage_discount)

elif (total_purchases > 50000):
	percentage_discount = (20/100) * total_purchases
	discount_amount = percentage_discount - total_purchases
	print("The Percentage discount ", percentage_discount)

elif (total_purchases < 1000):
	print("No discount for you oga!!!")
