'''collected my number input
did range 
and print output'''




number = int (input("Enter your number"))

for number_counter in range (1, 11):
	table = number_counter * number
	#print(table)
	print(number ,"x" ,number_counter, "=" , table)

