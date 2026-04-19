count = 0
sum_of_all_numbers = 0
for number_input in range(3):
	number_input =int(input("input your number: "))
	sum_of_all_numbers += number_input
	count += 1
	average_of_all_numbers = sum_of_all_numbers/count
	product_of_all_numbers = number_input * number_input * number_input
	
	
print("The sum of all numbers is", +sum_of_all_numbers)
print("The average of all numbers is", +average_of_all_numbers)
print("The product of all numbers is", +product_of_all_numbers)
