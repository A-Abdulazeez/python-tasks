number = int(input("input your five digit number: "))
reversed_number = 0
original_number = number

#i used original_number to save the inputed number by the user, bcus afret the loop number cant be relied on again

while number > 0:
	first_number = number % 10
	number = number // 10
	reversed_number = reversed_number * 10 + first_number

if original_number == reversed_number :
	print("it is a palindromes")
elif original_number != reversed_number :
	print("it is not a palindromes")